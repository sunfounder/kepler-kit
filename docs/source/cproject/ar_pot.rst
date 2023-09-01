.. _ar_pot:

2.11 - Turn the Knob
===========================

In the previous projects, we have used the digital input on the Pico W.
For example, a button can change the pin from low level (off) to high level (on). This is a binary working state.

However, Pico W can receive another type of input signal: analog input.
It can be in any state from fully closed to fully open, and has a range of possible values.
The analog input allows the microcontroller to sense the light intensity, sound intensity, temperature, humidity, etc. of the physical world.

Usually, a microcontroller needs an additional hardware to implement analog input-the analogue-to-digital converter (ADC).
But Pico W itself has a built-in ADC for us to use directly.


|pin_adc|

Pico W has three GPIO pins that can use analog input, GP26, GP27, GP28. That is, analog channels 0, 1, and 2.
In addition, there is a fourth analog channel, which is connected to the built-in temperature sensor and will not be introduced here.

In this project, we try to read the analog value of potentiometer.

* :ref:`cpn_potentiometer`

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schematic**

|sch_pot|

The potentiometer is an analog device and when you turn it in 2 different directions.

Connect the middle pin of the potentiometer to the analog pin GP28. The Raspberry Pi Pico W contains a multi-channel, 16-bit analog-to-digital converter. This means that it maps the input voltage between 0 and the operating voltage (3.3V) to an integer value between 0 and 65535, so the GP28 value ranges from 0 to 65535.

The calculation formula is shown below.

    (Vp/3.3V) x 65535 = Ap

Then program the value of GP28 (potentiometer) as the PWM value of GP15 (LED).
This way you will find that by rotating the potentiometer, the brightness of the LED will change at the same time.



**Wiring**


|wiring_pot|

**Code**


.. note::

   * You can open the file ``2.11_turn_the_knob.ino`` under the path of ``kepler-kit-main/arduino/2.11_turn_the_knob``. 
   * Or copy this code into **Arduino IDE**.


    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



When the program is running, we can see the analog value currently read by the GP28 pin in the Serial monitor. 
Turn the knob, and the value will change from 0 to 1023.
At the same time, the brightness of the LED will increase as the analog value increases.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3e3927a-bd1a-4756-83f2-141d47f99b1c/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
     



**How it works?**

To enable Serial Monitor, you need to start serial communication in ``setup()`` and set the datarate to 9600.

.. code-block:: arduino
    :emphasize-lines: 3

    void setup() {
        pinMode(ledPin, OUTPUT);
        Serial.begin(9600);
    }

    
* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

In the loop function, the value of the potentiometer is read, then the value is mapped from 0-1023 to 0-255 and finally the value after the mapping is used to control the brightness of the LED.

.. code-block:: arduino

    void loop() {
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
        int brightness = map(sensorValue, 0, 1023, 0, 255);
        analogWrite(ledPin, brightness);
    }

* `analogRead() <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ is used to read the value of the sensorPin (potentiometer) and assigns it to the variable ``sensorValue``.

.. code-block:: arduino

    int sensorValue = analogRead(sensorPin);

* Print the value of SensorValue in Serial Monitor.

.. code-block:: arduino

    Serial.println(sensorValue);

* Here, the `map(value, fromLow, fromHigh, toLow, toHigh) <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ function is required as the potentiometer value read is in the range 0-1023 and the value of a PWM pin is in the range 0-255. It is used to Re-maps a number from one range to another. That is, a value of fromLow would get mapped to toLow, a value of fromHigh to toHigh, values in-between to values in-between, etc.

.. code-block:: arduino

    int brightness = map(sensorValue, 0, 1023, 0, 255);

* Now we can use this value to control the brightness of the LED.

.. code-block:: arduino

    analogWrite(ledPin,brightness);