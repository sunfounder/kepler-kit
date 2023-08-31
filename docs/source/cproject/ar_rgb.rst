.. _ar_rgb:


2.4 - Colorful Light
==============================================

As we know, light can be superimposed. For example, mix blue light and green light give cyan light, red light and green light give yellow light.
This is called "The additive method of color mixing".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Based on this method, we can use the three primary colors to mix the visible light of any color according to different specific gravity. For example, orange can be produced by more red and less green.

In this chapter, we will use RGB LED to explore the mystery of additive color mixing!

RGB LED is equivalent to encapsulating Red LED, Green LED, Blue LED under one lamp cap, and the three LEDs share one cathode pin.
Since the electric signal is provided for each anode pin, the light of the corresponding color can be displayed. By changing the electrical signal intensity of each anode, it can be made to produce various colors.

* :ref:`cpn_rgb`

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
        - Resistor
        - 3（1-330Ω, 2-220Ω）
        - |link_resistor_buy|
    *   - 6
        - RGB LED
        - 1
        - |link_rgb_led_buy|

**Schematic**

|sch_rgb|

The PWM pins GP13, GP14 and GP15 control the Red, Green and Blue pins of the RGB LED respectively, and connect the common cathode pin to GND. This allows the RGB LED to display a specific color by superimposing light on these pins with different PWM values.



**Wiring**

|img_rgb_pin|

An RGB LED has 4 pins: the longest pin is the common cathode pin, which is usually connected to GND, the left pin next to the longest pin is Red, and the 2 pins on the right are Green and Blue.


|wiring_rgb|


**Code**

Here, we can choose our favorite color in drawing software (such as paint) and display it with RGB LED.

.. note::

   * You can open the file ``2.4_colorful_light.ino`` under the path of ``kepler-kit-main/arduino/2.4_colorful_light``. 
   * Or copy this code into **Arduino IDE**.


    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.




.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/c869191c-026c-4aac-8396-09eaf6ee2204/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



|img_take_color|

Write the RGB value into ``color_set()``, you will be able to see the RGB light up the colors you want.


**How it works?**

In this example, the function used to assign values to the three pins of RGB is packaged in an independent subfunction ``color()``.

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

In ``loop()``, RGB value works as an input argument to call the function ``color()`` to realize that the RGB can emit different colors.

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); //  red 
        delay(1000); 
        color(0,255, 0); //  green  
        delay(1000);  
        color(0, 0, 255); //  blue  
        delay(1000);
    }

    