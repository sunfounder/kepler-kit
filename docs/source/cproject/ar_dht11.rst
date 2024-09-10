.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

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

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - PURCHASE LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Schematic**

|sch_dht11|

**Wiring**

|wiring_dht11|

**Code**

.. note::

    * You can open the file ``6.2_dht11.ino`` under the path of ``euler-kit/arduino/6.2_dht11``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``DHT sensor library`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_dht.png



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

After the code is run, you will see the Serial Monitor continuously print out the temperature and humidity, and as the program runs steadily, these two values will become more and more accurate.

**How it works?**

#. Inclusion of necessary libraries and definition of constants.
   This part of the code includes the DHT sensor library and defines the pin number and sensor type used in this project.

   .. code-block:: arduino
    
      #include <DHT.h>
      #define DHTPIN 16       // Define the pin used to connect the sensor
      #define DHTTYPE DHT11  // Define the sensor type

#. Creation of DHT object.
   Here we create a DHT object using the defined pin number and sensor type.

   .. code-block:: arduino

      DHT dht(DHTPIN, DHTTYPE);  // Create a DHT object

#. This function is executed once when the Arduino starts. We initialize the serial communication and the DHT sensor in this function.

   .. code-block:: arduino

      void setup() {
        Serial.begin(9600);
        Serial.println(F("DHT11 test!"));
        dht.begin();  // Initialize the DHT sensor
      }

#. Main loop.
   The ``loop()`` function runs continuously after the setup function. Here, we read the humidity and temperature values, calculate the heat index, and print these values to the serial monitor.  If the sensor read fails (returns NaN), it prints an error message.

   .. note::
    
      The |link_heat_index| is a way to measure how hot it feels outside by combining the air temperature and the humidity. It is also called the "felt air temperature" or "apparent temperature".

   .. code-block:: arduino

      void loop() {
        delay(2000);
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
        float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      }
