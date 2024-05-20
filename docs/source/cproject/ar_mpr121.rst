.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_mpr121:

4.3 - Elektroden-Tastatur
================================

Der MPR121 ist eine gute Wahl, wenn Sie Ihrem Projekt eine Vielzahl von Berührungsschaltern hinzufügen möchten. Das Modul besitzt Elektroden, die mit Leitern erweitert werden können.
Verbinden Sie die Elektroden beispielsweise mit einer Banane, verwandeln Sie diese in einen Berührungsschalter.

* :ref:`cpn_mpr121`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten:

Einen Komplettbausatz zu kaufen ist sicherlich praktisch, hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die Teile auch einzeln über die folgenden Links beziehen:

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schaltplan**

|sch_mpr121|

**Verdrahtung**

|wiring_mpr121|

**Code**

.. note::

    * Die Datei ``4.3_electrode_keyboard.ino`` finden Sie im Verzeichnis ``kepler-kit-main/arduino/4.3_electrode_keyboard``.
    * Alternativ können Sie den Code in die **Arduino IDE** kopieren.

    * Vergessen Sie nicht, das richtige Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf **Hochladen** klicken.
    * Die Bibliotheken ``Adafruit_MPR121`` und ``Adafruit_BusIO`` werden hier verwendet. Bitte lesen Sie :ref:`add_libraries_ar`, um zu erfahren, wie sie zur Arduino IDE hinzugefügt werden können.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f31048b7-0f98-4d49-8c2e-26b3908e98cb/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Sobald das Programm läuft, können Sie die zwölf Elektroden auf dem MPR121-Modul berühren, und der Berührungsstatus wird in einem 12-Bit-Booleschen Array gespeichert und im seriellen Monitor angezeigt.
Wenn die erste und die elfte Elektrode berührt werden, wird ``100000000010`` ausgegeben.

Sie können die Elektroden durch Anschluss anderer Leiter wie Früchte, Draht, Folie usw. erweitern. Dadurch eröffnen sich Ihnen weitere Möglichkeiten, diese Elektroden zu betätigen.

**Wie funktioniert es?**

Initialisieren Sie das ``MPR121``-Objekt. Ab diesem Zeitpunkt werden die Zustände der Modul-Elektroden als Ausgangswerte gespeichert.
Wenn Sie die Elektroden erweitern, müssen Sie das Beispiel neu starten, um die Ausgangswerte zurückzusetzen.

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

Erhält den Wert der aktuellen Elektrode, es wird ein 12-Bit-Binärwert erhalten. Wenn Sie die erste und die elfte Elektrode berühren, erhält sie "100000000010".

.. code-block:: arduino

    // Get the currently touched pads
    currtouched = cap.touched();

Determine if the electrode state has changed.

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // reset our state
        lasttouched = currtouched;
    }

Wenn eine Änderung des Elektrodenzustands erkannt wird, werden die Werte von ``currtouched`` bitweise im Array ``touchStates[12]`` gespeichert. Schließlich wird das Array ausgegeben.

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }