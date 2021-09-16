======================
	TO DO
======================
remove non-volume control files from checkin.

$ uname -n
    mockup lubuntu & virtual machine:  mixer -D pulse set Master 50%
​
    mockup lubuntu & yocto on D0: mixer set Master 50%


Add types to parameters and return types.

        @return: int - Range [0 - 100] the master volume, as a percent of max volume.
        @return: int - -1 there was an error

Add doxygen style comments to test functions

test values: -100, -1, 0, 1, 100, 10


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



