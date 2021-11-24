package com.zoetis.hub.platform.dto;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;

import org.json.JSONException;
import org.junit.jupiter.api.Test;

import com.fasterxml.jackson.databind.ObjectMapper;

public class UnitTestDtoSerDe_platform
{
	private final ObjectMapper objectMapper = new ObjectMapper();
	
	@Test
	void printFileDto_SerDeRT_WithoutDetails()
			throws IOException, JSONException
	{
		var dtoIsOut = new PrintFileDto();
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer);
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintFileDto.class);
			assertEquals (dtoIsOut, dtoIsIn);
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}
	
	@Test
	void printFileDto_SerDeRT_WithDetails()
			throws IOException, JSONException
	{
		int correlationID = 34567;
		String printerName = "HP LaserJet";
		String fileName = "/home/bag/test_files/file.pdf";
		boolean colorEnabled = false;
		boolean duplexEnabled = true;
		int     copies = 2;

		final var dtoIsOut = new PrintFileDto(
				correlationID,
				printerName,
				fileName,
				colorEnabled,
				duplexEnabled,
				copies);
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer.toString());
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintFileDto.class);
			assertEquals (dtoIsOut, dtoIsIn);
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}

	@Test
	void printJobCancelDto_SerDeRT_WithoutDetails()
			throws IOException, JSONException
	{
		var dtoIsOut = new PrintJobCancelDto();
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer);
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintJobCancelDto.class);
			assertEquals (dtoIsOut, dtoIsIn);
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}
	
	@Test
	void printJobCancelDto_SerDeRT_WithDetails()
			throws IOException, JSONException
	{
		int correlationID = 34567;

		final var dtoIsOut = new PrintJobCancelDto(correlationID);
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer.toString());
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintJobCancelDto.class);
			assertEquals (dtoIsOut, dtoIsIn);
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}
}
