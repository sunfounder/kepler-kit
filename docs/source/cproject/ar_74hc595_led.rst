.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_74hc_led:

5.1 Mikrochip - 74HC595
===========================

Ein integrierter Schaltkreis (englisch: integrated circuit), kurz IC, ist eine Art Miniatur-Elektronikbauteil.

Mithilfe eines bestimmten Prozesses werden die für einen Schaltkreis benötigten Transistoren, Widerstände, Kondensatoren, Induktoren und weitere Komponenten sowie Verdrahtungen auf einem oder mehreren kleinen Halbleiter-Wafern oder dielektrischen Substraten angeordnet und dann in einem Gehäuse verpackt. Dadurch entsteht eine mikrostrukturierte Einheit mit den erforderlichen Schaltkreisfunktionen; alle Komponenten sind als eine Einheit strukturiert. Dies markiert einen bedeutenden Schritt in Richtung Mikrominiaturisierung, geringem Energieverbrauch, Intelligenz und hoher Zuverlässigkeit der Elektronikkomponenten.

Die Erfinder der integrierten Schaltkreise sind Jack Kilby (integrierte Schaltungen auf Germaniumbasis (Ge)) und Robert Norton Noyce (integrierte Schaltungen auf Siliziumbasis (Si)).

Das Set enthält einen IC, den 74HC595, der den Gebrauch von GPIO-Pins erheblich reduziert. Genauer gesagt können durch das Schreiben einer 8-Bit-Binärzahl 8 Pins für den digitalen Signalausgang ersetzt werden.

* `Binärzahl - Wikipedia <https://de.wikipedia.org/wiki/Bin%C3%A4rzahl>`_

* :ref:`74HC595`

**Erforderliche Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset ist natürlich praktisch, hier der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - ELEMENTE IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Set	
        - 450+
        - |link_kepler_kit|

Sie können die Einzelteile auch über die unten stehenden Links erwerben.

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
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Schaltplan**

|sch_74hc_led|

* Wenn MR (Pin 10) auf hohem Pegel und OE (Pin 13) auf niedrigem Pegel ist, wird die Daten beim ansteigenden Flanken von SHcp eingelesen und über die ansteigende Flanke von SHcp ins Speicherregister übertragen.
* Sind die beiden Taktgeber miteinander verbunden, ist das Schieberegister immer einen Impuls vor dem Speicherregister.
* Im Speicherregister gibt es einen seriellen Schiebeeingangspin (Ds), einen seriellen Ausgangspin (Q) und eine asynchrone Reset-Taste (niedriges Pegel).
* Das Speicherregister gibt einen parallelen 8-Bit-Bus in drei Zuständen aus.
* Ist OE aktiviert (niedriges Pegel), werden die Daten im Speicherregister auf den Bus (Q0 ~ Q7) ausgegeben.

**Verdrahtung**

|wiring_74hc_led|

**Code**

.. note::

   * Die Datei ``5.1_microchip_74hc595.ino`` finden Sie im Verzeichnis ``kepler-kit-main/arduino/5.1_microchip_74hc595``.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.


   * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den korrekten Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/71854882-0c1b-4d09-b3e7-5ef7272f7293/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Während das Programm läuft, können Sie sehen, wie die LEDs nacheinander aufleuchten.

**Wie funktioniert das?**

Deklarieren Sie ein Array und speichern Sie mehrere 8-Bit-Binärzahlen, die dazu verwendet werden, den Arbeitszustand der acht von 74HC595 gesteuerten LEDs zu ändern.

.. code-block:: arduino

    int datArray[] = {0b00000000, 0b00000001, 0b00000011, 0b00000111, 0b00001111, 0b00011111, 0b00111111, 0b01111111, 0b11111111};

Setzen Sie zuerst ``STcp`` auf niedriges Pegel und dann auf hohes Pegel. Dadurch wird ein ansteigender Impuls von ``STcp`` erzeugt.

.. code-block:: arduino

    digitalWrite(STcp, LOW);

``shiftOut()`` wird verwendet, um ein Byte Daten bitweise zu verschieben. Das heißt, es verschiebt ein Byte Daten in datArray[num] zum Schieberegister über den DS-Pin. MSBFIRST bedeutet, dass von den höheren Bits aus bewegt wird.

.. code-block:: arduino

    shiftOut(DS, SHcp, MSBFIRST, datArray[num]);

Nach Ausführung von ``digitalWrite(STcp, HIGH)``, ist STcp an der ansteigenden Flanke. Zu diesem Zeitpunkt werden die Daten im Schieberegister ins Speicherregister verschoben.

.. code-block:: arduino

    digitalWrite(STcp, HIGH);

Nach 8 Durchläufen wird ein Byte Daten ins Speicherregister übertragen. Dann werden die Daten des Speicherregisters auf den Bus (Q0-Q7) ausgegeben. Zum Beispiel wird durch shiftOut ``B00000001`` die von Q0 gesteuerte LED eingeschaltet und die von Q1~Q7 gesteuerten LEDs ausgeschaltet.
