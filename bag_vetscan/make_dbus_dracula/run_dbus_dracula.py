#!/usr/bin/env python3

"""
File: run_dbus_dracula.py

Purpose: Create a DBus service that can domonstrate interface to an analyzer app.

pip3 install dbus-next

Use d-feet GUI app to see this service.
Install d-feet: sudo apt-get install -y d-feet
d-feet can be used to call methods with data, and see the response.

"""

from dbus_next.aio import MessageBus
import asyncio

import CAnalyzer
from analyzer_dbus_config import (get_analyzer_dbus_request_name, get_analyzer_dbus_service_path)


async def main():
    bus = await MessageBus().connect()
    str_request_name = get_analyzer_dbus_request_name()
    str_service_path  = get_analyzer_dbus_service_path()
    interface = CAnalyzer.CZoetisAnalyzerInterface(str_request_name)
    bus.export(str_service_path, interface)
    await bus.request_name(str_request_name)

    # emit the changed signal after two seconds.
    await asyncio.sleep(2)

    interface.Changed()

    await bus.wait_for_disconnect()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
