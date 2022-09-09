.. _py_photoresistor:

2.12 Feel the Light
=============================

The photoresistor is a typical device for analog inputs and it is used in a very similar way to a potentiometer. Its resistance value depends on the intensity of the light, the stronger the irradiated light, the smaller its resistance value; conversely, it increases.


* :ref:`cpn_light`


**Schematic**

|sch_photoresistor|

In this circuit, the 10K resistor and the photoresistor are connected in series, and the current passing through them is the same. The 10K resistor acts as a protection, and the GP28 reads the value after the voltage conversion of the photoresistor.

When the light is enhanced, the resistance of the photoresistor decreases, then its voltage decreases, so the value from GP28 will decrease; if the light is strong enough, the resistance of the photoresistor will be close to 0, and the value of GP28 will be close to 0. At this time, the 10K resistor plays a protective role, so that 3.3V and GND are not connected together, resulting in a short circuit.

If you place the photoresistor in a dark situation, the value of GP28 will increase. In a dark enough situation, the resistance of the photoresistor will be infinite, and its voltage will be close to 3.3v (the 10K resistor is negligible), and the value of GP28 will be close to the maximum value of 65535.


The calculation formula is shown below.

    (Vp/3.3V) x 65535 = Ap



**Wiring**

|wiring_photoresistor|

**Code**

.. note::

    * Open the ``2.12_feel_the_light.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

After the program runs, the Shell prints out the photoresistor values. You can shine a flashlight on it or cover it up with your hand to see how the value will change.

