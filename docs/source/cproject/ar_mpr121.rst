.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_mpr121:

4.3 - Electrode Keyboard
================================

The MPR121 is a good choice when you want to add a large number of touch switches to your project. It has electrodes that can be extended with conductors.
If you connect the electrodes to a banana, you can turn the banana into a touch switch.

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schematic**

|sch_mpr121_ar|



**Wiring**

|wiring_mpr121_ar|

**Code**

.. note::

    * You can open the file ``4.3_electrode_keyboard.ino`` under the path of ``euler-kit/arduino/4.3_electrode_keyboard``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit MPR121`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_mpr121.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f31048b7-0f98-4d49-8c2e-26b3908e98cb/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


After the program runs, you can touch the twelve electrodes on the MPR121 module by hand and the touch status of these electrodes will be recorded in a 12-bit Boolean type array that will be printed on the serial monitor.
If the first and eleventh electrodes are touched, ``100000000010`` is printed.

You can extend the electrodes by connecting other conductors such as fruit, wire, foil, etc. This will give you more ways to trigger these electrodes.

**How it works?**

Initialize the ``MPR121`` object. At this point the state of the module's electrodes will be recorded as initial values.
If you extend the electrodes, you need to rerun the example to reset the initial values.

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

Gets the value of the current electrode, it will get a 12-bit binary value. If you touch the first and the eleventh electrode, it gets ``100000000010``.

.. code-block:: arduino

    // Get the currently touched pads
    currtouched = cap.touched();

Determine if the electrode state has changed.

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // reset our state
        lasttouched = currtouched;
    }

If a change in electrode state is detected, the values of ``currtouched`` are stored in the ``touchStates[12]`` array bit by bit. Finally, the array is printed.

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }