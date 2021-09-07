#!/usr/bin/env python3
# 
# File: run_webclient.py

import thread_connect_hub
import thread_webclient
import threading


if __name__ == '__main__':
    print("")

    print("start_thread_connect_to_hub()")
    thread_waiting_for_hub = thread_connect_hub.class_connect_to_hub(50007, b"Dracula")     # The same port as used by the server
    thread_waiting_for_hub.start()

    #thread_webclient = thread_webclient.class_analyzer_web_client("ws://localhost:8765")
    #thread_webclient.start()

    forever = threading.Event()
    forever.wait()

