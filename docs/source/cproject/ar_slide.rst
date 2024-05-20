.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_slide:

2.7 - Links und Rechts Umschalten
=====================================

|img_slide|

Der Schiebeschalter ist ein 3-poliges Bauteil. Der mittlere Pin (Pin 2) dient als gemeinsamer Anschluss. Wenn der Schalter nach links geschoben wird, werden die beiden linken Pins miteinander verbunden. Bei Verschiebung nach rechts werden die beiden rechten Pins verbunden.

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein Gesamtpaket zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|


Sie können die Komponenten auch einzeln über die untenstehenden Links erwerben.

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schaltplan**

|sch_slide|

GP14 erhält ein unterschiedliches Signalniveau, je nachdem, ob der Schiebeschalter nach rechts oder links verschoben wird.

Der Zweck des 10K-Widerstands besteht darin, GP14 während des Umschaltens auf einem niedrigen Pegel zu halten (nicht ganz links und nicht ganz rechts).

Der 104-Keramikkondensator dient hier zur Eliminierung von Störungen.

* :ref:`cpn_slide_switch`
* :ref:`cpn_capacitor`


**Verdrahtung**

|wiring_slide|

**Code**

.. note::

   * Die Datei ``2.7_toggle_left_right.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/2.7_toggle_left_right``.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.


    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/a20c0733-f234-4d4b-862d-db87f2c249e9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Während das Programm läuft, wird im seriellen Monitor "EIN" oder "AUS" angezeigt, je nachdem, in welche Richtung Sie den Schalter schieben.

