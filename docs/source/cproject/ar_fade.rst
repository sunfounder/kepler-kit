.. _ar_fade:

2.3 - Verblassende LED
======================

Bislang haben wir lediglich zwei Ausgangssignale verwendet: hohes und niedriges Signal (oder auch als 1 & 0, EIN & AUS bezeichnet), was als digitale Ausgabe bezeichnet wird.
In der Praxis funktionieren jedoch viele Geräte nicht einfach durch Ein- oder Ausschalten, etwa bei der Geschwindigkeitsregelung eines Motors oder der Helligkeitsregulierung einer Schreibtischlampe.
Früher wurde ein regelbarer Widerstand genutzt, um diese Ziele zu erreichen, was jedoch stets unzuverlässig und ineffizient war.
Deshalb hat sich die Pulsweitenmodulation (PWM) als praktikable Lösung für solche komplexen Probleme etabliert.

Ein digitales Ausgangssignal, das aus einem hohen und einem niedrigen Signal besteht, wird als Puls bezeichnet. Die Pulsdauer dieser Pins kann durch Änderung der Ein-/Ausschaltgeschwindigkeit angepasst werden.

Kurz gesagt, wenn wir in einer kurzen Zeitspanne (wie etwa 20 ms, die durchschnittliche visuelle Verweilzeit der meisten Menschen)
die LED einschalten, ausschalten und wieder einschalten, werden wir nicht bemerken, dass sie ausgeschaltet wurde, jedoch wird die Helligkeit etwas geringer sein.
Je länger die LED in diesem Zeitraum eingeschaltet ist, desto heller wird sie sein.
Mit anderen Worten, je breiter der Puls im Zyklus ist, desto größer ist die "elektrische Signalstärke", die vom Mikrocontroller ausgegeben wird.
So steuert PWM die Helligkeit der LED (oder die Geschwindigkeit des Motors).

* `Pulsweitenmodulation – Wikipedia <https://de.wikipedia.org/wiki/Pulsweitenmodulation>`_

Beim Einsatz von PWM mit dem Pico W gibt es einige Punkte zu beachten. Werfen wir einen Blick auf dieses Bild.

|pin_pwm|

Jeder GPIO-Pin des Pico W unterstützt PWM, tatsächlich stehen jedoch insgesamt nur 16 unabhängige PWM-Ausgänge zur Verfügung (statt 30), die zwischen GP0 bis GP15 auf der linken Seite verteilt sind, und der PWM-Ausgang der rechten GPIO ist dem der linken Seite gleichwertig.

Worauf wir achten müssen, ist, denselben PWM-Kanal während der Programmierung nicht für verschiedene Zwecke einzusetzen. (Zum Beispiel sind GP0 und GP16 beide PWM_0A)

Nachdem wir dieses Wissen erworben haben, versuchen wir nun, den Effekt einer verblassenden LED zu erzielen.

* :ref:`cpn_led`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist sicherlich praktisch, ein komplettes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IM SET
        - KAUF-LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die folgenden Links kaufen.

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schaltplan**

|sch_led|

Dieses Projekt nutzt denselben Schaltkreis wie das erste Projekt :ref:`ar_led`, allerdings mit einem unterschiedlichen Signaltyp. Im ersten Projekt wurden digitale Hoch- und Niedrigpegel (0&1) direkt von GP15 ausgegeben, um die LEDs ein- oder auszuschalten. In diesem Projekt wird ein PWM-Signal von GP15 ausgegeben, um die Helligkeit der LED zu steuern.

**Verdrahtung**

|wiring_led|

**Code**

.. note::

   * Die Datei ``2.3_fading_led.ino`` können Sie im Pfad ``kepler-kit-main/arduino/2.3_fading_led`` finden.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   
   * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Upload**-Button klicken.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/86807da4-4714-4d3c-b6af-0f1b9a62223b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Mit der Ausführung des Programms wird die LED allmählich heller.

**Funktionsweise**

Pin 15 wird als ledPin deklariert.

.. code-block:: C

    const int ledPin = 15;

``analogWrite()`` weist im ``loop()`` dem ledPin einen analogen Wert (PWM-Welle) zwischen 0 und 255 zu, um die Helligkeit der LED zu ändern.

.. code-block:: C

    analogWrite(ledPin, value);

Mithilfe einer for-Schleife kann der Wert von ``analogWrite()`` schrittweise zwischen dem Minimalwert (0) und dem Maximalwert (255) geändert werden.

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
    }

Um das experimentelle Phänomen deutlich zu sehen, muss der for-Schleife ein ``delay(30)`` hinzugefügt werden, um die Zeit der Helligkeitsänderung zu steuern.

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
        delay(30);
    }
