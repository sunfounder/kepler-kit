.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_led_bar:

2.2 - Pegelanzeige
=============================

Nachdem das erste Projekt lediglich das Blinken einer einzelnen LED zum Ziel hatte, wollen wir uns nun dem LED-Balkendiagramm zuwenden. Dieses besteht aus einer Serie von 10 LEDs in einem Kunststoffgehäuse und dient in der Regel zur Darstellung von Leistungs- oder Lautstärkepegeln.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Erforderliche Bauteile**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist sicherlich bequem, gleich ein komplettes Kit zu kaufen. Hier der entsprechende Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IM SET
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Bauteile können jedoch auch einzeln über die unten aufgeführten Links erworben werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - Nr.
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
        - 10 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schaltplan**

|sch_ledbar|

Das LED-Balkendiagramm besteht aus 10 einzeln ansteuerbaren LEDs. Dabei ist die Anode jeder dieser LEDs an die Pins GP6 bis GP15 angeschlossen. Die Kathode ist jeweils über einen 220-Ohm-Widerstand mit GND verbunden.

**Verkabelung**

|wiring_ledbar|

**Programmcode**

.. note::

    * Sie können die Datei ``2.2_display_the_level.ino`` im Verzeichnis ``kepler-kit-main/arduino/2.2_display_the_level`` öffnen.
    * Oder Sie kopieren den Code in die **Arduino IDE**.

    * Vergessen Sie nicht, vor dem Hochladen das richtige Board (Raspberry Pi Pico) und den passenden Port auszuwählen.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/ae60e723-430e-4a58-ac39-566b9d1828e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Sobald das Programm läuft, werden Sie feststellen, dass die LEDs im LED-Balkendiagramm nacheinander aufleuchten und erlöschen.

**Funktionsweise**

Jede der zehn LEDs im LED-Balkendiagramm wird durch einen eigenen Pin gesteuert. Das bedeutet, dass wir diese zehn Pins zuerst definieren müssen.

Im Abschnitt ``setup()`` wird eine For-Schleife verwendet, um die Pins 6 bis 15 nacheinander als Ausgang (OUTPUT) zu initialisieren.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }

In der ``loop()``-Funktion wird ebenfalls eine For-Schleife verwendet, um die LEDs sequenziell blinken zu lassen (0,5 Sekunden ein, dann 0,5 Sekunden aus).

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }
