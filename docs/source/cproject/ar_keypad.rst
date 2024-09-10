.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_keypad:

4.2 - 4x4 Keypad
========================

The 4x4 keyboard, also known as the matrix keyboard, is a matrix of 16 keys excluded in a single panel.

The keypad can be found on devices that mainly require digital input, such as calculators, TV remote controls, push-button phones, vending machines, ATMs, combination locks, and digital door locks.

In this project, we will learn how to determine which key is pressed and get the related key value.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schematic**

|sch_keypad_ar|

The rows of the keyboard (G2 ~ G5) are programmed to go high; if one of G6 ~ G9 is read high, then we know which key is pressed.

For example, if G6 is read high, then numeric key 1 is pressed; this is because the control pins of numeric key 1 are G2 and G6, when numeric key 1 is pressed, G2 and G6 will be connected together and G6 is also high.


**Wiring**

|wiring_keypad_ar|

**Code**


.. note::

    * You can open the file ``4.2_4x4_keypad.ino`` under the path of ``euler-kit/arduino/4.2_4x4_keypad``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit Keypad`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_ad_keypad.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


After the program runs, the Shell will print out the keys you pressed on the Keypad.


**How it works**

1. Including the Library

   We start by including the ``Adafruit_Keypad`` library, which allows us to easily interface with the keypad.

   .. code-block:: arduino

     #include "Adafruit_Keypad.h"

2. Keypad Configuration

   .. code-block:: arduino

     const byte ROWS = 4;
     const byte COLS = 4;
     char keys[ROWS][COLS] = {
       { '1', '2', '3', 'A' },
       { '4', '5', '6', 'B' },
       { '7', '8', '9', 'C' },
       { '*', '0', '#', 'D' }
     };
     byte rowPins[ROWS] = { 2, 3, 4, 5 };
     byte colPins[COLS] = { 8, 9, 10, 11 };

   - The ``ROWS`` and ``COLS`` constants define the dimensions of the keypad. 
   - ``keys`` is a 2D array storing the label for each button on the keypad.
   - ``rowPins`` and ``colPins`` are arrays that store the Arduino pins connected to the keypad rows and columns.

   .. raw:: html

      <br/>


3. Initialize Keypad

   Create an instance of ``Adafruit_Keypad`` called ``myKeypad`` and initialize it.

   .. code-block:: arduino

     Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

4. setup() Function

   Initialize Serial communication and the custom keypad.

   .. code-block:: arduino

     void setup() {
       Serial.begin(9600);
       myKeypad.begin();
     }

5. Main Loop

   Check for key events and display them in the Serial Monitor.

   .. code-block:: arduino

     void loop() {
       myKeypad.tick();
       while (myKeypad.available()) {
         keypadEvent e = myKeypad.read();
         Serial.print((char)e.bit.KEY);
         if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
         else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
       }
       delay(10);
     }

