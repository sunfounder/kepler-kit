.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_keypad:

4.2 - 4x4 Tastenfeld
=======================

Das 4x4-Tastenfeld, auch als Matrix-Tastenfeld bekannt, besteht aus einer Matrix von 16 Tasten, die in einer einzigen Bedienoberfläche integriert sind.

Solche Tastenfelder findet man vor allem bei Geräten, die digitale Eingaben erfordern, wie zum Beispiel Taschenrechner, Fernbedienungen, Tastentelefone, Verkaufsautomaten, Geldautomaten, Zahlenschlösser und elektronische Türschlösser.

In diesem Projekt lernen wir, wie man ermittelt, welche Taste gedrückt wurde und den entsprechenden Tastenwert erhält.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://de.wikipedia.org/wiki/E.161>`_

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist natürlich praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Die Teile können aber auch einzeln über die untenstehenden Links gekauft werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENÜBERSICHT	
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
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schaltplan**

|sch_keypad_ar|

Vier Pull-down-Widerstände sind mit den jeweiligen Spalten des Matrix-Tastenfelds verbunden, damit G6 ~ G9 einen stabilen niedrigen Pegel erhalten, wenn keine Taste gedrückt ist.

Die Reihen des Tastenfelds (G2 ~ G5) sind so programmiert, dass sie einen hohen Pegel haben. Wird einer der Anschlüsse G6 ~ G9 als hoch gelesen, wissen wir, welche Taste gedrückt wurde.

Zum Beispiel wird bei einem hohen Signal auf G6 die Taste mit der Nummer 1 gedrückt; dies ist darauf zurückzuführen, dass die Steuerpins dieser Taste G2 und G6 sind. Wenn die Taste gedrückt wird, werden G2 und G6 miteinander verbunden und G6 ist ebenfalls hoch.

**Verdrahtung**

|wiring_keypad_ar|

Um die Verdrahtung zu vereinfachen, sind im obigen Schema die Spalte und die Reihe des Matrix-Tastenfelds sowie die 10K-Widerstände gleichzeitig in die Löcher eingesteckt, in denen sich G6 ~ G9 befinden.

**Code**

.. note::

    * Die Datei ``4.2_4x4_keypad.ino`` finden Sie im Verzeichnis ``kepler-kit-main/arduino/4.2_4x4_keypad``.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.
    * Die Bibliothek ``Adafruit Keypad`` wird hier verwendet. Sie können sie über den **Bibliotheksmanager** installieren.

      .. image:: img/lib_ad_keypad.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Programms wird die Shell die Tasten ausgeben, die Sie auf dem Tastenfeld gedrückt haben.

**Funktionsweise**

1. Einbinden der Bibliothek

   Wir beginnen mit der Einbindung der Bibliothek ``Adafruit_Keypad``, die uns eine einfache Schnittstelle zum Tastenfeld ermöglicht.

   .. code-block:: arduino

     #include "Adafruit_Keypad.h"

2. Tastenfeldkonfiguration

   .. code-block:: arduino

     const byte ROWS = 4;
     const byte COLS = 4;
     char keys[ROWS][COLS] = {
       { '1', '2', '3', 'A' },
       { '4', '5', '6', 'B' },
       { '7', '8', '9', 'C' },
       { '*', '0', '#', 'D' }
     };
     byte rowPins[ROWS] = { 2, 3, 4, 5 };
     byte colPins[COLS] = { 8, 9, 10, 11 };

   - Die Konstanten ``ROWS`` und ``COLS`` definieren die Abmessungen des Tastenfelds.
   - ``keys`` ist ein 2D-Array, das die Bezeichnung für jede Taste auf dem Tastenfeld speichert.
   - ``rowPins`` und ``colPins`` sind Arrays, die die Arduino-Pins speichern, die mit den Reihen und Spalten des Tastenfelds verbunden sind.

   .. raw:: html

      <br/>

3. Initialisierung des Tastenfelds

   Erstelle eine Instanz von ``Adafruit_Keypad`` mit dem Namen ``myKeypad`` und initialisiere sie.

   .. code-block:: arduino

     Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

4. setup() Funktion

   Initialisiere die serielle Kommunikation und das benutzerdefinierte Tastenfeld.

   .. code-block:: arduino

     void setup() {
       Serial.begin(9600);
       myKeypad.begin();
     }

5. Hauptschleife

   Überprüfe Tastenereignisse und zeige sie im seriellen Monitor an.

   .. code-block:: arduino

     void loop() {
       myKeypad.tick();
       while (myKeypad.available()) {
         keypadEvent e = myKeypad.read();
         Serial.print((char)e.bit.KEY);
         if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
         else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
       }
       delay(10);
     }