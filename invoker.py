#!/usr/bin/python
"""Invoke remote methods."""
import dbus

"""Proxy object from the Test object in receiver."""
obj = dbus.SessionBus().get_object('sub.domain.tld', '/tld/domain/sub/Test')

"""Call a method that simply retruns a string."""
print(obj.foo(dbus_interface='tld.domain.sub.TestInterface'))

"""Invoke a method that throws an exception and catch it."""
try:
    obj.fail(dbus_interface='tld.domain.sub.TestInterface')
except Exception as e:
    print(str(e))

"""
Call the stop method of the proxxied object which will stop the receivers
main loop.
"""
print(obj.stop(dbus_interface='tld.domain.sub.TestInterface'))
