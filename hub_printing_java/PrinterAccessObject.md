PrinterAccessObject
========================================

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

	Verify that the default printer can meet the basic printing requirements.
		isPdfSupported()

	Use a test file to verify printing to the printer works.
		printTestFile()

Printing for file types
-------------------------------
	File formats: PDF, Text
		printFile(String pathFileName)
	Cancel print job
		cancelPrintJob()

Printing options supported
-----------------------------
Query, set or get a printer supported printing options.
	TODO getAttributes
	DUPLEX
		isDuplexSuported()
		enableDuplex(boolean bEnable)
		isDuplexEnabled()

	Color vs Black and White
		isColorSuported()
		enableColor(boolean bEnable)
		isColorEnabled()

	Number of copies
		setCopies(int nCopies))
		getCopies()

	SheetCollate
		isSheetCollateSupported()
		enableSheetCollate()
		isSheetCollateEnabled()


Printing status
-----------------------------
Provide status for the print job.
	isPrintJobComplete()

Printing errors
--------------------------------
Provide printer error handling.
Provide print queue error handling.
Handle exception.
	getPrinterError()?
		printer ink levels
		paper jam
	getPrintQueueError()?
		printer off-line


CUPS
---------------------
CUPS Service in Ubuntu 16.04 is defaulting to on-demand mode and Java can't wake-up the CUPS service to query the printer.
Change the CUPS Service to always running by modifying /lib/systemd/system/cups.service
  from ExecStart=/usr/sbin/cupsd -l
  into ExecStart=/usr/sbin/cupsd -f






