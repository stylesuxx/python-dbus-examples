### Simple python dbus example

* dbus-monitor | grep /tld/domain/sub
* Run the receiver

Then you can either
* run the invoker, which will call the proxxied object's methods and stop the receivers main loop
* run the emitter, which will emit some singals on the dbus before emitting a signal stopping the receivers main loop