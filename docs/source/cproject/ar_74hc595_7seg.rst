.. _ar_74hc_7seg:

5.2 - Zahlenanzeige
=======================

LED-Segmentanzeigen sind überall im Alltag zu finden.
Zum Beispiel kann sie auf einer Klimaanlage zur Temperaturanzeige verwendet werden oder an einer Verkehrsanzeige, um einen Timer anzuzeigen.

Die LED-Segmentanzeige besteht im Wesentlichen aus einem Gerät, das mit 8 LEDs verpackt ist, von denen 7 streifenförmige LEDs eine "8"-Form bilden und eine etwas kleinere gepunktete LED als Dezimalpunkt dient. Diese LEDs sind als a, b, c, d, e, f, g und dp gekennzeichnet. Sie haben eigene Anodenpins und teilen sich Kathoden. Ihre Pin-Positionen sind im untenstehenden Bild dargestellt.

|img_7seg_cathode|

Das bedeutet, dass sie von 8 digitalen Signalen gleichzeitig gesteuert werden muss, um vollständig zu funktionieren, und der 74HC595 kann dies leisten.

* :ref:`cpn_7_segment`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
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

**Verdrahtung**

|wiring_74hc_7seg|

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

**Code**

.. note::

   * Sie können die Datei ``5.2_number_display.ino`` im Pfad ``kepler-kit-main/arduino/5.2_number_display`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die Schaltfläche **Upload** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a237801f-40d7-4920-80fb-a349307b1e05/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    
Wenn das Programm läuft, können Sie sehen, dass die LED-Segmentanzeige die Zahlen 0~9 nacheinander anzeigt.

**Wie funktioniert es?**

``shiftOut()`` lässt den 74HC595 8 digitale Signale ausgeben.
Es gibt das letzte Bit der Binärzahl an Q0 aus und den Ausgang des ersten Bits an Q7. Das bedeutet, dass beim Schreiben der Binärzahl "00000001" Q0 ein hohes Signal ausgibt und Q1~Q7 ein niedriges Signal.

Nehmen wir an, das 7-Segment-Display zeigt die Zahl "1" an, wir müssen ein hohes Signal für b, c schreiben und ein niedriges Signal für a, d, e, f, g und dg.
Das heißt, die Binärzahl "00000110" muss geschrieben werden. Aus Gründen der Lesbarkeit verwenden wir die Hexadezimalnotation als "0x06".

* `Hexadezimal <https://de.wikipedia.org/wiki/Hexadezimalsystem>`_

* `BinaryHex Konverter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

Ebenso können wir das LED-Segmentdisplay auf die gleiche Weise zur Anzeige anderer Zahlen verwenden. Die folgende Tabelle zeigt die entsprechenden Codes für diese Zahlen.

.. list-table:: Glyphen-Code
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

Fügen Sie diese Codes in die Funktion ``shiftOut()`` ein, um die jeweiligen Zahlen auf dem LED-Segmentdisplay darzustellen.

