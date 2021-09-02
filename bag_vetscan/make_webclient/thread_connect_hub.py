#!/usr/bin/env python3
# coding: utf-8

"""
File: thread_connect_hub.py
"""

import socket
import time
import threading
#import ctypes


class class_connect_to_hub(threading.Thread):
    def __init__(self, port_number, binaryAnalyzerName):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.port_number = port_number
        self.host = socket.gethostname() # Get local machine name
        self.bConnected = False
        self.binaryAnalyzerName = binaryAnalyzerName
        self.terminate = False

    # Override the run() function of Thread class
    def run(self):
        try:
            self.__stay_connected()
        finally:
            #print("thread ended")
            pass

    """
    # raise and exception to get the thread to exit
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
    """

    def terminate_thread(self):
        self.terminate = True

    def __stay_connected(self):
        while not self.terminate:
            socketToServer = None
            for res in socket.getaddrinfo(self.host, self.port_number, socket.AF_UNSPEC, socket.SOCK_STREAM):
                af, socktype, proto, canonname, sa = res
                try:
                    socketToServer = socket.socket(af, socktype, proto)
                    socketToServer.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                except OSError as msg:
                    print("OSError: %s" % msg, flush=True)
                    socketToServer = None
                    break
                try:
                    socketToServer.connect(sa)
                except OSError as msg:
                    print("OSError: %s" % msg, flush=True)
                    socketToServer.close()
                    socketToServer = None
                    break

            if socketToServer is None:
                print('could not open socket', flush=True)
                print("sleep...", flush=True)
                time.sleep(10)
                print("  end of sleep.", flush=True)
                print("    use send() and recv() to verify Hub is still there", flush=True)
                continue

            socketToServer.settimeout(100.0)
            self.bConnected = True
            while self.bConnected and not self.terminate:
                try:
                    print("sendall(%s)" % self.binaryAnalyzerName, flush=True)
                    socketToServer.send(self.binaryAnalyzerName)
                    try:
                        print("  wait for recv() from server: Hub", flush=True)
                        msg = socketToServer.recv(128)
                        if (0 == len(msg)):
                            self.bConnected = False
                        else:
                            print("  received ", msg)
                            if (b"Hub" == msg):
                                print("got Hub response, sleeping...")
                                if (self.terminate):
                                    self.bConnected = False
                                    break
                                time.sleep(30)
                            else:
                                print("not Hub, recv() again")
                    except:
                        self.bConnected = False
                except:
                    self.bConnected = False

            print("Disconnected from Server", flush=True)
            socketToServer.close()
            if (self.terminate):
                break

            print("sleep...", flush=True)
            time.sleep(10)
            print("  end of sleep", flush=True)

    def get_id(self):
         # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id


if __name__ == '__main__':
    print("Test class_connect_to_hub\n")

    print("start class_connect_to_hub")
    thread_wait_for_hub = class_connect_to_hub(50007, b"Dracula")     # The same port as used by the server
    thread_wait_for_hub.start()

    time.sleep(25)
    #thread_wait_for_hub.raise_exception()
    thread_wait_for_hub.terminate_thread()
    print("waiting for thread to end")
    thread_wait_for_hub.join()
    print("thread ended")

    #forever = threading.Event()
    #forever.wait()
