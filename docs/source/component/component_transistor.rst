.. _cpn_transistor:

Transistor
============

|img_NPN&PNP|

Transistor is a semiconductor device that controls current by current. It functions by amplifying weak signal to larger amplitude signal and is also used for non-contact switch. 

A transistor is a three-layer structure composed of P-type and N-type semiconductors. They form the three regions internally. The thinner in the middle is the base region; the other two are both N-type or P-type ones – the smaller region with intense majority carriers is the emitter region, when the other one is the collector region. This composition enables the transistor to be an amplifier. 
From these three regions, three poles are generated respectively, which are base (b), emitter (e), and collector (c). They form two P-N junctions, namely, the emitter junction and collection junction. The direction of the arrow in the transistor circuit symbol indicates that of the emitter junction. 

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

Based on the semiconductor type, transistors can be divided into two groups, the NPN and PNP ones. From the abbreviation, we can tell that the former is made of two N-type semiconductors and one P-type and that the latter is the opposite. See the figure below. 

.. note::
    s8550 is PNP transistor and the s8050 is the NPN one, They look very similar, and we need to check carefully to see their labels.

|img_transistor_symbol|

When a High level signal goes through an NPN transistor, it is energized. But a PNP one needs a Low level signal to manage it. Both types of transistor are frequently used for contactless switches, just like in this experiment.


* `S8050 Transistor Datasheet <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

Put the label side facing us and the pins facing down. The pins from left to right are emitter(e), base(b), and collector(c).

|img_ebc|

.. note::
    * The base is the gate controller device for the larger electrical supply. 
    * In the NPN transistor, the collector is the larger electrical supply and the emitter is the outlet for that supply, the PNP transistor is just the opposite.


.. Example
.. -------------------

.. :ref:`Two Kinds of Transistors`


**Example**

* :ref:`py_transistor` (For MicroPython User)
* :ref:`py_relay` (For MicroPython User)
* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)
* :ref:`ar_transistor` (For Arduino User)
* :ref:`ar_relay` (For Arduino User)
* :ref:`per_service_bell` (For Piper Make User)
* :ref:`per_reversing_system` (For Piper Make User)
* :ref:`per_reaction_game` (For Piper Make User)