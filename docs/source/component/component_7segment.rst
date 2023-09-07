.. _cpn_7_segment:

7-Segment-Anzeige
======================

|img_7seg|


Eine 7-Segment-Anzeige ist ein acht-förmiges Bauteil, das aus 7 LEDs besteht. Jede dieser LEDs wird als Segment bezeichnet - sobald es aktiviert ist, bildet ein Segment einen Teil einer darzustellenden Zahl.

Es gibt zwei Arten von Pin-Verbindungen: Gemeinsame Kathode (Common Cathode, CC) und Gemeinsame Anode (Common Anode, CA). Wie der Name bereits verrät, sind bei einer CC-Anzeige alle Kathoden der 7 LEDs verbunden, während bei einer CA-Anzeige alle Anoden der 7 Segmente miteinander verbunden sind.

In diesem Bausatz verwenden wir die 7-Segment-Anzeige mit gemeinsamer Kathode, hier ist das entsprechende elektronische Symbol.

|img_7seg_cathode|

Jedes der LEDs in der Anzeige hat eine positionelle Bezeichnung und einen der Anschlusspins, der aus dem rechteckigen Kunststoffgehäuse herausgeführt wird. Diese LED-Pins sind von "a" bis "g" beschriftet und repräsentieren jeweils eine einzelne LED. Die anderen LED-Pins sind zusammengeführt und bilden einen gemeinsamen Pin. Durch die Vorwärtsvorspannung der entsprechenden Pins der LED-Segmente in einer bestimmten Reihenfolge leuchten einige Segmente auf, während andere gedimmt bleiben, sodass der entsprechende Charakter auf der Anzeige dargestellt wird. 


* `7-Segment-Anzeige - Wikipedia <https://de.wikipedia.org/wiki/7-Segment-Anzeige>`_

**Anzeigecodes**

Um Ihnen zu helfen, zu verstehen, wie 7-Segment-Anzeigen (Gemeinsame Kathode) Zahlen darstellen, haben wir die folgende Tabelle erstellt. Die Zahlen sind die Zahlen von 0 bis F, die auf der 7-Segment-Anzeige dargestellt werden; (DP) GFEDCBA bezieht sich auf das jeweilige LED-Set, das auf 0 oder 1 gesetzt ist. Zum Beispiel bedeutet 00111111, dass DP und G auf 0 gesetzt sind, während die anderen auf 1 gesetzt sind. Daher wird die Zahl 0 auf der 7-Segment-Anzeige angezeigt, während der HEX-Code der entsprechenden Hexadezimalzahl entspricht.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Zahlen	
        - Binärer Code
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
    *   - A	
        - 01110111	
        - 0x77
    *   - B
        - 01111100	
        - 0x7c
    *   - C	
        - 00111001	
        - 0x39
    *   - D	
        - 01011110	
        - 0x5e
    *   - E	
        - 01111001	
        - 0x79
    *   - F	
        - 01110001	
        - 0x71

.. Beispiel
.. -------------------

.. :ref:`LED-Segmentanzeige`

**Beispiel**

* :ref:`py_74hc_7seg` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_7seg` (Für Arduino-Nutzer)
