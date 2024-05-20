.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_reed:

2.9 - Magnetismus spüren
===============================

Der am häufigsten verwendete Reed-Schalter enthält ein Paar magnetisierbarer, flexibler Metallzungen, deren Enden bei geöffnetem Schalter durch eine kleine Lücke getrennt sind. 

Ein Magnetfeld eines Elektromagneten oder eines Permanentmagneten führt dazu, dass die Metallzungen sich gegenseitig anziehen und somit einen elektrischen Stromkreis schließen.
Die Federkraft der Zungen lässt sie sich wieder trennen und den Kreislauf öffnen, sobald das Magnetfeld aufhört.

Ein geläufiges Anwendungsbeispiel für Reed-Schalter ist die Überwachung des Öffnens von Türen oder Fenstern in einem Sicherheitssystem.

* :ref:`cpn_reed`

**Erforderliche Komponenten**

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

Sie können diese auch separat über die folgenden Links erwerben.

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
        - :ref:`cpn_reed`
        - 1
        - 

**Schaltplan**

|sch_reed|

Standardmäßig ist GP14 niedrig; er wird hoch, wenn der Magnet in der Nähe des Reed-Schalters ist.

Der 10K-Widerstand dient dazu, den GP14 auf einem konstant niedrigen Niveau zu halten, wenn kein Magnet in der Nähe ist.

**Verdrahtung**

|wiring_reed|

**Code**

.. note::

   * Sie können die Datei ``2.9_feel_the_magnetism.ino`` im Pfad ``kepler-kit-main/arduino/2.9_feel_the_magnetism`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Anschluss auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bba18c-7921-4df9-806f-deffce17de9a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Wenn sich ein Magnet nähert, schließt sich der Stromkreis. Genau wie der Knopf im Kapitel :ref:`ar_button`.

