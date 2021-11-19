package com.zoetis.hub.platform.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PrintJobAbortedDto
{
	@NonNull
	private String printJobName;
	
	public String getPrintJobName() {
		return printJobName;
	}

	public void setPrintJobName(String printJobName) {
		this.printJobName = printJobName;
	}
}
