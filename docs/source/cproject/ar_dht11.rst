.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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
    * Die Bibliothek ``DHT sensor library`` wird hier verwendet. Sie können sie über den **Bibliotheksmanager** installieren.

      .. image:: img/lib_dht.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Codes werden Sie sehen, dass der Serielle Monitor kontinuierlich die Temperatur und die Feuchtigkeit ausgibt. Im Laufe der stabilen Programmausführung werden diese beiden Werte immer präziser.

**Wie funktioniert es?**

#. Einbindung notwendiger Bibliotheken und Definition von Konstanten.
   Dieser Teil des Codes bindet die DHT-Sensorbibliothek ein und definiert die Pinnummer sowie den Sensortyp, der in diesem Projekt verwendet wird.

   .. code-block:: arduino
    
      #include <DHT.h>
      #define DHTPIN 16       // Definiere den Pin für den Anschluss des Sensors
      #define DHTTYPE DHT11  // Definiere den Sensortyp

#. Erstellung eines DHT-Objekts.
   Hier erstellen wir ein DHT-Objekt unter Verwendung der definierten Pinnummer und des Sensortyps.

   .. code-block:: arduino

      DHT dht(DHTPIN, DHTTYPE);  // Erstelle ein DHT-Objekt

#. Diese Funktion wird einmal ausgeführt, wenn der Arduino startet. Wir initialisieren die serielle Kommunikation und den DHT-Sensor in dieser Funktion.

   .. code-block:: arduino

      void setup() {
        Serial.begin(9600);
        Serial.println(F("DHT11 Test!"));
        dht.begin();  // Initialisiere den DHT-Sensor
      }

#. Hauptschleife.
   Die Funktion ``loop()`` läuft kontinuierlich nach der Setup-Funktion. Hier lesen wir die Luftfeuchtigkeit und Temperatur aus, berechnen den Hitzeindex und geben diese Werte im seriellen Monitor aus. Wenn das Auslesen des Sensors fehlschlägt (NaN zurückgibt), wird eine Fehlermeldung ausgegeben.

   .. Hinweis::
    
      Der |link_heat_index| ist eine Methode, um zu messen, wie heiß es sich draußen anfühlt, indem die Lufttemperatur und die Luftfeuchtigkeit kombiniert werden. Er wird auch als "gefühlte Temperatur" oder "scheinbare Temperatur" bezeichnet.

   .. code-block:: arduino

      void loop() {
        delay(2000);
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
        float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      }