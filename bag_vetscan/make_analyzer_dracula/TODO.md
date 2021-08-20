Domonstrate interface to DBus app

Add web sockets
    The analyzers will need to use web sockets to notify Hub when some event occurs or status changes.

	https://websockets.readthedocs.io/en/3.0/intro.html
	https://websockets.readthedocs.io/en/stable/

https://python-dbus-next.readthedocs.io/en/latest/high-level-client/index.html


######################################################
DBus
######################################################

This example connects to a media player and controls it with the MPRIS DBus interface.

from dbus_next.aio import MessageBus

import asyncio

loop = asyncio.get_event_loop()


async def main():
    bus = await MessageBus().connect()
    # the introspection xml would normally be included in your project, but
    # this is convenient for development
    introspection = await bus.introspect('org.mpris.MediaPlayer2.vlc', '/org/mpris/MediaPlayer2')

    obj = bus.get_proxy_object('org.mpris.MediaPlayer2.vlc', '/org/mpris/MediaPlayer2', introspection)
    player = obj.get_interface('org.mpris.MediaPlayer2.Player')
    properties = obj.get_interface('org.freedesktop.DBus.Properties')

    # call methods on the interface (this causes the media player to play)
    await player.call_play()

    volume = await player.get_volume()
    print(f'current volume: {volume}, setting to 0.5')

    await player.set_volume(0.5)

    # listen to signals
    def on_properties_changed(interface_name, changed_properties, invalidated_properties):
        for changed, variant in changed_properties.items():
            print(f'property changed: {changed} - {variant.value}')

    properties.on_properties_changed(on_properties_changed)

    await loop.create_future()

loop.run_until_complete(main())    