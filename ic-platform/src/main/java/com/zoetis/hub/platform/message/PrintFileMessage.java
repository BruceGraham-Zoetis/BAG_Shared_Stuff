package com.zoetis.hub.platform.message;

import com.fasterxml.jackson.annotation.JsonTypeName;
import com.zoetis.hub.platform.dto.PrintFileDto;

import lombok.NoArgsConstructor;
import lombok.NonNull;

@NoArgsConstructor
@JsonTypeName("PRINT_FILE")
public final class PrintFileMessage extends PrintAccessObjectMessage<PrintFileDto>
{
	public PrintFileMessage(PrintFileDto payload)
	{
		super(payload);
	}

	@NonNull
	@Override
	public Action getAction ()
	{
		return Action.PRINT_FILE;
	}
}
