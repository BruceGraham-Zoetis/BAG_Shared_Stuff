======================
	TO DO
======================
work on pull request: https://github.com/ZoetisDenmark/vetscan-hub-os-utilities/pull/1

java version of openAPI client
diagram data flow dbus app <--> web app



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



