.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_mpr121:

4.3 Elektroden-Tastatur
================================

Der MPR121 ist eine hervorragende Option, wenn Sie eine Vielzahl von Berührungsschaltern in Ihr Projekt integrieren möchten. Er verfügt über Elektroden, die mit Leitern erweitert werden können. 
Wenn Sie die Elektroden an einer Banane befestigen, können Sie diese in einen Berührungsschalter verwandeln.

* :ref:`cpn_mpr121`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist durchaus praktisch, gleich ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ARTIKEL IM KIT
        - LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die unten stehenden Links beziehen.

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schaltplan**

|sch_mpr121|

**Verdrahtung**

|wiring_mpr121|

**Code**

.. note::

    * Öffnen Sie die Datei ``4.3_electrode_keyboard.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Anschließend klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

    * Sie benötigen die Bibliothek ``mpr121.py``. Prüfen Sie, ob diese bereits auf dem Pico W hochgeladen wurde. Eine ausführliche Anleitung finden Sie unter :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # Überprüfen aller Tasten
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

Nachdem das Programm ausgeführt wurde, können Sie die zwölf Elektroden am MPR121 berühren, und die berührten Elektroden werden ausgegeben.

Sie können die Elektroden erweitern, um andere Leiter wie Obst, Draht, Folie usw. anzuschließen. Dies eröffnet Ihnen weitere Möglichkeiten zur Auslösung dieser Elektroden.

**Funktionsweise?**

In der mpr121-Bibliothek haben wir die Funktionalität in die Klasse ``MPR121`` integriert.

.. code-block:: python

    from mpr121 import MPR121

Der MPR121 ist ein I2C-Modul, für dessen Initialisierung ein Satz I2C-Pins definiert werden muss. Zu diesem Zeitpunkt werden die Anfangszustände der Elektroden des Moduls aufgezeichnet. Falls die Elektroden erweitert werden, muss das Beispiel erneut ausgeführt werden, um die Anfangswerte zurückzusetzen.

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://de.wikipedia.org/wiki/I%C2%B2C>`_

Verwenden Sie dann ``mpr.get_all_states()`` um zu lesen, ob die Elektroden ausgelöst werden. Wenn die Elektroden 2 und 3 ausgelöst werden, wird der Wert ``[2, 3]`` erzeugt.

.. code-block::

    while True:
        value = mpr.get_all_states()
        if len(value) ! = 0:
            print(value)
        time.sleep_ms(100)

Sie können auch ``mpr.is_touched(electrode)`` verwenden, um eine bestimmte Elektrode zu überprüfen. Wenn sie ausgelöst wird, gibt die Methode ``True`` zurück, andernfalls ``False``.

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)
