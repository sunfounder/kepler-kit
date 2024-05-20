.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_4_dit_7_segment:

4-stellige 7-Segment-Anzeige
==================================

Eine 4-stellige 7-Segment-Anzeige besteht aus vier eigenständigen 7-Segment-Displays.

|img_4-digit-sche|

Jedes der 7-Segment-Displays in der 4-stelligen Anzeige arbeitet unabhängig voneinander. Auf dem Prinzip der Trägheit des menschlichen Auges basierend, werden die Zeichen auf jedem 7-Segment schnell nacheinander angezeigt, um einen durchgehenden Text darzustellen.

Zum Beispiel: Wenn "1234" angezeigt wird, erscheint die "1" auf dem ersten 7-Segment, während die "234" nicht dargestellt werden. Nach einer kurzen Zeit wird die "2" auf dem zweiten 7-Segment angezeigt, während die anderen inaktiv bleiben. Dieser Vorgang wiederholt sich sehr schnell (typischerweise in 5 ms) für alle vier Displays. Aufgrund des Nachleuchteffekts und der visuellen Trägheit nehmen wir alle vier Zeichen gleichzeitig wahr.

|img_4-digit-sche-ca|

**Anzeigencodes**

Um das Verständnis für die Darstellung von Zahlen auf 7-Segment-Anzeigen (Common Cathode) zu erleichtern, haben wir die folgende Tabelle erstellt. Die Zahlen repräsentieren die auf dem 7-Segment-Display dargestellten Werte von 0-F; (DP) GFEDCBA bezieht sich auf die entsprechenden LEDs, die auf 0 oder 1 gesetzt sind. Zum Beispiel bedeutet 00111111, dass DP und G auf 0 und alle anderen auf 1 gesetzt sind. Daraus ergibt sich, dass die Zahl 0 auf dem Display angezeigt wird, während der HEX-Code der entsprechenden hexadezimalen Nummer entspricht.

.. list-table:: Glyph Code
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

**Beispiel**

* :ref:`py_74hc_4dig` (Für MicroPython-Nutzer)
* :ref:`py_passage_counter` (Für MicroPython-Nutzer)
* :ref:`py_10_second` (Für MicroPython-Nutzer)
* :ref:`py_traffic_light` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_4dig` (Für Arduino-Nutzer)
