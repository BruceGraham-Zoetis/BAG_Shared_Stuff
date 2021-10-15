/*
@brief PrinterAccessObject.java
*/

import javax.print.*;
import javax.print.PrintService;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
//import java.io.IOException;
import javax.print.DocFlavor;
import javax.print.SimpleDoc;
import javax.print.PrintException;
//import javax.print.PrintService;
import javax.print.Doc;
import javax.print.DocPrintJob;
import javax.print.PrintServiceLookup;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.standard.Sides;
//import javax.print.attribute.standard.MediaSize;
import javax.print.attribute.standard.MediaSizeName;
import javax.print.attribute.standard.Copies;
import javax.print.event.*;
import javax.print.attribute.standard.Chromaticity;
//import javax.print.attribute.standard.ColorSupported;
import javax.print.attribute.standard.SheetCollate;


public class PrinterAccessObject {

    DocPrintJob   m_job;
    boolean       m_bPrintJobCompleted;
    PrintRequestAttributeSet m_printAttributes;

    MediaSizeName m_mediaSizeName;
    int      m_nCopies;       // the number of copies to print
    boolean  m_bColor;        // true = Color printing, false = Monochrome
    boolean  m_bDuplex;       // true = Duplex printing, false = Single sheet per page
    boolean  m_bSheetCollate; // true = Collate copies, false = don't collate copies

    PrinterAccessObject()
    {
        m_bPrintJobCompleted = false;

        // default attributes
        m_mediaSizeName = MediaSizeName.NA_LETTER;
        m_nCopies       = 1;
        m_bColor        = false;
        m_bDuplex       = false;
        m_bSheetCollate = true;
    }

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
            if (m_bDuplex)https://github.com/ZoetisDenmark/vetscan-hub
                printAttributes.add(Sides.DUPLEX);
            else
                printAttributes.add(Sides.ONE_SIDED);
        }

        return printAttributes;
    }


    /**
     * Determines if the last print job has completed
     * 
     * @return true - completed
     * @return false - not completed
     */
    public boolean isPrintJobComplete()
    {
        // TODO check the print job directly?
        return m_bPrintJobCompleted;
    }

    /**
     * Print a given file
     * 
     * @param[in] printerName - Device URI: Example: usb://Zebra/LP284
     * 
     * @return true - print job started successfully
     * @return false - print job start failed.
     */
    public boolean printFile(String pathFileName)
    {
        FileInputStream textStream;

        try {
            textStream = new FileInputStream(pathFileName); 
        }
        catch (FileNotFoundException ffne) { 
            System.out.println("file not found");
            return false;
        } 
        
        // Set the document type
        DocFlavor myFormat = DocFlavor.INPUT_STREAM.AUTOSENSE;
        
        // Create a Doc
        Doc attributesDoc = new SimpleDoc(textStream, myFormat, null); 

        PrintService printService = PrintServiceLookup.lookupDefaultPrintService();
        // Create a print job from one of the print services
        m_bPrintJobCompleted = false;
        m_job = printService.createPrintJob(); 

        try {
            m_job.addPrintJobListener(
                    new PrintJobAdapter()
                    {
                        @Override
                        public void printDataTransferCompleted(PrintJobEvent event)
                        {
                            //System.out.println("data transfer complete");
                            m_bPrintJobCompleted = true;
                        }
                        
                        @Override
                        public void printJobNoMoreEvents(PrintJobEvent event)
                        {
                            //System.out.println("received no more events");
                            m_bPrintJobCompleted = true;
                        }
                    }
                );

            PrintRequestAttributeSet printAttributes = buildPrintAttributes();
            m_job.print(attributesDoc, printAttributes);

        } catch (PrintException pe) {
            System.out.println("print failed " + pe);
            return false;
        }

        return true;
    }


    public void cancelPrintJob()
    {
        try
        {
            CancelablePrintJob cancelableJob = (CancelablePrintJob) m_job;
            // Stops further processing of a print job.
            cancelableJob.cancel();
        }
        catch (PrintException e) {
            System.out.println("Failed to cancel printing:" + e.getMessage());
        }
    }


    /**
     * Query support for printer option: DUPLEX
     * 
     * @return true - DUPLEX is supported
     * @return false - DUPLEX is not supported
     */
    public boolean isDuplexSuported()
    {
        boolean bRtn = false;

        try
        {
            PrintService printService = PrintServiceLookup.lookupDefaultPrintService();
            if (printService.isAttributeValueSupported(Sides.DUPLEX, null, null))
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
     * Enable or Disable the printer option: DUPLEX
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
     * Determine if the printer option is enabled: DUPLEX
     * 
     * @return true = option is supported
     * @return false = option is not supported
     */
    public boolean isDuplexEnabled()
    {
        return m_bDuplex;
    }


    /**
     * Query support for printer option: COLOR
     * 
     * @return true - COLOR is supported
     * @return false - COLOR is not supported
     */
    public boolean isColorSuported()
    {
        boolean bRtn = false;

        try
        {
            PrintService printService = PrintServiceLookup.lookupDefaultPrintService();

            if (printService.isAttributeValueSupported(Chromaticity.COLOR, null, null))
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
     * Enable or Disable the printer option: Color
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
     * Determine if the printer option is enabled: COLOR
     * 
     * @return true = option is enabled
     * @return false = option is not enabled
     */
    public boolean isColorEnabled()
    {
        return m_bColor;
    }


	/**
     * Set the number of copies to print during the next print job.
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


	/**COLLATED
     * Get the number of copies to print during the next print job.
     * 
     * @return - the number of copies to print
     */
	public int getCopies()
    {
        return m_nCopies;
    }


    /**
     * Query support for printer option: SheetCollate
     * COLLATED
     * @return true - SheetCollate is supported
     * @return false - SheetCollate is not supported
     */
    public boolean isSheetCollateSupported()
    {
        boolean bRtn = false;

        try
        {
            PrintService printService = PrintServiceLookup.lookupDefaultPrintService();

            if (printService.isAttributeValueSupported(SheetCollate.COLLATED, null, null))
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
     * Enable or Disable the printer option: Color
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
     * Determine if the printer option is enabled: SheetCollate
     * 
     * @return true = option is enabled
     * @return false = option is not enabled
     */
    public boolean isSheetCollateEnabled()
    {
        return m_bSheetCollate;
    }



    /**
     * Retrieves name of the default printer.
     * 
     * @return "" - there is no default printer
     * @return default printer name
     */
    public String getDefaultPrintername()
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


    /**
     * Verifies that the default printer is capabile of printing PDF files.
     * 
     * @return true - PDF printing is supported
     * @return false - PDF printing is not supported
     */
    public boolean isPdfSupported()
    {
        int count = 0;

        try
        {
            PrintService printService = PrintServiceLookup.lookupDefaultPrintService();

            for (DocFlavor docFlavor : printService.getSupportedDocFlavors())
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
           //System.out.println("PDF is supported by printer: " + printService.getName());
           return true;
        }
    }


    /**
     * Prints a test page to the printer.
     * 
     * @return true - print job started successfully
     * @return false - print job start failed.
     */
    public boolean printTestFile()
    {
        return true; // TODO
    }
}

