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
import thread_notify_hub

def start_thread_notify_hub():
    print("Starting waiting for Hub")
    thread = threading.Thread(target=thread_notify_hub.thread_notify_hub)
    thread.start()


def thread_analyzer_web_client():
    print("Running web client")

    uriServer = "ws://localhost:8765"

    while True:
        try:
            with websockets.connect(uriServer) as websocket:
                # Close the connection when receiving SIGTERM.
                this_loop = asyncio.get_event_loop()
                this_loop.add_signal_handler(
                    signal.SIGTERM, this_loop.create_task, websocket.close())
                    
                print("Connected to Hub")

                bConnected = True

                strToServer = "set name dracula"
                print("analyzer(client) -> server(Hub)\n\t" + strToServer)
                try:
                    websocket.send(strToServer)
                except:
                    print("Disconnected send")
                    bConnected = False

                while bConnected:
                    strToServer = "get datetime"
                    print("analyzer(client) -> server(Hub)\n\t" + strToServer)
                    try:
                        websocket.send(strToServer)
                    except:
                        print("Disconnected send")
                        bConnected = False

                    try:
                        for strFromClient in websocket:
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

        #print("Trying to connect to Hub. Sleeping...")
        time.sleep(5)




def start_thread_analyzer_web_client():
    thread = threading.Thread(target = thread_analyzer_web_client)
    thread.start()
    return thread


if __name__ == '__main__':
    print("")

    start_thread_notify_hub()    
    threadClient = start_thread_analyzer_web_client()

