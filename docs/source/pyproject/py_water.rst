.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_water:

2.14 Wasserstand erfühlen
=====================================

|img_water_sensor|

Der Wasserstandssensor ist zur Wasserdetektion konzipiert und kann vielfältig zur Messung von Regenfällen, Wasserstand und sogar Flüssigkeitsaustritt eingesetzt werden.

Er misst den Wasserstand, indem er eine Reihe von freiliegenden parallelen Drahtspuren verwendet, um die Größe der Wassertropfen/das Volumen zu messen. Das Wasserstandsvolumen lässt sich leicht in ein analoges Signal umwandeln, und der ausgegebene Analogwert kann direkt vom Hauptsteuerboard abgelesen werden, um den Wasserstandsalarm auszulösen.

.. warning::

    Der Sensor darf nicht vollständig unter Wasser getaucht werden. Lassen Sie nur den Teil, an dem sich die zehn Spuren befinden, mit Wasser in Kontakt kommen. Zudem wird das Einschalten des Sensors in einer feuchten Umgebung die Korrosion der Sonde beschleunigen und die Lebensdauer des Sensors verkürzen. Es wird daher empfohlen, den Sensor nur beim Ablesen einzuschalten.

* :ref:`cpn_water_level`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - ANZAHL
        - LINK

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Schaltplan**

|sch_water|


**Verdrahtung**

|wiring_water|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.14_feel_the_water_level.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie anschließend auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für ausführliche Tutorials verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value=sensor.read_u16()
        print(value)
        utime.sleep_ms(200)


Nachdem das Programm ausgeführt wurde, tauchen Sie das Wasserstandsmodul langsam ins Wasser. Mit zunehmender Tiefe wird die Shell einen höheren Wert ausgeben.

**Mehr erfahren**

Es gibt eine Möglichkeit, das Analogeingangsmodul als digitales Modul zu verwenden.

Zunächst ermitteln Sie den Wert des Wasserstandssensors in einer trockenen Umgebung und verwenden diesen als Schwellenwert. Dann führen Sie die Programmierung durch und lesen den Wert des Wasserstandssensors erneut ab. Weicht der Messwert des Sensors deutlich vom Wert in einer trockenen Umgebung ab, ist er Flüssigkeiten ausgesetzt. Mit anderen Worten: Platzieren Sie dieses Gerät in der Nähe eines Wasserrohrs, kann es feststellen, ob ein Leck im Rohr vorliegt.

.. note::

    * Öffnen Sie die Datei ``2.14_water_level_threshold.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie anschließend auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für ausführliche Tutorials verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000 #Dieser Wert muss an die Umgebung angepasst werden.

    while True:
        value=sensor.read_u16()
        if value > threshold :
            print("Liquid leakage!")
        utime.sleep_ms(200)

