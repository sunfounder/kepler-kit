.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_led:

2.1 - Hallo, LED!
=======================================

Genauso wie der Ausdruck „Hallo Welt!“ der erste Schritt beim Programmierenlernen ist, stellt das Ansteuern einer LED mittels Programm die klassische Einführung in die physische Programmierung dar.

* :ref:`cpn_led`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein Komplettset ist definitiv praktisch, hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler-Set
        - 450+
        - |link_kepler_kit|

Sie können die Bauteile auch einzeln über die folgenden Links erwerben.

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

Das Prinzip dieser Schaltung ist simpel und die Stromrichtung ist in der Abbildung dargestellt. Wenn GP15 ein hohes Signal (3,3 V) ausgibt, leuchtet die LED nach dem 220-Ohm-Vorwiderstand auf. Bei einem niedrigen Signal (0 V) geht die LED aus.

**Verdrahtung**

|wiring_led|

Lassen Sie uns den Stromfluss folgen und die Schaltung aufbauen!

1. Wir verwenden das elektrische Signal vom GP15-Pin der Pico W-Platine, um die LED zum Leuchten zu bringen; hier beginnt die Schaltung.
#. Der Strom muss durch einen 220-Ohm-Widerstand fließen (zum Schutz der LED). Stecken Sie ein Ende des Widerstands (beliebiges Ende) in die gleiche Reihe wie den GP15-Pin des Pico W (Reihe 20 in meiner Schaltung) und das andere Ende in eine freie Reihe des Steckbretts (Reihe 24 in meiner Schaltung).
#. Nehmen Sie die LED; ein Bein ist länger als das andere. Stecken Sie das längere Bein in dieselbe Reihe wie das Ende des Widerstands und das kürzere Bein über die mittlere Lücke des Steckbretts in die gleiche Reihe.
#. Stecken Sie das Stecker-zu-Stecker-Kabel (M2M) in dieselbe Reihe wie das kurze Bein der LED und verbinden Sie es mit der negativen Stromschiene des Steckbretts.
#. Verbinden Sie die negative Stromschiene mit dem GND-Pin des Pico W.

**Code**

.. note::

   * Sie können die Datei ``2.1_hello_led.ino`` im Pfad ``kepler-kit-main/arduino/2.1_hello_led`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

    * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den richtigen Anschluss auszuwählen, bevor Sie auf **Hochladen** klicken.



.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/898b8ba7-9bdf-468d-9181-ca8535e8dca6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nachdem der Code ausgeführt wurde, wird die LED blinken.

**Wie funktioniert es?**

Hier schließen wir die LED an den digitalen Pin 15 an, daher müssen wir zu Beginn des Programms eine int-Variable namens ledPin deklarieren und den Wert 15 zuweisen.

.. code-block:: C

    const int ledPin = 15;

Jetzt initialisieren Sie den Pin in der ``setup()``-Funktion, wo Sie den Pin auf den ``OUTPUT``-Modus setzen müssen.

.. code-block:: C

    void setup() {
        pinMode(ledPin, OUTPUT);
    }

In der ``loop()``-Funktion wird ``digitalWrite()`` verwendet, um ein 3,3-V-Hochpegelsignal für ledPin bereitzustellen, was eine Spannungsdifferenz zwischen den LED-Pins erzeugt und die LED zum Leuchten bringt.

.. code-block:: C

    digitalWrite(ledPin, HIGH);

Wenn das Pegelsignal auf LOW geändert wird, wird das Signal von ledPin auf 0 V zurückgesetzt, um die LED auszuschalten.

.. code-block:: C

    digitalWrite(ledPin, LOW);

Für einen sichtbaren Wechsel zwischen Ein- und Ausschalten ist eine Verzögerung notwendig, daher verwenden wir den Befehl ``delay(1000)``, um den Controller für 1000 ms inaktiv zu halten.

.. code-block:: C

    delay(1000);
