.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pa_buz:

3.2 - Individueller Ton
==========================================

Im vorherigen Projekt haben wir einen aktiven Summer verwendet. Diesmal greifen wir auf einen passiven Summer zurück.

Ähnlich wie der aktive Summer funktioniert auch der passive Summer auf Grundlage der elektromagnetischen Induktion. Der Unterschied besteht darin, dass ein passiver Summer keine eigene Schwingungsquelle hat. Deshalb gibt er keinen Ton ab, wenn Gleichstromsignale verwendet werden. Dies ermöglicht es jedoch dem passiven Summer, seine eigene Schwingungsfrequenz anzupassen und unterschiedliche Töne wie "Do, Re, Mi, Fa, Sol, La, Si" auszugeben.

Lassen Sie den passiven Summer eine Melodie spielen!

* :ref:`cpn_buzzer`

**Erforderliche Bauteile**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Set zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die Teile auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schaltplan**

|sch_buzzer|

Wenn der GP15-Ausgang hoch ist, leitet der S8050 (NPN-Transistor) nach dem 1K-Strombegrenzungswiderstand (zum Schutz des Transistors) den Strom, sodass der Summer ertönt.

Die Aufgabe des S8050 (NPN-Transistor) besteht darin, den Strom zu verstärken und den Klang des Summers lauter zu machen. Tatsächlich könnten Sie den Summer auch direkt an GP15 anschließen, würden jedoch feststellen, dass der Ton leiser ist.

**Verkabelung**

|img_buzzer|

Im Kit sind zwei Summer enthalten; wir verwenden einen passiven Summer (einen mit freiliegender Leiterplatte auf der Rückseite).

Für die Funktion des Summers ist ein Transistor erforderlich; hier verwenden wir den S8050.

|wiring_buzzer|

**Code**

.. note::

   * Die Datei ``3.2_custom_tone.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/3.2_custom_tone``.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

   * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.



.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/69c55e56-9eeb-46bb-b3a8-b354c500cc17/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


**Wie funktioniert es?**

Wenn dem passiven Summer ein digitales Signal gegeben wird, kann er nur die Membran bewegen, ohne einen Ton zu erzeugen.

Daher verwenden wir die Funktion ``tone()`` um das PWM-Signal zu erzeugen, das den passiven Summer zum Klingen bringt.

Diese Funktion hat drei Parameter:

  * **pin**, der GPIO-Pin, der den Summer steuert.
  * **frequency**, die Tonhöhe des Summers wird durch die Frequenz bestimmt; je höher die Frequenz, desto höher die Tonhöhe.
  * **Duration**, die Dauer des Tons.

* `tone <https://www.arduino.cc/reference/de/language/functions/advanced-io/tone/>`_

**Mehr erfahren**

Wir können den spezifischen Ton gemäß der Grundfrequenz des Klaviers simulieren, um ein vollständiges Musikstück zu spielen.

* `Piano key frequencies - Wikipedia <https://de.wikipedia.org/wiki/Frequenzen_der_gleichstufigen_Stimmung>`_

.. note::

   * Die Datei ``3.2_custom_tone_2.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/3.2_custom_tone_2``.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

   * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.


.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/f934c785-7204-4972-aae5-01edde3c79cc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
