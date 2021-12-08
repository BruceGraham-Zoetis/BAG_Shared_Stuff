package com.zoetis.hub.PrintFileMessageTest;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.io.IOException;

import org.json.JSONException;
import org.junit.jupiter.api.Test;
import org.skyscreamer.jsonassert.JSONAssert;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.zoetis.hub.platform.message.PrintAccessObjectMessage;
import com.zoetis.hub.platform.message.PrintFileMessage;
import com.zoetis.hub.platform.message.PrintJobCancelMessage;

public class PrintFileMessageTest
{
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Parses a JSON message as a PrintAccessObjectMessage, checks that it is resolved to the expected type,
     * and checks that converting back to JSON results in the same content.
     */
    private void deserializesPrintAccessObjectMessage(
            String resourcePath,
            Class<? extends PrintAccessObjectMessage<?>> type
    ) throws IOException, JSONException {
        var resourceStream = getClass().getClassLoader().getResourceAsStream(resourcePath);
        assertNotNull(resourceStream);
        var jsonMessage = new String(resourceStream.readAllBytes());

        var message = objectMapper.readValue(jsonMessage, PrintAccessObjectMessage.class);

        // Make sure it parsed to the correct type
        assertEquals(type, message.getClass());

        // Compare the result matches the initial JSON
        JSONAssert.assertEquals(jsonMessage, objectMapper.writeValueAsString(message), false);
    }

    @Test
    void deserializesPrintFileMessage() throws IOException, JSONException {
        deserializesPrintAccessObjectMessage("print-file.json", PrintFileMessage.class);
    }

    @Test
    void deserializesPrintJobCancelMessage() throws IOException, JSONException {
        deserializesPrintAccessObjectMessage("printjob-cancel.json", PrintJobCancelMessage.class);
    }
}
