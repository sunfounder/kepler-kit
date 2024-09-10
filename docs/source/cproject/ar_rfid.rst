.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_rfid:


6.5 - Radio Frequency Identification
================================================

Radio Frequency Identification (RFID) refers to technologies that involve using wireless communication between an object (or tag) and an interrogating device (or reader) to automatically track and identify such objects. The tag transmission range is limited to several meters from the reader. A clear line of sight between the reader and tag is not necessarily required.

Most tags contain at least one integrated circuit (IC) and an antenna. 
The microchip stores information and is responsible for managing the radio frequency (RF) communication with the reader. Passive tags do not have an independent energy source and depend on an external electromagnetic signal, provided by the reader, to power their operations. 
Active tags contain an independent energy source, such as a battery. 
Thus, they may have increased processing, transmission capabilities and range.

* :ref:`cpn_mfrc522`

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - PURCHASE LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Schematic**

|sch_rfid|


**Wiring**

|wiring_rfid|

**Code**

.. note::

   * The ``MFRC522`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_mfrc522.png

The main function is divided into two:

* ``6.5_rfid_write`` to write information to the card (or key).

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  After running you will be able to enter message in the serial monitor, ending with ``#``, and then write the message to the card by placing the card (or key) close to the MFRC522 module.

* ``6.5_rfid_read`` to read the information from the card (or key).

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  After running, you will be able to read the message stored in the card (or key).


**How it works?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         9
    #define SS_PIN          17

    MFRC522 mfrc522(SS_PIN, RST_PIN);

First, instantiate ``MFRC522()`` class.

For simplicity of use, the ``MFRC522`` library is further encapsulated with the following functions.

* ``void simple_mfrc522_init()`` : Starts SPI communication and initializes the mfrc522 module.
* ``void simple_mfrc522_get_card()`` : Suspends the program until the card (or key) is detected, prints the card UID and PICC type.
* ``void simple_mfrc522_write(String text)`` : Write a string for the card (or key).
* ``void simple_mfrc522_write(byte* buffer)`` : Writes information for the card (or key), which usually comes from the serial port.
* ``void simple_mfrc522_write(byte section, String text)`` : Writes a string for a specific sector. ``section`` is set to 0 to write sectors 1-2; ``section`` is set to 1 to write sectors 3-4.
* ``void simple_mfrc522_write(byte section, byte* buffer)`` : Writes information for a specific sector, usually from the serial port. ``section`` set to 0, writes 1-2 sectors; ``section`` set to 1, writes 3-4 sectors.
* ``String simple_mfrc522_read()`` : Reads the information in the card (or key), returns a string.
* ``String simple_mfrc522_read(byte section)`` : Reads the information in a specific sector, returns a string. ``section`` is set to 0, writes 1-2 sectors; ``section`` is set to 1, writes 3-4 sectors.


In the ``6.5_rfid_write.ino`` example, the ``Serial.readBytesUntil()`` function is used, which is a common serial input method.

* `Serial.readBytesUntil <https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytesuntil/>`_