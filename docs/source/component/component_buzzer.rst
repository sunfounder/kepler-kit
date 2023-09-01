.. _cpn_buzzer:

Buzzer
=======


As a type of electronic buzzer with an integrated structure, buzzers, which are supplied by DC power, are widely used in computers, printers, photocopiers, alarms, electronic toys, automotive electronic devices, telephones, timers and other electronic products or voice devices. 

Buzzers can be categorized as active and passive ones (see the following picture). Turn the buzzer so that its pins are facing up, and the buzzer with a green circuit board is a passive buzzer, while the one enclosed with a black tape is an active one.


|img_buzzer|

The difference between an active buzzer and a passive buzzer: 

An active buzzer has a built-in oscillating source, so it will make sounds when electrified. But a passive buzzer does not have such source, so it will not beep if DC signals are used; instead, you need to use square waves whose frequency is between 2K and 5K to drive it. The active buzzer is often more expensive than the passive one because of multiple built-in oscillating circuits.

The following is the electrical symbol of a buzzer. It has two pins with positive and negative poles. With a + in the surface represents the anode and the other is the cathode. 

|img_buzzer_symbol|

You can check the pins of the buzzer, the longer one is the anode and the shorter one is the cathode. Please don't mix them up when connecting, otherwise the buzzer will not make sound. 

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Example
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**Example**

* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)
* :ref:`per_service_bell` (For Piper Make User)
* :ref:`per_reversing_system` (For Piper Make User)
* :ref:`per_reaction_game` (For Piper Make User)