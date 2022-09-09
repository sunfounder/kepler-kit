.. _ar_pump:

3.6 - Pumping
=======================


Small centrifugal pumps are suitable for projects with automatic plant watering.
It can also be used to make tiny smart water features.

Its power component is an electric motor, driven in exactly the same way as a normal motor.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Connect the tube to the motor outlet, submerge the pump in water, and then power it on.
    #. You need to make sure that the water level is always higher than the motor. Idling may damage the motor due to heat generation and will also generate noise.
    #. If you are watering plants, you need to avoid soil being drawn in, as this can clog the pump.
    #. If water does not come out of the tube, there may be residual water in the tube blocking the air flow and needs to be drained first.


**Schematic**

|sch_pump|


**Wiring**

.. note::

    * Since pump require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.


|wiring_pump|

**Code**

.. note::

   * You can open the file ``3.6_pumping.ino`` under the path of ``kepler-kit-main/arduino/3.6_pumping``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.
    


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/4194feb8-92d4-4ab4-b51c-286d014af0a6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe> 



After the code is run, the pump starts working and you will see water flowing out of the tube at the same time.


.. note::

    * If you can not upload the code again, this time you need to connect the **RUN** pin on the Pico W with a wire to GND to reset it, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico W to disconnect from the computer. 

    |wiring_run_reset|