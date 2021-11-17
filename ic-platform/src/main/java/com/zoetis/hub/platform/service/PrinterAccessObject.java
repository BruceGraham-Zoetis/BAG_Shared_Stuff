package com.zoetis.hub.platform.service;

/**
 * @brief PrinterAccessObject.java
 * 
 * Note: See printer config in http://localhost:631/printers/admin
 *   The printer queue option MUST be enabled if you want to use it.
 *   For example, to use Duplex, the printer's print queue MUST have the Duplex option set.
 * 
*/

import java.util.*;

import javax.print.*;
import javax.print.PrintService;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.print.DocFlavor;
import javax.print.SimpleDoc;
import javax.print.PrintException;
import javax.print.Doc;
import javax.print.DocPrintJob;
import javax.print.PrintServiceLookup;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.standard.Sides;
import javax.print.attribute.standard.Copies;
import javax.print.attribute.standard.PrinterName;

import org.springframework.stereotype.Component;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;

import javax.print.attribute.standard.Chromaticity;
import javax.print.attribute.standard.SheetCollate;
import javax.print.attribute.AttributeSet;
import javax.print.attribute.Attribute;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;
import javax.print.attribute.standard.PrinterURI;
import javax.print.attribute.standard.PrinterStateReasons;
import javax.print.attribute.standard.Severity;
import javax.print.attribute.standard.QueuedJobCount;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;

@Component
public class PrinterAccessObject
{
    //private boolean       m_bDebugTrace;
    private boolean       m_bPrinting;
    private DocPrintJob   m_job;
    private boolean       m_bPrintJobProcessingCompleted;
    private boolean       m_bPrintJobFailed;
    private boolean       m_bPrintJobRequiresAttention;
    //private MediaSizeName m_mediaSizeName;
    private PrintService m_printService; // the targeted printer queue service.
    private String   m_strPrinterName; // the name of print queue to use.
    private int      m_nCopies;       // the number of copies to print
    private boolean  m_bColor;        // true = Color printing, false = Monochrome
    private boolean  m_bDuplex;       // true = Duplex printing, false = Single sheet per page
    private boolean  m_bSheetCollate; // true = Collate copies, false = don't collate copies
    private ThreadMonitorPrintQueue m_threadMonitor;

    enum E_QUEUE_STATE
    {
        // occurs during print job creation
        E_QUEUE_STATE_UNKNOWN,
        E_QUEUE_STATE_IDLE,
        E_QUEUE_STATE_PROCESSING,
        E_QUEUE_STATE_STOPPED
    }

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

        m_bPrinting                    = false;
        m_bPrintJobProcessingCompleted = false;
        m_bPrintJobFailed              = false;
        m_bPrintJobRequiresAttention   = false;

        // default printing attributes
        m_printService = null;
        m_strPrinterName = "";
        //m_mediaSizeName = MediaSizeName.NA_LETTER;
        m_nCopies       = 1;
        m_bColor        = false;
        m_bDuplex       = false;
        m_bSheetCollate = false;

        try
        {
            PrintService printService = PrintServiceLookup.lookupDefaultPrintService();
            m_strPrinterName  = printService.getName();
            m_printService = printService;
        }
        catch (Exception e)
        {
            throw new PrintAccessException(
                    PrintAccessException.E_EXCEPTION_ID.PRINTER_DEFAULT_NOT_FOUND,
                    "Default printer is not set");
        }
        
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
     * @brief Verify that specified printer options are supported.
     * 
     * @param[in] bColor         = true = Color printing, false = Monochrome
     * @param[in] bDuplex        = true = Duplex printing, false = Single sheet per page
     * @param[in] bSheetCollate  = true = Collate copies, false = don't collate copies
     * 
     * @return true - the printer supports setting the specified options
     * 
     * @throws PrintAccessException
     */
    public boolean verifyPrinterOptionsAreSupported(
                boolean  bColor,
                boolean  bDuplex,
                boolean  bSheetCollate
                ) throws PrintAccessException
    {
        if (!isPdfSupported())
        {
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTER_PDF_NOT_SUPPORTED,
                "Printer does not support PDF");
        }

        if (bColor && !isColorSuported())
        {
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTER_COLOR_NOT_SUPPORTED,
                "Printer does not support color");
        }

        if (bDuplex && !isDuplexSuported())
        {
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTER_DUPLEX_NOT_SUPPORTED,
                "Printer does not support Duplex");
        }

        if (bSheetCollate && !isSheetCollateSupported())
        {
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTER_SHEETCOLLATE_NOT_SUPPORTED,
                "Printer does not support SheetCollate");
        }

        return true;
    }

    /**
     * Sets the print job's attributes that where enabled when the object was created.
     * 
     * Note: Only attributes that are enabled in the printer's queue are set.
     * 
     */
    private PrintRequestAttributeSet buildPrintAttributes()
    {

        PrintRequestAttributeSet printAttributes = new HashPrintRequestAttributeSet();

        printAttributes.add(new Copies(m_nCopies));

        if (isSheetCollateSupported())
        {
            if (m_bSheetCollate)
                printAttributes.add(SheetCollate.COLLATED);
            else
                printAttributes.add(SheetCollate.UNCOLLATED);
        }

        if (isColorSuported())
        {
            if (m_bColor)
                printAttributes.add(Chromaticity.COLOR);
            else
                printAttributes.add(Chromaticity.MONOCHROME);
        }

        if (isDuplexSuported())
        {
            if (m_bDuplex)
                printAttributes.add(Sides.DUPLEX);
            else
                printAttributes.add(Sides.ONE_SIDED);
        }

        return printAttributes;
    }

    /**
     * @brief : Print a given file given a file's path and name
     * 
     * @param[in] pathFileName - the path and name of a file
     * 
     * @return true - print job started successfully
     * @return false - print job start failed.
     */
    public boolean printFile(PrintFileRequestDto requestDetails) throws PrintAccessException
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
        String strPrinterName;
        PrintService printService = null;
        
        try
        {
    		enableColor(requestDetails.getColorEnabled());
    		enableDuplex(requestDetails.getDuplexEnabled());
    		setCopies(requestDetails.getCopies());
    		strPrinterName = requestDetails.getPrinterName();
    		if (strPrinterName.equals(""))
    		{ // use default printer
    	        try
    	        {
    	            printService = PrintServiceLookup.lookupDefaultPrintService();
    	            m_strPrinterName  = printService.getName();
    	            m_printService = printService;
    	        }
    	        catch (Exception e)
    	        {
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
	    	            m_strPrinterName  = printService.getName();
	    	            m_printService = printService;
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

            String pathFileName = requestDetails.getFileName();
            fileInputStream = new FileInputStream(pathFileName); 
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

        // Create a print job from one of the print services
        m_bPrintJobProcessingCompleted = false;
        m_bPrintJobFailed              = false;
        m_bPrintJobRequiresAttention   = false;

        m_job = printService.createPrintJob();
        m_threadMonitor.addMonitoredPrintJob(m_job, requestDetails.getPrintJobName());

        //printService.addPrintServiceAttributeListener(this);
        printService.addPrintServiceAttributeListener(m_threadMonitor);

        try
        {
            //m_job.addPrintJobListener(this);
        	m_job.addPrintJobListener(m_threadMonitor);

            PrintRequestAttributeSet printAttributes = buildPrintAttributes();
            m_job.print(attributesDoc, printAttributes);
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
     * @brief Determines if the print job has completed
     * 
     * @return true - completed
     * @return false - not completed
     */
    public boolean isPrintJobProcessingCompleted()
    {
        return m_bPrintJobProcessingCompleted;
    }

    /**
     * @brief Determines if the print job has failed
     * 
     * @return true - completed
     * @return false - not completed
     */
    public boolean isPrintJobFailed()
    {
        return m_bPrintJobFailed;
    }

    /**
     * @brief Determines if the print job requires attention.
     * 
     * Ex: Printer is out of paper.
     * 
     * @return true - completed
     * @return false - not completed
     */
    public boolean isPrintJobRequiringAttention()
    {
        return m_bPrintJobRequiresAttention;
    }


    /**
     * @brief Wait for the print job to complete
     * 
     * see https://www.baeldung.com/java-wait-notify
     * 
     * Notes: If there is an error, then an exception will be thrown
     * 
     * 
     * @return true - completed
     * @return false - not completed.
     */
    public synchronized void waitForPrintJobProcessingCompleted() throws PrintAccessException
    {
        try
        {
            while (true)
            {
                if (m_bPrintJobProcessingCompleted)
                    // System.err.println("Print job finished.");
                    break;
                else if (m_bPrintJobFailed)
                {
                    throw new PrintAccessException(
                        PrintAccessException.E_EXCEPTION_ID.PRINTJOB_FAILED,
                        "Print job failed.");
                }
                else if (m_bPrintJobRequiresAttention)
                {
                    throw new PrintAccessException(
                        PrintAccessException.E_EXCEPTION_ID.PRINTJOB_REQUIRES_ATTENTION,
                        "Print job requires attention. Ex: out of paper.");
                }
                else
                    wait();
            }
        }
        catch (InterruptedException e)
        {
            Thread.currentThread().interrupt(); 
        }
    }

    /**
     * @brief Stops further processing of a print job.
     * 
     */
    public void stopPrintJobProcessing() throws PrintAccessException
    {
        try
        {
            CancelablePrintJob cancelableJob = (CancelablePrintJob) m_job;
            
            cancelableJob.cancel();
        }
        catch (PrintException e) {
            throw new PrintAccessException(
                PrintAccessException.E_EXCEPTION_ID.PRINTJOB_CANCEL_FAILED,
                "Failed to cancel printing:" + e.getMessage());
        }
    }

    /**
     * @brief Gets the printer queue state.
     * 
     * Note: If status is STOPPED, then use getPrinterStateReason() to get reason.
     * 
     * --- Returned Map ---
     * State: 
     *   E_QUEUE_STATE_UNKNOWN    = The printer state is unknown. The printer driver does not provide state info.
     *   E_QUEUE_STATE_IDLE       = Indicates that new jobs can start processing without waiting.
     *   E_QUEUE_STATE_PROCESSING = Indicates that jobs are processing; new jobs will wait before processing.
     *   E_QUEUE_STATE_STOPPED    = Indicates that no jobs can be processed and intervention is required.
     * 
     * Reason: Text string returned from printer driver, CUPS, IPP, LPD, etc.
     * 
     * Percent:
     *   -1 = unknown.
     *   0 to 100 = Percent completed printing.
     * 
     * @return Map ["State": E_QUEUE_STATE, "Reason": String, "Percent": Int]
     */
    public Map<String, Object> getPrinterState()
    {
        Map<String, Object> map = new HashMap<>();
        
        PrinterState prnState = m_printService.getAttribute(PrinterState.class);
        if (null == prnState)
        {
            map = getLpstat();
        }
        else
        {
            map.put("Percent", 0);
            
            if (PrinterState.UNKNOWN == prnState)
                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_UNKNOWN);

            else if (PrinterState.IDLE == prnState)
                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_IDLE);

            else if (PrinterState.PROCESSING == prnState)
                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
            
            else if (PrinterState.STOPPED == prnState)
                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_STOPPED);

            else
                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_UNKNOWN);
            
            String strReason = getPrinterStateReason();
            map.put("Reason", strReason);
        }

        return map;
    }
    
    /**
     * @brief Use lpstat to get the printer queue's status
     * 
     * --- Returned Map ---
     * State: 
     *   E_QUEUE_STATE_UNKNOWN    = The printer state is unknown. The printer driver does not provide state info.
     *   E_QUEUE_STATE_IDLE       = Indicates that new jobs can start processing without waiting.
     *   E_QUEUE_STATE_PROCESSING = Indicates that jobs are processing; new jobs will wait before processing.
     *   E_QUEUE_STATE_STOPPED    = Indicates that no jobs can be processed and intervention is required.
     * 
     * Reason: Text string returned from printer driver, CUPS, IPP, LPD, etc.
     * 
     * Percent:
     *   -1 = unknown.
     *   0 to 100 = Percent completed printing.
     * 
     * @return Map ["State": E_QUEUE_STATE, "Reason": String, "Percent": Int]
     */
    private Map<String, Object> getLpstat()
    {
        Map<String, Object> map = new HashMap<>();
        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_UNKNOWN);
        map.put("Reason", "UNKNOWN");
        map.put("Percent", -1);

        String[] cmd = { "lpstat", "-o", "-l", m_strPrinterName };

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
                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_STOPPED);
                        map.put("Reason", "Connecting to printer.");
                    }
                    else if (strLine.contains("Connected to printer."))
                    {
                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_STOPPED);
                        map.put("Reason", "Connected to printer");
                    }    
                    else if (strLine.contains("The printer is not responding."))
                    {
                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_STOPPED);
                        map.put("Reason", "The printer is not responding.");
                    }    
                    else if (strLine.contains("Waiting for printer to finish."))
                    {
                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
                        map.put("Reason", "Waiting for printer to finish.");
                    }
                    else if (strLine.contains("Waiting for job to complete."))
                    {
                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
                        map.put("Reason", "Waiting for job to complete.");
                    }
                    else if (strLine.contains("Copying print data."))
                    {
                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
                        map.put("Reason", "Copying print data.");
                    }

                    else if (strLine.contains("Spooling job,"))
                    {
                        int iPos = strLine.indexOf("Spooling job,");
                        if (-1 != iPos)
                        {
                            String strReason = strLine.substring(iPos + 8);
                            map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
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
                                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_UNKNOWN);
                                map.put("Reason", strReason);
                            }
                            else
                            { 
                                while ((strLine = br.readLine()) != null)
                                {
                                    if (strLine.contains("job printing"))
                                    {
                                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
                                        map.put("Reason", "Print job is printing.");
                                    }
                                    else if (strLine.contains("queued"))
                                    {
                                        map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_PROCESSING);
                                        map.put("Reason", "Print job is queued.");
                                    }
                                }
                            }
                        }    
                    }
                }

                /*
                String strState = map.get("State").toString();
                String strReason = map.get("Reason").toString();
                if (strState.equals("E_QUEUE_STATE_UNKNOWN") && strReason.equals("UNKNOWN"))
                {
                    System.out.println(strLine);
                }
                */
            }

            if (0 == iLineCount)
            {
                map.put("State", E_QUEUE_STATE.E_QUEUE_STATE_IDLE);
                map.put("Reason", "Print queue is empty.");
            }
        }
        catch (IOException e)
        {
            //System.out.println(e);
        }

        return map;
    }

    /**
     * @brief Get the desciption of the printer queue state
     * 
     * Note: Use this when getPrinterState() returns STOPPED
     * 
     * @return String - Desciption of the reason
     */
    private String getPrinterStateReason()
    {
        String strReason = "";

        StringBuilder str = new StringBuilder();

        PrinterStateReasons prnStateReasons = m_printService.getAttribute(PrinterStateReasons.class);
        if (prnStateReasons != null)
        {
            Set<PrinterStateReason> errors = prnStateReasons.printerStateReasonSet(Severity.REPORT);

            for (PrinterStateReason reason : errors)
            {
                str.append(reason.getName());
                str.append(";");
            }
        }

        strReason = str.toString();
        return strReason;
    }

    /**
     * @brief Get the count of print jobs in the targeted printer's print queue
     * 
     * Note that a printer driver may not provide a count. In this case, 0 will be returned.
     * 
     * @return the count of print jobs waiting in the print queue.
     */
    public Integer getPrinterQueueCount()
    {
        int nQueuedJobCount = 0;
    
        if (m_printService != null)
        {
            AttributeSet attributes = m_printService.getAttributes();
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
     * @brief Query support for printer option: DUPLEX
     * 
     * @return true - DUPLEX is supported
     * @return false - DUPLEX is not supported
     */
    public boolean isDuplexSuported()
    {
        boolean bRtn = false;

        try
        {
            if (m_printService.isAttributeValueSupported(Sides.DUPLEX, null, null))
            {
                bRtn = true;
            }
        }
        catch (Exception e)
        {
            //
        }
        return bRtn;
    }

    /**
     * @brief Enable or Disable the printer option: DUPLEX
     * 
     * @param[in] bEnable - true = enable DUPLEX. false = disable DUPLEX
     * 
     * @return true = success
     * @return false = failed. Print queue does not support Duplex.
     */
    public boolean enableDuplex(boolean bEnable)
    {
        if (isDuplexSuported())
        {
            m_bDuplex  = bEnable;
            return true;
        }
        else
        {
            return false;
        }
    }

    /**
     * @brief Determine if the printer option is enabled: DUPLEX
     * 
     * @return true = option is supported
     * @return false = option is not supported
     */
    public boolean isDuplexEnabled()
    {
        return m_bDuplex;
    }

    /**
     * @brief Query support for printer option: COLOR
     * 
     * @return true - COLOR is supported
     * @return false - COLOR is not supported
     */
    public boolean isColorSuported()
    {
        boolean bRtn = false;

        try
        {
            if (m_printService.isAttributeValueSupported(Chromaticity.COLOR, null, null))
            {
                bRtn = true;
            }
        }
        catch (Exception e)
        {
            //
        }
        return bRtn;
    }

    /**
     * @brief Enable or Disable the printer option: Color
     * 
     * @param[in] bEnable - true = print job will be in color
     * @param[in] bEnable - false = print job will be in monochrome
     * 
     * @return true = success
     * @return false = failed. Print queue does not support Color.
     */
    public boolean enableColor(boolean bEnable)
    {
        if (isColorSuported())
        {
            m_bColor = bEnable;
            return true;
        }
        else
        {
            return false;
        }
    }

    /**
     * @brief Determine if the printer option is enabled: COLOR
     * 
     * @return true = option is enabled
     * @return false = option is not enabled
     */
    public boolean isColorEnabled()
    {
        return m_bColor;
    }

	/**
     * @brief Set the number of copies to print during the next print job.
     * 
     * @param[in] nCopies - the number of copies to print
     * 
     * @return true - success
     * @return false - failure.
     */
    public boolean setCopies(int nCopies)
    {
        if (0 < nCopies)
        {
            m_nCopies = nCopies;
            return true;
        }
        else
        {
            return false;
        }
    }

	/**
     * Get the number of copies to print during the next print job.
     * 
     * @return - the number of copies to print
     */
	public int getCopies()
    {
        return m_nCopies;
    }

    /**
     * @brief Query support for printer option: SheetCollate
     *
     * @return true - SheetCollate is supported
     * @return false - SheetCollate is not supported
     */
    public boolean isSheetCollateSupported()
    {
        boolean bRtn = false;

        try
        {
            if (m_printService.isAttributeValueSupported(SheetCollate.COLLATED, null, null))
            {
                bRtn = true;
            }
        }
        catch (Exception e)
        {
            //
        }
        return bRtn;
    }

    /**
     * @brief Enable or Disable the printer option: Color
     * 
     * @param[in] bEnable - true = print job will be in color
     * @param[in] bEnable - false = print job will be in monochrome
     * 
     * @return true = success
     * @return false = failed. Print queue does not support Color.
     */
    public boolean enableSheetCollate(boolean bEnable)
    {
        if (isSheetCollateSupported())
        {
            m_bSheetCollate = bEnable;
            return true;
        }
        else
        {
            return false;
        }
    }

    /**
     * @brief Determine if the printer option is enabled: SheetCollate
     * 
     * @return true = option is enabled
     * @return false = option is not enabled
     */
    public boolean isSheetCollateEnabled()
    {
        return m_bSheetCollate;
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

    /**
     * @brief Verifies that the target printer is capabile of printing PDF files.
     * 
     * @return true - PDF printing is supported
     * @return false - PDF printing is not supported
     */
    public boolean isPdfSupported()
    {
        int count = 0;

        try
        {
            for (DocFlavor docFlavor : m_printService.getSupportedDocFlavors())
            {
                //System.err.println(docFlavor.toString());
    
                if (docFlavor.toString().contains("pdf"))
                {
                    count++;
                    break;
                }
            }
        }
        catch (Exception e)
        {
            //
        }

        if (count == 0)
        {
            return false;
        }
        else
        {
           //System.out.println("INFO: PDF is supported by printer: " + printService.getName());
           return true;
        }
    }
}

