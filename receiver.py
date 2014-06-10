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

def catchall_handler(*args, **kwargs):
    print ("Caught signal: "
           + kwargs['dbus_interface'] + "." + kwargs['member'])
    for arg in args:
        print "        " + str(arg)

def quit_handler():
	print "Quitting...."
	loop.quit()

"""
Register to dbus and run the main loop.
Will provide the Test object via dbus.
"""
loop = gobject.MainLoop()
session_bus = dbus.SessionBus()

bus_name = dbus.service.BusName('sub.domain.tld', bus = session_bus)
obj = Test(bus_name, '/tld/domain/sub/test', loop)
session_bus.add_signal_receiver(catchall_handler, interface_keyword='dbus_interface', member_keyword='member')
session_bus.add_signal_receiver(quit_handler, dbus_interface = "tld.domain.sub.event", signal_name = "quit_signal")

loop.run()
