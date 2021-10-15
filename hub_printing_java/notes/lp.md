CUPS - open source printing system
Originally standing for Common Unix Printing System.
CUPS allows a computer to act as a print server.

Uniform Resource Identifier (URI)


# Setup the printer
# -p Specifies the name of the printer to add.
# -E Enables the destination and accepts jobs.
# -v Sets the device-uri attribute of the print queue.
$ lpadmin -p HPOfficejetPro -E -v cups-brf:/


# list drivers and related information.

$ lpinfo -v
serial serial:/dev/ttyS0?baud=115200
network https
file cups-brf:/
network beh
network http
network lpd
network socket
network ipps
network ipp
direct hp
direct hpfax

# display the status of a printer
$ lpstat -p
printer CUPS-BRF-Printer is idle.  enabled since Wed 15 Sep 2021 02:21:22 PM EDT
printer HP is idle.  enabled since Wed 15 Sep 2021 05:10:52 PM EDT
printer HPOfficejetPro is idle.  enabled since Wed 15 Sep 2021 02:47:01 PM EDT

# lists available printers
$ lpstat -d
system default destination: CUPS-BRF-Printer

# print queue status
$ lpq
CUPS-BRF-Printer is ready
no entries
