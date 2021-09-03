#!/bin/bash

# File: run_all.sh
# Purpose: starts the applications in the proper order.


########################################
# kill the Hub application
########################################
# python3 ./make_hub/test_run_hub_app.py
kill $(ps aux | grep '[p]ython ./make_hub/test_run_hub_app.py' | awk '{print $2}')

########################################
# kill the webclient application
########################################
# python3 ./make_webclient/test_webclient.py
kill $(ps aux | grep '[p]ython3 ./make_webclient/test_webclient.py' | awk '{print $2}')

########################################
# kill the DBusopenAPI Server application
########################################
# python3 ./make_openapi_server/test_run_openapi_server.py
kill $(ps aux | grep '[p]ython3 ./make_openapi_server/test_run_openapi_server.py' | awk '{print $2}')

########################################
# kill the DBus application
########################################
# python3 ./make_dbus_dracula/test_run_dbus_dracula.py
kill $(ps aux | grep '[p]ython3 ./make_dbus_dracula/test_run_dbus_dracula.py' | awk '{print $2}')

