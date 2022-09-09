.. _py_mpr121:

4.3 Electrode Keyboard
================================

The MPR121 is a good choice when you want to add a large number of touch switches to your project. It has electrodes that can be extended with conductors.
If you connect the electrodes to a banana, you can turn the banana into a touch switch.

* :ref:`cpn_mpr121`


**Schematic**

|sch_mpr121|


**Wiring**

|wiring_mpr121|

**Code**

.. note::

    * Open the ``4.3_electrode_keyboard.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`. 
    
    * Here you need to use the library called ``mpr121.py``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # check all keys
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

After the program runs, you can touch the twelve electrodes on the MPR121 with your hand and the touched electrodes will be printed out.

You can extend the electrodes to connect other conductors such as fruit, wire, foil, etc. This will give you more ways to trigger these electrodes.

**How it works?**

In the mpr121 library, we have integrated the functionality into the ``MPR121`` class.

.. code-block:: python

    from mpr121 import MPR121

MPR121 is an I2C module that requires a set of I2C pins to be defined to initialize the ``MPR121`` object. At this point the state of the module's electrodes will be recorded as initial values. If the electrodes are extended, the example needs to be rerun to reset the initial values.

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

Then use ``mpr.get_all_states()`` to read if the electrodes are triggered. If electrodes 2 and 3 are triggered, the value ``[2, 3]`` will be generated.


.. code-block::

    while True:
        value = mpr.get_all_states()
        if len(value) ! = 0:
            print(value)
        time.sleep_ms(100)

You can also use ``mpr.is_touched(electrode)`` to detect a specific electrode. When triggered, it returns ``True``, otherwise it returns ``False``.

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)