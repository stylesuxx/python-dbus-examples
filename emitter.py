#!/usr/bin/python
import dbus
import dbus.service
import dbus.glib

class Emitter(dbus.service.Object):
	def __init__(self, bus_name, object_path):
		dbus.service.Object.__init__(self, bus_name, object_path)

	@dbus.service.signal('tld.domain.sub.event')
	def test(self):
		print "Emitted a test signal"

	@dbus.service.signal('tld.domain.sub.event')
	def quit_signal(self):
		print "Emitted a quit signal"

"""
Emit a test signal on the dbus.
Emit a receiver_quit signal which should stop the receiver.
"""
session_bus = dbus.SessionBus()
bus_name = dbus.service.BusName('sub.domain.tld', bus = session_bus)
emitter = Emitter(bus_name, '/tld/domain/sub/event')
emitter.test()
emitter.quit_signal()