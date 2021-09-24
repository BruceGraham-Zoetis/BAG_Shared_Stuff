#!/usr/bin/env python3
"""
@breif analyzer_dbus_config.py

Purpose: DBus service info for the analyzer app.

The service is on the Session Bus.
    Name: com.zoetis.dracula
    Methods:
        configuration_get()
        configuration_put()
        configuration_schema_get()
    Properties
        None
    Signals
        Changed


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
    str_analyzer_name = "dracula"
    return str_analyzer_name

def get_analyzer_dbus_request_name() -> str:
    str_request_name = 'com.zoetis.' + get_analyzer_name()
    return str_request_name


def get_analyzer_dbus_service_path() -> str:
    str_service_path = '/com/zoetis/' + get_analyzer_name()
    return str_service_path
