package com.zoetis.hub.platform.service;

import javax.print.DocPrintJob;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReasons;
import javax.print.event.PrintJobEvent;

import com.zoetis.hub.platform.dto.PrintFileDto;

public class HubPrintJobEvent
{
	int correlationID;
	
	PrintJobEvent m_printJobEvent;
	
	// set of job attributes
	DocPrintJob m_job;

	public HubPrintJobEvent()
	{
		// TODO Auto-generated constructor stub
	}

}
