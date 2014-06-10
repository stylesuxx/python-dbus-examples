### Simple python dbus example

* Run dbus monitor and grep for the interesting output:

    dbus-monitor | grep /tld/domain/sub

* Run the receiver

Then you can either
* Run the invoker, which will call the proxxied object's methods.
* run the emitter, which will emit a test signal and a quit signal.

After running either of them, the receiver should be stopped.