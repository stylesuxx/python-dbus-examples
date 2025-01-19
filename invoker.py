#!/usr/bin/python
"""Invoke remote methods."""
import dbus

bus_name = 'sub.domain.tld'
interface_name = 'tld.domain.sub.TestInterface'
object_path = '/tld/domain/sub/Test'

"""Proxy object from the Test object in receiver."""
obj = dbus.SessionBus().get_object(bus_name, object_path)

"""Call a method that simply retruns a string."""
print(obj.foo(dbus_interface=interface_name))

"""Invoke a method that throws an exception and catch it."""
try:
    obj.fail(dbus_interface=interface_name)
except Exception as e:
    print(str(e))

"""
Call the stop method of the proxxied object which will stop the receivers
main loop.
"""
print(obj.stop(dbus_interface=interface_name))
