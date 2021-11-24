package com.zoetis.hub.platform.dto;

import java.io.Serializable;

/**
 * 
 * @author bag
 */

/**
 * Example JSON string
 * {
 * 		"correlationID": 5481863,
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
	
	private int correlationID; 
	private String state;
	private String printerStateReasons;
	
	public PrintJobStateDto()
	{
		this.setCorrelationID(-1); 
		this.setState("");
		this.setPrinterStateReasons("");
	}

	public int getCorrelationID() {
		return correlationID;
	}

	public void setCorrelationID(int correlationID) {
		this.correlationID = correlationID;
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
