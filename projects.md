

bag_vetscan
    make_analyzer_dracula			"Dracula" analyzer. Network server.
        make_analyzer.sh			Rebuild the "Dracula" analyzer server.
        templates				Files copied to analyzer_app.
        					Copied when the analyzer server is rebuilt.
        analyzer_app				The generated analyzer server.
        analyzer_dracula.code-workspace	Visual Studio Code - workspace
        test_run_analyzer_app.py		Runs the "Dracula" analyzer server.
        
    make_dbus_dracula				"Dracula" DBus demon (DBus service).
        dbus_dracula.code-workspace		Visual Studio Code - workspace
        test_run_dbus_dracula.py		Runs the "Dracula" DBus demon.
        
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
        
    openAPISpecs
        openAPISpec.json			openAPI JSON file.
        


