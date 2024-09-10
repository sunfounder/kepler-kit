.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_temp:

2.13 - Thermometer
===========================

Ein Thermometer ist ein Gerät, das die Temperatur oder ein Temperaturgefälle (den Grad der Wärme oder Kälte eines Objekts) misst. Ein Thermometer besteht aus zwei wichtigen Elementen: (1) einem Temperatursensor (z.B. der Glühbirne eines Quecksilberthermometers oder dem pyrometrischen Sensor in einem Infrarotthermometer), bei dem eine Veränderung mit einer Temperaturänderung eintritt; 
und (2) einer Methode zur Umwandlung dieser Veränderung in einen Zahlenwert (z.B. die sichtbare Skala, die auf einem Quecksilberthermometer markiert ist, oder die digitale Anzeige bei einem Infrarotmodell). 
Thermometer finden in Technologie und Industrie zur Prozessüberwachung, in der Meteorologie, in der Medizin und in der wissenschaftlichen Forschung breite Anwendung.

Ein Thermistor ist eine Art von Temperatursensor, dessen Widerstand stark temperaturabhängig ist. Es gibt zwei Typen: 
Negativer Temperaturkoeffizient (NTC) und Positiver Temperaturkoeffizient (PTC), 
auch bekannt als NTC und PTC. Der Widerstand von PTC-Thermistoren steigt mit der Temperatur, während der Zustand von NTC dem entgegengesetzt ist.

In diesem Experiment verwenden wir einen **NTC-Thermistor**, um ein Thermometer zu bauen.

* :ref:`cpn_thermistor`

**Benötigte Bauteile**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Set zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - BAUTEILBESCHREIBUNG
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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Schaltplan**

|sch_temp|

In diesem Schaltkreis sind der 10K-Widerstand und der Thermistor in Reihe geschaltet, und der durch sie fließende Strom ist derselbe. Der 10K-Widerstand dient als Schutz, und GP28 liest den Wert nach der Spannungsumwandlung des Thermistors.

Wenn die Temperatur steigt, sinkt der Widerstandswert des NTC-Thermistors, dann sinkt seine Spannung, so dass der Wert von GP28 sinkt; Wenn die Temperatur hoch genug ist, wird der Widerstand des Thermistors nahezu 0 sein, und der Wert von GP28 wird nahezu 0 sein. In diesem Fall spielt der 10K-Widerstand eine schützende Rolle, so dass 3,3V und GND nicht direkt miteinander verbunden sind, was zu einem Kurzschluss führen würde.

Wenn die Temperatur fällt, wird der Wert von GP28 steigen. Wenn die Temperatur niedrig genug ist, wird der Widerstand des Thermistors unendlich sein, und seine Spannung wird nahe an 3,3V liegen (der 10K-Widerstand ist vernachlässigbar), und der Wert von GP28 wird nahe am Maximalwert von 65535 liegen.

Die Berechnungsformel ist unten dargestellt.

    (Vp/3,3V) x 65535 = Ap

**Verdrahtung**

|wiring_temp|

.. #. Verbinden Sie 3V3 und GND von Pico W mit der Stromschiene des Steckbretts.
.. #. Verbinden Sie ein Bein des Thermistors mit dem GP28-Pin, dann verbinden Sie dasselbe Bein mit der positiven Stromschiene mit einem 10K-Ohm-Widerstand.
.. #. Verbinden Sie das andere Bein des Thermistors mit der negativen Stromschiene.

.. note::
    * Der Thermistor ist schwarz und mit 103 markiert.
    * Der Farbring des 10K-Ohm-Widerstands ist rot, schwarz, schwarz, rot und braun.

**Code**

.. note::

    * Sie können die Datei ``2.13_thermometer.ino`` unter dem Pfad ``kepler-kit-main/arduino/2.13_thermometer`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1ae1a028-2647-4e4c-b647-0d4759f6fd03/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Nachdem das Programm ausgeführt wurde, wird der Serielle Monitor die Temperaturen in Celsius und Fahrenheit ausgeben.

**Wie funktioniert es?**

Jeder Thermistor hat einen Normwiderstand.
Hier beträgt er 10k Ohm, gemessen bei 25 Grad Celsius.

Wenn die Temperatur steigt, sinkt der Widerstand des Thermistors.
Dann werden die Spannungsdaten durch den A/D-Adapter in digitale Mengen umgewandelt.

Die Temperatur in Celsius oder Fahrenheit wird durch die Programmierung ausgegeben.

.. code-block:: arduino

    long a = analogRead(analogPin);

Diese Zeile dient zum Auslesen des Werts des Thermistors.

.. code-block:: arduino

    float tempC = beta / (log((1025.0 * 10 / a - 10) / 10) + beta / 298.0) - 273.0;
    float tempF = 1.8 * tempC + 32.0;

Diese Berechnungen wandeln die Werte des Thermistors in Grad Celsius und Fahrenheit um.

.. note::
    Hier ist der Zusammenhang zwischen Widerstand und Temperatur:

    **RT = RN expB(1/TK – 1/TN)**

    * RT ist der Widerstand des NTC-Thermistors, wenn die Temperatur TK beträgt.
    * RN ist der Widerstand des NTC-Thermistors bei der Nenntemperatur TN. Hier beträgt der Zahlenwert von RN 10k.
    * TK ist eine Kelvin-Temperatur und die Einheit ist K. Hier beträgt der Zahlenwert von TK 273,15 + Grad Celsius.
    * TN ist eine Nenntemperatur in Kelvin; die Einheit ist ebenfalls K. Hier beträgt der Zahlenwert von TN 273,15+25.
    * Und B (Beta), die Materialkonstante des NTC-Thermistors, wird auch als Wärmeempfindlichkeitsindex bezeichnet und hat einen Zahlenwert von 3950.
    * exp ist die Abkürzung für Exponential, und die Basiszahl e ist eine natürliche Zahl und beträgt ungefähr 2,7.

    Wandeln Sie diese Formel TK=1/(ln(RT/RN)/B+1/TN) um, um die Kelvin-Temperatur zu erhalten, die minus 273,15 gleich Grad Celsius ist.

    Dieser Zusammenhang ist eine empirische Formel. Sie ist nur dann genau, wenn die Temperatur und der Widerstand im wirksamen Bereich liegen.

Dieser Code bezieht sich darauf, Rt in die Formel TK=1/(ln(RT/RN)/B+1/TN) einzusetzen, um die Kelvin-Temperatur zu erhalten.
