# Python DBUS examples

> A collection of python DBUS examples.

## Abstract
The first time I had to deal with python and DBUS I was overwhelmed by the lack
of concrete examples, so this repository was born. More documentation may be found in the comments.

## Dependencies

The following are python dependencies:
* dbus-python
  * relies on libdbus-1-dev
* PyGObject
  * relies on libgirepository1.0-dev

## Usage
In your first terminal run the **dbus monitor** and grep for the examples methods:

    dbus-monitor | grep /tld/domain/sub

In a second terminal run the **reciever**:

    ./receiver.py

The receiver has a *catch all* handler, so a lot of output is expected there.

in a third terminal you can now either:
* Run the **invoker**, which will call the proxxied receivers Test object methods:

        ./invoker.py

    The invoker will invoke 3 Methodes on the receiver:
    * foo: This will simply return *Foo* as a string
    * fail: Will trigger an exception in the receiver which the invoker can handle
    * quit: Will stop the receiver

* run the **emitter**, which will emit a test signal and a quit signal:

        ./emitter.py

After running either of them, the *receiver will be stopped*.
