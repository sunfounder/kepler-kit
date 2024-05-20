.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_tilt:

2.6 - Kipp es!
==========================

|img_tilt|

Der Kippschalter ist ein 2-poliges Bauelement mit einer Metallkugel im Inneren. In aufrechter Position sind die beiden Anschlüsse verbunden; neigt man den Schalter, werden die Anschlüsse getrennt.

**Erforderliche Bauteile**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset ist definitiv praktisch, hier der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - INHALT DES KITS
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch einzeln über die untenstehenden Links gekauft werden.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**Schaltplan**

|sch_tilt|

In aufrechter Position wird GP14 auf High gesetzt; kippt man den Schalter, wechselt GP14 auf Low.

Der 10K-Widerstand dient dazu, GP14 im gekippten Zustand stabil auf Low zu halten.

* :ref:`cpn_tilt`

**Verkabelung**

|wiring_tilt|

**Code**

.. note::

   * Die Datei ``2.6_tilt_it.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/2.4_colorful_light``.
   * Alternativ können Sie diesen Code in die **Arduino IDE** kopieren.

    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0421b002-a697-4f22-a965-0e62e8dc3abf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Hochladen des Programms erscheint in der Konsole die Meldung "Der Schalter funktioniert!", wenn Sie das Breadboard (Kippschalter) kippen.
