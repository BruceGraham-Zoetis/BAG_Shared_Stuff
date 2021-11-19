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
	/**
	 * The name for the print job that is provided by Hub apps. 
	 */
	@NonNull
	private String printJobName;
}
