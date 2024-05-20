.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_74hc_4dig:

5.3 - Zeitmesser
===============================

Ein 4-stelliges 7-Segment-Display besteht aus vier miteinander verknüpften 7-Segment-Anzeigen.

Das 4-stellige 7-Segment-Display arbeitet eigenständig. Es nutzt das Prinzip der visuellen Persistenz des menschlichen Auges, um die Zeichen jedes 7-Segment-Displays in einer Schleife schnell anzuzeigen und so fortlaufende Zeichenfolgen zu bilden.

Zum Beispiel, wenn "1234" angezeigt wird, erscheint die "1" im ersten 7-Segment-Display, während "234" nicht angezeigt werden. Nach einer kurzen Zeit zeigt das zweite 7-Segment-Display "2", während die ersten, dritten und vierten 7-Segmente aus bleiben. Und so weiter, alle vier Ziffern werden nacheinander angezeigt. Dieser Prozess ist sehr kurz (typischerweise 5ms), und durch den optischen Nachleuchteffekt sowie das Prinzip der visuellen Persistenz sehen wir alle vier Zeichen gleichzeitig.

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler-Set
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die Komponenten auch einzeln über die untenstehenden Links erwerben.

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
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schaltplan**

|sch_4dig|

Die Verdrahtungsprinzipien sind im Grunde die gleichen wie bei :ref:`ar_74hc_led`, der einzige Unterschied besteht darin, dass Q0-Q7 an die a ~ g Pins des 4-stelligen 7-Segment-Displays angeschlossen sind.

Dann werden G10 ~ G13 verwendet, um auszuwählen, welches 7-Segment-Display aktiv sein soll.

**Verdrahtung**

|wiring_4dig|

**Code**

.. note::

    * Die Datei ``5.3_time_counter.ino`` finden Sie im Verzeichnis ``kepler-kit-main/arduino/5.3_time_counter``.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port vor dem Klicken auf die **Hochladen**-Taste auszuwählen.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/0e97386e-417e-4f53-a026-5f37e36deba4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nach dem Ausführen des Programms wird das 4-stellige 7-Segment-Display zu einem Zähler, und die Zahl erhöht sich jede Sekunde um 1.

**Wie funktioniert es?**

Das Senden von Signalen an jedes 7-Segment-Display erfolgt auf die gleiche Weise wie bei :ref:`ar_74hc_7seg`, mit der Funktion ``hc595_shift()``.
Der Kernpunkt beim 4-stelligen 7-Segment-Display ist die selektive Aktivierung jedes 7-Segment-Displays. Der damit verbundene Code ist wie folgt.

.. code-block:: arduino

    const int placePin[4] = {13,12,11,10}; 

    void setup ()
    {
        for (int i = 0; i<4;i++){
            pinMode(placePin[i],OUTPUT);
        }
    }

    void loop()
    { 
        pickDigit(0);
        hc595_shift(count%10/1);
        
        pickDigit(1);
        hc595_shift(count%100/10);
        
        pickDigit(2);
        hc595_shift(count%1000/100);
        
        pickDigit(3);
        hc595_shift(count%10000/1000);
    }

    void pickDigit(int digit){
        for(int i = 0; i < 4; i++){
            digitalWrite(placePin[i],HIGH);
        }
        digitalWrite(placePin[digit],LOW);
    }

Hier werden vier Pins (GP10, GP11, GP12, GP13) verwendet, um jede Stelle des 4-stelligen 7-Segment-Displays einzeln zu steuern.
Wenn der Status dieser Pins ``LOW`` ist, ist das entsprechende 7-Segment-Display aktiv; wenn der Status ``HIGH`` ist, arbeitet es nicht.

Die Funktion ``pickDigit(digit)`` wird verwendet, um alle 7-Segment-Displays zu deaktivieren und dann eine bestimmte Ziffer individuell zu aktivieren.
Danach wird ``hc595_shift()`` verwendet, um den entsprechenden 8-Bit-Code für das 7-Segment-Display zu schreiben.

Das 4-stellige 7-Segment-Display muss kontinuierlich nacheinander aktiviert werden, damit alle vier Ziffern sichtbar sind. Das bedeutet, dass man im Hauptprogramm nicht einfach Code hinzufügen kann, der das Timing beeinflusst.

Allerdings ist es notwendig, diesem Beispiel eine Timing-Funktion hinzuzufügen. Wenn wir ein ``delay(1000)`` einfügen, wird offensichtlich, dass nur ein 7-Segment-Display jeweils aktiv ist und die Illusion entlarvt wird, dass alle vier 7-Segment-Displays gleichzeitig arbeiten.

Eine ausgezeichnete Methode, dies zu erreichen, ist die Verwendung der ``millis()``-Funktion.

.. code-block:: arduino

    void setup()
    {
        timerStart = millis();
    }

    void loop()
    {
        unsigned int count = (millis() - timerStart) / 1000;
    }

Die ``millis()``-Funktion gibt die Anzahl der Millisekunden zurück, die seit dem Start des aktuellen Programms vergangen sind. Der erste Zeitwert wird als ``timerStart`` gespeichert;

wenn die Zeit erneut abgerufen werden muss, rufen wir die ``millis()``-Funktion wieder auf und subtrahieren ``timerStart``, um die bisherige Laufzeit des Programms zu ermitteln.

Abschließend wird dieser Zeitwert umgewandelt, um ihn auf dem 4-stelligen 7-Segment-Display darzustellen.

* `millis() <https://www.arduino.cc/reference/de/language/functions/time/millis/>`_
