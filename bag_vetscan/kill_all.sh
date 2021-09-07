#!/bin/bash

# File: kill_all.sh
# Purpose: kills the applications in the proper order.


########################################
# kill the Hub application
########################################
# python3 ./make_hub/run_hub_app.py
kill $(ps aux | grep '[p]ython ./make_hub/run_hub_app.py' | awk '{print $2}')

########################################
# kill the webclient application
########################################
# python3 ./make_webclient/webclient.py
kill $(ps aux | grep '[p]ython3 ./make_webclient/webclient.py' | awk '{print $2}')

########################################
# kill the DBusopenAPI Server application
########################################
# python3 ./make_openapi_server/run_openapi_server.py
kill $(ps aux | grep '[p]ython3 ./make_openapi_server/run_openapi_server.py' | awk '{print $2}')

########################################
# kill the DBus application
########################################
# python3 ./make_dbus_dracula/run_dbus_dracula.py
kill $(ps aux | grep '[p]ython3 ./make_dbus_dracula/run_dbus_dracula.py' | awk '{print $2}')

