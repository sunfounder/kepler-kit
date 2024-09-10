.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_transistor:

2.15 - Two Kinds of Transistors
==========================================

This kit is equipped with two types of transistors, S8550 and S8050, the former is PNP and the latter is NPN. They look very similar, and we need to check carefully to see their labels.
When a High level signal goes through an NPN transistor, it is energized. But a PNP one needs a Low level signal to manage it. Both types of transistor are frequently used for contactless switches, just like in this experiment.

|img_NPN&PNP|

Let's use LED and button to understand how to use transistor!

:ref:`cpn_transistor`

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
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|

**Way to connect NPN (S8050) transistor**

|sch_s8050|

In this circuit, when the button is pressed, GP14 is high.

By programming GP15 to output high, after a 1k current limiting resistor (to protect the transistor), the S8050 (NPN transistor) is allowed to conduct, thus allowing the LED to light up.


|wiring_s8050|

.. 1. Connect 3V3 and GND of Pico W to the power bus of the breadboard.
.. #. Connect the anode lead of the LED to the positive power bus via a 220Ω resistor.
.. #. Connect the cathode lead of the LED to the **collector** lead of the transistor.
.. #. Connect the base lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **emitter** lead of the transistor to the negative power bus.
.. #. Connect one side of the button to the GP14 pin, and use a 10kΩ resistor connect the same side and negative power bus. The other side to the positive power bus.

.. .. note::
..     * The color ring of 220Ω resistor is red, red, black, black and brown.
..     * The color ring of the 1kΩ resistor is brown, black, black, brown and brown.
..     * The color ring of the 10kΩ resistor is brown, black, black, red and brown.

**Way to connect PNP(S8550) transistor**

|sch_s8550|

In this circuit, GP14 is low by the default and will change to high when the button is pressed.

By programming GP15 to output **low**, after a 1k current limiting resistor (to protect the transistor), the S8550 (PNP transistor) is allowed to conduct, thus allowing the LED to light up.

The only difference you will notice between this circuit and the previous one is that in the previous circuit the cathode of the LED is connected to the **collector** of the **S8050 (NPN transistor)**, while this one is connected to the **emitter** of the **S8550 (PNP transistor)**.

|wiring_s8550|

.. 1. Connect 3V3 and GND of Pico W to the power bus of the breadboard.
.. #. Connect the anode lead of the LED to the positive power bus via a 220Ω resistor.
.. #. Connect the cathode lead of the LED to the **emitter** lead of the transistor.
.. #. Connect the base lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **collector** lead of the transistor to the negative power bus.
.. #. Connect o

**Code**

.. note::

    * You can open the file ``2.15_transistor.ino`` under the path of ``kepler-kit-main/arduino/2.15_transistor``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/77c437de-028f-47c1-9d79-177e90eb0599/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Two kinds of transistors can be controlled with the same code. When we press the button, Pico W will send a high-level signal to the transistor; when we release it, it will send a low-level signal.
We can see that diametrically opposite phenomena have occurred in the two circuits.

* The circuit using the S8050 (NPN transistor) will light up when the button is pressed, which means it is receiving a high-level conduction circuit;
* The circuit that uses the S8550 (PNP transistor) will light up when it is released, which means it is receiving a low-level conduction circuit.