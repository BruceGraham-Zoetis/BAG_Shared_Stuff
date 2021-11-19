package com.zoetis.hub.platform.dto;

public class UnitTestDtoSerDe {

	public UnitTestDtoSerDe()
	{
		/*
		private final ObjectMapper objectMapper = new ObjectMapper ().registerModule (new JavaTimeModule ());
		
		@Test
		void instrumentStatusDtoSerDeRT_WithoutDetails () throws IOException, JSONException
		{
			var dtoIsOut = new InstrumentStatusDto (
				InstrumentStatus.IDLE, new InstrumentStatusDetailDto[] {}
			);
			String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
			
			var dtoIsIn = objectMapper.readValue (dtoSer, InstrumentStatusDto.class);
			assertEquals (dtoIsOut, dtoIsIn);
		}
		
		@Test
		void instrumentStatusDtoSerDeRT_WithDetails () throws IOException, JSONException
		{
			final var dtoDetail1 = new InstrumentStatusDetailDto (
				"SPE-999",
				"Connection error downloading software update.",
				StatusSeverity.RECOVERABLE,
				Instant.now ()
	    	);
			
			final var dtoDetail2 = new InstrumentStatusDetailDto (
				"SPE-998",
				"Software update signature check failed.",
				StatusSeverity.RECOVERABLE,
				Instant.now ()
	    	);
			
			var dtoIsOut = new InstrumentStatusDto (
				InstrumentStatus.IDLE, new InstrumentStatusDetailDto[] {dtoDetail1, dtoDetail2}
			);
			String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
			
			var dtoIsIn = objectMapper.readValue (dtoSer, InstrumentStatusDto.class);
			assertEquals (dtoIsOut, dtoIsIn);
		}
		*/
	}

}
