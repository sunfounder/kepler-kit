.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_led_bar:

2.2 Display the Level
=============================

The first project is simply to make the LED blink. For this project, let's use the LED Bar Graph, which contains 10 LEDs in a plastic enclosure, generally used to display power or volume levels.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schematic**

|sch_ledbar|

In the LED Bar Graph, there are 10 LEDs, each of which can be controlled individually. Each LED's anode is connected to GP6*GP15, and its cathode to a 220ohm resistor, and then to GND.



**Wiring**

|wiring_ledbar|

**Code**

.. note::

    * Open the ``2.2_display_the_level.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

On the LED Bar Graph, you'll see LEDs lighting up and then turning off in sequence when the program is running.

**How it works?**

The LED Bar consists of ten LEDs that are controlled by ten pins, which means that we must define these pins.
The process would be too tedious if we defined them one by one. So, here we use ``Lists``.

.. note::
    Python lists are one of the most versatile data types that allow us to work with multiple elements at once, and created by placing elements inside square brackets [], separated by commas.

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

A list ``pin`` is defined by this line of code, which contains the ten elements ``6,7,8,9,10,11,12,13,14,15``.
We can use the index operator [] to access an item in a list. In Python, indices start at 0. So, a list having 10 elements will have an index from 0 to 9.
Using this list as an example, ``pin[0]`` is ``6`` and ``pin[4]`` is ``10``.

Next, declare an empty list ``led`` that will be used to define ten LED objects.

.. code-block:: python

    led = []    

Due to the length of the list, which is 0, direct operations on the array, such as printing led[0]**, won't work. There are new items we need to add.


.. code-block:: python

    led.append(None)

As a result of this ``append()`` method, the list ``led`` has its first item, of length 1, and ``led[0]`` becomes a valid element despite its current value of ``None`` (which stands for null).

Our next step is to define ``led[0]``, the LED connected to pin 6, as the first LED object.

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

The first LED object has now been defined.

As you can see, we have created the ten pin numbers as a list **pin**, which we can substitute into this line to make it easier to do bulk operations.

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

Use a ``for`` statement to have all 10 pins execute the above statement.

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`syntax_list`
* :ref:`syntax_forloop`

Use another ``for`` loop to make the ten LEDs on the LED Bar switch states one by one.

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

The code is finished by putting the above piece of code in a while loop.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)


