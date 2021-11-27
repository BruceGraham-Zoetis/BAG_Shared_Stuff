package com.zoetis.hub.platform.message;

import com.zoetis.hub.platform.dto.PrinterStateDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;

@NoArgsConstructor
public final class PrinterStateMessage extends PrintJobMessage<PrinterStateDto>
{
	public PrinterStateMessage(PrinterStateDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINTER_STATE;
	}
}

