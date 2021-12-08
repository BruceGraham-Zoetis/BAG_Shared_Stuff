PrinterAccessObject
========================================
This class provides functions for:
* determine installed printers
* select a printer for printing
* printing from a file's input stream
* printing PDF and TXT files
* monitoring print job processing
* monitoring status of the print job in the print queue

Assumptions
-----------------
Only one printer will be installed.
	The printer will be setup as the default printer.

Printer Setup
	A Zoetis tech will add/remove and setup the printer.

The default printer basic printing requirements.
	* PostScript files,
	* PDF files,
	* text files.

Only 1 print job will be managed at a time.
	Start and cancel a print job.

Supported printer options:
	Duplex vs single sided
	Color vs Black and White
	Number of copies

If the printer supports an option, then the provide functions for setting option.

Requirements
========================
The Java object that is able to interface with printers shall be
integrated into the Operating System Interface microservice.
Associated Kafka messaging should be specified and documented as part of this task.


Language
--------------
Java


APIs
==================

Printer Management
-------------------------
	Get default printer's name.
		getDefaultPrintername()

	Get map containing a list of available printers.
	Uses class PrinterInfo to make it easier to get printer info.
		getPrinters()

	Verify that the default printer can meet the basic printing requirements.
		isPdfSupported()

Printing for file types
-------------------------------
	Print file using formats: PDF, Text
		printFile(String pathFileName)

	Print stream from file.
		printFile(FileInputStream fileInputStream)

	Cancel print job
		stopPrintJobProcessing()

Printing options supported
-----------------------------
Query, enable or enable a printer supported printing option.

	DUPLEX
	Printing of a sheet of paper on both sides automatically.
		isDuplexSuported()
		enableDuplex(boolean bEnable)
		isDuplexEnabled()

	Color vs Monochrome
		isColorSuported()
		enableColor(boolean bEnable)
		isColorEnabled()

	Number of copies
		setCopies(int nCopies))
		getCopies()

	SheetCollate
	The printer “accumulates” these documents together to create a complete set.
		isSheetCollateSupported()
		enableSheetCollate()
		isSheetCollateEnabled()


Printing Processing status
-----------------------------
Note that when processing is complete, the print job is sent to the printer queue.
The printer has not printed the document yet.
You need to check the printer queue to see if it is empty.

	Provide status for the print job.
		isPrintJobProcessingCompleted()

	Wait for the print job processing to complete.
		waitForPrintJobProcessingCompleted()


Printer Queue info
-------------------------------
Note that when the printer queue is empty, the printer may have buffered the print data
and may not have completed printing the last page.

	Get the count of print jobs in the printer's queue.
		getPrinterQueueCount()

	Monitor print job's progress in the print queue.
	Get the state and reason for the state.
	The reason string is the driver's response to an event. Your printer's responses may differ.
		getPrinterState()

		-- Typical printer states and reasons when the printer is off before printing, then turned on. --
		State: E_QUEUE_STATE_STOPPED  Reason: Connecting to printer.
		State: E_QUEUE_STATE_STOPPED  Reason: The printer is not responding.
		State: E_QUEUE_STATE_PROCESSING  Reason: Print job is queued.
		State: E_QUEUE_STATE_PROCESSING  Reason: Waiting for printer to finish.


Printing errors
--------------------------------
Class PrintAccessException provides printer error handling.
If the printer is out of paper, or has a paper jam, the printer diver may not provide
this info, so you will not get an error during printing.

	Get the error ID.
		getErrorID()

	Get the error message.
		getErrorMsg()

CUPS
---------------------
CUPS Service in Ubuntu 16.04 is defaulting to on-demand mode and Java can't wake-up the CUPS service to query the printer.
Change the CUPS Service to always running by modifying /lib/systemd/system/cups.service
  from ExecStart=/usr/sbin/cupsd -l
  into ExecStart=/usr/sbin/cupsd -f






