.. _ar_micro:

2.8 - Sanft Drücken
===================

|img_micro_switch|

Ein Mikroschalter ist ebenfalls ein 3-poliges Gerät, die Reihenfolge der drei Pins sind C (Common Pin), NO (Normalerweise offen) und NC (Normalerweise geschlossen).

Wenn der Mikroschalter nicht gedrückt ist, sind 1 (C) und 3 (NC) miteinander verbunden. Wird er gedrückt, sind 1 (C) und 2 (NO) miteinander verbunden.

* :ref:`cpn_micro_switch`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links kaufen.

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
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Schaltplan**

|sch_limit_sw|

Standardmäßig ist GP14 niedrig und wird beim Drücken hoch.

Der Zweck des 10K-Widerstands ist es, GP14 während des Drückens niedrig zu halten.

Der 104-Keramikkondensator wird hier verwendet, um Rauschen zu eliminieren.

**Verkabelung**

|wiring_limit_sw|

**Code**

.. note::

   * Sie können die Datei ``2.8_press_gently.ino`` im Pfad ``kepler-kit-main/arduino/2.8_press_gently`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino-IDE**.

   
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/92a2e356-35da-4e34-92cd-80234e1b59c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Nach dem Start des Programms erscheint "The switch works!" im seriellen Monitor, wenn Sie den Schiebeschalter nach rechts bewegen.
