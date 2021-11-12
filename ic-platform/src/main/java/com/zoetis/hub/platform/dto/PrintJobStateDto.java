package com.zoetis.hub.platform.dto;

import java.io.Serializable;

/**
 * 
 * @author bag
 */

/**
 * Example JSON string
 * {
 * 		"printJobName": "job-5481863",
 * 		"state": "PENDING",
 * 		"printerStateReasons": "Out of paper."
 * }

 *
 */
public class PrintJobStateDto implements Serializable
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private String printJobName; 
	private String state;
	private String printerStateReasons;
	
	public PrintJobStateDto()
	{
		this.setPrintJobName(""); 
		this.setState("");
		this.setPrinterStateReasons("");
	}

	public String getPrintJobName() {
		return printJobName;
	}

	public void setPrintJobName(String printJobName) {
		this.printJobName = printJobName;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getPrinterStateReasons() {
		return printerStateReasons;
	}

	public void setPrinterStateReasons(String printerStateReasons) {
		this.printerStateReasons = printerStateReasons;
	}

}
