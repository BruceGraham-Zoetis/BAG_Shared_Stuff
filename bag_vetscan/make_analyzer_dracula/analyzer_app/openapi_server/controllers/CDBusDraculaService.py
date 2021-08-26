#!/usr/bin/env python3

"""
File: CDBusDraculaService.py

TODO: Intergrate this code into the analyzer app.

pip3 install pydbus
"""

from pydbus import SessionBus
from pydbus import SystemBus
import threading

"""
Class for the Dracula service. This is a singleton.

"""
#class CDBusDraculaService(object):
class CDBusDraculaService():
    # bus: single instance of the session bus
    # draculad: the single instance of the dracula demon

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            # another thread could have created the instance
            # before we acquired the lock. So check that the
            # instance is still nonexistent.
            if not cls._instance:
                cls._instance = super(CDBusDraculaService, cls).__new__(cls)
                # Put any initialization here.
                cls.bus      = SessionBus()
                cls.draculad = cls.bus.get('com.zoetis.dracula')
                #print('Created new singleton ', cls._instance)
            else:
                #print("using singleton ", cls._instance)
                pass

        return cls._instance

    """
    @property
    def Bar(self) -> int:
        return self.draculad.Bar

    @Bar.setter
    def Bar(self, iValue : int):
        self.draculad.Bar = iValue

    def measurement_supported_consumables_get(self) -> str:
        strRtn = self.draculad.measurement_supported_consumables_get()
        return strRtn
    """


if __name__ == '__main__':
    oDracula = CDBusDraculaService()

    # Start or stop oDracula unit
    """
    job1 = oDracula.StopUnit("ssh.service", "fail")
    job2 = oDracula.StartUnit("ssh.service", "fail")
    """

    print()

    # get and set Bar 
    iValue = oDracula.Bar
    print("Bar: %d" % oDracula.Bar)
    oDracula.Bar += 10
    print("Bar after += 10: %d" % oDracula.Bar)

    strRtn = oDracula.measurement_supported_consumables_get()
    print("Consumables: %s" % strRtn)
    