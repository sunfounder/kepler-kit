.. _ar_water:

2.14 - Feel the Water Level
=====================================

|img_water_sensor|

Water sensor is designed for water detection, which can be widely used in sensing rainfall, water level, and even liquid leakage.

It measures the water level by having a series of exposed parallel wire traces to measure the size of the water drops/volume. The water volume is easily converted to an analog signal, and the output analog value can be read directly by the main control board to achieve the water level alarm effect.

.. warning:: 
    
    The sensor cannot be fully submerged in water, please only leave the part where the ten Traces are located in contact with water. Also, energizing the sensor in a humid environment will accelerate the corrosion of the probe and reduce the life of the sensor, so it is recommended that you only supply power when taking readings.

* :ref:`cpn_water`

**Bill of Materials**

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
        - Raspberry Pi Pico W
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - Breadboard
        - 1
        - |link_breadboard_buy|
    *   - 4
        - Wires
        - Several
        - |link_wires_buy|
    *   - 5
        - Water Level Module
        - 1
        - 

**Schematic**

|sch_water|


**Wiring**

|wiring_water|

**Code**

.. note::

   * You can open the file ``2.14_feel_the_water_level.ino`` under the path of ``kepler-kit-main/arduino/2.14_feel_the_water_level``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/32ee87a1-08eb-482f-bf4c-b12b24ef05c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

After the program is run, submerge the Water Sensor module slowly into the water, and as the depth increases, the Shell will print a larger value.


**Learn More**

There is a way to use the analog input module as a digital module.

First, take a reading of the Water Sensor in a dry environment first, record it, and use it as a threshold value. Then, complete the programming and re-read the reading of the water sensor. When the reading of the water sensor deviates significantly from the reading in a dry environment, it is exposed to liquid. In other words, by placing this device near a water pipe, it can detect if a water pipe is leaking.


.. note::

   * You can open the file ``2.14_water_level_threshold.ino`` under the path of ``kepler-kit-main/arduino/2.14_water_level_threshold``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.


.. :raw-code: