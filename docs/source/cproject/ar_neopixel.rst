.. _ar_neopixel:

3.3 WS2812 RGB-Strip
======================

WS2812 ist eine intelligente LED-Lichtquelle, bei der die Steuerschaltung und der RGB-Chip in einem 5050-Komponentenpaket integriert sind.
Sie enthält einen intelligenten digitalen Port-Datenlatch und eine Signalformungsverstärkungs-Schaltung.
Darüber hinaus verfügt sie über einen präzisen internen Oszillator und einen programmierbaren konstanten Stromsteuerungsteil,
der effektiv die hohe Konsistenz der Lichtfarbe jedes Pixels sicherstellt.

Das Datenübertragungsprotokoll verwendet den einzelnen NZR-Kommunikationsmodus.
Nach dem Einschalten des Pixels erhält der DIN-Port Daten vom Controller, das erste Pixel sammelt die anfänglichen 24-Bit-Daten und sendet sie an den internen Datenlatch. Die restlichen Daten werden von der internen Signalformungsverstärkungs-Schaltung umgeformt und über den DO-Port an das nächste kaskadierte Pixel gesendet. Nach der Übertragung für jedes Pixel reduziert sich das Signal um 24 Bit.
Das Pixel verwendet die Auto-Reshaping-Transmit-Technologie, sodass die Anzahl der kaskadierten Pixel nicht durch die Signalübertragung begrenzt ist, sondern nur von der Geschwindigkeit der Signalübertragung abhängt.

* :ref:`cpn_ws2812`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die folgenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - ANZAHL
        - KAUF-LINK

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

**Verdrahtung**

|wiring_ws2812|


.. warning::
    Achten Sie besonders auf den Strombedarf.

    Obwohl der LED-Strip mit einer beliebigen Anzahl von LEDs im Pico W verwendet werden kann, ist die Leistung seines VBUS-Pins begrenzt.
    Hier werden wir acht LEDs verwenden, die sicher sind.
    Wenn Sie jedoch mehr LEDs verwenden möchten, benötigen Sie eine separate Stromversorgung.
    

**Code**

.. note::

    * Sie können die Datei ``3.3_rgb_led_strip.ino`` im Verzeichnis ``kepler-kit-main/arduino/3.3_rgb_led_strip`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.
    * Die Bibliothek ``Adafruit_NeoPixel`` wird hier verwendet. Bitte beziehen Sie sich auf :ref:`add_libraries_ar` für das Hinzufügen in die Arduino IDE.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/efe5d60f-ea0f-4446-bc5b-30c76197fedf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Wählen Sie einige Ihrer Lieblingsfarben aus und zeigen Sie sie auf dem RGB-LED-Strip an!


**Wie funktioniert es?**

Ein Objekt vom Typ Adafruit_NeoPixel wird deklariert, welches an ``PIXEL_PIN`` angeschlossen ist und auf dem Streifen befinden sich ``PIXEL_COUNT`` RGB-LEDs.

.. code-block:: arduino

    #define PIXEL_PIN    0
    #define PIXEL_COUNT 8

    // Declare our NeoPixel strip object:
    Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
    // Argument 1 = Number of pixels in NeoPixel strip
    // Argument 2 = Arduino pin number (most are valid)
    // Argument 3 = Pixel type flags, add together as needed:
    //   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
    //   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
    //   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
    //   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
    //   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)

Streifenobjekt initialisieren und alle Pixel auf 'aus' setzen.

Funktionen
    * ``strip.begin()`` : NeoPixel-Streifenobjekt initialisieren (ERFORDERLICH).
    * ``strip.setPixelColor(index, color)`` : Pixel-Farbe (im RAM) setzen, die ``color`` muss ein einzelner 'gepackter' 32-Bit-Wert sein.
    * ``strip.Color(red, green, blue)`` : Farbe als einzelner 'gepackter' 32-Bit-Wert.
    * ``strip.show()`` : Streifen mit neuem Inhalt aktualisieren.

**Mehr erfahren**

Wir können zufällige Farben generieren und ein farbenfrohes, fließendes Licht erzeugen.

.. note::

   * Sie können die Datei ``3.3_rgb_led_strip_flowing.ino`` im Pfad ``kepler-kit-main/arduino/3.3_rgb_led_strip_flowing`` öffnen.
   * Oder diesen Code in die **Arduino IDE** kopieren.
   
   * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die **Hochladen**-Schaltfläche klicken.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/a3d7c520-b4f8-4445-9454-5fe7d2a24fd9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Oder lassen Sie diesen WS2812 LED-Streifen in einem Regenbogenzyklus um das Farbrad (Bereich 65535) rotieren.

.. note::

   * Sie können die Datei ``3.3_rgb_led_strip_rainbow.ino`` im Pfad ``kepler-kit-main/arduino/3.3_rgb_led_strip_rainbow`` öffnen.
   * Oder diesen Code in die **Arduino IDE** kopieren.

   * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die **Hochladen**-Schaltfläche klicken.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/47d84804-3560-48fa-86df-49f8e2f6ad63/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

* ``strip.getPixelColor(index)`` : Die Farbe eines zuvor eingestellten Pixels abfragen.
* ``strip.ColorHSV(pixelHue)`` : Farbton, Sättigung und Wert in eine 'gepackte' 32-Bit-RGB-Farbe umwandeln, die an ``setPixelColor()`` oder andere RGB-kompatible Funktionen übergeben werden kann.
* ``strip.gamma32()`` : Ermöglicht eine "echtere" Farbwiedergabe, bevor sie jedem Pixel zugewiesen wird.

