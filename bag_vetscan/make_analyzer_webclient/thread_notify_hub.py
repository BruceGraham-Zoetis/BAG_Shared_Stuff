

"""
File: thread_notify_hub.py
"""

import socket
import class_state_machine_state
   

def thread_notify_hub():
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

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 37020))

    stateMa = class_state_machine_state.state_machine_states()

    stateMa.add_state("BroadcastToHub", 0)
    stateMa.add_state("WaitForHubResponse", 1)
    stateMa.add_state("WaitForHubRestart", 2)

    stateMa.set("BroadcastToHub")
    bTrace = False

    while True:
        strState = stateMa.get_name()
        if (bTrace): print("  sync - State: " + stateMa.get_name())

        if ("BroadcastToHub" == strState):
            if (bTrace): print("  sync - Broadcast analyzer name to Hub", flush=True)
            server.sendto(message, ("localhost", 37020))
            strState = stateMa.set("WaitForHubResponse")

        elif ("WaitForHubResponse" == strState):
            if (bTrace): print("  sync - Waiting for Hub response...")
            try:
                client.settimeout(10)
                while True:
                    name, addr = client.recvfrom(1024)
                    if (b"Hub" == name):
                        if (bTrace): print("  sync - Got Hub response %s" % addr)
                        strState = stateMa.set("WaitForHubRestart")
                        break
                    else:
                        if (bTrace): print("  sync - Got: %s %s" % name, addr)
            except:
                if (bTrace): print("  sync - Timeout no Hub response")
                stateMa.set("BroadcastToHub")

        elif ("WaitForHubRestart" == strState):
            if (bTrace): print("  sync - Waiting for Hub restart", flush=True)
            client.settimeout(None) # blocking mode
            while True:
                name, addr = client.recvfrom(1024)
                if (b"Hub" == name):
                    if (bTrace): print("  sync - Got Hub response")
                    strState = stateMa.set("BroadcastToHub")
