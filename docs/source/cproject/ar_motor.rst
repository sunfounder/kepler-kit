.. _ar_motor:

3.5 - Small Fan
=======================
Now we use the TA6586 to drive the DC motor to make it rotate clockwise and counterclockwise. 
Since the DC motor requires a relatively large current, for safety reasons, 
here we use a power module to supply power to the motor.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`


**Schematic**

|sch_motor|




**Wiring**

.. note::

    * Since DC motors require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.


|wiring_motor|



**Code**

.. note::

   * You can open the file ``3.5_small_fan.ino`` under the path of ``kepler-kit-main/arduino/3.5_small_fan``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Once the program is running, the motor will rotate back and forth in a regular pattern.


.. note::

    * If you can not upload the code again, this time you need to connect the **RUN** pin on the Pico W with a wire to GND to reset it, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico W to disconnect from the computer. 

    |wiring_run_reset|