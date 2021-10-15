/*
@brief PrintTextFile.java
*/

import java.io.FileInputStream;
import java.io.FileNotFoundException;
//import java.io.IOException;
import javax.print.DocFlavor;
import javax.print.SimpleDoc;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.Doc;
import javax.print.DocPrintJob;
import javax.print.PrintServiceLookup;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
//import javax.print.attribute.standard.Sides;
//import javax.print.attribute.standard.MediaSize;
import javax.print.attribute.standard.Copies;


public class PrintTextFile {
    public static void main (String [] args)
    {
        // Input the file
        FileInputStream textStream;

        try { 
            textStream = new FileInputStream("file.txt"); 
        }
        catch (FileNotFoundException ffne) { 
            System.out.println("file not found");
            return;
        } 
        
        // Set the document type
        DocFlavor myFormat = DocFlavor.INPUT_STREAM.TEXT_PLAIN_UTF_8;
        
        // Create a Doc
        Doc myDoc = new SimpleDoc(textStream, myFormat, null); 
        
        // Build a set of attributes
        PrintRequestAttributeSet aset = new HashPrintRequestAttributeSet(); 
        aset.add(new Copies(5)); 
        //aset.add(MediaSize.Engineering.A); // 8.5" x 11"
        //aset.add(Sides.DUPLEX);

        // discover the printers that can print the format according to the
        // instructions in the attribute set
        PrintService[] services = PrintServiceLookup.lookupPrintServices(myFormat, aset);
        // Create a print job from one of the print services
        if (0 < services.length) { 
            DocPrintJob job = services[0].createPrintJob(); 
            try { 
                job.print(myDoc, aset); 
            } catch (PrintException pe) {
                System.out.println("print failed");
            }
        }
    }
}

