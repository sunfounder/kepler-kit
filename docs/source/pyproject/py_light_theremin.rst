.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_light_theremin:

7.1 Licht-Theremin
=========================

Ein Theremin ist ein elektronisches Musikinstrument, das keinen physischen Kontakt erfordert. Je nach Position der Hand des Spielers erzeugt es unterschiedliche Töne.

Üblicherweise besteht der Steuerungsbereich aus zwei Metallantennen, die die Position der Hände des Thereministen erfassen und Oszillatoren mit einer Hand und die Lautstärke mit der anderen steuern. Die elektrischen Signale vom Theremin werden verstärkt und an einen Lautsprecher gesendet.

Zwar können wir das gleiche Instrument mit Pico W nicht nachbilden, jedoch können wir mit einem Fotowiderstand und einem passiven Summer ein ähnliches Spielgefühl erzeugen.

* `Theremin - Wikipedia <https://de.wikipedia.org/wiki/Theremin>`_

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

Sie können die Teile auch einzeln über die unten stehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - MENGE
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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Aktiver :ref:`cpn_buzzer`
        - 1
        -
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schaltplan**

|sch_light_theremin|

Bevor Sie mit dem Projekt beginnen, bewegen Sie Ihre Hand auf und ab über den Fotowiderstand, um den Lichtintensitätsbereich zu kalibrieren. Die mit GP16 verbundene LED dient zur Anzeige der Debugging-Zeit; sie leuchtet beim Debugging-Start und erlischt beim Debugging-Ende.

Wenn GP15 ein hohes Signal ausgibt, leitet der S8050 (NPN-Transistor) und der passive Summer ertönt.

Je stärker das Licht, desto kleiner ist der Wert an GP28; umgekehrt ist er größer, wenn das Licht schwächer ist. Durch Programmierung des Fotowiderstandswerts zur Beeinflussung der Frequenz des passiven Summers kann ein lichtempfindliches Gerät simuliert werden.

**Verdrahtung**

|wiring_light_theremin|

**Code**

.. note::

    * Öffnen Sie die Datei ``7.1_light_theremin.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(16, machine.Pin.OUT)
    photoresistor = machine.ADC(28) 
    buzzer = machine.PWM(machine.Pin(15))

    light_low=65535
    light_high=0

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    # calibrate the photoresistor max & min values.
    timer_init_start = utime.ticks_ms()
    led.value(1)    
    while utime.ticks_diff(utime.ticks_ms(), timer_init_start)<5000:
        light_value = photoresistor.read_u16()
        if light_value > light_high:
            light_high = light_value
        if light_value < light_low:
            light_low = light_value   
    led.value(0)    

    # play
    while True:
        light_value  = photoresistor.read_u16()
        pitch = int(interval_mapping(light_value,light_low,light_high,50,6000))
        if pitch > 50 :
            tone(buzzer,pitch,20)
        utime.sleep_ms(10)

Sobald das Programm startet, leuchtet die LED auf, und wir haben fünf Sekunden Zeit, um den Erfassungsbereich des Fotowiderstands zu kalibrieren.

Dies ist auf die verschiedenen Lichtverhältnisse zurückzuführen, unter denen das Gerät eingesetzt werden könnte (z. B. unterschiedliche Lichtintensitäten zu Mittag und in der Dämmerung) sowie auf die Höhe unserer Hände über dem Fotowiderstand. Sie müssen die maximale und minimale Höhe Ihrer Hand über dem Fotowiderstand festlegen, die zugleich die Höhe ist, in der Sie das Instrument spielen.

Nach Ablauf der fünf Sekunden erlischt die LED, und wir können unsere Hände über dem Fotowiderstand bewegen und spielen.

