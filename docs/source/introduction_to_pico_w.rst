Introduction to Raspberry Pi Pico W
=======================================

|pico_w_side|

Raspberry Pi Pico W brings wireless connectivity to the best-selling Raspberry Pi Pico
product line. Built around our RP2040 silicon platform, Pico products bring our signature
values of high performance, low cost, and ease of use to the microcontroller space.

Raspberry Pi Pico W offers 2.4GHz 802.11 b/g/n wireless LAN support, with an on-board
antenna, and modular compliance certification. It is able to operate in both station and
access-point modes. Full access to network functionality is available to both C and
MicroPython developers.
Raspberry Pi Pico W pairs RP2040 with 2MB of flash memory, and a power supply chip
supporting input voltages from 1.8–5.5V. It provides 26 GPIO pins, three of which can
function as analogue inputs, on 0.1”-pitch through-hole pads with castellated edges.
Raspberry Pi Pico W is available as an individual unit, or in 480-unit reels for automated
assembly

Features
--------------

* 21 mm × 51 mm form factor
* RP2040 microcontroller chip designed by Raspberry Pi in the UK
* Dual-core Arm Cortex-M0+ processor, flexible clock running up to 133 MHz
* 264kB on-chip SRAM
* 2MB on-board QSPI flash
* 2.4GHz 802.11n wireless LAN
* 26 multifunction GPIO pins, including 3 analogue inputs
* 2 × UART, 2 × SPI controllers, 2 × I2C controllers, 16 × PWM channels
* 1 × USB 1.1 controller and PHY, with host and device support
* 8 × Programmable I/O (PIO) state machines for custom peripheral support
* Supported input power 1.8–5.5V DC
* Operating temperature -20°C to +70°C
* Castellated module allows soldering direct to carrier boards
* Drag-and-drop programming using mass storage over USB
* Low-power sleep and dormant modes
* Accurate on-chip clock
* Temperature sensor
* Accelerated integer and floating-point libraries on-chip

Pico's Pins
------------

|pico_pin|


.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - Name
        - Description
        - Function
    *   - GP0-GP28
        - General-purpose input/output pins
        - Act as either input or output and have no fixed purpose of their own
    *   - GND
        - 0 volts ground
        - Several GND pins around Pico W to make wiring easier.
    *   - RUN
        - Enables or diables your Pico
        - Start and stop your Pico W from another microcontroller.
    *   - GPxx_ADCx
        - General-purpose input/output or analog input
        - Used as an analog input as well as a digital input or output – but not both at the same time.
    *   - ADC_VREF
        - Analog-to-digital converter (ADC) voltage reference
        - A special input pin which sets a reference voltage for any analog inputs.
    *   - AGND
        - Analog-to-digital converter (ADC) 0 volts ground
        - A special ground connection for use with the ADC_VREF pin.
    *   - 3V3(O)
        - 3.3 volts power
        - A source of 3.3V power, the same voltage your Pico W runs at internally, generated from the VSYS input.
    *   - 3v3(E)
        - Enables or disables the power
        - Switch on or off the 3V3(O) power, can also switches your Pico W off.
    *   - VSYS
        - 2-5 volts power
        - A pin directly connected to your Pico’s internal power supply, which cannot be switched off without also switching Pico W off.
    *   - VBUS
        - 5 volts power
        - A source of 5 V power taken from your Pico’s micro USB port, and used to power hardware which needs more than 3.3 V.

The best place to find everything you need to get started with your Raspberry Pi Pico W is `here <https://www.raspberrypi.org/documentation/pico/getting-started/>`_

Or you can click on the links below: 

* `Raspberry Pi Pico W product brief <https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf>`_
* `Raspberry Pi Pico W datasheet <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf>`_
* `Getting started with Raspberry Pi Pico: C/C++ development <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `API-level Doxygen documentation for the Raspberry Pi Pico C/C++ SDK <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2040 datasheet <https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf>`_
* `Hardware design with RP2040 <https://datasheets.raspberrypi.org/rp2040/hardware-design-with-rp2040.pdf>`_
* `Raspberry Pi Pico W design files <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEP file <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
