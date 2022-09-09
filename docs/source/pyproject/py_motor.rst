.. _py_motor:

3.5 Small Fan
=======================


Now we use the TA6586 to drive the DC motor to make it rotate clockwise and counterclockwise. 
Since the DC motor requires a relatively large current, for safety reasons, 
here we use a power module to supply power to the motor.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`


**Schematic**

|sch_motor|



**Wiring**

.. note::

    * Since DC motors require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.


|wiring_motor|


**Code**

.. note::

    * Open the ``3.5_small_fan.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)


Once the program is running, the motor will rotate back and forth in a regular pattern.


.. note::

    * If the motor is still spinning after you click the Stop button, you need to reset the **RUN** pin on the Pico W with a wire to GND at this time, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico W to disconnect from the computer. 

    |wiring_run_reset|