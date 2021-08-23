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

import asyncio
# pip3 install websockets
import websockets
import time
import datetime

def analyzer_apis():
    print("")

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


async def analyzer_client(uri):
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to Hub")
                strMsg = "analyzer_client "
                strMsg += datetime.datetime.now().time()
                await websocket.send(strMsg)
                print(strMsg)
        except:
            print("Trying to connect to Hub.")
            pass

        time.sleep(5)


if __name__ == '__main__':
    print()
    asyncio.get_event_loop().run_until_complete(
        analyzer_client('ws://localhost:8765'))

    analyzer_apis()
