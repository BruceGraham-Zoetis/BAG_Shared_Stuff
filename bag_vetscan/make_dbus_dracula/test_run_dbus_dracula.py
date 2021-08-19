#!/usr/bin/env python3

"""
File: test_run_dbus_dracula.py

Purpose: Create a DBus service that can domonstrate interface to an analyzer app.

pip3 install dbus-next

Use d-feet GUI app to see this service.
Install d-feet: sudo apt-get install -y d-feet
d-feet can be used to call methods with data, and see the response.


The service is on the Session Bus.
    Name: com.zoetis.dracula
    Methods:
        Bazify()
        Frobate()
        Mogrify()
    Properties
        Byte Bar (read / write)
    Signals
        Changed


"""

from dbus_next.aio import MessageBus
from dbus_next.service import (ServiceInterface,
                               method, dbus_property, signal)
from dbus_next import Variant, DBusError

import asyncio

import CAnalyzer


async def main():
    bus = await MessageBus().connect()
    strAnalyzerName = "dracula"
    interface = CAnalyzer.CZoetisAnalyzerInterface(strAnalyzerName)
    bus.export('/com/zoetis/dracula', interface)
    await bus.request_name('com.zoetis.dracula')

    # emit the changed signal after two seconds.
    await asyncio.sleep(2)

    interface.Changed()

    await bus.wait_for_disconnect()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
