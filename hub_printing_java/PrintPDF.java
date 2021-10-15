/*
@brief Print a PDF file using PrinterJob in Java
*/

import javax.print.*;
import javax.print.PrintService;
import java.io.FileInputStream;
//import java.io.FileNotFoundException;
import java.io.IOException;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
//import javax.print.attribute.standard.Sides;


public class PrintPDF {
    public static void main(String[] args) throws PrintException, IOException {
        DocFlavor flavor = DocFlavor.SERVICE_FORMATTED.PAGEABLE;
        PrintRequestAttributeSet patts = new HashPrintRequestAttributeSet();
        //patts.add(Sides.DUPLEX);
        PrintService[] services = PrintServiceLookup.lookupPrintServices(flavor, patts);
        if (0 == services.length) {
            throw new IllegalStateException("No Printer found");
        }
        //System.out.println("Available printers: " + Arrays.asList(services));

        PrintService myService = null;
        for (PrintService printService : services) {
            if (printService.getName().equals("RTPP1005")) {
                myService = printService;
                break;
            }
        }

        if (myService == null) {
            //throw new IllegalStateException("Printer not found");
            myService = services[0];
        }

        FileInputStream fis = new FileInputStream("./file.pdf");
        Doc pdfDoc = new SimpleDoc(fis, DocFlavor.INPUT_STREAM.AUTOSENSE, null);
        DocPrintJob printJob = myService.createPrintJob();
        printJob.print(pdfDoc, new HashPrintRequestAttributeSet());
        fis.close();
    }
}
