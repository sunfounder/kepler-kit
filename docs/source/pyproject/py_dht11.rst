.. _py_dht11:

6.2 Temperatur - Feuchtigkeit
=======================================

Feuchtigkeit und Temperatur stehen sowohl im Hinblick auf die physikalische Größe selbst als auch im tatsächlichen Leben der Menschen in engem Zusammenhang. 
Die Temperatur und Feuchtigkeit unserer Umgebung beeinflussen direkt die Thermoregulationsfunktion und den Wärmeübertragungseffekt des menschlichen Körpers. 
Dies beeinflusst weiterhin die Denkaktivität und den geistigen Zustand und somit die Effizienz unserer Lern- und Arbeitsprozesse.

Temperatur ist eine der sieben grundlegenden physikalischen Größen im Internationalen Einheitensystem und dient zur Messung des Wärme- oder Kältegrades eines Objekts. 
Celsius ist eine der weltweit am häufigsten verwendeten Temperaturskalen und wird durch das Symbol "℃" ausgedrückt.

Feuchtigkeit ist die Konzentration von Wasserdampf in der Luft. 
Die relative Luftfeuchtigkeit wird im Alltag häufig verwendet und in %RH ausgedrückt. Sie steht in engem Zusammenhang mit der Temperatur. 
Für ein bestimmtes Volumen von abgeschlossenem Gas gilt: Je höher die Temperatur, desto niedriger die relative Feuchtigkeit und umgekehrt.

|img_Dht11|

Ein grundlegender digitaler Temperatur- und Feuchtigkeitssensor, der **DHT11**, ist in diesem Kit enthalten.
Er verwendet einen kapazitiven Feuchtigkeitssensor und einen Thermistor, um die umgebende Luft zu messen und gibt ein digitales Signal an den Datenpins aus (analoge Eingangspins sind nicht erforderlich).

* :ref:`cpn_dht11`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist definitiv praktisch, ein gesamtes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler-Set	
        - 450+
        - |link_kepler_kit|

Sie können diese auch über die nachfolgenden Links einzeln erwerben:

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
        - Micro USB Kabel
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

    * Öffnen Sie die Datei ``6.2_temperature_humidity.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Detaillierte Anleitungen finden Sie unter :ref:`open_run_code_py`.
    
    * Hier müssen Sie die Bibliothek ``dht.py`` verwenden. Bitte überprüfen Sie, ob sie auf Pico W hochgeladen wurde. Eine detaillierte Anleitung finden Sie unter :ref:`add_libraries_py`.

.. code-block:: python

    from machine import Pin, I2C
    import utime as time
    from dht import DHT11, InvalidPulseCount

    pin = Pin(16, Pin.IN, Pin.PULL_UP)
    sensor = DHT11(pin)
    time.sleep(5)  # initial delay

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')


Nachdem der Code ausgeführt wurde, werden Temperatur und Feuchtigkeit kontinuierlich in der Shell ausgegeben. Mit fortlaufender Programmausführung werden diese Werte immer genauer.

**Wie funktioniert es?**

In der dht-Bibliothek haben wir die relevante Funktionalität in die Klasse ``DHT11`` integriert.

.. code-block:: python

    from dht import DHT11, InvalidPulseCount

Initialisieren Sie das ``DHT11``-Objekt. Für dieses Gerät wird nur ein digitaler Eingang benötigt.

.. code-block:: python

    pin = Pin(16, Pin.IN, Pin.PULL_UP)
    sensor = DHT11(pin)

Verwenden Sie ``sensor.measure()``, um die aktuelle Temperatur und Feuchtigkeit zu lesen, die in ``sensor.temperature`` und ``sensor.humidity`` gespeichert werden. Diese Werte werden dann ausgegeben. 
Die Abtastrate des DHT11 beträgt 1HZ, daher wird in der Schleife ein ``time.sleep(1)`` benötigt.

.. code-block:: python

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')

