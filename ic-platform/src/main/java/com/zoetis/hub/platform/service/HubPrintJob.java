package com.zoetis.hub.platform.service;


import java.util.Set;

import javax.print.DocPrintJob;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;

import com.zoetis.hub.platform.dto.PrintJobProcessingStates;

public class HubPrintJob
{
	/**
	 * The ID provided by Hub apps to identify a print job.
	 * The ID is used to identify response topic messages. 
	 */
	private int correlationID;
	
	private PrintJobProcessingStates processingState;
	private Set<PrinterStateReason> printerStateReasons;
	private PrinterState printerState;

	// set of job attributes
	private DocPrintJob docPrintJob;

	public HubPrintJob()
	{
		this.setCorrelationID(-1); 
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

	public Set<PrinterStateReason> getPrinterStateReasons() {
		return printerStateReasons;
	}

	public void setPrinterStateReasons(Set<PrinterStateReason> printerStateReasons) {
		this.printerStateReasons = printerStateReasons;
	}

	public PrinterState getPrinterState() {
		return printerState;
	}

	public void setPrinterState(PrinterState printerState) {
		this.printerState = printerState;
	}

	public DocPrintJob getDocPrintJob() {
		return docPrintJob;
	}

	public void setDocPringJob(DocPrintJob docPrintJob) {
		this.docPrintJob = docPrintJob;
	}

}
		