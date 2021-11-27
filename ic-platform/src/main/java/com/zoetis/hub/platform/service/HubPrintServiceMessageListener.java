package com.zoetis.hub.platform.service;


import javax.print.attribute.standard.JobState;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobCancelDto;
import com.zoetis.hub.platform.dto.PrintJobStateDto;
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
	private KafkaTemplate<String, PrintJobStateDto> kafkaPrintJobState;
    
	@KafkaListener(topics = PrintAccessObjectMessage.TOPIC)
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
                logger.error("Unrecognized message received: {}", message);
            }
        }
        catch (Exception e)
        {
            logger.error("Error PrintAccessObjectListener", e);
        }
	}

	private void handlePrintFileMessage(PrintFileDto requestDetails)
	{
		try
		{
			System.out.println("Message: printFile");
			System.out.println("\tcorrelationID: " + requestDetails.getCorrelationID());
			System.out.println("\tprinterName: " + requestDetails.getPrinterName());
			System.out.println("\tfileName: " + requestDetails.getFileName());
			System.out.println("\tcolorEnabled: " + requestDetails.getColorEnabled());
			System.out.println("\tduplexEnabled: " + requestDetails.getDuplexEnabled());
			System.out.println("\tcopies: " + requestDetails.getCopies());

			if (prtAccObj.printFile(requestDetails))
			{
				PrintJobStateDto data = new PrintJobStateDto();
				data.setCorrelationID(requestDetails.getCorrelationID());
				data.setJobState(JobState.PROCESSING); 
				sendPrintJobState(data);
			}
			else
			{
				PrintJobStateDto data = new PrintJobStateDto();
				data.setCorrelationID(requestDetails.getCorrelationID());
				data.setJobState(JobState.ABORTED);
				sendPrintJobState(data);
			}
		}
		catch (PrintAccessException e)
		{
			logger.error("printFile", e.getErrorMsg());
		}
	}
	
	private void handlePrintJobCancelMessage(PrintJobCancelDto requestDetails)
	{
   		try
		{
			System.out.println("Message: printJobCancel");
			System.out.println(requestDetails.toString());

			prtAccObj.stopPrintJobProcessing();
   			
		}
		catch (PrintAccessException e)
		{
			logger.error("printJobCancel", e.getErrorMsg());
		}
	}
	
	private void sendPrintJobState(PrintJobStateDto data)
	{
		final String topic = "printJobState";
		
		System.out.println("Producer Topic: " + topic);
		System.out.println(data.toString());

		kafkaPrintJobState.send(topic, data);
	}
}
