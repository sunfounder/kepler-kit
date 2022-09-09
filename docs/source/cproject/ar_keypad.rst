.. _ar_keypad:

4.2 - 4x4 Keypad
========================

The 4x4 keyboard, also known as the matrix keyboard, is a matrix of 16 keys excluded in a single panel.

The keypad can be found on devices that mainly require digital input, such as calculators, TV remote controls, push-button phones, vending machines, ATMs, combination locks, and digital door locks.

In this project, we will learn how to determine which key is pressed and get the related key value.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

**Schematic**

|sch_keypad|

4 pull-down resistors are connected to each of the columns of the matrix keyboard, so that G6 ~ G9 get a stable low level when the keys are not pressed.

The rows of the keyboard (G2 ~ G5) are programmed to go high; if one of G6 ~ G9 is read high, then we know which key is pressed.

For example, if G6 is read high, then numeric key 1 is pressed; this is because the control pins of numeric key 1 are G2 and G6, when numeric key 1 is pressed, G2 and G6 will be connected together and G6 is also high.


**Wiring**

|wiring_keypad|

To make the wiring easier, in the above diagram, the column row of the matrix keyboard and the 10K resistors are inserted into the holes where G6 ~ G9 are located at the same time.


**Code**


.. note::

    * You can open the file ``4.2_4x4_keypad.ino`` under the path of ``kepler-kit-main/arduino/4.2_4x4_keypad``. 
    * Or copy this code into **Arduino IDE**.
    * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
    
    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

    Here you need to use the library called ``Keypad``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_ar`.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


After the program runs, the Shell will print out the keys you pressed on the Keypad.


**How it works**

By calling the ``Keypad.h`` library, you can easily use Keypad.

.. code-block:: arduino

    #include <Keypad.h> 

Library Functions：

.. code-block:: arduino

    Keypad(char *userKeymap, byte *row, byte *col, byte numRows, byte numCols)

Initializes the internal keymap to be equal to ``userKeymap``.

``userKeymap``: The symbols on the buttons of the keypads.

``row``, ``col``: Pin configuration.

``numRows``, ``numCols``: Keypad sizes.

.. code-block:: arduino

    char getKey()

Returns the key that is pressed, if any. This function is non-blocking.