======================
	TO DO
======================
define printer queue name vs. printer URI
use printer_queue_name
select_printer_queue
set_default_printer_queue(printer_queue_name, uri)
set_printing_options(dict_options : dict):

Unittest print results to log file.

rename doxygen output directory
  vetscan_hub_os_utilities_doxygen

work on pull request:

java version of openAPI client
diagram data flow dbus app <--> web app
  use doxygen command in a file to generate diagram.

printer
  support USB and WIFI.
  cups SUPPORT?

===========================
	TO DO - suspended
===========================
finish openapi_server tests



sync process - openAPI server -> DBus service
async process - websocket server

dbus_dracula
==================
* Add a timer to simulate signals to analyzer_webclient

openapi_server
==================
* security_controller_.py ? why no functions?


webclient
==================
* wait for connected server
* connect to dbus_dracula and get "signals".
* forward "signals" to hub_app

hub_app
===================
* wait for forwarded "signals" from analyzer_webclient.



