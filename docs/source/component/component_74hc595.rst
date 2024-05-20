.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_74hc595:

74HC595
===========

|img_74hc595|

Der 74HC595 besteht aus einem 8-Bit-Schieberegister und einem Speicherregister mit dreizuständigen parallelen Ausgängen. Er wandelt serielle Eingaben in parallele Ausgaben um, sodass IO-Ports eines MCU gespart werden können.

* Bei hohem Pegel an MR (Pin10) und niedrigem Pegel an OE (Pin13) wird die Daten am steigenden Flanken von SHcp eingelesen und durchlaufen das Speicherregister über die steigende Flanke von SHcp.
* Wenn die beiden Taktgeber miteinander verbunden sind, liegt das Schieberegister immer einen Taktimpuls vor dem Speicherregister.
* Im Speicherregister gibt es einen seriellen Schiebeeingangspin (Ds), einen seriellen Ausgangspin (Q) und eine asynchrone Reset-Taste (niedriger Pegel).
* Das Speicherregister gibt einen Bus mit parallelem 8-Bit und in drei Zuständen aus.
* Ist OE aktiviert (niedriger Pegel), werden die Daten im Speicherregister zum Bus (Q0 ~ Q7) ausgegeben.

* `74HC595 Datenblatt <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

|img_74jc595_pin|

Pins des 74HC595 und ihre Funktionen:

* **Q0-Q7**: 8-Bit-parallele Daten-Ausgangspins, direkt für die Steuerung von 8 LEDs oder 8 Pins einer 7-Segment-Anzeige geeignet.
* **Q7'**: Serieller Ausgangspin, verbunden mit DS eines weiteren 74HC595 zur seriellen Verknüpfung mehrerer 74HC595.
* **MR**: Reset-Pin, aktiv bei niedrigem Pegel.
* **SHcp**: Zeitsequenz-Eingang des Schieberegisters. An der steigenden Flanke rückt die Daten im Schieberegister jeweils um ein Bit vor, d.h. Daten in Q1 bewegen sich zu Q2 usw. An der fallenden Flanke bleiben die Daten unverändert.
* **STcp**: Zeitsequenz-Eingang des Speicherregisters. An der steigenden Flanke wandern die Daten aus dem Schieberegister ins Speicherregister.
* **OE**: Enable-Pin für den Ausgang, aktiv bei niedrigem Pegel.
* **DS**: Serieller Dateneingangspin.
* **VCC**: Positive Versorgungsspannung.
* **GND**: Masse.

.. Beispiel
.. -------------------

.. :ref:`Microchip - :ref:`cpn_74hc595``

**Beispiel**

* :ref:`py_74hc_led` (Für MicroPython-Anwender)
* :ref:`py_74hc_7seg` (Für MicroPython-Anwender)
* :ref:`py_74hc_4dig` (Für MicroPython-Anwender)
* :ref:`py_74hc_788bs` (Für MicroPython-Anwender)
* :ref:`py_passage_counter` (Für MicroPython-Anwender)
* :ref:`py_10_second` (Für MicroPython-Anwender)
* :ref:`py_traffic_light` (Für MicroPython-Anwender)
* :ref:`py_bubble_level` (Für MicroPython-Anwender)
* :ref:`ar_74hc_led` (Für Arduino-Anwender)
* :ref:`ar_74hc_7seg` (Für Arduino-Anwender)
* :ref:`ar_74hc_4dig` (Für Arduino-Anwender)
* :ref:`ar_74hc_788bs` (Für Arduino-Anwender)
