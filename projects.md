
Notes:
    * d-feet
        Linux DBus monitor application.
    
    * dbus_dracula
        DBus service: com.zoetis.dracula
    
    * hub_app
       Socket Server
           uses python websockets
       Web Client
           uses xx.xx.xx.xx:8080/<SOME API PATH>

    * Web Browser
         Ex: Chrome
         uses xx.xx.xx.xx:8080/ui/#/<SOME API PATH>
         
    * webclient
        Socket Client
            uses python websockets
            
## openAPI calls
dbus_dracula
  <--Methods-->
  <--Property getters setters-->
    DBus
      <--Methods-->
      <--Property getters setters-->
        d-feet
        openapi_server
          <--HTML-->
            hub_app
          <--HTML-->
            Web Browser

## Events from Deamon sent to Hub App
dbus_dracula
  [Signals-->
    DBus
      [Signals-->
        webclient
          [send-->
            hub_app

## Directories and files
bag_vetscan\
    make_openapi_server\			openAPI server: "Dracula"
        make_openapi_server.sh		Rebuild the "Dracula" analyzer server.
        templates\				Files copied to analyzer_app.
        					Copied when the analyzer server is rebuilt.
        analyzer_app\				The generated analyzer server.
        openapi_server.code-workspace	Visual Studio Code - workspace
        test_run_openapi_server.py		Runs the "Dracula" analyzer server.
        
    make_dbus_dracula\				DBus service (aka deamon): "Dracula"
        dbus_dracula.code-workspace		Visual Studio Code - workspace
        test_run_dbus_dracula.py		Runs the "Dracula" DBus deamon.
        
    make_hub\					openAPI client, webserver, GUI: "Hub"
        make_hub.sh				Rebuild the "Hub" app.
        hub_app.code-workspace		Visual Studio Code - workspace
        hub_app\				The generated analyzer client.
        templates\				Files copied to hub_app.
        					Copied when the hub client is rebuilt.
        hub_app_gui\				
            class_vetscan_hub.py		Hub and analyzer classes.
        					Hub contains a dictionary of analyzers.
        test_run_hub_app.py			Runs the "Hub" GUI app.
        
    make_webclient\
    	TODO - 
    	
    openAPISpecs\
        openAPISpec.json			openAPI JSON file.
    
    


