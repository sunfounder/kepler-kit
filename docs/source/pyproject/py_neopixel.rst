.. _py_neopixel:

3.3 RGB LED Strip
======================

WS2812 is a intelligent control LED light source that the control circuit and RGB chip are integrated in a package of 5050 components. 
It internal include intelligent digital port data latch and signal reshaping amplification drive circuit. 
Also include a precision internal oscillator and a programmable constant current control part, 
effectively ensuring the pixel point light color height consistent.

The data transfer protocol use single NZR communication mode. 
After the pixel power-on reset, the DIN port receive data from controller, the first pixel collect initial 24bit data then sent to the internal data latch, the other data which reshaping by the internal signal reshaping amplification circuit sent to the next cascade pixel through the DO port. After transmission for each pixel，the signal to reduce 24bit. 
pixel adopt auto reshaping transmit technology, making the pixel cascade number is not limited the signal transmission, only depend on the speed of signal transmission.


* :ref:`cpn_ws2812`

**Schematic**

|sch_ws2812|


**Wiring**


|wiring_ws2812|


.. warning::
    One thing you need to pay attention to is current.

    Although the LED Strip with any number of LEDs can be used in Pico W, the power of its VBUS pin is limited.
    Here, we will use eight LEDs, which are safe.
    But if you want to use more LEDs, you need to add a separate power supply.
    

**Code**

.. note::

    * Open the ``3.3_rgb_led_strip.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`. 
    
    * Here you need to use the library called ``ws2812.py``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

    import machine 
    from ws2812 import WS2812

    ws = WS2812(machine.Pin(0),8)

    ws[0] = [64,154,227]
    ws[1] = [128,0,128]
    ws[2] = [50,150,50]
    ws[3] = [255,30,30]
    ws[4] = [0,128,255]
    ws[5] = [99,199,0]
    ws[6] = [128,128,128]
    ws[7] = [255,100,0]
    ws.write()


Let's select some favorite colors and display them on the RGB LED Strip!

**How it works?**

In the ws2812 library, we have integrated related functions into the WS2812 class.

You can use the RGB LED Strip with the following statement.

.. code-block:: python

    from ws2812 import WS2812

Declare a WS2812 type object, named "ws", it is connected to "pin", there are "number" RGB LEDs on the WS2812 strip.

.. code-block:: python

    ws = WS2812(pin,number)

ws is an array object, each element corresponds to one RGB LED on the WS2812 strip, for example, ws[0] is the first one, ws[7] is the eighth.

We can assign color values to each RGB LED, these values must be 24-bit color (represented with six hexadecimal digits) or list of 3 8-bit RGB.

For example, the red value is "0xFF0000" or "[255,0,0]".

.. code-block:: python

    ws[i] = color value

Then use this statement to write the color for the LED Strip and light it up.

.. code-block:: python

    ws.write()


You can also directly use the following statement to make all LEDs light up the same color.

.. code-block:: python

    ws.write_all(color value)


**Learn More**

We can randomly generate colors and make a colorful flowing light.

.. note::

    * Open the ``3.3_rgb_led_strip_2.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812
    import utime
    import urandom

    ws = WS2812(machine.Pin(0),8)

    def flowing_light():
        for i in range(7,0,-1):
            ws[i] = ws[i-1]
        ws[0] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write()
        utime.sleep_ms(80)

    while True:
        flowing_light()
        print(ws[0])