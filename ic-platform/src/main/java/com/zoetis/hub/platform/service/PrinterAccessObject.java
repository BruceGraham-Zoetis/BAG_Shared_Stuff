package com.zoetis.hub.platform.service;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
/**
 * @brief PrinterAccessObject.java
 * 
 * Note: See printer config in http://localhost:631/printers/admin
 *   The printer queue option MUST be enabled if you want to use it.
 *   For example, to use Duplex, the printer's print queue MUST have the Duplex option set.
 * 
*/
import java.util.HashMap;
import java.util.Map;

import javax.print.Doc;
import javax.print.DocFlavor;
import javax.print.DocPrintJob;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.PrintServiceLookup;
import javax.print.SimpleDoc;
import javax.print.attribute.Attribute;
import javax.print.attribute.AttributeSet;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.standard.Chromaticity;
import javax.print.attribute.standard.Copies;
import javax.print.attribute.standard.JobName;
import javax.print.attribute.standard.PrinterName;
import javax.print.attribute.standard.PrinterURI;
import javax.print.attribute.standard.QueuedJobCount;
import javax.print.attribute.standard.SheetCollate;
import javax.print.attribute.standard.Sides;

import org.springframework.stereotype.Component;

import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobCancelDto;

@Component
public class PrinterAccessObject
{
    //private boolean       m_bDebugTrace;
    private boolean       m_bPrinting;
    private ThreadMonitorPrintQueue m_threadMonitor;
    
    /**
     * @brief Constructor using default printer with all options being required.
     * 
     * Default Settings:
     *       Copies: 1
     *        Color: not set, uses default printer's setting
     *       Duplex: not set, uses default printer's setting
     * SheetCollate: not set, uses default printer's setting
     * 
     * @throws PrintAccessException
     */
    PrinterAccessObject() throws PrintAccessException
    {
        //m_bDebugTrace = false;

        m_bPrinting = false;

        m_threadMonitor = new ThreadMonitorPrintQueue();
        new Thread(m_threadMonitor).start();
    }

    /**
     * @brief Enable or Disable printing debug info to System.out 
     * 
     * @param bEnable
     */
    public void setDebugTrace(boolean bEnable)
    {
        //m_bDebugTrace = bEnable;
        m_threadMonitor.setDebugTrace(bEnable);
    }

    /**
     * @brief : Print a given file given a file's path and name
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
        
        try
        {
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
    	                    "Default printer is not set");
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
        try
        {
        	m_threadMonitor.stopPrintJobProcessing(printJobCancelDto.getCorrelationID());
        }
        catch (PrintException e) {
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTJOB_CANCEL_FAILED,
                "Failed to cancel printing:" + e.getMessage());
        }
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

    /**
     * @brief Retrieves name of the default printer.
     * 
     * @return "" - there is no default printer
     * @return default printer name
     */
    public static String getDefaultPrintername()
    {
        String strName = "";

        try
        {
            PrintService printService = PrintServiceLookup.lookupDefaultPrintService();
            strName = printService.getName();
        }
        catch (Exception e)
        {
            strName = "";
        }

        return strName;
    }

    public class PrinterInfo extends Object
    {
        private String  m_strPrintQueueName; // Ex: "My Printer"
        private String  m_strModelName;      // Ex: "HP Color LserJet Pro M454dw"
        private String  m_strConnection;     // TODO
        private String  m_strLocation;       // Ex: "desk"
        private boolean m_bDefault;          // true: This is the default printer, false: not the default printer.

        /**
         * 
         */
        PrinterInfo()
        {
            m_strPrintQueueName = "";
            m_strModelName      = "";
            m_strConnection     = "";
            m_strLocation       = "";
            m_bDefault          = false;
        }

        /**
         * 
         */
        PrinterInfo(String strPrintQueueName,
                    String strModelName,
                    String strConnection,
                    String strLocation,
                    boolean bDefault)
        {
            m_strPrintQueueName = strPrintQueueName;
            m_strModelName      = strModelName;
            m_strConnection     = strConnection;
            m_strLocation       = strLocation;
            m_bDefault          = bDefault;
        }

        public String getPrintQueueName()
        {
            return m_strPrintQueueName;
        }
        
        public void setPrintQueueName(String strPrintQueueName)
        {
            this.m_strPrintQueueName = strPrintQueueName;
        }
        
        public String getModelName()
        {
            return m_strModelName;
        }
        
        public void setModelName(String strModelName)
        {
            this.m_strModelName = strModelName;
        }

        public String getConnection()
        {
            return m_strConnection;
        }
        
        public void setConnection(String strConnection)
        {
            this.m_strConnection = strConnection;
        }

        public String getLocation()
        {
            return m_strLocation;
        }
        
        public void setLocation(String strLocation)
        {
            this.m_strLocation = strLocation;
        }


        public boolean isDefaultPrinter()
        {
            return m_bDefault;
        }
        
        public void setDefaultPrinter(boolean bDefault)
        {
            this.m_bDefault = bDefault;
        }

        public PrinterAccessObject.PrinterInfo getValue()
        {
            return this;
        }

        @Override
        public String toString()
        {
            StringBuilder sb = new StringBuilder();

            sb.append("{\n");
            sb.append("\"Queue\": " + "\"" + getPrintQueueName() + "\"" + ",\n");
            sb.append("\"Model\": " + "\"" + getModelName() + "\"" + ",\n");
            sb.append("\"Connection\": " + "\"" + getConnection() + "\"" + ",\n");
            sb.append("\"Location\": " + "\"" + getLocation() + "\"" + ",\n");
            if (isDefaultPrinter())
                sb.append("\"Default\": " + "\"true\"\n");
            else
                sb.append("\"Default\": " + "\"false\"\n");

            sb.append("}\n");
            
            return sb.toString();
        }        
    }

    /**
     * @brief Retrieves info about the printers in the system.
     * 
     * 
     * @return Map containing info about each printer
     */
    public static Map<String, PrinterInfo> getPrinters()
    {
        Map<String, PrinterInfo> map = new HashMap<>();

        PrintService[] printServices = PrintServiceLookup.lookupPrintServices(null, null);

        String strDefaultPrinterName = PrinterAccessObject.getDefaultPrintername();
        
        for (PrintService printService : printServices)
        {
            PrinterAccessObject obj;
            PrinterAccessObject.PrinterInfo printerInfo;
            try
            {
                obj = new PrinterAccessObject();
                printerInfo = obj.new PrinterInfo();

                Attribute[] attrs = printService.getAttributes().toArray();
                for (int i = 0; i < attrs.length; i++)
                {
                    String strName = attrs[i].getName();
                    String strValue = attrs[i].toString();
                    //System.out.printf("** Name: %s  Value: %s%n", strName, strValue);

                    if (0 == strName.compareTo("printer-name"))
                    {
                        printerInfo.setPrintQueueName(strValue);

                        if (0 == strDefaultPrinterName.compareTo(strValue))
                            printerInfo.setDefaultPrinter(true);
                        else
                            printerInfo.setDefaultPrinter(false);
                    }

                    if (0 == strName.compareTo("printer-info"))
                        printerInfo.setModelName(strValue);

                    if (0 == strName.compareTo("printer-location"))
                        printerInfo.setLocation(strValue);
        
                }

                PrinterURI uri = printService.getAttribute(PrinterURI.class);
                if (null != uri)
                    printerInfo.setConnection(uri.getURI().toString());

                if (0 < printerInfo.getPrintQueueName().length())
                    map.put(printerInfo.getPrintQueueName(), printerInfo);
            }
            catch (PrintAccessException e)
            {
                //
            }

        }

        return map;
    }
}

