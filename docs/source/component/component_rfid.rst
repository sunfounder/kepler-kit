.. _cpn_mfrc522:

MFRC522 Module
====================

|img_mfrc522|

MFRC522 is a kind of integrated read and write card chip. It is commonly
used in the radio at 13.56MHz. Launched by the NXP Company, it is a
low-voltage, low-cost, and small-sized non-contact card chip, a best
choice of intelligent instrument and portable handheld device.

The MF RC522 uses advanced modulation and demodulation concept which
fully presented in all types of 13.56MHz passive contactless
communication methods and protocols. In addition, it supports rapid
CRYPTO1 encryption algorithm to verify MIFARE products. MFRC522 also
supports MIFARE series of high-speed non-contact communication, with a
two-way data transmission rate up to 424kbit/s. As a new member of the
13.56MHz highly integrated reader card series, MF RC522 is much similar
to the existing MF RC500 and MF RC530 but there also exists great
differences. It communicates with the host machine via the serial manner
which needs less wiring. You can choose between SPI, I2C and serial UART
mode (similar to RS232), which helps reduce the connection, save PCB
board space (smaller size), and reduce cost.


* `MFRC522 Data sheet <https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf>`_


**Example**

* :ref:`py_rfid` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`ar_rfid` (For Arduino User)