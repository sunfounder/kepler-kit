.. _cpn_motor:

DC Motor
===================

|img_dc_motor|

This is a 3V DC motor. When you give a high level and a low level to each of the 2 terminals, it will rotate.

* **Size**: 25*20*15MM
* **Operation Voltage**: 1-6V
* **Free-run Current** (3V): 70m
* **A Free-run Speed** (3V): 13000RPM
* **Stall Current** (3V): 800mA
* **Shaft Diameter**: 2mm

Direct current (DC) motor is a continuous actuator that converts electrical energy into mechanical energy. DC motors make rotary pumps, fans, compressors, impellers, and other devices work by producing continuous angular rotation.

A DC motor consists of two parts, the fixed part of the motor called the **stator** and the internal part of the motor called the **rotor** (or **armature** of a DC motor) that rotates to produce motion.
The key to generating motion is to position the armature within the magnetic field of the permanent magnet (whose field extends from the north pole to the south pole). The interaction of the magnetic field and the moving charged particles (the current-carrying wire generates the magnetic field) produces the torque that rotates the armature.

|img_dc_motor_sche|

Current flows from the positive terminal of the battery through the circuit, through the copper brushes to the commutator, and then to the armature.
But because of the two gaps in the commutator, this flow reverses halfway through each complete rotation.
This continuous reversal essentially converts the DC power from the battery to AC, allowing the armature to experience torque in the right direction at the right time to maintain rotation.

* `DC Motor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Fleming's left-hand rule for motors - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_



**Example**

* :ref:`py_motor` (For MicroPython User)
* :ref:`ar_motor` (For Arduino User)
* :ref:`per_smart_fan` (For Piper Make User)