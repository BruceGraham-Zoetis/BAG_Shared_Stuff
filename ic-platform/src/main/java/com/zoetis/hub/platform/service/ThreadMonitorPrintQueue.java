package com.zoetis.hub.platform.service;

import java.util.List;
import java.util.Set;

import javax.print.PrintService;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;
import javax.print.attribute.standard.PrinterStateReasons;
import javax.print.attribute.standard.Severity;
import javax.print.event.PrintJobEvent;
import javax.print.event.PrintJobListener;
import javax.print.event.PrintServiceAttributeEvent;
import javax.print.event.PrintServiceAttributeListener;

/**
 * @brief Thread for monitoring the System Print Queue
 * 
 */
public class ThreadMonitorPrintQueue implements Runnable, PrintServiceAttributeListener, PrintJobListener {

	private List<PrintJobStatus> m_listPrintJobs;
    private boolean       m_bDebugTrace;
	
	public ThreadMonitorPrintQueue(List<PrintJobStatus> listPrintJobs)
	{
		m_bDebugTrace = false;
		m_listPrintJobs = listPrintJobs;
	}
	
	@Override
	public void run()
	{
		synchronized(m_listPrintJobs)
		{
    		while (true)
    		{
    	        if(m_listPrintJobs.size() == 0)
    	        {
    	            try
    	            {
    	                m_listPrintJobs.wait(10000);
    	            }
    	            catch (InterruptedException e)
    	            {
		                Thread.currentThread().interrupt(); 
		                //System.out.printf("Thread interrupted %s\n", e.toString()); 
    	            }
    	        }
    	        else
    	        {
        			System.out.println("Checking Print Queue");
    	            m_listPrintJobs.remove(0);
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
     * 
     * Used by PrintServiceAttributeListener
     */
    private void jobCompleted()
    {
	    synchronized (m_listPrintJobs)
	    {
            PrintJobStatus printJobStatus = new PrintJobStatus();
	        m_listPrintJobs.add(printJobStatus);
	        m_listPrintJobs.notifyAll(); // synchronize/wait on the same object.
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

        synchronized (m_listPrintJobs)
        {
        	PrintService printService = printJobEvent.getPrintJob().getPrintService();
        	
        	PrintJobStatus printJobStatus = new PrintJobStatus();
        	
        	printJobStatus.m_job = printJobEvent.getPrintJob();

            PrinterState prnState =
                    (PrinterState)printService.getAttribute(PrinterState.class);
        	printJobStatus.m_printerState = prnState;
        	
            PrinterStateReasons prnStateReasons =
                    (PrinterStateReasons)printService.getAttribute(PrinterStateReasons.class);
        	printJobStatus.m_printerStateReasons = prnStateReasons; 
        	
        	m_listPrintJobs.add(printJobStatus);
            m_listPrintJobs.notifyAll(); // synchronize/wait on the same object.
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

        jobCompleted();
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

        jobCompleted();
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

        jobCompleted();
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

        jobCompleted();
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
        synchronized (m_listPrintJobs)
        {
            //m_bPrintJobRequiresAttention = true;
        	m_listPrintJobs.notifyAll(); // synchronize/wait on the same object.
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
     * 
     * Used by PrintJobAttributeListener
     */
    public void attributeUpdate(PrintServiceAttributeEvent psae)
    {
        //System.out.println("");

        //Attribute[] attrs = psae.getAttributes().toArray();
        //for (int i = 0; i < attrs.length; i++)
        //{
            //String attrName = attrs[i].getName();
            //String attrValue = attrs[i].toString();
            //System.out.printf("** attributeUpdate() Name: %s  Value: %s%n", attrName, attrValue);

            //Attribute attr = attrs[i];
            //if (attr.equals(PrinterIsAcceptingJobs.ACCEPTING_JOBS))
            //{
                //if (m_bDebugTrace) System.out.println("INFO: ACCEPTING_JOBS");
                //m_listPrintJobs.notifyAll(); // synchronize/wait on the same object.
            //}
        //}
    }

}
