.. _ar_74hc_7seg:

5.2 - Number Display
=======================

LED Segment Display can be seen everywhere in life.
For example, on an air conditioner, it can be used to display temperature; on a traffic indicator, it can be used to display a timer.

The LED Segment Display is essentially a device packaged by 8 LEDs, of which 7 strip-shaped LEDs form an "8" shape, and there is a slightly smaller dotted LED as a decimal point. These LEDs are marked as a, b, c, d, e, f, g, and dp. They have their own anode pins and share cathodes. Their pin locations are shown in the figure below.

|img_7seg_cathode|

This means that it needs to be controlled by 8 digital signals at the same time to fully work and the 74HC595 can do this.

* :ref:`cpn_7-seg`


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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - 7 Segment Display
        - 1
        - |link_7segment_buy|
    *   - 7
        - 74HC595
        - 1
        - |link_74hc595_buy|

**Schematic**

|sch_74hc_7seg|

**Wiring**

|wiring_74hc_7seg|


.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - 74HC595
        - LED Segment Display
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp


**Code**

.. note::

   * You can open the file ``5.2_number_display.ino`` under the path of ``kepler-kit-main/arduino/5.2_number_display``. 
   * Or copy this code into **Arduino IDE**.


    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a237801f-40d7-4920-80fb-a349307b1e05/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    
When the program is running, you will be able to see the LED Segment Display display 0~9 in sequence.

**How it works?**

``shiftOut()`` will make 74HC595 output 8 digital signals.
It outputs the last bit of the binary number to Q0, and the output of the first bit to Q7. In other words, writing the binary number "00000001" will make Q0 output high level and Q1~Q7 output low level.

Suppose that the 7-segment Display display the number "1", we need to write a high level for b, c, and write a low level for a, d, e, f, g, and dg.
That is, the binary number "00000110" needs to be written. For readability, we will use hexadecimal notation as "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

Similarly, we can also make the LED Segment Display display other numbers in the same way. The following table shows the codes corresponding to these numbers.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Numbers	
        - Binary Code
        - Hex Code  
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f

Write these codes into ``shiftOut()`` to make the LED Segment Display display the corresponding numbers.