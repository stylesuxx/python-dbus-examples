#!/usr/bin/python
import dbus
import dbus.service
import dbus.glib

class Emitter(dbus.service.Object):
	def __init__(self, bus_name, object_path, loop):
		dbus.service.Object.__init__(self, bus_name, object_path)

	@dbus.service.signal('tld.domain.sub.TestInterface.event')
	def send(self):


"""
Emit a signal on the dbus
"""
session_bus = dbus.SessionBus()
bus_name = dbus.service.BusName('sub.domain.tld', bus = session_bus)
emitter = Emitter(bus_name, '/tld/domain/sub/event')