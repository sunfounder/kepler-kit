.. _py_74hc_7seg:

5.2 Nummernanzeige
=======================

7-Segment-Anzeigen begegnen uns im Alltag an vielen Stellen.
Sie finden beispielsweise in Klimaanlagen Verwendung zur Temperaturanzeige oder in Verkehrsleitsystemen als Timer.

Im Grunde genommen handelt es sich bei einer 7-Segment-Anzeige um ein aus 8 LEDs bestehendes Paket, von denen 7 in Streifenform ein "8" bilden, während eine etwas kleinere punktförmige LED als Dezimalpunkt dient. Diese LEDs sind als a, b, c, d, e, f, g und dp markiert. Sie haben eigene Anodenstifte und teilen sich Kathoden. Ihre Stiftpositionen sind in der untenstehenden Abbildung dargestellt.

|img_7seg_cathode|

Das bedeutet, dass zur vollständigen Steuerung 8 digitale Signale gleichzeitig benötigt werden, und der 74HC595 kann dies leisten.

* :ref:`cpn_7_segment`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein Komplettset ist natürlich besonders praktisch, hier der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - TEILE IM SET
        - LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Die Komponenten können natürlich auch einzeln über die untenstehenden Links erworben werden.

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
        - :ref:`cpn_resistor`
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schaltplan**

|sch_74hc_7seg|

Hier ist das Verdrahtungsprinzip im Wesentlichen das gleiche wie bei :ref:`py_74hc_led`. Der einzige Unterschied besteht darin, dass Q0-Q7 an die Pins a ~ g der 7-Segment-Anzeige angeschlossen sind.

.. list-table:: Verdrahtung
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segmentanzeige
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp


**Verdrahtung**

.. 1. Verbinden Sie 3V3 und GND des Pico W mit der Stromschiene des Steckbretts.
.. #. Setzen Sie den 74HC595 in die mittlere Lücke des Steckbretts ein.
.. #. Verbinden Sie den GP0-Pin des Pico W mit dem DS-Pin (Pin 14) des 74HC595 mittels eines Verbindungskabels.
.. #. Verbinden Sie den GP1-Pin des Pico W mit dem STcp-Pin (12-Pin) des 74HC595.
.. #. Verbinden Sie den GP2-Pin des Pico W mit dem SHcp-Pin (Pin 11) des 74HC595.
.. #. Verbinden Sie den VCC-Pin (16 Pin) und den MR-Pin (10 Pin) am 74HC595 mit der positiven Stromschiene.
.. #. Verbinden Sie den GND-Pin (8-Pin) und den CE-Pin (13-Pin) am 74HC595 mit der negativen Stromschiene.
.. #. Setzen Sie die LED-Segmentanzeige in das Steckbrett ein und schließen Sie einen 220Ω-Widerstand in Reihe zum GND-Pin an die negative Stromschiene an.
.. #. Folgen Sie der untenstehenden Tabelle, um den 74HC595 und die LED-Segmentanzeige zu verbinden.

|wiring_74hc_7seg|


**Code**

.. note::

    * Öffnen Sie die Datei ``5.2_number_display.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5, um es auszuführen.

    * Vergessen Sie nicht, im unteren rechten Eck den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)
        
    while True:
        for num in range(10):
            hc595_shift(SEGCODE[num])
            time.sleep_ms(500)

Während das Programm läuft, werden die Zahlen 0 bis 9 sequenziell auf der LED-Segmentanzeige dargestellt.

**Wie funktioniert das?**

``hc595_shift()`` wird 74HC595 dazu bringen, 8 digitale Signale auszugeben. Es gibt das letzte Bit der Binärzahl an Q0 aus und das Ausgangssignal des ersten Bits an Q7. Mit anderen Worten, wenn die Binärzahl "00000001" geschrieben wird, gibt Q0 ein hohes Signal aus und Q1~Q7 geben niedrige Signale aus.

Angenommen, die 7-Segment-Anzeige zeigt die Zahl "1" an, müssen wir ein hohes Signal für b und c schreiben und ein niedriges Signal für a, d, e, f, g und dg schreiben.

|img_1_segment|

Das bedeutet, die Binärzahl "00000110" muss geschrieben werden. Zur besseren Lesbarkeit verwenden wir die hexadezimale Schreibweise "0x06".

* `Hexadezimal <https://de.wikipedia.org/wiki/Hexadezimalsystem>`_

* `Binär-Hex-Konverter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

In gleicher Weise können auch andere Zahlen auf der LED-Segmentanzeige dargestellt werden. Die nachfolgende Tabelle zeigt die entsprechenden Codes.

.. list-table:: Glyph-Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Zahlen	
        - Binärcode
        - Hex-Code  
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f

Geben Sie diese Codes in ``hc595_shift()`` ein, um die entsprechenden Zahlen auf der LED-Segmentanzeige darzustellen.
