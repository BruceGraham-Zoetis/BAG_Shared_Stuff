======================
	TO DO
======================
finish openapi_server tests
save tests to templates
save all controller files to templates
java version of openAPI client






sync process - openAPI server -> DBus service
async process - websocket server

dbus_dracula
==================
* use global analyzer object.
* Add a timer to simulate signals to analyzer_webclient

openapi_server
==================
* run copy_modified_files_to_templates.sh

* security_controller_.py ? why no functions?


webclient
==================
* wait for connected server
* connect to dbus_dracula and get "signals".
* forward "signals" to hub_app

hub_app
===================
* wait for forwarded "signals" from analyzer_webclient.

* Call APIs through generated code
* Add to class CVetscanAnalyzerInfo
* Move class CVetscanAnalyzerInfo to its own file.

MeasurementChannelApi.md
------------------------------------
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    
    try:
        api_response = api_instance.measurement_supported_consumables_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_supported_consumables_get: %s\n" % e)  


