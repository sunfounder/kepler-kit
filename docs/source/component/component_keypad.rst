.. _cpn_keypad:

Keypad
========================


Microcontroller system, if the use of more keys such as electronic code lock, telephone keypad, etc. generally have at least 12 to 16 keys, usually using a matrix keyboard.


Matrix keypad is also called row keypad, it is a keypad with four I/O lines as row lines and four I/O lines as column lines. One key is set at each intersection of the row and column lines. Thus the number of keys on the keyboard is 4*4. This row and column keyboard structure can effectively improve the utilization of I/O ports in a microcontroller system.

Their contacts are accessed via a header suitable for connection with a ribbon cable or insertion into a printed circuit board. 
In some keypads, each button connects with a separate contact in the header, while all the buttons share a common ground.

|img_keypad|

More often, the buttons are matrix encoded, meaning that each of them bridges a unique pair of conductors in a matrix. 
This configuration is suitable for polling by a microcontroller, which can be programmed to send an output pulse to each of the four horizontal wires in turn. 
During each pulse, it checks the remaining four vertical wires in sequence, to determine which one, if any, is carrying a signal. 
Pullup or pulldown resistors should be added to the input wires to prevent the inputs of the microcontroller from behaving unpredictably when no signal is present.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Example**

* :ref:`py_keypad` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_keypad` (For Arduino User)