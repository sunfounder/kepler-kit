.. _ar_dht11:

6.2 - Temperatur - Feuchtigkeit
=======================================

Temperatur und Feuchtigkeit sind sowohl in Bezug auf die physikalische Größe selbst als auch auf das alltägliche Leben der Menschen eng miteinander verbunden.
Die Temperatur und Feuchtigkeit der menschlichen Umgebung haben direkten Einfluss auf die thermoregulatorische Funktion und den Wärmeübertragungseffekt des menschlichen Körpers.
Dies wirkt sich weiter auf die Denkaktivität und den mentalen Zustand aus und beeinflusst damit die Effizienz unseres Lernens und Arbeitens.

Die Temperatur ist eine der sieben grundlegenden physikalischen Größen im Internationalen Einheitensystem und dient zur Messung des Wärmezustands eines Objekts.
Das Grad Celsius ist eine der weltweit am häufigsten verwendeten Temperaturskalen und wird durch das Symbol "℃" ausgedrückt.

Feuchtigkeit ist die Konzentration von Wasserdampf in der Luft.
Die relative Luftfeuchtigkeit wird im Alltag häufig verwendet und in %RH angegeben. Sie steht in engem Zusammenhang mit der Temperatur.
Für ein bestimmtes Volumen eingeschlossenen Gases gilt: Je höher die Temperatur, desto niedriger die relative Feuchtigkeit und umgekehrt.

|img_Dht11|

In diesem Kit ist ein grundlegender digitaler Temperatur- und Feuchtigkeitssensor, der **DHT11**, enthalten.
Er verwendet einen kapazitiven Feuchtigkeitssensor und einen Thermistor, um die umgebende Luft zu messen und gibt ein digitales Signal an den Datenpins aus (keine analogen Eingangspins erforderlich).

* :ref:`cpn_dht11`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die einzelnen Komponenten auch über die untenstehenden Links erwerben.

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|


**Schaltplan**

|sch_dht11|

**Verkabelung**

|wiring_dht11|

**Code**

.. note::

    * Die Datei ``6.2_dht11.ino`` finden Sie im Pfad ``kepler-kit-main/arduino/6.2_dht11``.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen**-Button klicken.
    * Hier wird die Bibliothek ``SimpleDHT`` verwendet. Wie Sie diese zur Arduino IDE hinzufügen, erfahren Sie unter :ref:`add_libraries_ar`.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Codes werden Sie sehen, dass der Serielle Monitor kontinuierlich die Temperatur und die Feuchtigkeit ausgibt. Im Laufe der stabilen Programmausführung werden diese beiden Werte immer präziser.

**Wie funktioniert es?**

Initialisierung des DHT11-Objekts. Für dieses Gerät ist lediglich ein digitaler Eingang erforderlich.

.. code-block:: arduino

    int pinDHT11 = 16;
    SimpleDHT11 dht11(pinDHT11);

Auslesen der aktuellen Temperatur und Feuchtigkeit, die in den Variablen ``temperature`` und ``humidity`` gespeichert werden. ``err`` dient zur Überprüfung der Gültigkeit der Daten.

.. code-block:: arduino

    byte temperature = 0;
    byte humidity = 0;
    int err = dht11.read(&temperature, &humidity, NULL);

Filtern ungültiger Daten.

.. code-block:: arduino

    if (err != SimpleDHTErrSuccess) {
        Serial.print("Read DHT11 failed, err="); 
        Serial.print(SimpleDHTErrCode(err));
        Serial.print(","); 
        Serial.println(SimpleDHTErrDuration(err)); 
        delay(1000);
        return;
    }     

Ausgabe der Temperatur und Feuchtigkeit.

.. code-block:: arduino

    Serial.print((int)temperature); 
    Serial.print(" °C, "); 
    Serial.print((int)humidity); 
    Serial.println(" %RH");

Abschließend ist die Abtastrate des DHT11 1 HZ, daher ist eine ``delay(1500)`` in der Schleife erforderlich.

.. code-block:: arduino

    delay(1500);
