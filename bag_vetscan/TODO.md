======================
	TO DO
======================

openAPISpec.json object types
================================
The data type is "object" in CAnalyzerBase.py
Need to expose the object's type so that the type can be 
used in the generated DBus service interface type.
Ex: configuration_put(self, body)
openAPISpec.json:
        "/configuration": {
        ...
            "put": {
        	...
        	"requestBody": {
                    "required": true,
                    "content": {
			application/json": {
                            "schema": {
                                "type": "object",
                                "description": "An object containing the full configuration for the analyzer"
                            }
                        }

==================
Models
==================

can multiparameters be passed to DBus service?
======================================================
def measurement_results_get(start_datetime=None, end_datetime=None):  # noqa: E501

define models
==================
Sometimes you don't want a model generated.
 In this case, you can simply specify an import mapping
  to tell the codegen what not to create.
   When doing this, every location that references a specific model
    will refer back to your classes.
     Note, this may not apply to all languages...

To specify an import mapping,
 use the --import-mappings argument and
  specify the model-to-import logic as such:

--import-mappings Pet=my.models.MyPet


rename generated function names
===================================
add operationId to json

https://stackoverflow.com/questions/64206487/openapi-generator-typescript-angular-adds-numbers-to-the-end-of-methods-names

name parameter object
===========================
completed: add x-codegen-request-body-name to json file
  


printer utility changes
============================
define printer queue name vs. printer URI
use printer_queue_name
select_printer_queue
set_default_printer_queue(printer_queue_name, uri)
set_printing_options(dict_options : dict):

Unittest print results to log file.
========================================

rename doxygen output directory
====================================
  vetscan_hub_os_utilities_doxygen

work on pull request:

java version of openAPI client


diagram data flow dbus app <--> web app
========================================
  use doxygen command in a file to generate diagram.




printers
==================
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



