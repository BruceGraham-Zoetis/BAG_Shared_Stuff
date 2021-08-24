#!/usr/bin/env python3
# 
# File: test_run_analyzer_app.py

from __future__ import absolute_import

import connexion

## fix path so that contained py files can be imported
import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
sys.path.append(strThisFilePath + "/analyzer_app")
from analyzer_app.openapi_server import encoder
from analyzer_app.openapi_server.controllers.CDBusDraculaService import CDBusDraculaService
import socket
import time


def analyzer_apis():
    print("Running openAPIs")

    app_options = {
        "swagger_ui": True
        #"swagger_ui": False
        }

    app = connexion.App(
                __name__,
                specification_dir='./analyzer_app/openapi_server/openapi/', 
                options = app_options)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Analyzer and HUB API'},
                pythonic_params=True)

    app.run(port=8080)



def notify_hub_of_presence():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # Enable port reusage so we will be able to run multiple clients and servers on single (host, port).
    # Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
    # For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
    # So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
    # Thanks to @stevenreddie
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    # Enable broadcasting mode
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    server.settimeout(0.2)

    message = b"dracula"
    server.sendto(message, ("localhost", 37020))
    print("message sent!", flush=True)


if __name__ == '__main__':
    print("")

    notify_hub_of_presence()    
    analyzer_apis()
