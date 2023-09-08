.. _ar_rgb:

2.4 - Farbenfrohes Licht
==============================================

Wie wir wissen, kann Licht überlagert werden. Zum Beispiel ergibt die Mischung aus blauem und grünem Licht Zyan-Licht, rotes und grünes Licht ergibt gelbes Licht.
Dies wird als "additive Farbmischung" bezeichnet.

* `Additive Farbmischung - Wikipedia <https://de.wikipedia.org/wiki/Additive_Farbmischung>`_

Basierend auf dieser Methode können wir mit den drei Grundfarben Licht in jeder sichtbaren Farbe erzeugen, je nach spezifischem Mischungsverhältnis. Zum Beispiel lässt sich Orange durch mehr Rot und weniger Grün erzeugen.

In diesem Kapitel werden wir die Geheimnisse der additiven Farbmischung mit einer RGB-LED ergründen!

Eine RGB-LED ist im Grunde eine Kapselung einer roten, einer grünen und einer blauen LED unter einer Lampenkappe; alle drei LEDs teilen sich einen gemeinsamen Kathodenpin.
Da jedem Anodenpin ein elektrisches Signal zugeführt wird, kann das Licht der entsprechenden Farbe angezeigt werden. Durch Veränderung der elektrischen Signalstärke an jedem Anodenpin können diverse Farben erzeugt werden.

* :ref:`cpn_rgb`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset ist natürlich praktisch, hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IM SET
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die folgenden Links kaufen.


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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schaltplan**

|sch_rgb|

Die PWM-Pins GP13, GP14 und GP15 steuern die roten, grünen und blauen Pins der RGB-LED. Der gemeinsame Kathodenpin ist mit GND verbunden. So kann die RGB-LED durch Überlagerung des Lichts an diesen Pins mit unterschiedlichen PWM-Werten eine spezifische Farbe anzeigen.


**Verkabelung**

|img_rgb_pin|

Eine RGB-LED hat 4 Pins: Der längste Pin ist der gemeinsame Kathodenpin, der normalerweise mit GND verbunden ist. Der linke Pin neben dem längsten Pin ist Rot, die beiden Pins rechts sind Grün und Blau.


|wiring_rgb|


**Code**

Hier können wir unsere Lieblingsfarbe in einer Zeichensoftware (wie Paint) auswählen und sie mit der RGB-LED darstellen.

.. note::

   * Sie können die Datei ``2.4_colorful_light.ino`` im Verzeichnis ``kepler-kit-main/arduino/2.4_colorful_light`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.


    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die **Upload**-Schaltfläche klicken.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/c869191c-026c-4aac-8396-09eaf6ee2204/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


|img_take_color|

Tragen Sie den RGB-Wert in ``color_set()`` ein, dann wird die RGB-LED die gewünschten Farben leuchten.


**Funktionsweise**

In diesem Beispiel ist die Funktion zum Zuweisen von Werten an die drei Pins der RGB-LED in einer eigenständigen Unterfunktion ``color()`` verpackt.

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

In ``loop()``, dient der RGB-Wert als Eingabeargument, um die Funktion ``color()`` aufzurufen und damit die RGB-LED in verschiedenen Farben leuchten zu lassen.

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); // Rot
        delay(1000); 
        color(0, 255, 0); // Grün
        delay(1000);  
        color(0, 0, 255); // Blau
        delay(1000);
    }

