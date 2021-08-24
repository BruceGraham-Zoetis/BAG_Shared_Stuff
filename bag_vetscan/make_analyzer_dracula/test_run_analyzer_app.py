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
import signal


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


async def analyzer_web_client():
    uri = "ws://localhost:8765"

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to Hub")

                # Close the connection when receiving SIGTERM.
                loop = asyncio.get_event_loop()
                loop.add_signal_handler(
                    signal.SIGTERM, loop.create_task, websocket.close())

                bConnected = True

                strToServer = "set name dracula"
                print("analyzer(client) -> server(Hub)\n\t" + strToServer)
                try:
                    await websocket.send(strToServer)
                except:
                    print("Disconnected send")
                    bConnected = False

                while bConnected:
                    strToServer = "get datetime"
                    print("analyzer(client) -> server(Hub)\n\t" + strToServer)
                    try:
                        await websocket.send(strToServer)
                    except:
                        print("Disconnected send")
                        bConnected = False

                    try:
                        async for strFromClient in websocket:
                            print("server(Hub) -> analyzer(client)\n\t" + strFromClient)
                            strMsg = "analyzer_client "
                            strMsg = datetime.datetime.now().time()
                            print("analyzer(client) -> server(Hub)\n\t" + strMsg)
                    except:
                        #print("Disconnected receive")
                        #bConnected = False
                        pass

                    print("Delay...")
                    time.sleep(5)
        except:
            pass

        print("Trying to connect to Hub. Sleeping...")
        time.sleep(5)



if __name__ == '__main__':
    """
    print("Running web client")
    asyncio.get_event_loop().run_until_complete(analyzer_web_client())
    """

    print("Running openAPIs")
    analyzer_apis()
