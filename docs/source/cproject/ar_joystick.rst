.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_joystick:

4.1 - Den Joystick bedienen
============================

Wenn du häufig Videospiele spielst, dürfte dir der Joystick bestens bekannt sein.
Er wird normalerweise verwendet, um die Spielfigur zu bewegen, den Bildschirm zu drehen usw.

Das Prinzip hinter der Fähigkeit des Joysticks, dem Computer unsere Bewegungen mitzuteilen, ist recht simpel.
Man kann sich den Joystick als Kombination aus zwei senkrecht zueinander stehenden Potentiometern vorstellen.
Diese beiden Potentiometer messen den analogen Wert des Joysticks in vertikaler und horizontaler Richtung, was in einem Wert (x,y) in einem rechtwinkligen Koordinatensystem resultiert.

Der Joystick dieses Sets verfügt auch über einen digitalen Eingang, der aktiviert wird, wenn der Joystick gedrückt wird.

* :ref:`cpn_joystick`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile. 

Es ist definitiv praktisch, gleich ein ganzes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Bauteile können auch einzeln über die folgenden Links erworben werden.

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
        - :ref:`cpn_joystick`
        - 1
        - 

**Schaltplan**

|sch_joystick|

Der SW-Pin ist über einen 10K Pull-up-Widerstand angeschlossen. Der Grund dafür ist, ein stabiles hohes Signal am SW-Pin (Z-Achse) zu erhalten, wenn der Joystick nicht gedrückt wird; andernfalls befindet sich der SW in einem unbestimmten Zustand und der Ausgabewert kann zwischen 0/1 variieren.

**Verdrahtung**

|wiring_joystick|

**Code**

.. note::

    * Die Datei ``4.1_toggle_the_joyostick.ino`` finden Sie im Pfad ``kepler-kit-main/arduino/4.1_toggle_the_joyostick``.
    * Oder kopieren Sie den Code in die **Arduino IDE**.

    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen**-Button klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/dfe53878-7cb4-4543-bb97-7f5ef5aad15a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Programms gibt die Shell die x,y,z-Werte des Joysticks aus.

* Die Werte der x- und y-Achse sind analoge Werte, die zwischen 0 und 65535 variieren.
* Die Z-Achse hat einen digitalen Wert mit einem Status von 1 oder 0.
