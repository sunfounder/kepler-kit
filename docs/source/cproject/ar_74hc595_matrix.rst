.. _ar_74hc_788bs:

5.4 - 8x8 Pixelgrafik
======================

Eine ED-Matrix ist ein Display mit geringer Auflösung, das auf einer Dot-Matrix-Technologie basiert. Sie nutzt ein Array aus lichtemittierenden Dioden als Pixel für strukturierte Darstellungen.

Diese Anzeigen sind hell genug, um bei Tageslicht im Freien sichtbar zu sein, und finden sich zum Beispiel an Geschäften, Werbetafeln, Schildern und variablen Anzeigesystemen (wie sie in öffentlichen Verkehrsmitteln verwendet werden).

In diesem Bausatz wird eine 8x8-Dot-Matrix mit 16 Pins verwendet. Die Anoden sind in Reihen und die Kathoden in Spalten (auf Schaltungsebene) verbunden, die gemeinsam diese 64 LEDs steuern.

Um die erste LED zu beleuchten, muss für Row1 ein hoher Pegel und für Col1 ein niedriger Pegel bereitgestellt werden. Für die zweite LED gilt: hoher Pegel für Row1, niedriger Pegel für Col2, und so weiter.
Durch die Steuerung des Stromflusses zwischen den einzelnen Reihen und Spalten kann jede LED individuell angesteuert werden, um Zeichen oder Bilder darzustellen.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein Komplettbausatz ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - TEILE IM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - MENGE
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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Schaltplan**

|sch_ledmatrix|

Die 8x8 Dot-Matrix wird von zwei 74HC595-Chips gesteuert, wobei einer die Reihen und der andere die Spalten kontrolliert. Beide Chips teilen sich die Ports G18~G20, was die Anzahl der benötigten I/O-Ports des Pico W Boards deutlich reduziert.

Der Pico W muss jeweils eine 16-Bit-Binärzahl ausgeben, wobei die ersten 8 Bits an den 74HC595 gehen, der die Reihen steuert, und die letzten 8 Bits an den 74HC595, der die Spalten steuert. Auf diese Weise kann die Dot-Matrix ein spezifisches Muster anzeigen.

Q7': Serieller Ausgangspin, verbunden mit dem DS eines weiteren 74HC595, um mehrere 74HC595s in Reihe zu schalten.

**Verkabelung**

Bauen wir den Schaltkreis auf. Die Verkabelung ist etwas komplex, daher gehen wir am besten schrittweise vor.

**Schritt 1:** Zunächst setzen Sie den Pico W, die LED-Punktmatrix und zwei 74HC595-Chips ins Steckbrett ein. Schließen Sie die 3,3V und GND-Anschlüsse des Pico W an die äußeren Steckbuchsen der Platine an. Verbinden Sie dann Pin 16 und 10 der beiden 74HC595-Chips mit VCC und Pin 13 und Pin 8 mit GND.

.. note::
   In der oberen Fritzing-Grafik ist die Seite mit dem Label unten abgebildet.

|wiring_ledmatrix_4|

**Schritt 2:** Verknüpfen Sie den Pin 11 beider 74HC595-Chips miteinander und dann mit GP20. Verfahren Sie genauso mit Pin 12 und GP19. Anschließend verbinden Sie Pin 14 des linken 74HC595 mit GP18 und Pin 9 mit Pin 14 des rechten 74HC595.

|wiring_ledmatrix_3|

**Schritt 3:** Der rechte 74HC595 ist für die Steuerung der Spalten der LED-Punktmatrix zuständig. Die Zuordnung finden Sie in der untenstehenden Tabelle. Somit korrespondieren die Pins Q0-Q7 des 74HC595 mit den Pins 13, 3, 4, 10, 6, 11, 15 und 16 der LED-Matrix.

|wiring_ledmatrix_2|

**Schritt 4:** Jetzt geht es an die Reihen der LED-Punktmatrix. Der linke 74HC595 steuert diese. Auch hier finden Sie die Zuordnung in der untenstehenden Tabelle. Die Pins Q0-Q7 dieses Chips sind mit den Pins 9, 14, 8, 12, 1, 7, 2 und 5 der LED-Matrix verknüpft.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code**

.. note::

   * Öffnen Sie die Datei ``5.4_8x8_pixel_graphics.ino`` im Verzeichnis ``kepler-kit-main/arduino/5.4_8x8_pixel_graphics``.
   * Alternativ können Sie den Code auch in die **Arduino IDE** kopieren.
   * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die Schaltfläche **Upload** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3682592-17d4-4690-a730-1c0a6fcbd353/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Sobald das Programm läuft, wird ein **X**-Symbol auf der 8x8-Punktmatrix dargestellt.

**Wie funktioniert es?**

Wir verwenden zwei 74HC595-Chips, um Signale für die Zeilen und Spalten der Punktmatrix bereitzustellen. Die Signalübertragung funktioniert ähnlich wie bei ``shiftOut()`` in den vorherigen Kapiteln, allerdings schreiben wir hier eine 16-Bit-Binärzahl auf einmal.

Die Hauptfunktion ruft ``shiftOut()`` zweimal auf, schreibt zwei 8-Bit-Binärzahlen und sendet sie dann an den Bus, sodass ein Muster angezeigt werden kann.

Allerdings verursacht die gemeinsame Polung der LEDs in der Punktmatrix bei gleichzeitiger Steuerung mehrerer Reihen oder Spalten Interferenzen (z.B. wenn (1,1) und (2,2) gleichzeitig leuchten, werden (1,2) und (2,1) unweigerlich ebenfalls leuchten). Daher ist es notwendig, jeweils nur eine Spalte (oder eine Reihe) zu aktivieren, das Ganze 8-mal zu wiederholen und nach dem Prinzip des Nachbildes das menschliche Auge die 8 Muster zusammenführen zu lassen, um ein Gesamtbild aus 8x8 Informationspunkten zu erhalten.

.. code-block:: arduino

   for(int num = 0; num <=8; num++)
   {
      digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
      shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
      shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
      //return the latch pin high to signal chip that it 
      //no longer needs to listen for information
      digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
   }

In diesem Beispiel nutzt die Hauptfunktion eine verschachtelte ``for``-Schleife. Bei einem Wert von ``i`` gleich 1 wird nur die erste Zeile aktiviert (der Chip der Steuerzeile erhält den Wert ``0x80``), und das Muster der ersten Zeile wird geschrieben. Bei ``i`` gleich 2 wird die zweite Zeile aktiviert (der Chip der Steuerzeile erhält den Wert ``0x40``), und das Muster der zweiten Zeile wird geschrieben. Und so weiter, bis alle 8 Ausgaben vollzogen sind.

Ähnlich wie bei der 4-stelligen 7-Segment-Anzeige muss die Aktualisierungsrate hochgehalten werden, um ein Flackern des menschlichen Auges zu vermeiden. Daher sollten zusätzliche ``sleep()``-Aufrufe in der Hauptfunktion möglichst vermieden werden.

**Mehr erfahren**

Ersetzen Sie ``datArray`` durch eines der folgenden Arrays und schauen Sie, welche Muster erscheinen!

.. code-block:: arduino

   int datArray1[] = {0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF};
   int datArray2[] = {0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF};
   int datArray3[] = {0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF};
   int datArray4[] = {0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF};
   int datArray5[] = {0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF};
   int datArray6[] = {0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF};

Oder versuchen Sie, eigene Grafiken zu entwerfen.

