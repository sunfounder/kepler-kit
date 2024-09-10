.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_ac_buz:

3.1 - Beep
==================
The active buzzer is a typical digital output device that is as easy to use as lighting up an LED!

* :ref:`cpn_buzzer`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Active :ref:`cpn_buzzer`
        - 1
        - 

**Schematic**

|sch_buzzer|

When the GP15 output is high, after the 1K current limiting resistor (to protect the transistor), the S8050 (NPN transistor) will conduct, so that the buzzer will sound.

The role of S8050 (NPN transistor) is to amplify the current and make the buzzer sound louder. In fact, you can also connect the buzzer directly to GP15, but you will find that the buzzer sound is smaller.

**Wiring**

Two types of buzzers are included in the kit. 
We need to use active buzzer. Turn them around, the sealed back (not the exposed PCB) is the one we want.

|img_buzzer|

The buzzer needs to use a transistor when working, here we use S8050 (NPN Transistor).


|wiring_beep|


**Code**


.. note::

    * You can open the file ``3.1_beep.ino`` under the path of ``kepler-kit-main/arduino/3.1_beep``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

After the code runs, you will hear a beep every second.