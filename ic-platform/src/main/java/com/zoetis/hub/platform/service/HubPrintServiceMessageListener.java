package com.zoetis.hub.platform.service;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobAbortedDto;
import com.zoetis.hub.platform.dto.PrintJobCancelDto;
import com.zoetis.hub.platform.dto.PrintJobCompletedDto;
import com.zoetis.hub.platform.message.PrintAccessObjectMessage;
import com.zoetis.hub.platform.message.PrintFileMessage;
import com.zoetis.hub.platform.message.PrintJobCancelMessage;

@Service
public class HubPrintServiceMessageListener
{
    @Autowired
    PrinterAccessObject prtAccObj;
    
    private Logger logger = LoggerFactory.getLogger (HubPrintServiceMessageListener.class); 
	
	@Autowired
    private ObjectMapper objectMapper;
    
	@Autowired
	private KafkaTemplate<String, PrintJobCompletedDto> kafkaPrintJobCompleted;
    
	@Autowired
	private KafkaTemplate<String, PrintJobAbortedDto> kafkaPrintJobAborted;
    
	@KafkaListener(topics = PrintAccessObjectMessage.TOPIC,  groupId = "printAccessObject")
	public void PrintAccessObjectListener(String messageJson) throws PrintAccessException
	{
		prtAccObj.setDebugTrace(true);
        try
        {
            logger.info ("Received Topic printAccessObject message: {}", messageJson);
            var message = objectMapper.readValue (messageJson, PrintAccessObjectMessage.class);
            logger.info ("Parsed Topic printAccessObject message: {}", message);

            if (message instanceof PrintFileMessage)
            {
            	PrintFileDto requestDetails;
            	try
            	{
            		requestDetails = (PrintFileDto) message.getPayload();
            	    handlePrintFileMessage(requestDetails);
            	}
                catch (Exception e)
                {
                	logger.error("Error message to printFileDto", e);
                }
            }
            else if (message instanceof PrintJobCancelMessage)
            {
            	PrintJobCancelDto requestDetails;
            	try
            	{
	            	requestDetails = (PrintJobCancelDto) message.getPayload();
	    			handlePrintJobCancelMessage(requestDetails);  
            	}
                catch (Exception e)
                {
                	logger.error("Error message to PrintJobCancelDto", e);
                }
            }
            else
            {
                logger.warn("Unrecognized message received: {}", message);
            }
        }
        catch (Exception e)
        {
            //logger.error("Error handling printFile message", e);
        	
        	// TODO - Define an error message
			PrintJobAbortedDto data = new PrintJobAbortedDto();
			data.setPrintJobName("printjob failed");
			sendPrintJobAborted(data);
        }
	}

	private void handlePrintFileMessage(PrintFileDto requestDetails)
	{
		try
		{
			System.out.println("Message: printFile");
			System.out.println("\tprintJobName: " + requestDetails.getPrintJobName());
			System.out.println("\tprinterName: " + requestDetails.getPrinterName());
			System.out.println("\tfileName: " + requestDetails.getFileName());
			System.out.println("\tcolorEnabled: " + requestDetails.getColorEnabled());
			System.out.println("\tduplexEnabled: " + requestDetails.getDuplexEnabled());
			System.out.println("\tcopies: " + requestDetails.getCopies());

			if (prtAccObj.printFile(requestDetails))
			{
				PrintJobCompletedDto data = new PrintJobCompletedDto();
				data.setPrintJobName(requestDetails.getPrintJobName());
				sendPrintJobCompleted(data);
			}
			else
			{
				PrintJobAbortedDto data = new PrintJobAbortedDto();
				data.setPrintJobName(requestDetails.getPrintJobName());
				sendPrintJobAborted(data);
			}
		}
		catch (PrintAccessException e)
		{
			logger.error(e.getErrorMsg());
			
			PrintJobAbortedDto data = new PrintJobAbortedDto();
			data.setPrintJobName("printFile failed");
			sendPrintJobAborted(data);
		}
	}
	
	private void handlePrintJobCancelMessage(PrintJobCancelDto requestDetails)
	{
   		try
		{
			System.out.println("Message: printJobCancel");
			System.out.println("\tprintJobName: " + requestDetails.getPrintJobName());
			prtAccObj.stopPrintJobProcessing();
   			
		}
		catch (PrintAccessException e)
		{
			// TODO - define a print service error message
			PrintJobAbortedDto data = new PrintJobAbortedDto();
			data.setPrintJobName("printJobCancel failed");
			sendPrintJobAborted(data);
		}
	}
	
	private void sendPrintJobCompleted(PrintJobCompletedDto data)
	{
		final String topic = "printJobState";
		
		System.out.println("Producer Topic: " + topic);
		System.out.println("\tprintJobName: " + data.getPrintJobName());
				
		kafkaPrintJobCompleted.send(topic, data);
	}

	private void sendPrintJobAborted(PrintJobAbortedDto data)
	{
		final String topic = "printJobState";
		
		System.out.println("Producer Topic: " + topic);
		System.out.println("\tprintJobName: " + data.getPrintJobName());
		kafkaPrintJobAborted.send(topic, data);
	}
}
