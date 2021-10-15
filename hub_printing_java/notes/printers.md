VETSCAN Instrument Controller Development VSIC-690
========================================================
VETSCAN Instrument Controller Development
Identify and Procure Example Printers for HUB Printer Testing

Description
--------------
Identify and procure printers that can be used to develop and test HUB printing functionality against.

Between all the printers identified, the following qualities are required:

1) Black and white only printing
2) Color or black and white printing
3) Network printer
4) USB printer
5) Printer that can print on both sides of a piece of paper.
6) Big name printer (ie HP, Brother, Cannon, etc)
7) Generic printer from relatively unknown company (ie Pantum)


Printers for Procurement
================================

Epson Expression Home XP-4100
---------------------------------
	Color Inkjet All-In-One Printer

	Connections:
		USB 2.0 Hi-Speed
		Wireless (802.11 b/g/n)2
		Wi-Fi Direct2 (4 connections)

	Printing Protocol:
		+ Line Printer Daemon protocol/Line Printer Remote protocol (or LPD, LPR)
			
	Linux Printer Setup:
		https://epson.com/faq/SPT_C11CG33201~faq-00004dc-shared?faq_cat=faq-8796127602764
		http://download.ebz.epson.net/man/linux/utility.html
		* Add new printer in Linux Printer dialog or CUPS Service http://localhost:631/.
		Example USB URL: usb://EPSON/XP-4100/
		Example LPD URL: lpd://192.168.1.3/

	$99.99 Office Max


HP DeskJet 2742e All-in-One Wireless
---------------------------------------
	Color Inkjet Printer (Sequoia)

	HP DeskJet 2700 All-in-One Printer series

	https://developers.hp.com/hp-linux-imaging-and-printing
	https://developers.hp.com/hp-linux-imaging-and-printing/supported_devices/index

	Printing Protocol:
		+ HPLIP
			License: GNU General Public License
			HPLIP (HP Linux Imaging & Printing) is an HP-developed solution for printing,
			scanning, and faxing with HP inkjet and laser printers in Linux.
		+ IPP (CUPS)

	Connections:
		Wireless 802.11a/b/g/n
		USB 2.0 Hi-Speed

	Linux Printer Setup
		https://developers.hp.com/hp-linux-imaging-and-printing/howtos/install
		* HPLIP should be already installed.
		* Add new printer in Linux Printer dialog or CUPS Sservice http://localhost:631/.
	
	$59.00 Walmart


Brother HL-L2370DW
--------------------------
	Wireless Monochrome (Black And White) Compact Laser Printer
	with Wireless & Ethernet and Duplex Printing
	Duplex Printing

	Connections:
		Wireless 802.11 b/g/n,
		Ethernet, 10/100 Base-TX Ethernet,
		WiFi Direct,
		USB 2.0 Hi-Speed

	Printing Protocol:
		Supported Network Protocols (IPv4)
			ARP, RARP, BOOTP, DHCP, APIPA (Auto IP), WINS/NetBIOS Name Resolution,
			DNS Resolver, mDNS, LLMNR Responder,
			+ LPR/LPD,
			+ Custom Raw Port/Port 9100,
			+ IPP,
			FTP Server, SNMPv1/v2c/v3,
			HTTP Server, TFTP Client and Server,
			SMTP Client, ICMP, Web Services (Print/Scan)
		Supported Network Protocols (IPv6)
			NDP, RA, DNS Resolver, mDNS, LLMNR Responder,
			+ LPR/LPD,
			+ Custom Raw Port/Port 9100,
			+ IPP,
			FTP Server,
			SNMPv1/v2c/v3,
			HTTP Server,
			TFTP Client and Server, SMTP Client, ICMPv6, LLTD Responder,
			Web Services (Print/Scan)

	Linux Printer Setup:
		https://kbpdfstudio.qoppa.com/install-printer-driver-on-linux/
		* Install driver
		* Add new printer in Linux Printer dialog or CUPS Sservice http://localhost:631/.

	$152.99 OfficeMax OfficeDepot


Pantum P2502W Wireless/USB Monochrome Laser Printer
---------------------------------------------------
	Printing Protocol:
		+ USB 2.0 High speed
		+ Wi-Fi 802.11b/g/n
		+ AirPrint (IPP)
		Web Services (Print/Scan)

	Linux Printer Setup:
		https://global.pantum.com/global/wp-content/uploads/2021/03/P2200-P2500-Serial-Printers-FAQ-V2020Q4.pdf
		https://askubuntu.com/questions/573839/how-can-i-install-a-pantum-2502w-laser-printer-on-ubuntu
		https://global.pantum.com/global/drive/2500w/
		* Use Web Services to setup the printer.
			For example, on a PC, or the vetscan, open chrome, enter the printer's web sevice page. Ex: 192.168.1.2/index.html
		* download driver from pantum.com
		* install driver
		-- USB
			* plug printer into A USB port.
		-- Network
			* connect the printer to the network.
			* get the printer's IP Address from its Web Services Network Settings page.
		* In the Vetscan desktop, open the printers application and choose Add. You should see the printer.
		* Select the printer. The printer properties dialog will open.
		* Enter the printer's properties for the printer's URL.

	$146.00 Walmart
