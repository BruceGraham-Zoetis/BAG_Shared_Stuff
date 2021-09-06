#!/usr/bin/env python3

"""
File: CDBusDraculaService.py

TODO:
* Create a DBus .service file

    File: com.zoetis.dracula.service 

    [D-BUS Service]
    Name=com.zoetis.dracula
    Exec=/home/myuser/Workspace/service-start
    User=myuser

pip3 install pydbus
"""

import os, sys
from pydbus import SessionBus
import threading


def get_analyzer_name() -> str:
    str_analyzer_name = "dracula"
    return str_analyzer_name

def get_analyzer_dbus_request_name() -> str:
    str_request_name = 'com.zoetis.' + get_analyzer_name()
    return str_request_name


"""
Class for accessing the Dracula service. This is a singleton.

"""
class CDBusDraculaService():
    # bus: single instance of the session bus
    # draculad: the single instance of the dracula demon

    _instance = None
    _lock = threading.Lock()

    def get_request_name(self) -> str:
        str_request_name = get_analyzer_dbus_request_name()
        return str_request_name


    def __new__(cls, *args, **kwargs):
        with cls._lock:
            # another thread could have created the instance
            # before we acquired the lock. So check that the
            # instance is still nonexistent.
            if not cls._instance:
                cls._instance = super(CDBusDraculaService, cls).__new__(cls)
                # Put any initialization here.
                str_request_name = get_analyzer_dbus_request_name()

                cls.bus      = SessionBus()
                cls.draculad = cls.bus.get(str_request_name)
                #print('Created new singleton ', cls._instance)
            else:
                #print("using singleton ", cls._instance)
                pass

        return cls._instance

    @property
    def measurement_id(self) -> str:
        return self.draculad.measurement_id

    @measurement_id.setter
    def measurement_id(self, str_value : str):
        self.draculad.measurement_id = str_value


g_dbus_dracula_service = CDBusDraculaService()


