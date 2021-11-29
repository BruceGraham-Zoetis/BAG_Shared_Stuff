package com.zoetis.hub.platform.dto;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.io.IOException;
import java.net.URL;

import javax.print.attribute.standard.JobState;
import javax.print.attribute.standard.PrinterState;
import javax.print.attribute.standard.PrinterStateReason;

import org.json.JSONException;
import org.junit.jupiter.api.Test;

import com.fasterxml.jackson.databind.ObjectMapper;

public class UnitTestDtoSerDe_platform
{
	private final ObjectMapper objectMapper = new ObjectMapper();
	
	//////////////////////////////////////////
	// PrintFileDto
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
			assertEquals (dtoIsOut.toString(), dtoIsIn.toString());
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
		String fileName;
		boolean colorEnabled = false;
		boolean duplexEnabled = true;
		int     copies = 2;
		
		URL url = getClass().getClassLoader().getResource("file.pdf");
		fileName = url.getFile();
        assertNotNull(fileName);

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
			assertEquals (dtoIsOut.toString(), dtoIsIn.toString());
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}

	//////////////////////////////////////////
	// PrintJobCancelDto
	@Test
	void PrintJobCancelDto_SerDeRT_WithoutDetails()
			throws IOException, JSONException
	{
		var dtoIsOut = new PrintJobCancelDto();
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer);
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintJobCancelDto.class);
			assertEquals (dtoIsOut.toString(), dtoIsIn.toString());
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}
	
	@Test
	void PrintJobCancelDto_SerDeRT_WithDetails()
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
			assertEquals (dtoIsOut.toString(), dtoIsIn.toString());
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}

	//////////////////////////////////////////
	// PrintJobStateDto
	@Test
	void printJobStateDto_SerDeRT_WithoutDetails()
			throws IOException, JSONException
	{
		int correlationID = 34567;

		var dtoIsOut = new PrintJobStateDto();
		dtoIsOut.setCorrelationID(correlationID);
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer);
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintJobStateDto.class);
			assertEquals (dtoIsOut.toString(), dtoIsIn.toString());
		}
		catch (Exception e)
		{
			System.out.println(e);
			assert(false);
		}
	}
	
	@Test
	void printJobStateDto_SerDeRT_WithDetails()
			throws IOException, JSONException
	{
		int correlationID = 34567;

		final var dtoIsOut = new PrintJobStateDto();
		dtoIsOut.setCorrelationID(correlationID);
		dtoIsOut.jobState = JobState.PROCESSING.getValue();
		dtoIsOut.printerState = PrinterState.STOPPED.getValue();
		//dtoIsOut.setPrinterState(PrinterState.STOPPED);
		dtoIsOut.addPrinterStateReason(PrinterStateReason.COVER_OPEN);
		dtoIsOut.addPrinterStateReason(PrinterStateReason.DOOR_OPEN);
		System.out.println(dtoIsOut.toString());
		String dtoSer = objectMapper.writeValueAsString (dtoIsOut);
		System.out.println(dtoSer.toString());
		
		try
		{
			var dtoIsIn = objectMapper.readValue (dtoSer, PrintJobStateDto.class);
			System.out.println("dtoIsOut " + dtoIsOut);
			System.out.println("dtoIsIn " + dtoIsIn);
			assertEquals (dtoIsOut.toString(), dtoIsIn.toString());
		}
		catch (Exception e)
		{
			System.out.println(e);
			assertEquals(true, false);
		}
	}
}
