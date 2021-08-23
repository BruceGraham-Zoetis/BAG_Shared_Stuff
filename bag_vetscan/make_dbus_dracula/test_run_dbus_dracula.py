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


import asyncio

import CAnalyzer


"""
Interface names
Interfaces have names with type STRING, meaning that they must be valid UTF-8.
 However, there are also some additional restrictions that apply to interface names specifically:

Interface names are composed of 2 or more elements separated by a period ('.') character.
 All elements must contain at least one character.

Each element must only contain the ASCII characters "[A-Z][a-z][0-9]_" and must not begin with a digit.

Interface names must not exceed the maximum name length.

Interface names should start with the reversed DNS domain name of the author of the interface (in lower-case),
 like interface names in Java. It is conventional for the rest of the interface name to consist of
 words run together, with initial capital letters on all words ("CamelCase"). Several levels of
 hierarchy can be used. It is also a good idea to include the major version of the interface in the name, and increment it if incompatible changes are made; this way, a single object can implement several versions of an interface in parallel, if necessary.

For instance, if the owner of example.com is developing a D-Bus API for a music player,
 they might define interfaces called com.example.MusicPlayer1, com.example.MusicPlayer1.Track
 and com.example.MusicPlayer1.Seekable.

If the author's DNS domain name contains hyphen/minus characters ('-'), which are not allowed
 in D-Bus interface names, they should be replaced by underscores. If the DNS domain name contains
 a digit immediately following a period ('.'), which is also not allowed in interface names),
 the interface name should add an underscore before that digit.
 For example, if the owner of 7-zip.org defined an interface for out-of-process plugins,
 it might be named org._7_zip.Plugin.
"""

def get_analyzer_name() -> str:
    strAnalyzerName = "dracula"
    return strAnalyzerName

def get_analyzer_dbus_request_name() -> str:
    strRequestName = 'com.zoetis.' + get_analyzer_name()
    return strRequestName


def get_analyzer_dbus_service_path() -> str:
    strServicePath = '/com/zoetis/' + get_analyzer_name()
    return strServicePath


async def main():
    bus = await MessageBus().connect()
    strRequestName = get_analyzer_dbus_request_name()
    strServicePath  = get_analyzer_dbus_service_path()
    interface = CAnalyzer.CZoetisAnalyzerInterface(strRequestName)
    bus.export(strServicePath, interface)
    await bus.request_name(strRequestName)

    # emit the changed signal after two seconds.
    await asyncio.sleep(2)

    interface.Changed()

    await bus.wait_for_disconnect()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
