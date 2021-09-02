#!/usr/bin/env python3
# coding: utf-8

"""
File: thread_webclient.py
"""

from __future__ import absolute_import


import asyncio
# pip3 install websockets
import websockets
import time
import datetime
import signal
import threading


class class_analyzer_web_client(threading.Thread):
    def __init__(self, uriServer):
        self.uriServer = uriServer
        self.websocket = {}
        self.terminate = False

    # Override the run() function of Thread class
    def run(self):
        try:
            print("Running web client")

            while not self.terminate:
                try:
                    with websockets.connect(self.uriServer) as self.websocket:
                        self.__stay_connected()
                except:
                    if (not self.terminate):
                        print("Trying to connect to Hub. Sleeping...")
                        time.sleep(5)
        finally:
            #print("thread ended")
            pass

    def terminate_thread(self):
        self.terminate = True

    def __stay_connected(self):
        # Close the connection when receiving SIGTERM.
        this_loop = asyncio.get_event_loop()
        this_loop.add_signal_handler(
            signal.SIGTERM, this_loop.create_task, self.websocket.close())
            
        print("Connected to Hub")

        bConnected = True

        strToServer = "set name dracula"
        print("analyzer(client) -> server(Hub)\n\t" + strToServer)
        try:
            self.websocket.send(strToServer)
        except:
            print("Disconnected send")
            bConnected = False

        while bConnected:
            strToServer = "get datetime"
            print("analyzer(client) -> server(Hub)\n\t" + strToServer)
            try:
                self.websocket.send(strToServer)
            except:
                print("Disconnected send")
                bConnected = False

            try:
                for strFromClient in self.websocket:
                    print("server(Hub) -> analyzer(client)\n\t" + strFromClient)
                    strMsg = "analyzer_client "
                    strMsg = datetime.datetime.now().time()
                    print("analyzer(client) -> server(Hub)\n\t" + strMsg)
            except:
                #print("Disconnected receive")
                #bConnected = False
                pass




if __name__ == '__main__':
    print("Test class_analyzer_web_client\n")

    print("start analyzer_web_client")
    thread_webclient = class_analyzer_web_client("ws://localhost:8765")
    thread_webclient.start()
    
    time.sleep(25)
    #thread_wait_for_hub.raise_exception()
    thread_webclient.terminate_thread()
    print("waiting for thread_webclient to end")
    thread_webclient.join()
    print("thread_webclient ended")

    #forever = threading.Event()
    #forever.wait()

