package com.zoetis.hub.platform.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PrintJobCancelDto
{
	@NonNull
	private String action;
	
	@NonNull
	private String name;
	
	/**
	 * The name for the print job that is provided by Hub apps. 
	 */
	@NonNull
	private String printJobName;
	
	public String toString()
	{ 
		String str;
		str = "{\"action\":\"" + this.action + "\", ";
		str += "\"name\":\"" + this.name + "\", ";
		str += "\"printJobName\":\"" + this.printJobName + "\"}";
	    return str;
	}
	
}
