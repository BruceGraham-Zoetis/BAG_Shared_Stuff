#!/usr/bin/env python3
# 
# File: test_analyzer_webclient.py

from __future__ import absolute_import


import asyncio
# pip3 install websockets
import websockets
import time
import datetime
import signal
import threading


async def analyzer_web_client():
    print("Running web client")

    uriServer = "ws://localhost:8765"

    while True:
        try:
            async with websockets.connect(uriServer) as websocket:
                # Close the connection when receiving SIGTERM.
                this_loop = asyncio.get_event_loop()
                this_loop.add_signal_handler(
                    signal.SIGTERM, this_loop.create_task, websocket.close())
                    
                print("Connected to Hub")

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


def start_loop(loop, client):
    loop.run_until_complete(client)
    loop.run_forever()


def start_thread_analyzer_web_client():
    new_loop = asyncio.new_event_loop()

    thread = threading.Thread(target=start_loop, args=(new_loop, analyzer_web_client))
    thread.start()


if __name__ == '__main__':
    print("")
    
    start_thread_analyzer_web_client()

