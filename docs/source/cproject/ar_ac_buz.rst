.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_ac_buz:

3.1 - Piepton
==================
Der aktive Summer ist ein typisches digitales Ausgabegerät, das genauso einfach zu bedienen ist wie eine LED zum Leuchten zu bringen!

* :ref:`cpn_buzzer`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist durchaus praktisch, ein gesamtes Set zu kaufen, hier der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links erwerben.

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
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        - 

**Schaltplan**

|sch_buzzer|

Wenn der GP15-Ausgang auf "High" geschaltet ist, lässt der 1K-Strombegrenzungswiderstand (zum Schutz des Transistors) den S8050 (NPN-Transistor) durchschalten, sodass der Summer ertönt.

Die Aufgabe des S8050 (NPN-Transistor) ist es, den Strom zu verstärken und den Summer lauter klingen zu lassen. Tatsächlich könnten Sie den Summer auch direkt an GP15 anschließen, würden jedoch feststellen, dass der Ton dann leiser ist.

**Verkabelung**

Im Kit sind zwei verschiedene Summertypen enthalten.
Wir benötigen den aktiven Summer. Drehen Sie sie um, der versiegelte Rücken (nicht die freiliegende PCB) ist der, den wir verwenden möchten.

|img_buzzer|

Für den Betrieb des Summers ist ein Transistor erforderlich, hier verwenden wir den S8050 (NPN-Transistor).

|wiring_beep|


**Code**


.. note::

   * Die Datei ``3.1_beep.ino`` finden Sie im Pfad ``kepler-kit-main/arduino/3.1_beep``.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

   * Vergessen Sie nicht, vor dem Klicken auf die Schaltfläche **Hochladen** das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nachdem der Code ausgeführt wurde, hören Sie jede Sekunde einen Piepton.
