======================
	TO DO
======================


dbus_dracula
==================
* use global analyzer object.
* Add a timer to simulate signals to analyzer_webclient

analyzer_dracula
==================
* run copy_modified_files_to_templates.sh

* security_controller_.py ? why no functions?


analyzer_webclient
==================
* wait for connected server
* connect to dbus_dracula and get "signals".
* forward "signals" to hub_app

hub_app
===================
* wait for connected clients
* wait for forwarded "signals" from analyzer_webclient.

  


