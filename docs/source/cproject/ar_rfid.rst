.. _ar_rfid:


6.5 - Radio Frequency Identification
================================================

Radio Frequency Identification (RFID) refers to technologies that involve using wireless communication between an object (or tag) and an interrogating device (or reader) to automatically track and identify such objects. The tag transmission range is limited to several meters from the reader. A clear line of sight between the reader and tag is not necessarily required.

Most tags contain at least one integrated circuit (IC) and an antenna. 
The microchip stores information and is responsible for managing the radio frequency (RF) communication with the reader. Passive tags do not have an independent energy source and depend on an external electromagnetic signal, provided by the reader, to power their operations. 
Active tags contain an independent energy source, such as a battery. 
Thus, they may have increased processing, transmission capabilities and range.

* :ref:`cpn_mfrc522`

**Schematic**

|sch_rfid|


**Wiring**

|wiring_rfid|

**Code**

.. note::

   * You can open the file ``6.5_rfid_write.ino`` under the path of ``kepler-kit-main/arduino/6.5_rfid_write``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.

   Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

Here you need to use the library called ``MFRC522``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_ar`.


The main function is divided into two:

* ``6.5_rfid_write.ino``: Used to write information to the card (or key).
* ``6.5_rfid_read.ino``: used to read the information in the card (or key)

.. note::

   * You can open the file ``6.5_rfid_write.ino`` under the path of ``kepler-kit-main/arduino/6.5_rfid_write``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   
   Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

After running you will be able to enter message in the serial monitor, ending with ``#``, and then write the message to the card by placing the card (or key) close to the MFRC522 module.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


.. note::

   * You can open the file ``6.5_rfid_read.ino`` under the path of ``kepler-kit-main/arduino/6.5_rfid_read``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   
   Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.

After running, you will be able to read the message stored in the card (or key).

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


**How it works?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         0
    #define SS_PIN          5

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