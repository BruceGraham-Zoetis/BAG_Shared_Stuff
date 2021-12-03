package com.zoetis.hub.platform.service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import javax.print.DocPrintJob;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.PrintServiceLookup;
import javax.print.attribute.Attribute;
import javax.print.attribute.AttributeSet;
import javax.print.attribute.PrintJobAttributeSet;
import javax.print.attribute.standard.JobName;
import javax.print.attribute.standard.JobState;
import javax.print.attribute.standard.PrinterIsAcceptingJobs;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;
import javax.print.attribute.standard.PrinterStateReasons;
import javax.print.attribute.standard.PrinterURI;
import javax.print.attribute.standard.QueuedJobCount;
import javax.print.attribute.standard.Severity;
import javax.print.event.PrintJobEvent;
import javax.print.event.PrintJobListener;
import javax.print.event.PrintServiceAttributeEvent;
import javax.print.event.PrintServiceAttributeListener;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;

import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobStateDto;
import com.zoetis.hub.platform.dto.PrinterInfoDto;

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
        			
        			PrinterState prnState = hubPrintJobEvent.m_job.getPrintService().getAttribute(PrinterState.class);
        	        if (null != prnState)
        	        {
        	        	data.printerState = prnState.getValue();
        	        	//data.percent = 0;
        	        }
        	        else
        	        {
        	            /*
        	            Map<String, Object> map = new HashMap<>();
        	            
        	        	String strPrinterName;
        	        	strPrinterName = hubPrintJobEvent.m_job.getPrintService().getName(); 
        	            map = getLpstat(strPrinterName);
        	            */
        	        	
        	        	data.printerState = PrinterState.UNKNOWN.getValue();
        	            //data.percent = 0;
        	        }

        	        switch(hubPrintJobEvent.m_printJobEvent.getPrintEventType())
    				{
    				case PrintJobEvent.JOB_CANCELED:
    				    /**
    				     * The job was canceled by the
    				     * {@link javax.print.PrintService PrintService}.
    				     */
    					data.jobState = JobState.CANCELED.getValue();
    					break;
    					
    				case PrintJobEvent.JOB_COMPLETE:
    				    /**
    				     * The document is completely printed.
    				     */
    					data.jobState = JobState.COMPLETED.getValue();
    					break;
    					
    				case PrintJobEvent.JOB_FAILED:
    				    /**
    				     * The print service reports that the job cannot be completed. The
    				     * application must resubmit the job.
    				     */
    					data.jobState = JobState.ABORTED.getValue();
    					break;
    					
    				case PrintJobEvent.REQUIRES_ATTENTION:
    				    /**
    				     * The print service indicates that a - possibly transient - problem may
    				     * require external intervention before the print service can continue. One
    				     * example of an event that can generate this message is when the printer
    				     * runs out of paper.
    				     */
    					data.jobState = JobState.PROCESSING_STOPPED.getValue();
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
    					break;
    					
    				case PrintJobEvent.DATA_TRANSFER_COMPLETE:
    				    /**
    				     * The job is not necessarily printed yet, but the data has been transferred
    				     * successfully from the client to the print service. The client may free
    				     * data resources.
    				     */
    					data.jobState = JobState.PROCESSING.getValue();
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
     * @brief Enable or Disable printing debug info to System.out 
     * 
     * @param bEnable
     */
    public void setDebugTrace(boolean bEnable)
    {
        m_bDebugTrace = bEnable;
    }
    
    /**
     * @brief Use lpstat to get the printer queue's status
     * 
     * @param[in] strPrinterName - name of the printer
     * 
     * --- Returned Map ---
     * State: 
     *   PrinterState.UNKNOWN    = The printer state is unknown. The printer driver does not provide state info.
     *   PrinterState.IDLE       = Indicates that new jobs can start processing without waiting.
     *   PrinterState.PROCESSING = Indicates that jobs are processing; new jobs will wait before processing.
     *   PrinterState.STOPPED    = Indicates that no jobs can be processed and intervention is required.
     * 
     * Reason: Text string returned from printer driver, CUPS, IPP, LPD, etc.
     * 
     * Percent:
     *   -1 = unknown.
     *   0 to 100 = Percent completed printing.
     * 
     * @return Map ["State": E_QUEUE_STATE, "Reason": String, "Percent": Int]
     */
    /* TODO
    private Map<String, Object> getLpstat(String strPrinterName)
    {
        Map<String, Object> map = new HashMap<>();
        map.put("State", PrinterState.UNKNOWN.getValue());
        map.put("Reason", "UNKNOWN");
        map.put("Percent", -1);

        String[] cmd = { "lpstat", "-o", "-l", strPrinterName };

        try
        {
            InputStream stdin = Runtime.getRuntime().exec(cmd).getInputStream();
            InputStreamReader isr = new InputStreamReader(stdin);
            BufferedReader br = new BufferedReader(isr);

            String strLine;
            int iLineCount = 0;
            while ((strLine = br.readLine()) != null)
            {
                iLineCount++;

                if (strLine.contains("Status:"))
                {
                    if (strLine.contains("Connecting to printer."))
                    {
                        map.put("State", PrinterState.STOPPED.getValue());
                        map.put("Reason", "Connecting to printer.");
                    }
                    else if (strLine.contains("Connected to printer."))
                    {
                    	map.put("State", PrinterState.STOPPED.getValue());
                        map.put("Reason", "Connected to printer");
                    }    
                    else if (strLine.contains("The printer is not responding."))
                    {
                    	map.put("State", PrinterState.STOPPED.getValue());
                        map.put("Reason", "The printer is not responding.");
                    }    
                    else if (strLine.contains("Waiting for printer to finish."))
                    {
                    	map.put("State", PrinterState.PROCESSING.getValue());
                        map.put("Reason", "Waiting for printer to finish.");
                    }
                    else if (strLine.contains("Waiting for job to complete."))
                    {
                    	map.put("State", PrinterState.PROCESSING.getValue());
                        map.put("Reason", "Waiting for job to complete.");
                    }
                    else if (strLine.contains("Copying print data."))
                    {
                    	map.put("State", PrinterState.PROCESSING.getValue());
                        map.put("Reason", "Copying print data.");
                    }

                    else if (strLine.contains("Spooling job,"))
                    {
                        int iPos = strLine.indexOf("Spooling job,");
                        if (-1 != iPos)
                        {
                            String strReason = strLine.substring(iPos + 8);
                            map.put("State", PrinterState.PROCESSING.getValue());
                            map.put("Reason", "Spooling job.");
                            // Ex: Spooling job, 52%
                            iPos = strReason.indexOf("%");
                            String strPercent = strReason.substring(iPos - 3);
                            int iPercent = Integer.parseInt(strPercent);
                            if ((0 <= iPercent) && (iPercent <= 100))
                            {
                                map.put("Percent", iPercent);
                            }
                        }    
                    }

                    else
                    {
                        int iPos = strLine.indexOf("Status:");
                        if (-1 != iPos)
                        {
                            String strReason = strLine.substring(iPos + 8);
                            if (0 != strReason.length())
                            {
                            	map.put("State", PrinterState.UNKNOWN.getValue());
                                map.put("Reason", strReason);
                            }
                            else
                            { 
                                while ((strLine = br.readLine()) != null)
                                {
                                    if (strLine.contains("job printing"))
                                    {
                                    	map.put("State", PrinterState.PROCESSING.getValue());
                                        map.put("Reason", "Print job is printing.");
                                    }
                                    else if (strLine.contains("queued"))
                                    {
                                    	map.put("State", PrinterState.PROCESSING.getValue());
                                        map.put("Reason", "Print job is queued.");
                                    }
                                }
                            }
                        }    
                    }
                }

                if (map.get("Reason").equals("UNKNOWN"))
                {
                    System.out.println("Reason ???: " + map.get("Reason"));
                }
            }

            if (0 == iLineCount)
            {
            	map.put("State", PrinterState.IDLE.getValue());
                map.put("Reason", "Print queue is empty.");
            }
        }
        catch (IOException e)
        {
            //System.out.println(e);
        }

        return map;
    }
    */

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


    /**
     * @brief Retrieves info about the printers in the system.
     * 
     * 
     * @return Map containing info about each printer
     */
    public static Map<String, PrinterInfoDto> getPrinters()
    {
        Map<String, PrinterInfoDto> map = new HashMap<>();

        PrintService[] printServices = PrintServiceLookup.lookupPrintServices(null, null);

        PrintService printServiceDefault = PrintServiceLookup.lookupDefaultPrintService();
        String strDefaultPrinterName = printServiceDefault.getName();
        
        for (PrintService printService : printServices)
        {
            PrinterInfoDto printerInfoDto = new PrinterInfoDto();

            Attribute[] attrs = printService.getAttributes().toArray();
            for (int i = 0; i < attrs.length; i++)
            {
                String strName = attrs[i].getName();
                String strValue = attrs[i].toString();
                //System.out.printf("** Name: %s  Value: %s%n", strName, strValue);

                if (0 == strName.compareTo("printer-name"))
                {
                    printerInfoDto.setPrintQueueName(strValue);

                    if (0 == strDefaultPrinterName.compareTo(strValue))
                        printerInfoDto.setDefaultPrinter(true);
                    else
                        printerInfoDto.setDefaultPrinter(false);
                }

                if (0 == strName.compareTo("printer-info"))
                    printerInfoDto.setModelName(strValue);

                if (0 == strName.compareTo("printer-location"))
                    printerInfoDto.setPrinterLocation(strValue);
    
            }

            PrinterURI uri = printService.getAttribute(PrinterURI.class);
            if (null != uri)
                printerInfoDto.setConnection(uri.getURI().toString());

            if (0 < printerInfoDto.getPrintQueueName().length())
                map.put(printerInfoDto.getPrintQueueName(), printerInfoDto);
        }
        return map;
    }
    
    /**
     * @brief Get the count of print jobs in the targeted printer's print queue
     * 
     * @param[in] printService - The printer service
     * 
     * Note that a printer driver may not provide a count. In this case, 0 will be returned.
     * 
     * @return the count of print jobs waiting in the print queue.
     */
    public Integer getPrinterQueueCount(PrintService printService)
    {
        int nQueuedJobCount = 0;
    
        if (printService != null)
        {
            AttributeSet attributes = printService.getAttributes();
            Attribute att = attributes.get(QueuedJobCount.class);
            if (null != att)
            {
                // found
                String value = att.toString();
                nQueuedJobCount = Integer.parseInt(value);
            }
            else
            {
                nQueuedJobCount = 0;
            }

            //System.out.println("INFO: QueuedJobCount: " + nQueuedJobCount);
        }

        return nQueuedJobCount;
    }
}
