#!/usr/bin/env python3
# coding: utf-8

"""
File: thread_wait_for_clients
"""

import config
import asyncio
import time
import threading
import socket
import select

debug_use_ui = True
debug_print = True


if (debug_print):
    print_lock = threading.Lock()

def print_locked(output):
    if (debug_print):
        print_lock.acquire()
        print(output, flush=True)
        print_lock.release()

"""
Wait for client disconnect
"""
def thread_wait_for_client_disconnect(clientsocket, strAddress, str_client_name):
    print_locked("Connected client: %s %s" % (strAddress, str_client_name))

    if (debug_use_ui):
        config.g_vetscan_hub.analyzer_connected(strAddress, str_client_name)

    clientsocket.settimeout(100.0)
    bConnected = True
    while bConnected:
        try:
            print_locked("send(b\"Hub\") to client: %s" % (str_client_name))
            clientsocket.send(b"Hub")
            print_locked("  wait for recv() from client: %s" % (str_client_name))
            msg = clientsocket.recv(128)
            if (0 == len(msg)):
                bConnected = False
            else:
                print_locked("  received %s" % msg)
                #time.sleep(30)
        except:
            bConnected = False

    clientsocket.close()
    print_locked("Disconnected client: %s %s" % (strAddress, str_client_name))
    if (debug_use_ui):
        config.g_vetscan_hub.analyzer_disconnected(strAddress)



"""
Handle client connections.
"""
def thread_wait_for_clients():
    config.g_vetscan_hub
    config.g_window

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    HOST = socket.gethostname() # Get local machine name
    PORT = 50007                # Reserve a port for your service.

    soc.setblocking(0)
    try:
        soc.bind((HOST, PORT))        # Bind to the port
    except:
        print_locked("error bind()")
        return

    try:
        print_locked("listen() for client connection.")
        soc.listen(5)
    except:
        print_locked("error listen()")
        return

    while True:
        # Detecting clients that disappeared does NOT work when we ARE
        # watching if any sockets are writable
        readable, writable, exceptional = select.select([soc], [], [])
        
        try:
            print_locked("accept()")
            socket_client, arr_address = soc.accept()
        except:
            print_locked("error accept()")
            return

        bin_client_name = socket_client.recv(128)
        str_client_name = bin_client_name.decode('utf-8')
        str_address = arr_address[0]
        thread = threading.Thread(target=thread_wait_for_client_disconnect, args=(socket_client, str_address, str_client_name))
        thread.start()


def start_thread_hub_server():
    print_locked("Starting Hub server")
    thread = threading.Thread(target = thread_wait_for_clients)
    thread.start()
    return thread

if __name__ == '__main__':
    print("\n")

    debug_use_ui = False
    thread = start_thread_hub_server()
    forever = threading.Event()
    forever.wait()
