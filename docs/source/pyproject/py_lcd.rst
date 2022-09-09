.. _py_lcd:

3.4 Liquid Crystal Display
===============================

LCD1602 is a character type liquid crystal display, which can display 32 (16*2) characters at the same time.

As we all know, though LCD and some other displays greatly enrich the man-machine interaction, 
they share a common weakness. When they are connected to a controller, 
multiple IOs will be occupied of the controller which has no so many outer ports. 
Also it restricts other functions of the controller. 
Therefore, LCD1602 with an I2C bus is developed to solve the problem.

* :ref:`cpn_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_


|pin_i2c|

Here we will use the I2C0 interface to control the LCD1602 and display text.


**Schematic**

|sch_lcd|

**Wiring**

|wiring_lcd|

**Code**

.. note::

    * Open the ``3.4_liquid_crystal_display.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`. 
    
    * Here you need to use the library called ``lcd1602.py``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

    from lcd1602 import LCD
    import utime

    lcd = LCD()
    string = " Hello!\n"
    lcd.message(string)
    utime.sleep(2)
    string = "    Sunfounder!"   
    lcd.message(string)
    utime.sleep(2)
    lcd.clear()   

After the program runs, you will be able to see two lines of text appear on the LCD in turn, and then disappear.

.. note:: When the code is running, if the screen is blank, you can use a screwdriver to turn the potentiometer on the back of the module to increase the contrast.

**How it works?**

In the lcd1602 library, we integrate the relevant functions of lcd1602 into the LCD class.

Import lcd1602 library

.. code-block:: python

    from lcd1602 import LCD    

Declare an object of the LCD class and name it lcd.

.. code-block:: python

    lcd = LCD()

This statement will display the text on the LCD. It should be noted that the argument must be a string type. If we want to pass an integer or float, we must use the forced conversion statement ``str()``.

.. code-block:: python

    lcd.message(string)


If you call this statement multiple times, lcd will superimpose the texts. This requires the use of the following statement to clear the display.

.. code-block:: python

    lcd.clear()

