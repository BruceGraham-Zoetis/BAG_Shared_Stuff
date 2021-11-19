package com.zoetiz.hub.PrintFileMessageTest;

public class PrintFileMessageTest
{

	public PrintFileMessageTest()
	{
	    //private final ObjectMapper objectMapper = new ObjectMapper();

	    /**
	     * Parses a JSON message as a DiscoveryMessage, checks that it is resolved to the expected type,
	     * and checks that converting back to JSON results in the same content.
	     */
		/*
	    private void deserializesDiscoveryMessage(
	            String resourcePath,
	            Class<? extends DiscoveryMessage<?>> type
	    ) throws IOException, JSONException {
	        var resourceStream = getClass().getClassLoader().getResourceAsStream(resourcePath);
	        assertNotNull(resourceStream);
	        var jsonMessage = new String(resourceStream.readAllBytes());

	        var message = objectMapper.readValue(jsonMessage, DiscoveryMessage.class);

	        // Make sure it parsed to the correct type
	        assertEquals(type, message.getClass());

	        // Compare the result matches the initial JSON
	        JSONAssert.assertEquals(jsonMessage, objectMapper.writeValueAsString(message), false);
	    }

	    @Test
	    void deserializesPresentMessage() throws IOException, JSONException {
	        deserializesDiscoveryMessage("instrument-present.json", InstrumentPresentMessage.class);
	    }

	    @Test
	    void deserializesConnectedMessage() throws IOException, JSONException {
	        deserializesDiscoveryMessage("instrument-connected.json", InstrumentConnectedMessage.class);
	    }

	    @Test
	    void deserializesStatusMessage() throws IOException, JSONException {
	        deserializesDiscoveryMessage("instrument-status.json", InstrumentStatusMessage.class);
	    }

	    @Test
	    void deserializesRemoveMessage() throws IOException, JSONException {
	        deserializesDiscoveryMessage("instrument-remove.json", InstrumentRemoveMessage.class);
	    }
	    */
	}

}
