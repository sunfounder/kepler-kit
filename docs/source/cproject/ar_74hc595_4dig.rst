.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_4dig:

5.3 - Time Counter
================================


4-Digit 7-segment display consists of four 7- segment displays working
together.

The 4-digtal 7-segment display works independently. It uses the
principle of human visual persistence to quickly display the characters
of each 7-segment in a loop to form continuous strings.

For example, when "1234" is displayed on the display, "1" is displayed
on the first 7-segment, and "234" is not displayed. After a period of
time, the second 7-segment shows "2", the 1st 3th 4th of 7-segment does
not show, and so on, the four digital display show in turn. This process
is very short (typically 5ms), and because of the optical afterglow
effect and the principle of visual residue, we can see four characters
at the same time.

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
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Schematic**

|sch_4dig|

Here the wiring principle is basically the same as :ref:`ar_74hc_led`, the only difference is that Q0-Q7 are connected to the a ~ g pins of the 4-digit 7-segment display.

Then G10 ~ G13 will select which 7-segment display to work.

**Wiring**


|wiring_4dig|

**Code**

.. note::

    * You can open the file ``5.3_time_counter.ino`` under the path of ``kepler-kit-main/arduino/5.3_time_counter``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0e97386e-417e-4f53-a026-5f37e36deba4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

After the program is run, you will see the 4-digit 7-segment display become a counter and the number increases by 1 per second.


**How it works?**

Writing signals to each 7-segment display is done in the same way as :ref:`ar_74hc_7seg`, using the ``hc595_shift()`` function.
The core point of the 4-digit 7-segment display is to selectively activate each 7-segment display. The code associated with this is as follows.

.. code-block:: arduino

    const int placePin[4] = {13,12,11,10}; 

    void setup ()
    {
        for (int i = 0; i<4;i++){
            pinMode(placePin[i],OUTPUT);
        }
    }

    void loop()
    { 
        pickDigit(0);
        hc595_shift(count%10/1);
        
        pickDigit(1);
        hc595_shift(count%100/10);
        
        pickDigit(2);
        hc595_shift(count%1000/100);
        
        pickDigit(3);
        hc595_shift(count%10000/1000);
    }

    void pickDigit(int digit){
        for(int i = 0; i < 4; i++){
            digitalWrite(placePin[i],HIGH);
        }
        digitalWrite(placePin[digit],LOW);
    }

Here, four pins (GP10, GP11, GP12, GP13) are used to control each bit of the  4-digit 7-segment display individually.
When the status of these pins is ``LOW``, the corresponding 7-segment display is active; when the status is ``HIGH``, the 7-segment display does not work.


Here the ``pickDigit(digit)`` function is used to unable all 7-segment displays and then enable a particular digit individually.
After that, ``hc595_shift()`` is used to write the corresponding 8 bits code for the 7-segment display.

The 4-digit 7-segment display needs to be continuously activated in turn so that we can see it display four digits, which means that the main program cannot easily add code that would affect the timing.

However, we need to add a timing function to this example, if we add a ``delay (1000)``, we will be able to detect the illusion of its four 7-segment displays working at the same time, exposing the fact that only one 7-segment display at a time to light.

Then, using the ``millis()`` function is an excellent way to do this.

.. code-block:: arduino

    void setup ()
    {
        timerStart = millis();
    }

    void loop()
    {
        unsigned int count = (millis()-timerStart)/1000;
    }

The ``millis()`` function gets the number of milliseconds that have passed since the current program was started. We record the first time value as ``timerStart``; 

then when we need to get the time again, we call the ``millis()`` function again and subtract ``timerStart`` from the value to get how long the program has been running.

Finally, convert this time value and let the 4-digit 7-segment display to display it.


* `millis() <https://www.arduino.cc/reference/en/language/functions/time/millis/>`_