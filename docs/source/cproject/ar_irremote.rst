.. _ar_irremote:


6.4 - IR Remote Control
================================

In consumer electronics, remote controls are used to operate devices such as televisions and DVD players.
In some cases, remote controls allow people to operate devices that are out of their reach, such as central air conditioners.

IR Receiver is a component with photocell that is tuned to receive to infrared light. 
It is almost always used for remote control detection - every TV and DVD player has one of these in the front to receive for the IR signal from the clicker. 
Inside the remote control is a matching IR LED, which emits IR pulses to tell the TV to turn on, off or change channels.

* :ref:`cpn_irrecv`

**Bill of Materials**

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
        - Raspberry Pi Pico W
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - Breadboard
        - 1
        - |link_breadboard_buy|
    *   - 4
        - Wires
        - Several
        - |link_wires_buy|
    *   - 5
        - IR Receiver
        - 1
        - |link_receiver_buy|

**Schematic**

|sch_irrecv|

**Wiring**

|wiring_irrecv|


**Code**

.. note::

    * You can open the file ``6.4_ir_remote_control.ino`` under the path of ``kepler-kit-main/arduino/6.4_ir_remote_control``. 
    * Or copy this code into **Arduino IDE**.
    * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
    
    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

    Here you need to use the library called ``IRsmallDecoder``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_ar`.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


The new remote control has a plastic piece at the end to isolate the battery inside. You need to pull out this plastic piece to power up the remote when you are using it.
Once the program is running, when you press the remote control, the Serial Monitor will print out the key you pressed.


.. **How it works?**


