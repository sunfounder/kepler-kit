.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_music_player:

7.8 RFID-Musikplayer
====================

In unserem vorherigen Projekt, :ref:`py_rfid`, haben wir gelernt, dass das MFRC522-Modul uns erlaubt, bis zu 48 Zeichen Informationen auf die Karte (oder den Schlüssel) zu schreiben. Dies schließt sowohl den Schlüssel als auch die Identitätsinformationen ein, sowie die Noten für die Musik.

Zum Beispiel, wenn Sie ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` schreiben, wird der Summer die Melodie spielen, wenn die Karte (oder der Schlüssel) erneut gelesen wird. Es kann auch mit einem WS2812 ausgestattet werden, um beeindruckende Effekte darzustellen.

Sie können weitere Notenblätter im Internet finden oder sogar Ihre eigene Musik schreiben, diese auf die Karte (oder den Schlüssel) übertragen und sie mit Ihren Freunden teilen!

|rfid_player|

**Benötigte Bauteile**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - KOMPONENTEN IN DIESEM KIT
        - LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Bauteile auch einzeln über die unten stehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - ANZAHL
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
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
        - Passiver :ref:`cpn_buzzer`
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

**Schaltplan**

|sch_music_player|


**Verdrahtung**

|wiring_rfid_music_player| 



**Code**

#. Öffnen Sie die Datei ``6.5_rfid_write.py`` im Verzeichnis ``kepler-kit-main/micropython`` und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

#. Nach dem Ausführen geben Sie ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` im Shell ein und halten Sie dann die Karte (oder den Schlüssel) nahe am MFRC522-Modul. Auf diese Weise wird die Partitur der Ode an die Freude gespeichert.

#. Öffnen Sie die Datei ``7.8_rfid_music_player.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.


    .. code-block:: python


        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # ws2812
        ws = WS2812(machine.Pin(0),8)

        # mfrc522
        reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)
        # buzzer
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        buzzer = machine.PWM(machine.Pin(15))
        note=[NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5]

        def tone(pin,frequency,duration):
            pin.freq(frequency)
            pin.duty_u16(30000)
            time.sleep_ms(duration)
            pin.duty_u16(0)


        # lightup
        def lumi(index):
            for i in range(8):
                ws[i] = 0x0000FF
            ws[index] = 0xFF0000 # int(urandom.uniform(0, 0xFFFFFF))  
            ws.write() 


        # encode text to index
        words=["C","D","E","F","G","A","B","N"]
        def take_text(text):
            string = text.replace(' ', '').upper()  # Remove spaces and convert to uppercase
            while len(string) > 0:
                if string[0] in words:  # Check if the character is in the words list
                    index = words.index(string[0])
                    tone(buzzer, note[index], 250)
                    lumi(index)
                else:
                    print(f"Skipping unknown character: {string[0]}")  # Print unknown character
                string = string[1:]  # Remove the first character and continue looping

        # read card
        def read():
            print("Reading...Please place the card...")
            id, text = reader.read()
            print("ID: %s\nText: %s" % (id,text))
            take_text(text)
            
        read()


#. Wenn Sie die Karte (oder den Schlüssel) erneut nahe am MFRC522-Modul platzieren, wird der Summer die auf der Karte (oder dem Schlüssel) gespeicherte Musik abspielen und der RGB-Streifen wird in einer zufälligen Farbe leuchten.
