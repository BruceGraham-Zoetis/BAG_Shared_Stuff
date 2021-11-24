package com.zoetis.hub.platform.dto;

import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;

/**
 * 
 * @author bag
 */

/**
 * Example JSON string
 * {
 * 		"correlationID": 5481863,
 * 		"processingState": "PENDING",
 * 		"printerStateReasons": [MEDIA_JAM, COVER_OPEN]
 * }

 *
 */
public class PrintJobStateDto implements Serializable
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	/**
	 * The ID provided by Hub apps to identify a print job.
	 * The ID is used to identify response topic messages. 
	 */
	private int correlationID;
	
	private PrintJobProcessingStates processingState;
	private Set<PrinterStateReason> printerStateReasons;
	private PrinterState printerState;

	
	public PrintJobStateDto()
	{
		this.setCorrelationID(-1); 
		this.setProcessingState(PrintJobProcessingStates.UNKNOWN);
		this.printerStateReasons = new HashSet<>();
		this.setPrinterState(PrinterState.UNKNOWN);
	}

	public String toString()
	{ 
		String str;
		str = "{\n";
		str += "\t\"correlationID\": \"" + this.correlationID + "\",\n";
		str += "\t\"processingState\": \"" + this.processingState.toString() + "\",\n";
		
		str += "\t\"printerStateReasons\":\n";
		str += "\t[\n";		
		if (null != printerStateReasons)
		{
			int iCount = printerStateReasons.size();
	        Set<PrinterStateReason> reasons = printerStateReasons;
	        for (PrinterStateReason reason : reasons)
	        {
	        	String strReason = reason.toString();
	        	String strTemp;
	        	iCount--;
	        	if (0 < iCount)
	        		strTemp = String.format("\t\t\"%s\",\n", strReason);
	        	else
	        		strTemp = String.format("\t\t\"%s\"\n", strReason);
	            str += strTemp;
	        }
		}
        str += "\t]\n";
        
		str += "}";
	    return str;
	}

	public int getCorrelationID() {
		return correlationID;
	}

	public void setCorrelationID(int correlationID) {
		this.correlationID = correlationID;
	}

	public PrintJobProcessingStates getProcessingState() {
		return processingState;
	}

	public void setProcessingState(PrintJobProcessingStates processingState) {
		this.processingState = processingState;
	}

	public void addPrinterStateReason(PrinterStateReason printerStateReason)
	{
		printerStateReasons.add(printerStateReason);
	}
	
	
	public PrinterState getPrinterState() {
		return printerState;
	}

	public void setPrinterState(PrinterState printerState) {
		this.printerState = printerState;
	}
}
