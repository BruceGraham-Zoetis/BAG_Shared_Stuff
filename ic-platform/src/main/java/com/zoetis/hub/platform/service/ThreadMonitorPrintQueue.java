package com.zoetis.hub.platform.service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Set;

import javax.print.CancelablePrintJob;
import javax.print.DocPrintJob;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.attribute.Attribute;
import javax.print.attribute.PrintJobAttributeSet;
import javax.print.attribute.standard.JobName;
import javax.print.attribute.standard.JobState;
import javax.print.attribute.standard.PrinterIsAcceptingJobs;
import javax.print.attribute.standard.PrinterStateReason;
import javax.print.attribute.standard.PrinterStateReasons;
import javax.print.attribute.standard.Severity;
import javax.print.event.PrintJobEvent;
import javax.print.event.PrintJobListener;
import javax.print.event.PrintServiceAttributeEvent;
import javax.print.event.PrintServiceAttributeListener;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;

import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobStateDto;

/**
 * @brief Thread for monitoring the System Print Queue
 * 
 */
public class ThreadMonitorPrintQueue implements Runnable, PrintServiceAttributeListener, PrintJobListener {

	private final List<HubPrintJob> m_listHubPrintJobs;
	private final List<HubPrintJobEvent> m_listHubPrintJobEvent;
    private boolean m_bDebugTrace;
	
	@Autowired
	private KafkaTemplate<String, PrintJobStateDto> kafkaPrintJobState;
    
	public ThreadMonitorPrintQueue()
	{
		m_bDebugTrace = false;
		m_listHubPrintJobs = Collections.synchronizedList(new ArrayList<>());
		m_listHubPrintJobEvent = Collections.synchronizedList(new ArrayList<>());
	}
	
	@Override
	public void run()
	{
		synchronized(m_listHubPrintJobEvent)
		{
    		while (true)
    		{
    	        if(m_listHubPrintJobEvent.size() == 0)
    	        {
    	            try
    	            {
    	                m_listHubPrintJobEvent.wait(10000);
    	            }
    	            catch (InterruptedException e)
    	            {
		                Thread.currentThread().interrupt(); 
		                System.out.printf("Thread interrupted %s\n", e.toString()); 
    	            }
    	        }
    	        else
    	        {
        			HubPrintJobEvent hubPrintJobEvent = m_listHubPrintJobEvent.remove(0);
        			System.out.println("Print Event");
        			System.out.println(hubPrintJobEvent.m_job);
        			
    				PrintJobStateDto data = new PrintJobStateDto();
    				data.setCorrelationID(hubPrintJobEvent.correlationID);
    				
        			PrinterStateReasons psr = hubPrintJobEvent.m_job.getPrintService().getAttribute(PrinterStateReasons.class);
                    Set<PrinterStateReason> errors = psr.printerStateReasonSet(Severity.REPORT);
                    for (PrinterStateReason reason : errors)
                    {
                        System.out.printf(" Reason : %s",reason.getName());
                        data.printerStateReasons.add(reason.getValue());
                    }
                    System.out.println();
        			System.out.println("");

    				switch(hubPrintJobEvent.m_printJobEvent.getPrintEventType())
    				{
    				case PrintJobEvent.JOB_CANCELED:
    				    /**
    				     * The job was canceled by the
    				     * {@link javax.print.PrintService PrintService}.
    				     */
    					data.jobState = JobState.CANCELED.getValue();
            			data.printerState = 0; // TODO
    					break;
    					
    				case PrintJobEvent.JOB_COMPLETE:
    				    /**
    				     * The document is completely printed.
    				     */
    					data.jobState = JobState.COMPLETED.getValue();
            			data.printerState = 0; // TODO
    					break;
    					
    				case PrintJobEvent.JOB_FAILED:
    				    /**
    				     * The print service reports that the job cannot be completed. The
    				     * application must resubmit the job.
    				     */
    					data.jobState = JobState.ABORTED.getValue();
            			data.printerState = 0; // TODO
    					break;
    					
    				case PrintJobEvent.REQUIRES_ATTENTION:
    				    /**
    				     * The print service indicates that a - possibly transient - problem may
    				     * require external intervention before the print service can continue. One
    				     * example of an event that can generate this message is when the printer
    				     * runs out of paper.
    				     */
    					data.jobState = JobState.PROCESSING_STOPPED.getValue();
            			data.printerState = 0; // TODO
    					break;
    					
    				case PrintJobEvent.NO_MORE_EVENTS:
    				    /**
    				     * Not all print services may be capable of delivering interesting events,
    				     * or even telling when a job is complete. This message indicates the print
    				     * job has no further information or communication with the print service.
    				     * This message should always be delivered if a terminal event
    				     * (completed/failed/canceled) is not delivered. For example, if messages
    				     * such as {@code JOB_COMPLETE} have NOT been received before receiving this
    				     * message, the only inference that should be drawn is that the print
    				     * service does not support delivering such an event.
    				     */
    					data.jobState = JobState.COMPLETED.getValue();
            			data.printerState = 0; // TODO
    					break;
    					
    				case PrintJobEvent.DATA_TRANSFER_COMPLETE:
    				    /**
    				     * The job is not necessarily printed yet, but the data has been transferred
    				     * successfully from the client to the print service. The client may free
    				     * data resources.
    				     */
    					data.jobState = JobState.PROCESSING.getValue();
            			data.printerState = 0; // TODO
    					break;
    				}

        			final String topic = "printJobState";
        			System.out.println("Producer Topic: " + topic);
        			System.out.println(data.toString());
        			kafkaPrintJobState.send(topic, data);
    	        }
	    	}
		}
	}

	/**
     * @throws PrintAccessException 
	 * @brief Stops further processing of a print job.
     * 
     * @param[in] correlationID = the print job ID
     * 
     */
    public void stopPrintJobProcessing(int correlationID) throws PrintException, PrintAccessException
    {
		synchronized(m_listHubPrintJobs)
		{
	        for (HubPrintJob hubPrintJob : m_listHubPrintJobs)
	        {
	        	if (hubPrintJob.getCorrelationID() == correlationID)
    	        {
	        		DocPrintJob docPrintJob = hubPrintJob.getDocPrintJob();
	        		m_listHubPrintJobs.remove(hubPrintJob);

	        		try
	        		{
    	        		CancelablePrintJob cancelableJob = (CancelablePrintJob) docPrintJob;
	                    cancelableJob.cancel();

	                    final String topic = "printJobState";
	        			System.out.println("Producer Topic: " + topic);
	
	        			PrintJobStateDto data = new PrintJobStateDto();
	    				data.setCorrelationID(correlationID);
	        			System.out.println(data.toString());
	        			kafkaPrintJobState.send(topic, data);
	
	                    // TODO removePrintJobAttributeListener() ?
	                    // TODO removePrintJobListener() ?
	        		}
	                catch (PrintException e)
	        		{
	                    throw new PrintAccessException(
	                        PrintAccessException.E_EXCEPTION_ID.PRINTJOB_CANCEL_FAILED,
	                        "Failed to cancel printing: " + e);
	                }
    	        }
	        }
		}
    }
    
    /**
     * @brief Enable or Disable printing debug info to System.out 
     * 
     * @param bEnable
     */
    public void setDebugTrace(boolean bEnable)
    {
        m_bDebugTrace = bEnable;
    }
    
    /**
     * @brief Add a print job to monitor 
     * 
     * @param job - The print job
     * @param printFileDto - info about the print job, including the correlationID.
     * Note that printFileDto contains the correlationID is a user provided print job ID.
     */
    public void addMonitoredPrintJob(DocPrintJob job, PrintFileDto printFileDto)
    {
    	PrintService printService = job.getPrintService();
        printService.addPrintServiceAttributeListener(this);
      	job.addPrintJobListener(this);

    	HubPrintJob hubPrintJob = new HubPrintJob();
    	hubPrintJob.setCorrelationID(printFileDto.getCorrelationID()); 
    	hubPrintJob.setDocPrintJob(job);
    	this.m_listHubPrintJobs.add(hubPrintJob);
    }
    
    /**
     * 
     * Used by PrintServiceAttributeListener
     * 
     * @param[in] printJobEvent - info about a print job event
     */
    private void jobCompleted(PrintJobEvent printJobEvent)
    {
	    synchronized (m_listHubPrintJobEvent)
	    {
	    	HubPrintJobEvent hubPrintJobEvent = new HubPrintJobEvent();
	    	hubPrintJobEvent.correlationID = getCorrelationID(printJobEvent);
	        m_listHubPrintJobEvent.add(hubPrintJobEvent);
	        m_listHubPrintJobEvent.notifyAll(); // synchronize/wait on the same object.
	    }
    }

    /**
     * 
     * Called to notify the client that the job failed to 
     * complete successfully and will have to be resubmitted.
     * 
     * Used by PrintServiceAttributeListener
     */
    @Override
    public void printJobFailed(PrintJobEvent printJobEvent)
    {

        synchronized (m_listHubPrintJobEvent)
        {
        	HubPrintJobEvent hubPrintJobEvent = new HubPrintJobEvent();
        	hubPrintJobEvent.correlationID = getCorrelationID(printJobEvent);
        	m_listHubPrintJobEvent.add(hubPrintJobEvent);
            m_listHubPrintJobEvent.notifyAll(); // synchronize/wait on the same object.
        }

        if (m_bDebugTrace)
        {
            System.out.println("INFO: printJobFailed");

            PrinterStateReasons psr = printJobEvent.getPrintJob().getPrintService().getAttribute(PrinterStateReasons.class);
            if (psr != null)
            {
                Set<PrinterStateReason> errors = psr.printerStateReasonSet(Severity.REPORT);
                for (PrinterStateReason reason : errors)
                {
                    System.out.printf(" Reason : %s",reason.getName());
                }
                System.out.println();
            }
        }
    }

    /**
     * Called to notify the client that data has been successfully transferred to
     * the print service, and the client may free local resources allocated for that data.
     * 
     * The client should not assume that the data has been completely printed after receiving this event.
     * 
     * Used by PrintServiceAttributeListener
     */
	@Override
	public void printDataTransferCompleted(PrintJobEvent printJobEvent)
    {
        if (m_bDebugTrace) System.out.println("INFO: printDataTransferCompleted");

        jobCompleted(printJobEvent);
    }

    /**
     * Called to notify the client that the job completed successfully.
     * 
     * Used by PrintServiceAttributeListener
     */
    @Override
    public void printJobCompleted(PrintJobEvent printJobEvent)
    {
        if (m_bDebugTrace) System.out.println("INFO: printJobCompleted");

        jobCompleted(printJobEvent);
    }

    /**
     * Called to notify the client that the job was canceled by user or program.
     * 
     * Used by PrintServiceAttributeListener
     */
    @Override
    public void printJobCanceled(PrintJobEvent printJobEvent)
    {
        if (m_bDebugTrace) System.out.println("INFO: printJobCanceled");

        jobCompleted(printJobEvent);
    }

    /**
     * Called to notify the client that no more events will be delivered.
     * One cause of this event being generated is if the job has successfully completed, 
     * but the printing system is limited in capability and cannot verify this. 
     * This event is required to be delivered if none of the other 
     * terminal events (completed/failed/canceled) are delivered.
     * 
     * Used by PrintServiceAttributeListener
     */
    @Override
    public void printJobNoMoreEvents(PrintJobEvent printJobEvent)
    {
        if (m_bDebugTrace) System.out.println("INFO: printJobNoMoreEvents");

        jobCompleted(printJobEvent);
    }

    /**
     * Called to notify the client that some possibly 
     * user rectifiable problem occurs (eg printer out of paper).
     * 
     * Used by PrintServiceAttributeListener
     */
    @Override
    public void printJobRequiresAttention(PrintJobEvent printJobEvent)
    {
        synchronized (m_listHubPrintJobEvent)
        {
            //m_bPrintJobRequiresAttention = true;
        	m_listHubPrintJobEvent.notifyAll(); // synchronize/wait on the same object.
        }
        
        int pet = printJobEvent.getPrintEventType();
        if (m_bDebugTrace)
        {
            System.out.println("INFO: printJobRequiresAttention");
            System.out.printf("PrintEventType: %d%n", pet);
            System.out.println(printJobEvent);
        }

        PrinterStateReasons psr = printJobEvent.getPrintJob().getPrintService().getAttribute(PrinterStateReasons.class);
        if (psr != null)
        {
            if (m_bDebugTrace)
            {
                Set<PrinterStateReason> errors = psr.printerStateReasonSet(Severity.REPORT);
                for (PrinterStateReason reason : errors)
                {
                    System.out.printf(" Reason : %s",reason.getName());
                }
                System.out.println();
            }
        }
    }
    
    /**
     * @brief Returns the print job's correlationID which is the given print job name.  
     * 
     * @param pje - the print job event
     * @return int - the print job's correlationID
     */
	private int getCorrelationID(PrintJobEvent pje)
	{
		int correlationID = -1;
        
		PrintJobAttributeSet atts = pje.getPrintJob().getAttributes();
        Attribute[] arr = atts.toArray();
        for (int i = 0; i < arr.length; i++)
        {
            if (JobName.class == arr[i].getClass())
        	{
            	String strCorrelationID = arr[i].toString();
            	correlationID = Integer.parseInt(strCorrelationID);
        	}
        }
        
        return correlationID;
	}

    /**
     * 
     * Used by PrintJobAttributeListener
     */
    public void attributeUpdate(PrintServiceAttributeEvent psae)
    {
        System.out.println("");

        Attribute[] attrs = psae.getAttributes().toArray();
        for (int i = 0; i < attrs.length; i++)
        {
            String attrName = attrs[i].getName();
            String attrValue = attrs[i].toString();
            System.out.printf("** attributeUpdate() Name: %s  Value: %s%n", attrName, attrValue);

            Attribute attr = attrs[i];
            if (attr.equals(PrinterIsAcceptingJobs.ACCEPTING_JOBS))
            {
                if (m_bDebugTrace) System.out.println("INFO: ACCEPTING_JOBS");
                m_listHubPrintJobEvent.notify();  // synchronize/wait on the same object.
            }
        }
    }

}
