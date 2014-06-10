#!/usr/bin/python
import dbus

# Proxy object from the object in receiver
obj = dbus.SessionBus().get_object('sub.domain.tld', '/tld/domain/sub/test')

print obj.foo(dbus_interface = 'tld.domain.sub.TestInterface')

# Exceptions are passed through dbus
try:
	obj.fail(dbus_interface = 'tld.domain.sub.TestInterface')
except Exception, e:
	print str(e)

# Call the stop method of the proxxied object which will stop the receivers main loop
print obj.stop(dbus_interface = 'tld.domain.sub.TestInterface')