.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_ultrasonic:

6.1 - Abstandsmessung
======================================

Das Ultraschall-Sensormodul arbeitet nach dem Prinzip von Sonar- und Radarsystemen, um den Abstand zu einem Objekt zu ermitteln.

* :ref:`cpn_ultrasonic`

**Benötigte Bauteile**

Für dieses Projekt benötigen wir die folgenden Komponenten.

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

Die Komponenten können auch einzeln über die untenstehenden Links erworben werden.

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schaltplan**

|sch_ultrasonic|

**Verkabelung**

|wiring_ultrasonic|

**Code**

.. note::

    * Die Datei ``6.1_ultrasonic.ino`` finden Sie unter dem Pfad ``kepler-kit-main/arduino/6.1_ultrasonic``.
    * Alternativ können Sie den Code in die **Arduino IDE** kopieren.
  
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf **Hochladen** klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Sobald das Programm läuft, wird die serielle Monitoranzeige den Abstand des Ultraschallsensors zum vorausliegenden Hindernis ausgeben.

**Wie funktioniert es?**

Für die Anwendung des Ultraschallsensors können wir direkt die Unterfunktion überprüfen.

.. code-block:: arduino

    float readSensorData(){// ...}

Ein ``PING`` wird durch einen HIGH-Puls von 2 oder mehr Mikrosekunden ausgelöst. (Geben Sie vorher einen kurzen ``LOW``-Puls aus, um einen sauberen ``HIGH``-Puls zu gewährleisten.)

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

Der Echo-Pin wird verwendet, um das Signal von PING zu lesen, ein ``HIGH``-Puls, dessen Dauer die Zeit (in Mikrosekunden) von der Aussendung des Pings bis zum Empfang des Echos des Objekts ist.

.. code-block:: arduino

    microsecond = pulseIn(echoPin, HIGH);

Die Schallgeschwindigkeit beträgt 340 m/s oder 29 Mikrosekunden pro Zentimeter.

Dies gibt die vom Ping zurückgelegte Strecke an, hin und zurück, also teilen wir durch 2, um den Abstand des Hindernisses zu erhalten.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;

Beachten Sie, dass der Ultraschallsensor das Programm pausiert, während er arbeitet, was bei komplexen Projekten zu Verzögerungen führen kann.
