#!/usr/bin/python
"""Receiver related functionality."""
import dbus.service
import dbus.glib
import gobject
import dbus


class Test(dbus.service.Object):
    """Reciever test class."""

    loop = None

    def __init__(self, bus_name, object_path, loop):
        """Initialize the DBUS service object."""
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.loop = loop

    @dbus.service.method('tld.domain.sub.TestInterface')
    def foo(self):
        """Return a string."""
        return 'Foo'

    # Stop the main loop
    @dbus.service.method('tld.domain.sub.TestInterface')
    def stop(self):
        """Stop the receiver."""
        self.loop.quit()
        return 'Quit loop'

    # Pass an exception through dbus
    @dbus.service.method('tld.domain.sub.TestInterface')
    def fail(self):
        """Trigger an exception."""
        raise Exception('FAIL!')


def catchall_handler(*args, **kwargs):
    """Catch all signals we can get."""
    print('---- Caught signal ----')
    print('%s:%s\n' % (kwargs['dbus_interface'], kwargs['member']))

    print('Arguments:')
    for arg in args:
        print '* %s' % str(arg)

    print("\n")


def quit_handler():
    """Quit the receiver."""
    print 'Quitting....'
    loop.quit()

"""
Register to dbus and run the main loop.
Will provide the Test object via dbus.
"""
loop = gobject.MainLoop()
session_bus = dbus.SessionBus()

bus_name = dbus.service.BusName('sub.domain.tld', bus=session_bus)
obj = Test(bus_name, '/tld/domain/sub/test', loop)
session_bus.add_signal_receiver(catchall_handler,
                                interface_keyword='dbus_interface',
                                member_keyword='member')
session_bus.add_signal_receiver(quit_handler,
                                dbus_interface='tld.domain.sub.event',
                                signal_name='quit_signal')

loop.run()
