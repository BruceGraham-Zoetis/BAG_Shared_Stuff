package com.zoetis.hub.platform.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import com.zoetis.hub.platform.dto.PrintFileRequestDto;

@Service
public class Producer {
	public static final String topic = "mytopic";
	
	@Autowired
	private KafkaTemplate<String, PrintFileRequestDto> kafkaPrintFile;
	
	public void publishPrintFile(PrintFileRequestDto requestDetails) {
		
		String strFileName = requestDetails.getFileName();
		if ("" == strFileName)
		{
			return;
		}
		
		System.out.println("Publishing to topic " + topic);
		System.out.println(" printerName: " + requestDetails.getPrinterName());
		System.out.println(" fileName: " + requestDetails.getFileName());
		System.out.println(" colorEnabled: " + requestDetails.getColorEnabled());
		System.out.println(" duplexEnabled: " + requestDetails.getDuplexEnabled());
		System.out.println(" copies: " + requestDetails.getCopies());
				
		this.kafkaPrintFile.send(topic, requestDetails);
	}
	
	/*
	@Autowired
	private KafkaTemplate<String, String> kafkaTemplate;
	
	String kafkaTopic = "default-printer";
	
	public void send(String message) {
	    
	    kafkaTemplate.send(kafkaTopic, message);
	}
	*/
}
