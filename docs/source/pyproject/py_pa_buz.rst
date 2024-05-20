.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_pa_buz:

3.2 Custom Tone
==========================================


We have used active buzzer in the previous project, this time we will use passive buzzer.

Like the active buzzer, the passive buzzer also uses the phenomenon of electromagnetic induction to work. The difference is that a passive buzzer does not have oscillating source, so it will not beep if DC signals are used.
But this allows the passive buzzer to adjust its own oscillation frequency and can emit different notes such as "doh, re, mi, fa, sol, la, ti".

Let the passive buzzer emit a melody!

* :ref:`cpn_buzzer`

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
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schematic**

|sch_buzzer|

When the GP15 output is high, after the 1K current limiting resistor (to protect the transistor), the S8050 (NPN transistor) will conduct, so that the buzzer will sound.

The role of S8050 (NPN transistor) is to amplify the current and make the buzzer sound louder. In fact, you can also connect the buzzer directly to GP15, but you will find that the buzzer sound is smaller.


**Wiring**

|img_buzzer|

Two buzzers are included in the kit, we use a passive buzzer (one with an exposed PCB on the back).

The buzzer needs a transistor to work, here we use S8050.

|wiring_buzzer|

.. 1. Connect 3V3 and GND of Pico W to the power bus of the breadboard.
.. #. Connect the positive pin of the buzzer to the positive power bus.
.. #. Connect the cathode pin of the buzzer to the **collector** lead of the transistor.
.. #. Connect the **base** lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **emitter** lead of the transistor to the negative power bus.


**Code**

.. note::

    * Open the ``3.2_custom_tone.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    tone(buzzer,440,250)
    utime.sleep_ms(500)
    tone(buzzer,494,250)
    utime.sleep_ms(500)
    tone(buzzer,523,250)


**How it works?**

If the passive buzzer given a digital signal, it can only keep pushing the diaphragm without producing sound.

Therefore, we use the ``tone()`` function to generate the PWM signal to make the passive buzzer sound.

This function has three parameters:

* **pin**, the GPIO pin that controls the buzzer.
* **frequency**, the pitch of the buzzer is determined by the frequency, the higher the frequency, the higher the pitch.
* **Duration**, the duration of the tone.

We use the ``duty_u16()`` function to set the duty cycle to 30000(about 50%). It can be other numbers, and it only needs to generate a discontinuous electrical signal to oscillate.



**Learn More**

We can simulate the specific tone according to the fundamental frequency of the piano, so as to play a complete piece of music.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_



.. note::

    * Open the ``3.2_custom_tone_2.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    NOTE_C4 = 262
    NOTE_G3 = 196
    NOTE_A3 = 220
    NOTE_B3 = 247

    melody =[NOTE_C4,NOTE_G3,NOTE_G3,NOTE_A3,NOTE_G3,NOTE_B3,NOTE_C4]

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    for note in melody:
        tone(buzzer,note,250)
        utime.sleep_ms(150)
