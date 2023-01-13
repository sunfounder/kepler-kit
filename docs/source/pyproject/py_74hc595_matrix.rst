.. _py_74hc_788bs:

5.4 8x8 Pixel Graphics
=============================

LED matrix is a low-resolution dot-matrix display. it uses an array of light-emitting diodes as pixels for patterned displays.

They are bright enough to be visible in outdoor sunlight, and you can see them on some stores, billboards, signs, and variable message displays (such as those on public transit vehicles).

Used in this kit is an 8x8 dot matrix with 16 pins. Their anodes are connected in rows and their cathodes are connected in columns (at the circuit level), which together control these 64 LEDs.

To light the first LED, you should provide a high level for Row1 and a low level for Col1. To light the second LED, it should provide a high level for Row1, a low level for Col2, and so on.
By controlling the current through each pair of rows and columns, each LED can be controlled individually to display characters or pictures.

* :ref:`cpn_788bs`
* :ref:`cpn_74hc595`

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
        - 8x8 LED Matrix
        - 1
        - 
    *   - 6
        - 74HC595
        - 2
        - |link_74hc595_buy|

**Schematic**

|sch_ledmatrix|

The 8x8 dot matrix is controlled by two 74HC595 chips, one controlling the rows and one controlling the columns, while these two chips share G18~G20, which can greatly save the I/O ports of the Pico W board. 

Pico W needs to output a 16-bit binary number at a time, the first 8 bits are given to the 74HC595 which controls the rows, and the last 8 bits are given to the 75HC595 which controls the columns, so that the dot matrix can display a specific pattern.

Q7': Series output pin, connected to DS of another 74HC595 to connect multiple 74HC595s in series.

**Wiring**

Build the circuit. Since the wiring is complicated, let's
make it step by step.

**Step 1:**  First, insert the Pico W, the LED dot matrix
and two 74HC595 chips into breadboard. Connect the 3.3V and GND of the
Pico W to holes on the two sides of the board, then hook up pin16 and
10 of the two 74HC595 chips to VCC, pin 13 and pin 8 to GND.

.. note::
   In the Fritzing image above, the side with label is at the bottom.

|wiring_ledmatrix_4|

**Step 2:** Connect pin 11 of the two 74HC595 together, and then to
GP20; then pin 12 of the two chips, and to GP19; next, pin 14 of the
74HC595 on the left side to GP18 and pin 9 to pin 14 of the second
74HC595.

|wiring_ledmatrix_3|

**Step 3:** The 74HC595 on the right side is to control columns of the
LED dot matrix. See the table below for the mapping. Therefore, Q0-Q7
pins of the 74HC595 are mapped with pin 13, 3, 4, 10, 6, 11, 15, and 16
respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Step 4:** Now connect the ROWs of the LED dot matrix. The 74HC595 on
the left controls ROW of the LED dot matrix. See the table below for the
mapping. We can see, Q0-Q7 of the 74HC595 on the left are mapped with
pin 9, 14, 8, 12, 1, 7, 2, and 5 respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code**

.. note::

    * Open the ``5.4_8x8_pixel_graphics.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)


    glyph = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]

    # Shift the data to 74HC595
    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

Once the program is running, you will see a **x** graphic displayed on the 8x8 dot matrix.

**How it works?**

Here we use two 74HC595s to provide signals for the rows and columns of the dot matrix.
The method of providing signals is the same as ``hc595_shift(dat)`` in the previous chapters, but the difference is that here we need to write a 16-bit binary number at a time.
So we split ``hc595_shift(dat)`` into two functions ``hc595_in(dat)`` and ``hc595_out()``.

.. code-block:: python

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

Then, call ``hc595_in(dat)`` twice in the main loop, write two 8-bit binary numbers and then call ``hc595_out()`` so that a pattern can be displayed.

However, since the LEDs in the dot matrix use common poles, controlling multiple rows/multiple columns at the same time will interfere with each other (e.g., if you light up (1,1) and (2,2) at the same time, (1,2) and (2,1) will inevitably be lit up together).
Therefore, it is necessary to activate one column (or one row) at a time, cycle 8 times, and use the residual image principle to make the human eye merge 8 patterns, so as to get a pair of patterns containing 8x8 amount of information.

.. code-block:: python

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

In this example, the main function nests a ``for`` loop, and when ``i`` is 1, only the first line is activated (the chip in the control line gets the value ``0x80`` ) and the image of the first line is written. 
When ``i`` is 2, the second line is activated (the chip of the control line gets the value ``0x40``) and the image of the second line is written. And so on, completing 8 outputs.

Incidentally, like the 4-digit 7-segment display, it has to maintain the refresh rate to prevent flickering by the human eye, so the extra ``sleep()`` in the main loop should be avoided as much as possible.

**Learn More**

Try replacing ``glyph`` with the following array and see what comes up!

.. code-block:: python

    glyph1 = [0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF]
    glyph2 = [0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF]
    glyph3 = [0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF]
    glyph4 = [0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF]
    glyph5 = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]
    glyph6 = [0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF]

Or, you can try drawing your own graphics.