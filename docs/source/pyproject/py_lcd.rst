.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_lcd:

3.4 Flüssigkristallanzeige
===============================

LCD1602 ist eine Zeichen-Flüssigkristallanzeige, die gleichzeitig 32 (16*2) Zeichen anzeigen kann.

Wie wir alle wissen, haben LCDs und andere Displays, obwohl sie die Mensch-Maschine-Interaktion erheblich bereichern, 
eine gemeinsame Schwachstelle. Wenn sie an einen Controller angeschlossen sind, 
werden mehrere IOs des Controllers belegt, der nicht so viele externe Anschlüsse hat. 
Das schränkt auch andere Funktionen des Controllers ein. 
Deshalb wurde LCD1602 mit einem I2C-Bus entwickelt, um dieses Problem zu lösen.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://de.wikipedia.org/wiki/I%C2%B2C>`_

|pin_i2c|

Hier verwenden wir die I2C0-Schnittstelle, um den LCD1602 zu steuern und Text anzuzeigen.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können diese auch separat über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - MENGE
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Kabel
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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_lcd|

**Verkabelung**

|wiring_lcd|

**Code**

.. note::

    * Öffnen Sie die Datei ``3.4_liquid_crystal_display.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, dann klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen. 

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`. 

    * Hier benötigen Sie die Bibliothek ``lcd1602.py``. Bitte überprüfen Sie, ob sie auf Pico W hochgeladen wurde. Eine detaillierte Anleitung finden Sie unter :ref:`add_libraries_py`.

.. code-block:: python

    from machine import I2C, Pin
    from lcd1602 import LCD
    import time

    # Initialize I2C communication;
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for interfacing with the LCD1602 display
    lcd = LCD(i2c)

    # Display the first message on the LCD
    # Use '\n' to create a new line.
    string = "SunFounder\n    LCD Tutorial"
    lcd.message(string)
    # Wait for 2 seconds
    time.sleep(2)
    # Clear the display
    lcd.clear()

    # Display the second message on the LCD
    string = "Hello\n  World!"
    lcd.message(string)
    # Wait for 5 seconds
    time.sleep(5)
    # Clear the display before exiting
    lcd.clear()

Nachdem das Programm ausgeführt wurde, erscheinen nacheinander zwei Textzeilen auf dem LCD und verschwinden dann wieder.

.. note:: Wenn der Code läuft und der Bildschirm leer bleibt, können Sie das Potentiometer auf der Rückseite drehen, um den Kontrast zu erhöhen.

**Wie funktioniert das?**

#. Einrichten der I2C-Kommunikation

   Das Modul ``machine`` wird verwendet, um die I2C-Kommunikation einzurichten. SDA (Serial Data) und SCL (Serial Clock) Pins sind definiert (jeweils Pin 20 und 21), zusammen mit der I2C-Frequenz (400kHz).

   .. code-block:: python
      
      from machine import I2C, Pin
      i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

#. Initialisierung des LCD-Displays

   Die Klasse ``LCD`` aus dem Modul ``lcd1602`` wird instanziiert. Diese Klasse steuert die Kommunikation mit dem LCD-Display über I2C. Ein ``LCD``-Objekt wird unter Verwendung des ``i2c``-Objekts erstellt.

   Weitere Informationen zur Verwendung der ``lcd1602``-Bibliothek finden Sie in ``lcd1602.py``.

   .. code-block:: python
      
      from lcd1602 import LCD
      lcd = LCD(i2c)

#. Anzeigen von Nachrichten auf dem LCD

   Die Methode ``message`` des ``LCD``-Objekts wird verwendet, um Text auf dem Bildschirm anzuzeigen. Das Zeichen ``\n`` erstellt eine neue Zeile auf dem LCD. Die Funktion ``time.sleep()`` pausiert die Ausführung für eine bestimmte Anzahl von Sekunden.

   .. code-block:: python
      
      string = "SunFounder\n    LCD Tutorial"
      lcd.message(string)
      time.sleep(2)
      lcd.clear()

#. Löschen des Displays

   Die Methode ``clear`` des ``LCD``-Objekts wird aufgerufen, um den Text vom Display zu löschen.

   .. code-block:: python
      
      lcd.clear()

#. Anzeigen einer zweiten Nachricht

   Eine neue Nachricht wird angezeigt, gefolgt von einer Verzögerung und anschließendem Löschen des Bildschirms.

   .. code-block:: python
      
      string = "Hello\n  World!"
      lcd.message(string)
      time.sleep(5)
      lcd.clear()