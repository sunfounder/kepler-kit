.. _py_74hc_led:

5.1 Microchip - 74HC595
===========================

Integrated circuit (integrated circuit) is a kind of miniature electronic device or component, which is represented by the letter "IC" in the circuit.

A certain process is used to interconnect the transistors, resistors, capacitors, inductors and other components and wiring required in a circuit, fabricate on a small or several small semiconductor wafers or dielectric substrates, and then package them in a package , it has become a micro-structure with the required circuit functions; all of the components have been structured as a whole, making electronic components a big step towards micro-miniaturization, low power consumption, intelligence and high reliability.

The inventors of integrated circuits are Jack Kilby (integrated circuits based on germanium (Ge)) and Robert Norton Noyce (integrated circuits based on silicon (Si)).

This kit is equipped with an IC, 74HC595, which can greatly save the use of GPIO pins.
Specifically, it can replace 8 pins for digital signal output by writing an 8-bit binary number.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`74HC595`

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
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schematic**

|sch_74hc_led|

* When MR (pin10) is high level and OE (pin13) is low level, data is input in the rising edge of SHcp and goes to the memory register through the rising edge of SHcp. 
* If the two clocks are connected together, the shift register is always one pulse earlier than the memory register. 
* There is a serial shift input pin (Ds), a serial output pin (Q) and an asynchronous reset button (low level) in the memory register. 
* The memory register outputs a Bus with a parallel 8-bit and in three states. 
* When OE is enabled (low level), the data in memory register is output to the bus(Q0 ~ Q7).

**Wiring**

.. The 74HC595 is a 16-pin IC with a semi-circular notch on one side (usually the left side of the label). With the notch facing upwards, its pins are shown in the diagram below.


.. Refer to the figure below to build the circuit.


|wiring_74hc_led|

.. 1. Connect 3V3 and GND of Pico W to the power bus of the breadboard.
.. #. Insert 74HC595 across the middle gap into the breadboard.
.. #. Connect the GP0 pin of Pico W to the DS pin (pin 14) of 74HC595 with a jumper wire.
.. #. Connect the GP1 pin of Pico W to the STcp pin (12-pin) of 74HC595.
.. #. Connect the GP2 pin of Pico W to the SHcp pin (pin 11) of 74HC595.
.. #. Connect the VCC pin (16 pin) and MR pin (10 pin) on the 74HC595 to the positive power bus.
.. #. Connect the GND pin (8-pin) and CE pin (13-pin) on the 74HC595 to the negative power bus.
.. #. Insert 8 LEDs on the breadboard, and their anode leads are respectively connected to the Q0~Q1 pins (15, 1, 2, 3, 4, 5, 6, 7) of 74HC595.
.. #. Connect the cathode leads of the LEDs with a 220Ω resistor in series to the negative power bus.


**Code**

.. note::

    * Open the ``5.1_microchip_74hc595.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)

    num = 0

    for i in range(16):
        if i < 8:
            num = (num<<1) + 1
        elif i>=8:
            num = (num & 0b01111111)<<1
        hc595_shift(num)
        print("{:0>8b}".format(num))
        time.sleep_ms(200)

When the program is running, ``num`` will be written into the 74HC595 chip as an eight-bit binary number to control the on and off of the 8 LEDs.
We can see the current value of ``num`` in the shell.

**How it works?**

``hc595_shift()`` will make 74HC595 output 8 digital signals. It outputs the last bit of the binary number to Q0, and the output of the first bit to Q7. In other words, writing the binary number “00000001” will make Q0 output high level and Q1~Q7 output low level.