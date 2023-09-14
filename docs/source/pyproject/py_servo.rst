.. _py_servo:

3.7 Swinging Servo
===================

In this kit, in addition to LED and passive buzzer, there is also a device controlled by PWM signal, Servo.

Servo is a position (angle) servo device, which is suitable for those control systems that require constant angle changes and can be maintained. It has been widely used in high-end remote control toys, such as airplanes, submarine models, and remote control robots.

Now, try to make the servo sway!

* :ref:`cpn_servo`

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

You can also buy them separately from the links below.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**Schematic**

|sch_servo|

**Wiring**

|wiring_servo|

* Orange wire is signal and connected to GP15.
* Red wire is VCC and connected to VBUS(5V).
* Brown wire is GND and connected to GND.


.. 1. Press the Servo Arm into the Servo output shaft. If necessary, fix it with screws.
.. #. Connect **VBUS** (not 3V3) and GND of Pico W to the power bus of the breadboard.
.. #. Connect the red lead of the servo to the positive power bus with a jumper.
.. #. Connect the yellow lead of the servo to the GP15 pin with a jumper wire.
.. #. Connect the brawn lead of the servo to the negative power bus with a jumper wire.


**Code**

.. note::

    * Open the ``3.7_swinging_servo.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.



.. code-block:: python

    import machine
    import utime

    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servo_write(pin,angle):
        pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        pin.duty_u16(duty)

    while True:
        for angle in range(180):
            servo_write(servo,angle)
            utime.sleep_ms(20)
        for angle in range(180,-1,-1):
            servo_write(servo,angle)
            utime.sleep_ms(20)


When the program is running, we can see the Servo Arm swinging back and forth from 0° to 180°. 

The program will always run because of the ``while True`` loop, we need to press the Stop button to end the program.

**How it works?**

We defined the ``servo_write()`` function to make the servo run.

This function has two parameters:

* ``pin``, the GPIO pin that controls the servo.
* ``Angle``, the angle of the shaft output.

In this function, ``interval_mapping()`` is called to map the angle range 0 ~ 180 to the pulse width range 0.5 ~ 2.5ms.

.. code-block:: python

    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)

Why is it 0.5~2.5? This is determined by the working mode of the Servo. 

:ref:`cpn_servo`

Next, convert the pulse width from period to duty. Since ``duty_u16()`` cannot have decimals when used (the value cannot be a float type), we used ``int()`` to force the duty to be converted to an int type.

.. code-block:: python

    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))

Finally, write the duty value into ``duty_u16()``.