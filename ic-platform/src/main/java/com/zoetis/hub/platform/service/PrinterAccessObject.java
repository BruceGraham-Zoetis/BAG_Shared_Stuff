package com.zoetis.hub.platform.service;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import javax.print.Doc;
import javax.print.DocFlavor;
import javax.print.DocPrintJob;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.PrintServiceLookup;
import javax.print.SimpleDoc;
import javax.print.attribute.Attribute;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.standard.Chromaticity;
import javax.print.attribute.standard.Copies;
import javax.print.attribute.standard.JobName;
import javax.print.attribute.standard.PrinterName;
import javax.print.attribute.standard.SheetCollate;
import javax.print.attribute.standard.Sides;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobCancelDto;

@Component
public class PrinterAccessObject
{
    private boolean m_bPrinting;
    Logger logger;
    private ThreadMonitorPrintQueue m_threadMonitor;
    
    /**
     * @brief Constructor
     */
    PrinterAccessObject()
    {
        m_bPrinting = false;
        logger = LoggerFactory.getLogger (HubPrintServiceMessageListener.class);

        m_threadMonitor = new ThreadMonitorPrintQueue();
        new Thread(m_threadMonitor).start();
    }

    /**
     * @brief : Print a given the path to the file
     * 
     * @param[in] printFileDto - info about the print job
     * Note that printFileDto contains the correlationID is a user provided print job ID.
     * 
     * @return true - print job started successfully
     * @return false - print job start failed.
     */
    public boolean printFile(PrintFileDto printFileDto) throws PrintAccessException
    {
        synchronized (this)
        {
            if (m_bPrinting)
            {
                throw new PrintAccessException(
                    PrintAccessException.E_EXCEPTION_ID.PRINTJOB_IN_PROCESS,
                    "Already printing");
            } else
            {
                m_bPrinting = true;
            }
        }

        FileInputStream fileInputStream;
        PrintService printService = null;
        String   strPrinterName;
        
		strPrinterName = printFileDto.getPrinterName();
		
		if (strPrinterName.equals(""))
		{ // use default printer
	        try
	        {
	            printService = PrintServiceLookup.lookupDefaultPrintService();
	        }
	        catch (Exception e)
	        {
	        	m_bPrinting = false;
	            throw new PrintAccessException(
	                    PrintAccessException.E_EXCEPTION_ID.PRINTER_DEFAULT_NOT_FOUND,
	                    "Printer name not provided. Default printer is not set");
	        }
		}
		else
		{ // get the printServer for the given printer name
			PrintService[] printServices = PrintServiceLookup.lookupPrintServices(null, null);
	        for (PrintService ps : printServices)
	        {
	        	PrinterName printerName = (PrinterName)ps.getAttribute(PrinterName.class);
                if (printerName.getValue().equals(strPrinterName))
                {
                	printService = ps;
                    break;
                }
	        }
	        if (null == printService)
	        {
                m_bPrinting = false;
                throw new PrintAccessException(
                    PrintAccessException.E_EXCEPTION_ID.PRINTER_NAME_NOT_FOUND,
                    "Printer name not found");
	        }
		}

        try
        {
        	fileInputStream = new FileInputStream(printFileDto.getFileName());
        }
        catch (FileNotFoundException ffne)
        { 
            m_bPrinting = false;
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.FILE_NOT_FOUND,
                "File not found");
        }

        // Set the document type
        DocFlavor myFormat = DocFlavor.INPUT_STREAM.AUTOSENSE;
        
        // Create a Doc
        Doc attributesDoc = new SimpleDoc(fileInputStream, myFormat, null); 

        // Create a print job for the print service
        DocPrintJob docPrintJob;
        docPrintJob = printService.createPrintJob();
        // TODO m_threadMonitor.addMonitoredPrintJob(docPrintJob, printFileDto);

        try
        {
            PrintRequestAttributeSet printAttributes = new HashPrintRequestAttributeSet();

            if (0 < printFileDto.getCopies())
            {
            	printAttributes.add(new Copies(printFileDto.getCopies()));
            }
            else
            { // the printFileDto did not provide a valid copies, use default of 1.
            	printAttributes.add(new Copies(1));
            }

            if (printService.isAttributeValueSupported(SheetCollate.COLLATED, null, null))
            {
                if (printFileDto.getSheetCollate())
                    printAttributes.add(SheetCollate.COLLATED);
                else
                    printAttributes.add(SheetCollate.UNCOLLATED);
            }

            if (printService.isAttributeValueSupported(Chromaticity.COLOR, null, null))
            {
                if (printFileDto.getColorEnabled())
                    printAttributes.add(Chromaticity.COLOR);
                else
                    printAttributes.add(Chromaticity.MONOCHROME);
            }

            if (printService.isAttributeValueSupported(Sides.DUPLEX, null, null))
            {
                if (printFileDto.getDuplexEnabled())
                    printAttributes.add(Sides.DUPLEX);
                else
                    printAttributes.add(Sides.ONE_SIDED);
            }

            String jobName = String.valueOf(printFileDto.getCorrelationID());
            printAttributes.add(new JobName(jobName, null));
            
            docPrintJob.print(attributesDoc, printAttributes);
        }
        catch (PrintException pe)
        {
            m_bPrinting = false;
            String strMsg = "Print job failed " + pe;
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTJOB_FAILED,
                strMsg);
        }

        m_bPrinting = false;
        return true;
    }

    /**
     * @brief Stops further processing of a print job.
     * 
     * @param[in] printJobCancelDto = info about the print job to cancel
     * 
     */
    public void stopPrintJobProcessing(PrintJobCancelDto printJobCancelDto) throws PrintAccessException
    {
        //int    correlationID  = printJobCancelDto.getCorrelationID(); 
        String strPrinterName = printJobCancelDto.getPrinterName();
        //boolean bDeleted = false;
    	
        // loop through the printers
        PrintService[] printServices = PrintServiceLookup.lookupPrintServices(null, null);
        for (PrintService printService : printServices)
        {
            Attribute[] attrs = printService.getAttributes().toArray();
            for (int i = 0; i < attrs.length; i++)
            {
                String strName = attrs[i].getName();
                String strValue = attrs[i].toString();

                if (0 == strName.compareTo("printer-name"))
                {
                	logger.info("printer-name: " + strValue);
                	if (0 == strValue.compareTo(strPrinterName))
                	{
                		// loop through the printJobs

                        // TODO
                		
                		//bDeleted = true;
                		break;
                	}
                }
            }
            //if (bDeleted)
            	//break;
        }
		//debug
    }

    /**
     * @brief Cancel a print job in the given printer's print queue.
     * 
     * @param[in] printJobCancelDto = info about the print job to cancel
     * 
     */
    public void cancelQueuedPrintJob(PrintJobCancelDto printJobCancelDto) throws PrintAccessException
    {
        //int    correlationID  = printJobCancelDto.getCorrelationID(); 
        //String strPrinterName = printJobCancelDto.getPrinterName();
        
        /*
    	Since the caller can't provide the DocPrintJob, the printJob can't be cancelled directly.
    	DocPrintJob CancelablePrintJob cancel() will only cancel a print job while
    	it is being processed and written to the printer's queue,
    	but it will not cancel a print job that is fully in the printer's queue.
    	*/

    	/*
 		To cancel 1 print job in a printer's queue
		$ cancel {printerjob-id}
		Ex: cancel HP-LaserJet4-345
        */
    }
}

