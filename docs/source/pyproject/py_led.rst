.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_led:

2.1 Hello, LED! 
=======================================

Just as printing "Hello, world!" is the first step in learning to program, using a program to drive an LED is the traditional introduction to learning physical programming.

* :ref:`cpn_led`

**Required Components**

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schematic**

|sch_led|

This circuit works on a simple principle, and the current direction is shown in the figure. The LED will light up after the 220ohm current limiting resistor when GP15 outputs high level (3.3v). The LED will turn off when GP15 outputs low level (0v).

**Wiring**

|wiring_led|

To build the circuit, let's follow the current's direction!

1. The LED is powered by the GP15 pin of the Pico W board, and the circuit begins here.
#. To protect the LED, the current must pass through a 220 ohm resistor. One end of the resistor should be inserted into the same row as the Pico W GP15 pin (row 20 in my circuit), and the other end should be inserted into the free row of the breadboard (row 24).

    .. note::
        The color ring of the 220 ohm resistor is red, red, black, black and brown.

#. If you pick up the LED, you will see that one of its leads is longer than the other. Connect the longer lead to the same row as the resistor, and the shorter lead to the same row across the middle gap on the breadboard.

    .. note::
        The longer lead is the anode, which represents the positive side of the circuit; the shorter lead is the cathode, which represents the negative side. 

        The anode needs to be connected to the GPIO pin through a resistor; the cathode needs to be connected to the GND pin.

#. Using a male-to-male (M2M) jumper wire, connect the LED short pin to the breadboard's negative power bus.
#. Connect the GND pin of Pico W to the negative power bus using a jumper.


**Code**

.. note::

    * Open the ``2.1_hello_led.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

After the code runs, you will see the LED blinking.


**How it works?**


The machine library is required to use GPIO.

.. code-block:: python

    import machine

The library contains all the instructions needed to communicate between MicroPython and Pico W. 
In the absence of this line of code, we will not be able to control any GPIOs.

The next thing to notice is this line:

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

The object ``led`` is defined here. Technically, it can be any name, such as x, y, banana, Michael_Jackson, or any character. 
To ensure that the program is easy to read, it is best to use a name that describes the purpose.

In the second part of this line (the part after the equal sign), we call the Pin function found in the ``machine`` library. It is used to tell Pico's GPIO pins what to do.
A ``Pin`` function has two parameters: the first (15) represents the pin to set; 
The second parameter (machine.Pin.OUT) specifies that the pin should be output rather than input.

The above code has "set" the pin, but it will not light up the LED. To do this, we also need to "use" the pin.

.. code-block:: python

    led.value(1)

The GP15 pin has been set up previously and named ``led``. The function of this statement is to set the value of ``led`` to 1 to turn the LED on.

All in all, to use GPIO, these steps are necessary:

* **import machine library**: This is necessary, and it is only executed once.
* **Set GPIO**: Before using, each pin should be set.
* **Use**: Change the working state of the pin by assigning a value to it.

If we follow the above steps to write an example, then you will get code like this:

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

Run it and you will be able to light up the LED.

Next, we try to add the "extinguished" statement:

.. code-block:: python

    import machine   
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

Based on the code line, this program will turn on the LED first, then turn it off. 
But when you use it, you will find that this is not the case. 
There is no light coming from the LED. This is due to the very rapid execution speed between the two lines, much faster than the human eye can react. 
When the LED lights up, we don't perceive the light instantly. This can be fixed by slowing down the program.

The second line of the program should contain the following statement:

.. code-block:: python

    import utime

Similarly to ``machine``, the ``utime`` library is imported here, which handles all things time-related.
The delays we need to use are included in this. Add a delay statement between ``led.value(1)`` and ``led.value(0)`` and let them be separated by 2 seconds.

.. code-block:: python

    utime.sleep(2)

This is how the code should look now. 
We will see that the LED turns on first, then turns off when we run it:

.. code-block:: python

    import machine 
    import utime  
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

Finally, we should make the LED blink. 
Create a loop, rewrite the program, and it will be what you saw at the beginning of this chapter.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`py_syntax_while` 

**Learn More**


There will usually be an API (Application Programming Interface) file associated with the library. 
It contains all the information necessary to use this library, including detailed descriptions of functions, classes, return types, parameter types, etc.

In this article, we used MicroPython's ``machine`` and ``utime`` libraries, we can find more ways to use them here.

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

Please read the API file to understand this example of making the LED blink!

.. note::

    * Open the ``2.1_hello_led_2.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)