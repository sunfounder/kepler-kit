.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_button:

2.5 - Tastenwert auslesen
==============================================

Anhand der Bezeichnung GPIO (General-purpose input/output) lässt sich erkennen, dass diese Pins sowohl Eingabe- als auch Ausgabefunktionen haben. 
In den vorherigen Lektionen haben wir die Ausgabefunktion verwendet, in diesem Kapitel werden wir die Eingabefunktion nutzen, um den Wert der Taste auszulesen.

* :ref:`cpn_button`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Kit zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IN DIESEM KIT
        - KAUF-LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Die Teile können auch einzeln über die folgenden Links erworben werden.

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schaltplan**

|sch_button|

Ein Anschluss des Tastenpins ist mit 3,3V verbunden, und der andere Anschluss ist mit GP14 verbunden. Wenn die Taste gedrückt wird, wird GP14 auf "High" gesetzt. Ist die Taste jedoch nicht gedrückt, befindet sich GP14 in einem schwebenden Zustand und könnte sowohl "High" als auch "Low" sein. Um einen stabilen "Low"-Zustand zu erhalten, wenn die Taste nicht gedrückt ist, muss GP14 über einen 10K-Pull-down-Widerstand erneut mit GND verbunden werden.

**Verkabelung**

|wiring_button|


.. note::
    Man kann den vierbeinigen Taster als H-förmigen Taster betrachten. Seine linken (rechten) beiden Beine sind miteinander verbunden, was bedeutet, dass er nach Überqueren der mittleren Trennlinie die beiden halben Reihen derselben Reihennummer verbindet. (Beispielsweise sind in meiner Schaltung E23 und F23 verbunden, ebenso wie E25 und F25).

    Bevor die Taste gedrückt wird, sind die linke und rechte Seite voneinander unabhängig, und der Strom kann nicht von einer Seite zur anderen fließen.



**Code**

.. note::

   * Sie können die Datei ``2.5_reading_button_value.ino`` unter dem Pfad ``kepler-kit-main/arduino/2.5_reading_button_value`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.

   * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6fcb7cac-e866-4a2d-8162-8e0c6fd17660/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nachdem der Code ausgeführt wurde, klicken Sie auf das Lupensymbol in der oberen rechten Ecke der Arduino IDE (Serial Monitor).

.. image:: img/open_serial_monitor.png

Jetzt, wenn Sie den Knopf drücken, wird im Serial Monitor "Sie haben den Knopf gedrückt!" angezeigt.

**Wie funktioniert das?**

Um den Serial Monitor zu aktivieren, müssen Sie die serielle Kommunikation in ``setup()`` starten und die Datenrate auf 9600 einstellen.

.. code-block:: arduino

    Serial.begin(115200);

* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

Für den Knopf müssen wir ihren Modus auf ``INPUT`` setzen, um ihre Werte abrufen zu können.

.. code-block:: arduino

    pinMode(buttonPin, INPUT);

Lesen Sie den Status von ``buttonPin`` in ``loop()`` und weisen Sie ihn der Variablen ``buttonState`` zu.

.. code-block:: arduino

    buttonState = digitalRead(buttonPin);
    
* `digitalRead() <https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/>`_

Wenn der ``buttonState`` HIGH ist, wird die LED blinken.
Im Serial Monitor wird "You pressed the button!" angezeigt.

.. code-block:: arduino

    if (buttonState == HIGH) {
        Serial.println("You pressed the button!");
    }

**Pull-up Arbeitsmodus**

Als nächstes folgt die Verdrahtung und der Code, wenn der Knopf im Pull-up-Arbeitsmodus ist, probieren Sie es bitte aus.

|wiring_button_pullup|

.. 1. Verbinden Sie den 3V3-Pin von Pico W mit der positiven Stromschiene des Steckbretts.
.. #. Setzen Sie den Knopf in das Steckbrett ein und überbrücken Sie die mittlere Trennlinie.
.. #. Verwenden Sie ein Jumperkabel, um einen der Knopfpins mit der **negativen** Schiene zu verbinden (meiner ist der Pin oben rechts).
.. #. Verbinden Sie den anderen Pin (oben links oder unten links) mit GP14 über ein Jumperkabel.
.. #. Verwenden Sie einen 10K-Widerstand, um den Pin in der oberen linken Ecke des Knopfes und der **positiven** Schiene zu verbinden.
.. #. Verbinden Sie die negative Stromschiene des Steckbretts mit Picos GND.

Der einzige Unterschied, den Sie im Vergleich zum Pull-down-Modus sehen werden, ist, dass der 10K-Widerstand mit 3,3V verbunden ist und der Knopf mit GND verbunden ist. Wenn der Knopf also gedrückt wird, erhält GP14 ein niedriges Signal, was das Gegenteil des im Pull-down-Modus erhaltenen Wertes ist.
Ändern Sie diesen Code also zu ``if (buttonState == LOW)``.
