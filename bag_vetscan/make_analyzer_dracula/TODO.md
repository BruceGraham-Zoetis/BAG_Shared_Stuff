Domonstrate interface to DBus app

Add web sockets
    The analyzers will need to use web sockets to notify Hub when some event occurs or status changes.

	https://websockets.readthedocs.io/en/3.0/intro.html
	https://websockets.readthedocs.io/en/stable/


Send a desktop notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~
from pydbus import SessionBus
bus = SessionBus()
notifications = bus.get('org.freedesktop.Notifications')
notifications.Notify('test', 0, 'dialog-information', "Hello World!", "pydbus works :)", [], {}, 5000)
