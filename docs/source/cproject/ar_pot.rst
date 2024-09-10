.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pot:

2.11 - Drehen Sie den Knopf
===========================

In vorherigen Projekten haben wir den digitalen Eingang am Pico W verwendet. 
Ein Taster kann beispielsweise den Pin von einem niedrigen (aus) auf einen hohen Pegel (ein) umschalten. Dies ist ein binärer Arbeitszustand.

Der Pico W kann jedoch auch eine andere Art von Eingangssignal empfangen: den analogen Eingang. 
Dieser kann in einem beliebigen Zustand von vollständig geschlossen bis vollständig geöffnet sein und verfügt über eine Reihe möglicher Werte.
Der analoge Eingang ermöglicht es dem Mikrocontroller, die Lichtintensität, Schallintensität, Temperatur, Feuchtigkeit usw. der physischen Welt zu erfassen.

Normalerweise benötigt ein Mikrocontroller eine zusätzliche Hardware, um den analogen Eingang umzusetzen - den Analog-Digital-Wandler (ADC).
Aber der Pico W hat bereits einen integrierten ADC, den wir direkt nutzen können.

|pin_adc|

Der Pico W hat drei GPIO-Pins, die analogen Eingang nutzen können: GP26, GP27, GP28, also die analogen Kanäle 0, 1 und 2.
Zusätzlich gibt es einen vierten analogen Kanal, der mit dem eingebauten Temperatursensor verbunden ist und hier nicht vorgestellt wird.

In diesem Projekt versuchen wir, den Analogwert eines Potentiometers auszulesen.

* :ref:`cpn_potentiometer`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Die Teile können auch einzeln über die folgenden Links gekauft werden.

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schaltplan**

|sch_pot|

Das Potentiometer ist ein analoges Bauelement und kann in zwei verschiedene Richtungen gedreht werden.

Verbinden Sie den mittleren Pin des Potentiometers mit dem analogen Pin GP28. Der Raspberry Pi Pico W enthält einen mehrkanaligen, 16-Bit-Analog-Digital-Wandler. Das bedeutet, dass er die Eingangsspannung zwischen 0 und der Betriebsspannung (3,3V) auf einen Ganzzahlwert zwischen 0 und 65535 abbildet, sodass der Wert von GP28 zwischen 0 und 65535 liegt.

Die Berechnungsformel lautet wie folgt:

    (Vp/3.3V) x 65535 = Ap

Programmieren Sie anschließend den Wert von GP28 (Potentiometer) als PWM-Wert von GP15 (LED).
Auf diese Weise werden Sie feststellen, dass sich die Helligkeit der LED beim Drehen des Potentiometers gleichzeitig verändert.


**Verkabelung**

|wiring_pot|

**Code**

.. note::

    * Sie können die Datei ``2.11_turn_the_knob.ino`` im Pfad ``kepler-kit-main/arduino/2.11_turn_the_knob`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    
    * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den korrekten Anschluss auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.

Wenn das Programm läuft, können wir den aktuell von Pin GP28 gelesenen Analogwert im seriellen Monitor sehen.
Drehen Sie den Knopf, und der Wert wird sich von 0 bis 1023 ändern.
Gleichzeitig wird die Helligkeit der LED zunehmen, je höher der Analogwert ist.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3e3927a-bd1a-4756-83f2-141d47f99b1c/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**Wie funktioniert es?**

Um den seriellen Monitor zu aktivieren, müssen Sie die serielle Kommunikation in ``setup()`` starten und die Datenrate auf 9600 einstellen.

.. code-block:: arduino
    :emphasize-lines: 3

    void setup() {
        pinMode(ledPin, OUTPUT);
        Serial.begin(9600);
    }

* `Serial <https://www.arduino.cc/reference/de/language/functions/communication/serial/>`_

In der Loop-Funktion wird der Wert des Potentiometers gelesen, dann wird dieser Wert von 0-1023 auf 0-255 abgebildet, und schließlich wird der abgebildete Wert verwendet, um die Helligkeit der LED zu steuern.

.. code-block:: arduino

    void loop() {
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
        int brightness = map(sensorValue, 0, 1023, 0, 255);
        analogWrite(ledPin, brightness);
    }

* `analogRead() <https://www.arduino.cc/reference/de/language/functions/analog-io/analogread/>`_ wird verwendet, um den Wert des sensorPin (Potentiometer) zu lesen und ihn der Variable ``sensorValue`` zuzuweisen.

.. code-block:: arduino

    int sensorValue = analogRead(sensorPin);

* Der Wert von SensorValue wird im seriellen Monitor ausgegeben.

.. code-block:: arduino

    Serial.println(sensorValue);

* Hier wird die Funktion `map(value, fromLow, fromHigh, toLow, toHigh) <https://www.arduino.cc/reference/de/language/functions/analog-io/analogread/>`_ benötigt, da der gelesene Potentiometerwert im Bereich 0-1023 liegt und der Wert eines PWM-Pins im Bereich 0-255 liegt. Sie wird verwendet, um eine Zahl von einem Bereich in einen anderen umzumappen.

.. code-block:: arduino

    int brightness = map(sensorValue, 0, 1023, 0, 255);

* Nun können wir diesen Wert verwenden, um die Helligkeit der LED zu steuern.

.. code-block:: arduino

    analogWrite(ledPin, brightness);
