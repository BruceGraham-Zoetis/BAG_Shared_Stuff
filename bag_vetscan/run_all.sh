#!/bin/bash

# File: run_all.sh
# Purpose: starts the applications in the proper order.

########################################
# start the DBus application
########################################
python3 ./make_dbus_dracula/run_dbus_dracula.py &
dbus_dracula_pid=$!
# dbus_dracula_pid is the python3 process that is running the DBus app.
## name: python3 ./make_dbus_dracula/run_dbus_dracula.py
echo "Dracula DBus pid $dbus_dracula_pid"

# wait for task to end
# wait $dbus_dracula_pid

########################################
# start the openAPI Server application
########################################
python3 ./make_openapi_server/run_openapi_server.py &
openapi_server_pid=$!
# openapi_server_pid is the python3 process that is running the openAPI Server app.
echo "Dracula openAPI server pid $openapi_server_pid"

########################################
# start the webclient application
########################################
#python3 ./make_webclient/webclient.py &
#webclient_pid=$!
# webclient_pid is the python3 process that is running the webclient app.
#echo "Dracula webclient pid $webclient_pid"

########################################
# start the Hub application
########################################
#python3 ./make_hub/run_hub_app.py &
#hub_pid=$!
# hub_pid is the python3 process that is running the Hub app.
#echo "Hub pid $hub_pid"



