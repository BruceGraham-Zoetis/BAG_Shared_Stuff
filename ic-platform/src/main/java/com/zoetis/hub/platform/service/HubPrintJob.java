package com.zoetis.hub.platform.service;


import javax.print.DocPrintJob;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReasons;

public class HubPrintJob
{
	// user provided name of the print job
	String m_strPrintJobName;
	
	// set of job attributes
	DocPrintJob m_job;

	// EnumSyntax UNKOWN, IDLE, PROCESSING, STOPPED 
	PrinterState m_printerState;
	
	// HashMap<PrinterStateReason,Severity> MEDIA_JAM, SHUTDOWN, etc.
	PrinterStateReasons m_printerStateReasons;

	public HubPrintJob()
	{
		// TODO Auto-generated constructor stub
	}

}
		