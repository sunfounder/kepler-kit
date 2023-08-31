.. _ar_micro:

2.8 - Press Gently
==========================

|img_micro_switch|

Micro Switch is also a 3-pin device, the sequence of the 3 pins are C (common pin), NO (normally open) and NC (normally closed) .

When the micro switch is not pressed, 1 (C) and 3 (NC) are connected together, when pressed 1 (C) and 2 (NO) are connected together.

* :ref:`cpn_limit_sw`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - Capacitor
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - Micro Switch
        - 1
        - 

**Schematic**

|sch_limit_sw|

By default, GP14 is low and when pressed, GP14 is high.

The purpose of the 10K resistor is to keep the GP14 low during pressing.

The 104 ceramic capacitor is used here to eliminate jitter.


**Wiring**

|wiring_limit_sw|


**Code**

.. note::

   * You can open the file ``2.8_press_gently.ino`` under the path of ``kepler-kit-main/arduino/2.8_press_gently``. 
   * Or copy this code into **Arduino IDE**.


    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/92a2e356-35da-4e34-92cd-80234e1b59c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


After the program runs, when you toggle the slide switch to the right, "The switch works!" will appear in the Serial Monitor.