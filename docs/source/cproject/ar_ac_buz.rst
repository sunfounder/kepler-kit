.. _ar_ac_buz:

3.1 - Beep
==================
The active buzzer is a typical digital output device that is as easy to use as lighting up an LED!

* :ref:`Buzzer`


**Schematic**

|sch_buzzer|

When the GP15 output is high, after the 1K current limiting resistor (to protect the transistor), the S8050 (NPN transistor) will conduct, so that the buzzer will sound.

The role of S8050 (NPN transistor) is to amplify the current and make the buzzer sound louder. In fact, you can also connect the buzzer directly to GP15, but you will find that the buzzer sound is smaller.

**Wiring**

Two types of buzzers are included in the kit. 
We need to use active buzzer. Turn them around, the sealed back (not the exposed PCB) is the one we want.

|img_buzzer|

The buzzer needs to use a transistor when working, here we use S8050 (NPN Transistor).


|wiring_beep|


**Code**


.. note::

   * You can open the file ``3.1_beep.ino`` under the path of ``kepler-kit-main/arduino/3.1_beep``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

After the code runs, you will hear a beep every second.