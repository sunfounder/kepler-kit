.. _py_joystick:

4.1 Toggle the Joystick
================================

If you play a lot of video games, then you should be very familiar with the Joystick.
It is usually used to move the character around, rotate the screen, etc.

The principle behind Joystick's ability to allow the computer to read our actions is very simple.
It can be thought of as consisting of two potentiometers that are perpendicular to each other.
These two potentiometers measure the analog value of the joystick vertically and horizontally, resulting in a value (x,y) in a planar right-angle coordinate system.


The joystick of this kit also has a digital input, which is activated when the joystick is pressed.

* :ref:`cpn_joystick`

**Schematic**

|sch_joystick|

The SW pin is connected to a 10K pull-up resistor, the reason is to be able to get a stable high level on the SW pin (Z axis) when the joystick is not pressed; otherwise the SW is in a suspended state and the output value may vary between 0/1.

**Wiring**

|wiring_joystick|


**Code**

.. note::

    * Open the ``4.1_toggle_the_joystick.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200)    

After the program runs, the Shell prints out the x,y,z values of joystick.

* The x-axis and y-axis values are analog values that vary from 0 to 65535.
* The Z-axis is a digital value with a status of 1 or 0.