======================
	TO DO
======================


dbus_dracula
==================
* Add a timer to simulate signals to analyzer_webclient

analyzer_dracula
==================
* connect the web API calls to the DBus deamon.
    finish adding calls to draculad to generated file.

	def measurement_supported_consumables_get():
	    oDracula = CDBusDraculaService()
	    strConsumables = oDracula.draculad.measurement_supported_consumables_get()
	    return strConsumables
   
* run copy_modified_files_to_templates.sh


analyzer_webclient
==================
* connect to dbus_dracula and get "signals".
* forward "signals" to hub_app

hub_app
===================
* wait for forwarded "signals" from analyzer_webclient.

  


