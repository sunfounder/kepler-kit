.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_music_player:

7.8 RFID Music Player
==========================

Through our previous project, :ref:`py_rfid`, we learned that the MFRC522 module allows us to write up to 48 letters of information to the card (or key), including both the key and identity information, as well as the music score.

As an example, if you write ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC``, the buzzer will play the music when the card (or key) is read again. It can also be equipped with an WS2812 to display amazing effects.

You can find more sheet music on the Internet, or even write your own music, put them into the card (or key), and share them with your friends!

|rfid_player|

**Required Components**

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schematic**

|sch_music_player|


**Wiring**

|wiring_rfid_music_player| 

**Code**

#. Open the ``6.5_rfid_write.py`` file under the path of ``kepler-kit-main/micropython``, then click "Run Current Script" or simply press F5 to run it.

   .. note::

    Here you need to use the libraries in ``mfrc522`` folder, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

#. After running, type ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` in the shell, then bring the card (or key) close to the MFRC522 module to store a score of "Ode to Joy".

#. Open the ``7.8_rfid_music_player.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # WS2812 LED setup
        # Initialize an 8-LED WS2812 strip on pin 0
        ws = WS2812(machine.Pin(0), 8)

        # MFRC522 RFID reader setup
        # Initialize the RFID reader using SPI on specific pins
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # Buzzer note frequencies (in Hertz)
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # Initialize PWM for buzzer on pin 15
        buzzer = machine.PWM(machine.Pin(15))

        # List of note frequencies corresponding to musical notes
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # Function to play a tone on the buzzer with a specified frequency and duration
        def tone(pin, frequency, duration):
            pin.freq(frequency)  # Set the buzzer frequency
            pin.duty_u16(30000)  # Set duty cycle to 50% (approx)
            time.sleep_ms(duration)  # Play the tone for the specified duration
            pin.duty_u16(0)  # Stop the tone by setting duty cycle to 0

        # Function to light up a WS2812 LED at a specific index with a random color
        def lumi(index):
            for i in range(8):
                ws[i] = 0x000000  # Turn off all LEDs
            ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # Set a random color for the LED at the given index
            ws.write()  # Write the color data to the WS2812 LEDs

        # Encode musical notes text into indices and play the corresponding notes
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # Mapping of musical notes to text characters
        def take_text(text):
            string = text.replace(' ', '').upper()  # Remove spaces and convert the text to uppercase
            while len(string) > 0:
                index = words.index(string[0])  # Find the index of the first note in the string
                tone(buzzer, note[index], 250)  # Play the corresponding note on the buzzer for 250 ms
                lumi(index)  # Light up the LED corresponding to the note
                string = string[1:]  # Move to the next character in the string

        # Function to read from the RFID card and play the stored score
        def read():
            print("Reading...Please place the card...")
            id, text = reader.read()  # Read the RFID card (ID and stored text)
            print("ID: %s\nText: %s" % (id, text))  # Print the ID and text
            take_text(text)  # Play the score from the text stored on the card
            
        # Start reading from the RFID card and play the corresponding score
        read()



#. By putting the card (or key) close to the MFRC522 module again, the buzzer will play the music stored on the card (or key), and the RGB strip will light up in a random color.
