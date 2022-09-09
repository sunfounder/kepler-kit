.. _py_pump:

3.6 Pumping
=======================


Small centrifugal pumps are suitable for projects with automatic plant watering.
It can also be used to make tiny smart water features.

Its power component is an electric motor, driven in exactly the same way as a normal motor.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Connect the tube to the motor outlet, submerge the pump in water, and then power it on.
    #. You need to make sure that the water level is always higher than the motor. Idling may damage the motor due to heat generation and will also generate noise.
    #. If you are watering plants, you need to avoid soil being drawn in, as this can clog the pump.
    #. If water does not come out of the tube, there may be residual water in the tube blocking the air flow and needs to be drained first.


**Schematic**

|sch_pump|


**Wiring**

.. note::

    * Since pump require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.



|wiring_pump|

**Code**

.. note::

    * Open the ``3.6_pumping.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    while True:
        motor1A.high()
        motor2A.low()


After the code is run, the pump starts working and you will see water flowing out of the tube at the same time.

.. note::

    * If the motor is still spinning after you click the Stop button, you need to reset the **RUN** pin on the Pico W with a wire to GND at this time, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico W to disconnect from the computer. 

    |wiring_run_reset|