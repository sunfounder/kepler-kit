.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_dht11:

DHT11 Humiture Sensor
=============================

The digital temperature and humidity sensor DHT11 is a composite sensor that contains a calibrated digital signal output of temperature and humidity. 
The technology of a dedicated digital modules collection and the temperature and humidity sensing technology are applied to ensure that the product has high reliability and excellent long-term stability.

The sensor includes a resistive sense of wet component and an NTC temperature measurement device, and is connected with a high-performance 8-bit microcontroller. 

.. The schematic diagram of the Humiture Sensor Module is as shown following: |img_Hum-sch| 

Only three pins are available for use: VCC, GND, and DATA. 
The communication process begins with the DATA line sending start signals to DHT11, and DHT11 receives the signals and returns an answer signal. 
Then the host receives the answer signal and begins to receive 40-bit humiture data (8-bit humidity integer + 8-bit humidity decimal + 8-bit temperature integer + 8-bit temperature decimal + 8-bit checksum).

|img_Dht11|

**Features**

    #. Humidity measurement range: 20 - 90%RH
    #. Temperature measurement range: 0 - 60℃
    #. Output digital signals indicating temperature and humidity
    #. Working voltage:DC 5V; PCB size: 2.0 x 2.0 cm
    #. Humidity measurement accuracy: ±5%RH
    #. Temperature measurement accuracy: ±2℃


* `DHT11 Datasheet <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Example**

* :ref:`py_dht11` (For MicroPython User)
* :ref:`ar_dht11` (For Arduino User)