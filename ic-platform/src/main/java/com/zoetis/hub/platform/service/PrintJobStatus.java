package com.zoetis.hub.platform.service;

import java.util.HashMap;

import javax.print.DocPrintJob;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;
import javax.print.attribute.standard.PrinterStateReasons;
import javax.print.attribute.standard.Severity;

public class PrintJobStatus
{
	// set of job attributes
	DocPrintJob m_job;

	// EnumSyntax UNKOWN, IDLE, PROCESSING, STOPPED 
	PrinterState m_printerState;
	
	// HashMap<PrinterStateReason,Severity> MEDIA_JAM, SHUTDOWN, etc.
	PrinterStateReasons m_printerStateReasons;

	public PrintJobStatus()
	{
		// TODO Auto-generated constructor stub
	}

}
