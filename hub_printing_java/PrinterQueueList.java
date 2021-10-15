/*
@brief printer_queue_list.java
*/

import javax.print.*;
import javax.print.PrintService;


public class PrinterQueueList {
    public static void main (String [] args)
    {
        PrintService[] printServices = PrintServiceLookup.lookupPrintServices(null, null);
        System.out.println("Number of print services: " + printServices.length);

        for (PrintService printer : printServices)
            System.out.println("Printer: " + printer.getName());
    }
}
