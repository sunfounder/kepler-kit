.. _ar_dht11:


6.2 - Temperature - Humidity
=======================================

Humidity and temperature are closely related from the physical quantity itself to the actual people's life.
The temperature and humidity of human environment will directly affect the thermoregulatory function and heat transfer effect of human body.
It will further affect the thinking activity and mental state, thus affecting the efficiency of our study and work.

Temperature is one of the seven basic physical quantities in the International System of Units, which is used to measure the degree of hot and cold of an object.
Celsius is one of the more widely used temperature scales in the world, expressed by the symbol "℃".

Humidity is the concentration of water vapor present in the air.
The relative humidity of air is commonly used in life and is expressed in %RH. Relative humidity is closely related to temperature.
For a certain volume of sealed gas, the higher the temperature, the lower the relative humidity, and the lower the temperature, the higher the relative humidity.

|img_Dht11|

A basic digital temperature and humidity sensor, the **DHT11**, is provided in this kit.
It uses a capacitive humidity sensor and thermistor to measure the surrounding air and outputs a digital signal on the data pins (no analog input pins are required).

* :ref:`cpn_dht11`

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
        - Temperature and Humidity Sensor
        - 1
        - |link_dht22_buy|

**Schematic**

|sch_dht11|

**Wiring**

|wiring_dht11|

**Code**

.. note::

    * You can open the file ``6.2_dht11.ino`` under the path of ``kepler-kit-main/arduino/6.2_dht11``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.
    * The library ``SimpleDHT`` is used here. Please refer to :ref:`add_libraries_ar` for adding it to the Arduino IDE.




.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

After the code is run, you will see the Serial Monitor continuously print out the temperature and humidity, and as the program runs steadily, these two values will become more and more accurate.

**How it works?**

Initialize the DHT11 object. This device requires only a digital input to be used.

.. code-block:: arduino

    int pinDHT11 = 16;
    SimpleDHT11 dht11(pinDHT11);

Reads the current temperature and humidity, which are stored in the variables ``temperature`` and ``humidity``. ``err`` is used to determine the validity of the data.

.. code-block:: arduino

    byte temperature = 0;
    byte humidity = 0;
    int err = dht11.read(&temperature, &humidity, NULL);

Filter invalid data.

.. code-block:: arduino

    if (err != SimpleDHTErrSuccess) {
        Serial.print("Read DHT11 failed, err="); 
        Serial.print(SimpleDHTErrCode(err));
        Serial.print(","); 
        Serial.println(SimpleDHTErrDuration(err)); 
        delay(1000);
        return;
    }    

Print temperature and humidity.

.. code-block:: arduino

    Serial.print((int)temperature); 
    Serial.print(" *C, "); 
    Serial.print((int)humidity); 
    Serial.println(" H");

Finally, the DHT11 sampling rate is 1HZ, a ``delay(1500)`` is needed in the loop.

.. code-block:: arduino

    delay(1500);