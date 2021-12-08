package com.zoetis.hub.platform.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PrinterInfoDto
{
    private String  printQueueName; // Ex: "My Printer"
    private String  modelName;      // Ex: "HP Color LserJet Pro M454dw"
    private String  connection;     // TODO
    private String  printerLocation;  // Ex: "desk"
    private boolean isDefaultPrinter; // true: This is the default printer, false: not the default printer.

	public static void PrinterInfoDto_clear(PrinterInfoDto printerInfoDto)
	{
        printerInfoDto.printQueueName    = "";
        printerInfoDto.modelName         = "";
        printerInfoDto.connection        = "";
        printerInfoDto.printerLocation   = "";
        printerInfoDto.isDefaultPrinter  = false;
	}
	
	public static void PrinterInfoDto_init(
			PrinterInfoDto printerInfoDto,
			String  printQueueName,
		    String  modelName,
		    String  connection,
		    String  printerLocation,
		    boolean isDefaultPrinter)
	{
        printerInfoDto.printQueueName    = printQueueName;
        printerInfoDto.modelName         = modelName;
        printerInfoDto.connection        = connection;
        printerInfoDto.printerLocation   = printerLocation;
        printerInfoDto.isDefaultPrinter  = false;
	}
	
    public String toString()
    {
        StringBuilder sb = new StringBuilder();

        sb.append("{\n");
        sb.append("\"Queue\": " + "\"" + printQueueName + "\"" + ",\n");
        sb.append("\"Model\": " + "\"" + modelName + "\"" + ",\n");
        sb.append("\"Connection\": " + "\"" + connection + "\"" + ",\n");
        sb.append("\"Location\": " + "\"" + printerLocation + "\"" + ",\n");
        if (isDefaultPrinter)
            sb.append("\"Default\": " + "\"true\"\n");
        else
            sb.append("\"Default\": " + "\"false\"\n");

        sb.append("}\n");
        
        return sb.toString();
    }        


}
