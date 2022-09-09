.. _cpn_ultrasonic:

Ultrasonic Module
================================

Ultrasonic ranging module provides 2cm - 400cm non-contact measurement function, and the ranging accuracy can reach to 3mm. 
It can ensure that the signal is stable within 5m, and the signal is gradually weakened after 5m, till the 7m position disappears.

The module includes ultrasonic transmitters, receiver and control circuit. The basic principles are as follows:

#. Use an IO flip-flop to process a high level signal of at least 10us.

#. The module automatically sends eight 40khz and detects if there is a pulse signal return.

#. If the signal returns, passing the high level, the high output IO duration is the time from the transmission of the ultrasonic wave to the return of it. Here, test distance = (high time x sound speed (340 m / s) / 2.

|img_ultrasonic|

The timing diagram is shown below. You only need to supply a short 10us
pulse for the trigger input to start the ranging, and then the module
will send out an 8 cycle burst of ultrasound at 40 kHz and raise its
echo. You can calculate the range through the time interval between
sending trigger signal and receiving echo signal.

Formula: us / 58 = centimeters or us / 148 =inch; or: the range = high
level time \* velocity (340M/S) / 2; you are suggested to use
measurement cycle over 60ms in order to prevent signal collisions of
trigger signal and the echo signal.

|img_ultrasonic_timing|

**Example**

* :ref:`py_ultrasonic` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ultrasonic` (For Arduino User)
* :ref:`per_reversing_system` (For Piper Make User)