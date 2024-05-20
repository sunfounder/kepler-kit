.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_relay:

2.16 Control Another Circuit
=================================

In our daily life, we can press the switch to light up or turn off the lamp.
But what if you want to control the lamp with Pico W so that it can turn off automatically after ten minutes?

A relay can help you accomplish this idea.

A relay is actually a special kind of switch that is controlled by one side of the circuit (usually a low-voltage circuit) and used to control the other side of the circuit (usually a high-voltage circuit).
This makes it practical to modify our home appliances to be controlled by a program, to become smart devices, or even to access the Internet.

.. warning::
    Modification of electrical appliances comes with great danger, do not try it lightly, please do it under the guidance of professionals.

* :ref:`cpn_relay`

Here we only use a simple circuit powered by a breadboard power module as an example to show how to control it using relay.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|


**Wiring**

First, build a low-voltage circuit for controlling a relay.
Driving the relay requires a high current, so a transistor is needed, and here we use the S8050.

|sch_relay_1|

|wiring_relay_1|



A diode (continuity diode) is used here to protect the circuit. The cathode is the end with the silver ribbon connected to the power supply, and the anode is connected to the transistor.

When the voltage input changes from High (5V) to Low (0V), the transistor changes from saturation (amplification, saturation, and cutoff) to cutoff, and there is suddenly no way for current to flow through the coil. 

At this point, if this freewheeling diode does not exist, the coil will produce a self-induced electric potential at both ends that is several times higher than the supply voltage, and this voltage plus the voltage from the transistor power supply is enough to burn it.  

After adding the diode, the coil and the diode instantly form a new circuit powered by the energy stored in the coil to discharge, thus avoiding the excessive voltage will damage devices such as transistors on the circuit.

* :ref:`cpn_diode`    
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

At this point the program is ready to run, and after running you will hear the "tik tok" sound, which is the sound of the contactor coil inside the relay sucking and breaking.

Then we connect the two ends of the load circuit to pins 3 and 6 of the relay respectively.

..(Take the simple circuit powered by the breadboard power module described in the previous article as an example.)

|sch_relay_2|

|wiring_relay_2|

At this point, the relay will be able to control the load circuit on and off.

**Code**

.. note::

    * Open the ``2.16_control_another_circuit.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime
    
    relay = machine.Pin(15, machine.Pin.OUT)
    while True:
        relay.value(1)
        utime.sleep(2)
        relay.value(0)
        utime.sleep(2)

When the code is run, the relay will switch the operating state of the controlled circuit every two seconds.
You can manually comment out one of the lines to further clarify the correspondence between the relay circuit and the load circuit.


**Learn More**

Pin 3 of the relay is normally open and only turns on when the contactor coil is operating; pin 4 is normally closed and turns on when the contactor coil is energized.
Pin 1 is connected to pin 6 and is the common terminal of the load circuit.

By switching one end of the load circuit from pin 3 to pin 4, you will be able to get exactly the opposite operating state.