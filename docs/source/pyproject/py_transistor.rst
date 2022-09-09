.. _py_transistor:

2.15 Two Kinds of Transistors
==========================================
This kit is equipped with two types of transistors, S8550 and S8050, the former is PNP and the latter is NPN. They look very similar, and we need to check carefully to see their labels.
When a High level signal goes through an NPN transistor, it is energized. But a PNP one needs a Low level signal to manage it. Both types of transistor are frequently used for contactless switches, just like in this experiment.

|img_NPN&PNP|

Let's use LED and button to understand how to use transistor!

:ref:`cpn_transistor`


**Way to connect NPN (S8050) transistor**

|sch_s8050|

In this circuit, when the button is pressed, GP14 is high.

By programming GP15 to output high, after a 1k current limiting resistor (to protect the transistor), the S8050 (NPN transistor) is allowed to conduct, thus allowing the LED to light up.


|wiring_s8050|

**Way to connect PNP(S8550) transistor**

|sch_s8550|

In this circuit, GP14 is low by the default and will change to high when the button is pressed.

By programming GP15 to output **low**, after a 1k current limiting resistor (to protect the transistor), the S8550 (PNP transistor) is allowed to conduct, thus allowing the LED to light up.

The only difference you will notice between this circuit and the previous one is that in the previous circuit the cathode of the LED is connected to the **collector** of the **S8050 (NPN transistor)**, while this one is connected to the **emitter** of the **S8550 (PNP transistor)**.

|wiring_s8550|


**Code**

.. note::

    * Open the ``2.15_transistor.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)    

    while True:
        button_status = button.value()
        if button_status== 1:
            signal.value(1)
        elif button_status == 0:
            signal.value(0)



Two kinds of transistors can be controlled with the same code. When we press the button, Pico W will send a high-level signal to the transistor; when we release it, it will send a low-level signal.
We can see that diametrically opposite phenomena have occurred in the two circuits.

* The circuit using the S8050 (NPN transistor) will light up when the button is pressed, which means it is receiving a high-level conduction circuit;
* The circuit that uses the S8550 (PNP transistor) will light up when it is released, which means it is receiving a low-level conduction circuit.