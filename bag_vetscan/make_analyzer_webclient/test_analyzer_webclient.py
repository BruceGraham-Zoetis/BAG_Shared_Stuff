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
import socket


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
    print("sent name to Hub", flush=True)


def thread_analyzer_web_client():
    print("Running web client")

    uriServer = "ws://localhost:8765"

    while True:
        notify_hub_of_presence()

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

        print("Trying to connect to Hub. Sleeping...")
        time.sleep(5)




def start_thread_analyzer_web_client():
    new_loop = asyncio.new_event_loop()

    thread = threading.Thread(target = thread_analyzer_web_client)
    thread.start()


if __name__ == '__main__':
    print("")
    
    start_thread_analyzer_web_client()

