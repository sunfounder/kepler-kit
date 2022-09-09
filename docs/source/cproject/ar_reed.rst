.. _ar_reed:

2.9 - Feel the Magnetism
===============================

The most common type of reed switch contains a pair of magnetizable, flexible, metal reeds whose end portions are separated by a small gap when the switch is open. 

A magnetic field from an electromagnet or a permanent magnet will cause the reeds to attract each other, thus completing an electrical circuit.
The spring force of the reeds causes them to separate, and open the circuit, when the magnetic field ceases.

A common example of a reed switch application is to detect the opening of a door or windows, for a security alarm.

* :ref:`cpn_reed`

**Schematic**

|sch_reed|

By default, GP14 is low; and will go high when the magnet is near the reed switch.

The purpose of the 10K resistor is to keep the GP14 at a steady low level when no magnet is near.


**Wiring**


|wiring_reed|

**Code**

.. note::

   * You can open the file ``2.9_feel_the_magnetism.ino`` under the path of ``kepler-kit-main/arduino/2.9_feel_the_magnetism``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bba18c-7921-4df9-806f-deffce17de9a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



When a magnet approaches, the circuit will be closed. Just like the button in the :ref:`ar_button` chapter.


.. **Learn More**

.. This time, we tried a flexible way of using switches: interrupt requests, or IRQs.:  interrupt requests, or IRQs.

.. For example, you are reading a book page by page, as if a program is executing a thread. At this time, someone came to you to ask a question and interrupted your reading. Then the person is executing the interrupt request: asking you to stop what you are doing, answer his questions, and then let you return to reading the book after the end.

.. The interrupt request also works in the same way, it allows certain operations to interrupt the main program. 

.. .. :raw-code:

.. .. note::

..    * You can open the file ``2.9_feel_the_magnetism_irq.ino`` under the path of ``kepler-kit-main/arduino/2.9_feel_the_magnetism_irq``. 
..    * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
..    * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

..     Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.



.. A callback function ``detected()`` is defined here, called the interrupt handler. It will be executed when an interrupt request is triggered.
.. Then, an interrupt request is set up in ``setup``, which contains two parts: ``mode`` and ``ISR``.

.. In this program, ``mode`` is ``RISING``, which indicates that the value of the pin is raised from low to high (i.e., button pressed).

.. ``ISR`` is ``detected`` , the callback function we defined.

.. * `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_