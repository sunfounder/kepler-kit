.. _ar_pa_buz:


3.2 - Custom Tone
==========================================


We have used active buzzer in the previous project, this time we will use passive buzzer.

Like the active buzzer, the passive buzzer also uses the phenomenon of electromagnetic induction to work. The difference is that a passive buzzer does not have oscillating source, so it will not beep if DC signals are used.
But this allows the passive buzzer to adjust its own oscillation frequency and can emit different notes such as "doh, re, mi, fa, sol, la, ti".

Let the passive buzzer emit a melody!

* :ref:`Buzzer`

**Schematic**

|sch_buzzer|

When the GP15 output is high, after the 1K current limiting resistor (to protect the transistor), the S8050 (NPN transistor) will conduct, so that the buzzer will sound.

The role of S8050 (NPN transistor) is to amplify the current and make the buzzer sound louder. In fact, you can also connect the buzzer directly to GP15, but you will find that the buzzer sound is smaller.


**Wiring**

|img_buzzer|

Two buzzers are included in the kit, we use a passive buzzer (one with an exposed PCB on the back).

The buzzer needs a transistor to work, here we use S8050.

|wiring_buzzer|

**Code**


.. note::

   * You can open the file ``3.2_custom_tone.ino`` under the path of ``kepler-kit-main/arduino/3.2_custom_tone``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/69c55e56-9eeb-46bb-b3a8-b354c500cc17/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



**How it works?**

If the passive buzzer given a digital signal, it can only keep pushing the diaphragm without producing sound.

Therefore, we use the ``tone()`` function to generate the PWM signal to make the passive buzzer sound.

This function has three parameters:

  * **pin**, the GPIO pin that controls the buzzer.
  * **frequency**, the pitch of the buzzer is determined by the frequency, the higher the frequency, the higher the pitch.
  * **Duration**, the duration of the tone.


* `tone <https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/>`_

**Learn More**

We can simulate the specific tone according to the fundamental frequency of the piano, so as to play a complete piece of music.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_

.. note::

   * You can open the file ``3.2_custom_tone_2.ino`` under the path of ``kepler-kit-main/arduino/3.2_custom_tone_2``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f934c785-7204-4972-aae5-01edde3c79cc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>