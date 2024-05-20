.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_neopixel:

3.3 RGB LED-Streifen
======================

WS2812 ist eine intelligente LED-Lichtquelle, bei der die Steuerschaltung und der RGB-Chip in einem 5050-Komponentenpaket integriert sind.
Sie enthält eine intelligente digitale Port-Datenverriegelung und eine Signalformungsverstärkungs-Antriebsschaltung.
Zusätzlich verfügt sie über einen präzisen internen Oszillator und einen programmierbaren Konstantstromregler, der effektiv die Farbkonsistenz der einzelnen Pixel gewährleistet.

Das Datenübertragungsprotokoll verwendet den einzelnen NZR-Kommunikationsmodus.
Nach dem Einschalten des Pixels empfängt der DIN-Port Daten vom Controller. Das erste Pixel sammelt die ersten 24-Bit-Daten und sendet sie an die interne Datenverriegelung. Die weiteren, durch die interne Signalformungsverstärkung geformten Daten werden durch den DO-Port zum nächsten Kaskadenpixel gesendet. Nach der Übertragung für jedes Pixel verringert sich das Signal um 24 Bit. 
Das Pixel verwendet die automatische Signalumformungstechnologie, wodurch die Anzahl der kaskadierten Pixel nur von der Geschwindigkeit der Signalübertragung abhängt.

* :ref:`cpn_ws2812`

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Ein vollständiges Kit ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - TEILE IM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|


**Schaltplan**

|sch_ws2812|


**Verkabelung**

|wiring_ws2812|

.. warning::
    Ein Punkt, den Sie beachten müssen, ist der Strom.

    Obwohl der LED-Streifen mit beliebig vielen LEDs am Pico W betrieben werden kann, ist die Leistung seines VBUS-Pins begrenzt.
    Hier verwenden wir acht LEDs, was sicher ist.
    Wenn Sie jedoch mehr LEDs verwenden möchten, benötigen Sie eine separate Stromversorgung.


**Code**

.. note::

    * Öffnen Sie die Datei ``3.3_rgb_led_strip.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

    * Hier benötigen Sie die Bibliothek ``ws2812.py``, prüfen Sie, ob sie auf dem Pico W hochgeladen wurde. Eine detaillierte Anleitung finden Sie unter :ref:`add_libraries_py`.


.. code-block:: python

    import machine 
    from ws2812 import WS2812

    ws = WS2812(machine.Pin(0),8)

    ws[0] = [64,154,227]
    ws[1] = [128,0,128]
    ws[2] = [50,150,50]
    ws[3] = [255,30,30]
    ws[4] = [0,128,255]
    ws[5] = [99,199,0]
    ws[6] = [128,128,128]
    ws[7] = [255,100,0]
    ws.write()


Wählen Sie einige Ihrer Lieblingsfarben aus und zeigen Sie sie auf dem RGB-LED-Streifen an!

**Wie funktioniert das?**

In der ws2812-Bibliothek haben wir alle relevanten Funktionen in die Klasse WS2812 integriert.

Sie können den RGB-LED-Streifen mit dem folgenden Befehl nutzen.

.. code-block:: python

    from ws2812 import WS2812

Deklarieren Sie ein WS2812-Objekt mit dem Namen "ws", das an den "Pin" angeschlossen ist, auf dem sich "Anzahl" RGB-LEDs befinden.

.. code-block:: python

    ws = WS2812(pin, number)

ws ist ein Array-Objekt, dessen Elemente den einzelnen RGB-LEDs auf dem WS2812-Streifen entsprechen, beispielsweise ist ws[0] die erste und ws[7] die achte.

Sie können jeder RGB-LED Farbwerte zuweisen. Diese Werte müssen eine 24-Bit-Farbe sein (dargestellt durch sechs Hexadezimalziffern) oder eine Liste von drei 8-Bit-RGB-Werten.

Beispiel: Der rote Wert ist "0xFF0000" oder "[255,0,0]".

.. code-block:: python

    ws[i] = color value

Verwenden Sie dann diesen Befehl, um die Farbe für den LED-Streifen zu setzen und ihn zum Leuchten zu bringen.

.. code-block:: python

    ws.write()

Sie können auch direkt den folgenden Befehl verwenden, um alle LEDs in derselben Farbe leuchten zu lassen.

.. code-block:: python

    ws.write_all(color value)


**Mehr erfahren**

Wir können zufällig Farben generieren und ein buntes, fließendes Licht erzeugen.

.. note::

    * Öffnen Sie die Datei ``3.3_rgb_led_strip_2.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812
    import utime
    import urandom

    ws = WS2812(machine.Pin(0),8)

    def flowing_light():
        for i in range(7,0,-1):
            ws[i] = ws[i-1]
        ws[0] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write()
        utime.sleep_ms(80)

    while True:
        flowing_light()
        print(ws[0])
