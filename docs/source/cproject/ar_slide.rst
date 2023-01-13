.. _ar_slide:

2.7 - Toggle Left and Right
====================================

|img_slide|

The slide switch is a 3-pin device, with pin 2 (middle) being the common pin. When the switch is toggled to the left, the left two pins are connected together, and when toggled to the right, the right two pins are connected together. 

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
        - Slide Switch
        - 1
        - 

**Schematic**

|sch_slide|

GP14 will get a different level, when you toggle the slide switch to the right or left.

The purpose of the 10K resistor is to keep the GP14 low during toggling (not toggling to the far left and not toggling to the far right).

The 104 ceramic capacitor is used here to eliminate jitter.

* :ref:`cpn_slide`
* :ref:`cpn_cap`


**Wiring**

|wiring_slide|

**Code**

.. note::

   * You can open the file ``2.7_toggle_left_right.ino`` under the path of ``kepler-kit-main/arduino/2.7_toggle_left_right``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a20c0733-f234-4d4b-862d-db87f2c249e9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


When the program is running, the serial monitor will show "ON" or "OFF" when you toggle the switch to the left or right.