import javax.print.attribute.standard.DialogOwner;

public class PrintTest
{
    public static void main(String [] args)
    {
        PrinterAccessObject printAccess;
        try
        {
            // provide default or printer queue name, pdf, color, duplex, pages
            printAccess = new PrinterAccessObject();   
        }
        catch (Exception e) // HubPrintException -> missing pdf, color, duplex, no default printer.
        {
            System.err.printf("ERROR: %i", e);
            return;
        }

        String strPrinterName = printAccess.getDefaultPrintername();
        if (0 != strPrinterName.length())
            System.out.printf("Default Printer: %s%n%n", strPrinterName);
        else
            System.out.println("ERROR: Default Printer NOT set");

        boolean bRtn;

        if (printAccess.isPdfSupported())
            System.err.println("PDF is supported by printer");
        else
            System.err.println("PDF is NOT supported by printer");

        if (printAccess.isDuplexSuported())
            System.err.println("DUPLEX is supported by printer");
        else
            System.err.println("DUPLEX is NOT supported by printer");

        if (printAccess.isColorSuported())
            System.out.println("COLOR is supported by printer");
        else
            System.err.println("COLOR NOT supported by printer");

        if (printAccess.isSheetCollateSupported())
            System.out.println("SheetCollate is supported by printer");
        else
            System.err.println("SheetCollate NOT supported by printer");

        System.err.println("");
    
        if (printAccess.isPdfSupported())
        {
            printAccess.setCopies(2);

            if (printAccess.isDuplexSuported())
            {
                printAccess.enableDuplex(true);
                if (!printAccess.isDuplexEnabled())
                {
                    System.out.println("ERROR: Duplex NOT enabled");
                }
            }
/*
            if (printAccess.isColorSuported())
            {
                printAccess.enableColor(true);
                if (!printAccess.isColorEnabled())
                {
                    System.out.println("ERROR: Color NOT enabled");
                }
            }
  
            if (printAccess.isSheetCollateSupported())
            {
                printAccess.enableSheetCollate(true);
                if (!printAccess.isSheetCollateEnabled())
                {
                    System.out.println("ERROR: SheetCollate NOT enabled");
                }
            }
*/

            System.out.println("Printing PDF file.");
            bRtn = printAccess.printFile("./test_data_files/file.pdf");
            if (!bRtn)
            {
                System.out.println("Print job failed.");
            }
            else
            {
                do
                {
                    System.out.println("Waiting for printing to complete.");
                    try
                    {
                        Thread.sleep(1);
                        System.out.print(".");
                    }
                    catch(InterruptedException ioe)
                    {
                        Thread.currentThread().interrupt();
                    }
                } while(! printAccess.isPrintJobComplete());

                System.out.println("");
                System.out.printf("Print job completed.%n%n");
            }
        }

        /*
        System.out.println("Printing text file.");
        bRtn = printAccess.printFile("./test_data_files/file.txt");
        if (!bRtn)
        {
            System.out.println("Print job failed.");
        }
        else
        {
            do
            {
                System.out.println("Waiting for printing to complete.");
                try
                {
                    Thread.sleep(1);
                    System.out.print(".");
                }
                catch(InterruptedException ioe)
                {
                    Thread.currentThread().interrupt();
                }
            } while(! printAccess.isPrintJobComplete());

            System.out.println("");
            System.out.printf("Print job completed.%n%n");
        }
        */

    }
}


