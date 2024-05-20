.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_mpr121:

MPR121 Module
===========================

|img_mpr121|


* **3.3V**: Power supply
* **IRQ**: Open Collector Interrupt Output Pin, active low
* **SCL**: I2C Clock
* **SDA**: I2C Data
* **ADD**: I2C Address Select Input Pin. Connect the ADDR pin to the VSS, VDD, SDA or SCL line, the resulting I2C addresses are 0x5A, 0x5B, 0x5C and 0x5D respectively
* **GND**: Ground
* **0~11**: Electrode 0~11, electrode is a touch sensor. Typically, electrodes can just be some piece of metal, or a wire. But some times depending on the length of our wire, or the material the electrode is on, it can make triggering the sensor difficult. For this reason, the MPR121 allows you to configure what is needed to trigger and untrigger an electrode.

**MPR121 OVERVIEW**

The MPR121 is the second generation capacitive touch sensor controller after
the initial release of the MPR03x series devices. The MPR121 features
increased internal intelligence, some of the major additions include an
increased electrode count, a hardware configurable I2C address, an
expanded filtering system with debounce, and completely independent
electrodes with auto-configuration built in. The device also features a 13th
simulated sensing channel dedicated for near proximity detection using the
multiplexed sensing inputs.

* `MPR121 Datasheet <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Features**

* Low power operation
    • 1.71 V to 3.6 V supply operation
    • 29 μA supply current at 16 ms sampling interval period
    • 3 μA Stop mode current
* 12 capacitance sensing inputs
    • 8 inputs are multifunctional for LED driver and GPIO
* Complete touch detection
    • Auto-configuration for each sensing input
    • Auto-calibration for each sensing input
    • Touch/release threshold and debounce for touch detection
* I2C interface, with Interrupt output
* 3 mm x 3 mm x 0.65 mm 20 lead QFN package
* -40°C to +85°C operating temperature range



**Example**

* :ref:`py_mpr121` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`ar_mpr121` (For Arduino User)