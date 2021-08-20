#!/usr/bin/env python3

"""
File: test_run_analyzer_app.py

TODO: Intergrate this code into the analyzer app.
"""

from dbus_next.aio import MessageBus
from dbus_next import Variant

bus = await MessageBus().connect()

with open('introspection.xml', 'r') as f:
    introspection = f.read()

# alternatively, get the data dynamically:
# introspection = await bus.introspect('com.zoetis.name',
#                                      '/com/zoetis/sample_object0')

proxy_object = bus.get_proxy_object('com.zoetis.name',
                                    '/com/zoetis/sample_object0',
                                    introspection)

interface = proxy_object.get_interface('com.zoetis.SampleInterface0')

# Use call_[METHOD] in snake case to call methods, passing the
# in args and receiving the out args. The `baz` returned will
# be type 'a{us}' which translates to a Python dict with `int`
# keys and `str` values.
baz = await interface.call_frobate(5, 'hello')

# `bar` will be a Variant.
bar = await interface.call_bazify([-5, 5, 5])

await interface.call_mogrify([5, 5, [ Variant('s', 'foo') ])

# Listen to signals by defining a callback that takes the args
# specified by the signal definition and registering it on the
# interface with on_[SIGNAL] in snake case.

def changed_notify(new_value):
    print(f'The new value is: {new_value}')

interface.on_changed(changed_notify)

# Use get_[PROPERTY] and set_[PROPERTY] with the property in
# snake case to get and set the property.

bar_value = await interface.get_bar()

await interface.set_bar(105)

await bus.wait_for_disconnect()