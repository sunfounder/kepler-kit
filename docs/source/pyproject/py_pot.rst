.. _py_pot:

2.11 Turn the Knob
===========================

In the previous projects, we have used the digital input on the Pico W.
For example, a button can change the pin from low level (off) to high level (on). This is a binary working state.

However, Pico W can receive another type of input signal: analog input.
It can be in any state from fully closed to fully open, and has a range of possible values.
The analog input allows the microcontroller to sense the light intensity, sound intensity, temperature, humidity, etc. of the physical world.

Usually, a microcontroller needs an additional hardware to implement analog input-the analogue-to-digital converter (ADC).
But Pico W itself has a built-in ADC for us to use directly.


|pin_adc|

Pico W has three GPIO pins that can use analog input, GP26, GP27, GP28. That is, analog channels 0, 1, and 2.
In addition, there is a fourth analog channel, which is connected to the built-in temperature sensor and will not be introduced here.

In this project, we try to read the analog value of potentiometer.

* :ref:`cpn_potentiometer`

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
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|


**Schematic**

|sch_pot|

The potentiometer is an analog device and when you turn it in 2 different directions.

Connect the middle pin of the potentiometer to the analog pin GP28. The Raspberry Pi Pico W wcontains a multi-channel, 16-bit analog-to-digital converter. This means that it maps the input voltage between 0 and the operating voltage (3.3V) to an integer value between 0 and 65535, so the GP28 value ranges from 0 to 65535.

The calculation formula is shown below.

    (Vp/3.3V) x 65535 = Ap

Then program the value of GP28 (potentiometer) as the PWM value of GP15 (LED).
This way you will find that by rotating the potentiometer, the brightness of the LED will change at the same time.

**Wiring**



|wiring_pot|


**Code**


.. note::

    * Open the ``2.11_turn_the_knob.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value=potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

When the program is running, we can see the analog value currently read by the GP28 pin in the shell. 
Turn the knob, and the value will change from 0 to 65535.
At the same time, the brightness of the LED will increase as the analog value increases.

**How it works?**

.. code-block:: python

    potentiometer = machine.ADC(28)

Access the ADC associated with a source identified by id. In this example it is GP28.

.. code-block:: python

    potentiometer.read_u16()

Take an analog reading and return an integer in the range 0-65535. The return value represents the raw reading taken by the ADC, scaled such that the minimum value is 0 and the maximum value is 65535.


* `machine.ADC - MicroPython Docs <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_