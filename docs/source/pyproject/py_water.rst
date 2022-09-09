.. _py_water:

2.14 Feel the Water Level
=====================================

|img_water_sensor|

Water sensor is designed for water detection, which can be widely used in sensing rainfall, water level, and even liquid leakage.

It measures the water level by having a series of exposed parallel wire traces to measure the size of the water drops/volume. The water volume is easily converted to an analog signal, and the output analog value can be read directly by the main control board to achieve the water level alarm effect.

.. warning:: 
    
    The sensor cannot be fully submerged in water, please only leave the part where the ten Traces are located in contact with water. Also, energizing the sensor in a humid environment will accelerate the corrosion of the probe and reduce the life of the sensor, so it is recommended that you only supply power when taking readings.

* :ref:`cpn_water`




**Schematic**

|sch_water|


**Wiring**


|wiring_water|

**Code**

.. note::

    * Open the ``2.14_feel_the_water_level.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value=sensor.read_u16()
        print(value)
        utime.sleep_ms(200)


After the program is run, submerge the Water Sensor module slowly into the water, and as the depth increases, the Shell will print a larger value.

**Learn More**

There is a way to use the analog input module as a digital module.

First, take a reading of the Water Sensor in a dry environment first, record it, and use it as a threshold value. Then, complete the programming and re-read the reading of the water sensor. When the reading of the water sensor deviates significantly from the reading in a dry environment, it is exposed to liquid. In other words, by placing this device near a water pipe, it can detect if a water pipe is leaking.


.. note::

    * Open the ``2.14_water_level_threshold.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000 #This value needs to be modified with the environment.

    while True:
        value=sensor.read_u16()
        if value > threshold :
            print("Liquid leakage!")
        utime.sleep_ms(200)
