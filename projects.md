
## openAPI calls
dbus_dracula (service: com.zoetis.dracula)
  <--Methods-->
  <--Property getters setters-->
    DBus
      <--Methods-->
      <--Property getters setters-->
        d-feet (DBus monitor app)
        analyzer_dracula (openAPI Server)
          <--HTML-->
            hub_app (Web Client) xx.xx.xx.xx:8080/<SOME API PATH>
          <--HTML-->
            Chrome (Web Browser) xx.xx.xx.xx:8080/ui/#/<SOME API PATH>

## Events from Demon sent to Hub App
dbus_dracula (service: com.zoetis.dracula)
  [Signals-->
    DBus
      [Signals-->
        analyzer_webclient (Socket Client) uses python websockets
          [send-->
            hub_app (Socket Server) uses python websockets

## Directories and files
bag_vetscan
    make_analyzer_dracula			"Dracula" analyzer. Network server.
        make_analyzer.sh			Rebuild the "Dracula" analyzer server.
        templates				Files copied to analyzer_app.
        					Copied when the analyzer server is rebuilt.
        analyzer_app				The generated analyzer server.
        analyzer_dracula.code-workspace	Visual Studio Code - workspace
        test_run_analyzer_app.py		Runs the "Dracula" analyzer server.
        
    make_dbus_dracula				"Dracula" DBus deamon (DBus service).
        dbus_dracula.code-workspace		Visual Studio Code - workspace
        test_run_dbus_dracula.py		Runs the "Dracula" DBus deamon.
        
    make_hub					"Hub" GUI app. Network client.
        make_hub.sh				Rebuild the "Hub" GUI app.
        hub_app.code-workspace		Visual Studio Code - workspace
        hub_app				The generated analyzer client.
        templates				Files copied to hub_app.
        					Copied when the hub client is rebuilt.
        hub_app_gui				
            class_vetscan_hub.py		Hub and analyzer classes.
        					Hub contains a dictionary of analyzers.
        test_run_hub_app.py			Runs the "Hub" GUI app.
        
    analyzer_webclient
    	TODO - 
    	
    openAPISpecs
        openAPISpec.json			openAPI JSON file.
    
    


