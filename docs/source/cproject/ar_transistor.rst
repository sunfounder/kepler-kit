.. _ar_transistor:

2.15 - Zwei Arten von Transistoren
==========================================

Dieses Kit enthält zwei Typen von Transistoren, S8550 und S8050. Ersterer ist ein PNP-Transistor und der Letztere ein NPN-Transistor. Beide sehen sehr ähnlich aus, daher ist es wichtig, ihre Beschriftungen genau zu prüfen.
Während ein NPN-Transistor durch ein High-Level-Signal aktiviert wird, benötigt ein PNP-Transistor ein Low-Level-Signal. Beide Transistortypen finden häufig Anwendung in berührungslosen Schaltern, wie in diesem Experiment.

|img_NPN&PNP|

Verwenden wir eine LED und einen Taster, um den Umgang mit Transistoren zu verstehen!

:ref:`cpn_transistor`

**Benötigte Bauteile**

Für dieses Projekt sind folgende Komponenten erforderlich.

Ein Komplettset ist durchaus praktisch, hier der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - INHALT DES KITS
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch einzeln über die untenstehenden Links erworben werden.

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
        - :ref:`cpn_resistor`
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|

**Anschluss des NPN (S8050) Transistors**

|sch_s8050|

In dieser Schaltung ist GP14 high, wenn der Taster gedrückt wird.

Durch Programmierung von GP15 auf High und nach einem 1k-Strombegrenzungswiderstand (zum Schutz des Transistors) wird der S8050 (NPN-Transistor) zum Leiten gebracht, sodass die LED aufleuchtet.

|wiring_s8050|



**Anschluss des PNP (S8550) Transistors**

|sch_s8550|

In dieser Schaltung ist GP14 standardmäßig auf Low und wird auf High gesetzt, wenn der Taster gedrückt wird.

Durch Programmierung von GP15 auf **Low** und nach einem 1k-Strombegrenzungswiderstand wird der S8550 (PNP-Transistor) zum Leiten gebracht, sodass die LED leuchtet.

Der einzige Unterschied, den Sie zwischen dieser und der vorherigen Schaltung feststellen werden, ist, dass in der vorherigen Schaltung die Kathode der LED mit dem **Kollektor** des **S8050 (NPN-Transistor)** verbunden ist, während sie hier mit dem **Emitter** des **S8550 (PNP-Transistor)** verbunden ist.

|wiring_s8550|

.. 1. Verbinden Sie 3V3 und GND des Pico W mit der Stromschiene des Steckbretts.
.. #. Verbinden Sie die Anode der LED über einen 220Ω-Widerstand mit der positiven Stromschiene.
.. #. Verbinden Sie die Kathode der LED mit dem **Emitter**-Anschluss des Transistors.
.. #. Verbinden Sie den **Basis**-Anschluss des Transistors über einen 1kΩ-Widerstand mit dem GP15-Pin.
.. #. Verbinden Sie den **Kollektor**-Anschluss des Transistors mit der negativen Stromschiene.

**Code**

.. note::

   * Die Datei ``2.15_transistor.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/2.15_transistor``.
   * Alternativ können Sie den Code in die **Arduino IDE** kopieren.

   * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/77c437de-028f-47c1-9d79-177e90eb0599/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Beide Transistortypen können mit demselben Code gesteuert werden. Wenn wir den Taster drücken, sendet der Pico W ein High-Level-Signal an den Transistor; lassen wir ihn los, sendet er ein Low-Level-Signal.
Man wird feststellen, dass in den beiden Schaltungen diametral entgegengesetzte Phänomene auftreten.

* Die Schaltung mit dem S8050 (NPN-Transistor) leuchtet auf, wenn der Taster gedrückt wird, was bedeutet, dass sie ein High-Level-Leitungssignal erhält;
* Die Schaltung mit dem S8550 (PNP-Transistor) leuchtet auf, wenn sie losgelassen wird, was bedeutet, dass sie ein Low-Level-Leitungssignal erhält.
