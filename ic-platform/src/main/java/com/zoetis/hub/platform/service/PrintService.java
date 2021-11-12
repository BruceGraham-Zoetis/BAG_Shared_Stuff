package com.zoetis.hub.platform.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;

@Service
public class PrintService {
    
    @Autowired
    PrinterAccessObject obj;
    
	@KafkaListener(topics="print", groupId="groupPrinterAccess")
	public void consumePrintFile(PrintFileRequestDto requestDetails) throws PrintAccessException
	{
		System.out.println("Topic: print");
		System.out.println("\tprinterName: " + requestDetails.getPrinterName());
		System.out.println("\tfileName: " + requestDetails.getFileName());
		System.out.println("\tcolorEnabled: " + requestDetails.getColorEnabled());
		System.out.println("\tduplexEnabled: " + requestDetails.getDuplexEnabled());
		System.out.println("\tcopies: " + requestDetails.getCopies());
		
		obj.enableColor(requestDetails.getColorEnabled());
		obj.enableDuplex(requestDetails.getDuplexEnabled());
		obj.setCopies(requestDetails.getCopies());
		
		try
		{
			obj.printFile(requestDetails.getFileName());
		}
		catch (PrintAccessException e)
		{
			System.err.println(e.getErrorMsg());
		}
	}

    
}