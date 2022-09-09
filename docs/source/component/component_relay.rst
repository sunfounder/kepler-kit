.. _cpn_relay:

Relay
==========================================

|img_relay|

As we may know, relay is a device which is used to provide connection
between two or more points or devices in response to the input signal
applied. In other words, relays provide isolation between the controller
and the device as devices may work on AC as well as on DC. However, they
receive signals from a microcontroller which works on DC hence requiring
a relay to bridge the gap. Relay is extremely useful when you need to
control a large amount of current or voltage with small electrical
signal.

There are 5 parts in every relay:

**Electromagnet** - It consists of an iron core wounded by coil of
wires. When electricity is passed through, it becomes magnetic.
Therefore, it is called electromagnet.

**Armature** - The movable magnetic strip is known as armature. When
current flows through them, the coil is it energized thus producing a
magnetic field which is used to make or break the normally open (N/O) or
normally close (N/C) points. And the armature can be moved with direct
current (DC) as well as alternating current (AC).

**Spring** - When no currents flow through the coil on the
electromagnet, the spring pulls the armature away so the circuit cannot
be completed.

Set of electrical **contacts** - There are two contact points:

-  Normally open - connected when the relay is activated, and disconnected when it is inactive.

-  Normally close - not connected when the relay is activated, and connected when it is inactive.

**Molded frame** - Relays are covered with plastic for protection.

The working principle of relay is simple. When power is supplied to the
relay, currents start flowing through the control coil; as a result, the
electromagnet starts energizing. Then the armature is attracted to the
coil, pulling down the moving contact together thus connecting with the
normally open contacts. So the circuit with the load is energized. Then
breaking the circuit would a similar case, as the moving contact will be
pulled up to the normally closed contacts under the force of the spring.
In this way, the switching on and off of the relay can control the state
of a load circuit.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Example**

* :ref:`py_relay` (For MicroPython User)
* :ref:`ar_relay` (For Arduino User)