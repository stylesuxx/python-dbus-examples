#!/usr/bin/python
import gobject
import dbus
import dbus.service
import dbus.glib

class Test(dbus.service.Object):
	loop = None
	def __init__(self, bus_name, object_path, loop):
		dbus.service.Object.__init__(self, bus_name, object_path)
		self.loop = loop

	@dbus.service.method('tld.domain.sub.TestInterface')
	def foo(self):
		return "Foo"

	# Stop the main loop
	@dbus.service.method('tld.domain.sub.TestInterface')
	def stop(self):
		self.loop.quit()
		return "Quit loop"

	# Pass an exception through dbus
	@dbus.service.method('tld.domain.sub.TestInterface')
	def fail(self):
		raise Exception, 'FAIL!'

"""
Register to dbus and run the main loop.
Will provide the Test object via dbus.
"""
loop = gobject.MainLoop()
session_bus = dbus.SessionBus()
bus_name = dbus.service.BusName('sub.domain.tld', bus = session_bus)
obj = Test(bus_name, '/tld/domain/sub/test', loop)
loop.run()