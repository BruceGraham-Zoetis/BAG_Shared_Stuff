package com.zoetis.hub.PrintJobMessageTest;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.io.IOException;

import org.json.JSONException;
import org.junit.jupiter.api.Test;
import org.skyscreamer.jsonassert.JSONAssert;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.zoetis.hub.platform.message.PrintJobMessage;
import com.zoetis.hub.platform.message.PrintJobProcessingMessage;
import com.zoetis.hub.platform.message.PrinterStateMessage;

public class PrintJobMessageTest
{
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Parses a JSON message as a PrintJobMessage, checks that it is resolved to the expected type,
     * and checks that converting back to JSON results in the same content.
     */
    private void deserializesPrintJobMessage(
            String resourcePath,
            Class<? extends PrintJobMessage<?>> type
    ) throws IOException, JSONException {
        var resourceStream = getClass().getClassLoader().getResourceAsStream(resourcePath);
        assertNotNull(resourceStream);
        var jsonMessage = new String(resourceStream.readAllBytes());

		try
		{
			var message = objectMapper.readValue(jsonMessage, PrintJobMessage.class);

	        // Make sure it parsed to the correct type
	        assertEquals(type, message.getClass());

	        // Compare the result matches the initial JSON
	        JSONAssert.assertEquals(jsonMessage, objectMapper.writeValueAsString(message), false);
		}
		catch (Exception e)
		{
			System.out.println(e);
		}
    }

    @Test
    void deserializesPrintJobProcessingMessage() throws IOException, JSONException {
        deserializesPrintJobMessage("printjob-processing.json", PrintJobProcessingMessage.class);
    }

    @Test
    void deserializesPrinterStateMessage() throws IOException, JSONException {
        deserializesPrintJobMessage("printer-state.json", PrinterStateMessage.class);
    }
}
