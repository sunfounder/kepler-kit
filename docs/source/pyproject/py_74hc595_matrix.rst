.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_74hc_788bs:

5.4 8x8 Pixel-Grafik
=============================

Die LED-Matrix ist eine niedrigauflösende Punkt-Matrix-Anzeige und nutzt ein Array aus Leuchtdioden als Pixel für gemusterte Darstellungen.

Diese Anzeigen sind hell genug, um auch im Tageslicht im Freien sichtbar zu sein und finden sich in einigen Geschäften, Werbetafeln, Schildern und variablen Anzeigetafeln (wie beispielsweise in öffentlichen Verkehrsmitteln).

In diesem Bausatz wird eine 8x8 Punktmatrix mit 16 Pins verwendet. Die Anoden sind in Reihen und die Kathoden in Spalten (auf der Schaltungsebene) miteinander verbunden, um so die 64 LEDs zu steuern.

Um die erste LED zu beleuchten, sollte ein hohes Signal an Row1 und ein niedriges an Col1 angelegt werden. Für die zweite LED gilt dementsprechend ein hohes Signal an Row1 und ein niedriges an Col2, und so weiter. 
Jede LED lässt sich individuell steuern, indem der Stromfluss durch die jeweiligen Reihen und Spalten geregelt wird. Dadurch können Zeichen oder Bilder dargestellt werden.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist definitiv praktisch, ein komplettes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - KOMPONENTEN IM SET
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
        - MENGE
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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Schaltplan**

|sch_ledmatrix|

Die 8x8 Punktmatrix wird durch zwei 74HC595-Chips gesteuert, wobei einer die Reihen und der andere die Spalten steuert. Beide Chips teilen sich die Ports G18~G20, was die I/O-Ports des Pico W Boards erheblich einspart.

Pico W muss eine 16-Bit-Binärzahl ausgeben, wobei die ersten 8 Bit an den 74HC595 für die Reihen und die letzten 8 Bit an den 75HC595 für die Spalten gehen, damit die Punktmatrix ein bestimmtes Muster anzeigen kann.

Q7': Serieller Ausgangspin, verbunden mit DS eines weiteren 74HC595, um mehrere 74HC595 in Serie zu schalten.

**Verdrahtung**

Bauen Sie die Schaltung auf. Da die Verdrahtung kompliziert ist, gehen wir schrittweise vor.

**Schritt 1:** Setzen Sie zunächst den Pico W, die LED-Punktmatrix und die beiden 74HC595-Chips in das Steckbrett ein. Verbinden Sie 3,3V und GND des Pico W mit den Löchern an beiden Seiten der Platine, und schließen Sie dann Pin 16 und 10 der beiden 74HC595-Chips an VCC, Pin 13 und Pin 8 an GND an.

.. note::
   In der oben stehenden Fritzing-Abbildung ist die beschriftete Seite unten.

|wiring_ledmatrix_4|

**Schritt 2:** Verbinden Sie Pin 11 der beiden 74HC595 miteinander und dann mit GP20; danach Pin 12 der beiden Chips und mit GP19; als Nächstes Pin 14 des linken 74HC595 mit GP18 und Pin 9 mit Pin 14 des zweiten 74HC595.

|wiring_ledmatrix_3|

**Schritt 3:** Der 74HC595 auf der rechten Seite dient zur Steuerung der Spalten der LED-Punktmatrix. Untenstehende Tabelle zeigt die Zuordnung. Daher sind die Pins Q0-Q7 des 74HC595 jeweils mit den Pins 13, 3, 4, 10, 6, 11, 15 und 16 verbunden.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Schritt 4:** Verbinden Sie nun die Reihen der LED-Punktmatrix. Der 74HC595 auf der linken Seite steuert die Reihen der LED-Punktmatrix. Untenstehende Tabelle zeigt die Zuordnung. Wie man sieht, sind die Pins Q0-Q7 des linken 74HC595 jeweils mit den Pins 9, 14, 8, 12, 1, 7, 2 und 5 verbunden.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code**

.. note::

    * Öffnen Sie die Datei ``5.4_8x8_pixel_graphics.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    glyph = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]

    # Daten an 74HC595 senden
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

Sobald das Programm läuft, wird ein **x**-Grafikmuster auf der 8x8-Punktmatrix angezeigt.


**Wie funktioniert es?**

Hier nutzen wir zwei 74HC595-Chips, um die Signale für die Reihen und Spalten der Punkt-Matrix zu steuern. Die Methode zur Signalbereitstellung entspricht der Funktion ``hc595_shift(dat)`` aus vorherigen Kapiteln. Der Unterschied besteht jedoch darin, dass wir hier eine 16-Bit-Binärzahl auf einmal schreiben müssen. Daher teilen wir ``hc595_shift(dat)`` in zwei Funktionen auf: ``hc595_in(dat)`` und ``hc595_out()``.

.. code-block:: python

    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

Anschließend rufen Sie ``hc595_in(dat)`` zweimal in der Hauptschleife auf, schreiben zwei 8-Bit-Binärzahlen und rufen dann ``hc595_out()`` auf, damit ein Muster angezeigt werden kann.

Beachten Sie jedoch, dass die LEDs in der Punkt-Matrix gemeinsame Pole verwenden. Die gleichzeitige Steuerung mehrerer Reihen bzw. Spalten würde sich gegenseitig beeinflussen. Daher ist es notwendig, eine Spalte (oder eine Reihe) nach der anderen zu aktivieren, den Vorgang 8-mal zu wiederholen und das Prinzip der Nachbildwirkung zu nutzen, um das menschliche Auge 8 Muster verschmelzen zu lassen.

.. code-block:: python

    while True:
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()

In diesem Beispiel schachtelt die Hauptfunktion eine ``for``-Schleife. Wenn ``i`` 1 ist, wird nur die erste Zeile aktiviert, und das Bild der ersten Zeile wird geschrieben. Und so weiter, bis alle 8 Ausgaben abgeschlossen sind.

Übrigens sollte, ähnlich wie beim 4-stelligen 7-Segment-Display, die Aktualisierungsrate aufrechterhalten werden, um ein Flackern zu vermeiden. Daher sollte zusätzliches ``sleep()`` in der Hauptschleife möglichst vermieden werden.

**Mehr erfahren**

Versuchen Sie, ``glyph`` durch das folgende Array zu ersetzen und schauen Sie, was passiert!

.. code-block:: python

    glyph1 = [0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF]
    glyph2 = [0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF]
    glyph3 = [0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF]
    glyph4 = [0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF]
    glyph5 = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]
    glyph6 = [0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF]

Oder Sie könnten versuchen, Ihre eigenen Grafiken zu zeichnen.
