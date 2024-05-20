.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_pir:

2.10 Bewegungserkennung beim Menschen
=====================================

Ein passiver Infrarotsensor (PIR-Sensor) ist ein weit verbreiteter Sensor, der Infrarotstrahlung (IR) von Objekten in seinem Sichtfeld misst. 
Einfach ausgedrückt: Er nimmt die von einem Körper abgestrahlte Infrarotstrahlung auf und erkennt so die Bewegung von Menschen und anderen Tieren.
Konkret informiert er die Hauptsteuerplatine darüber, dass jemand den Raum betreten hat.

:ref:`cpn_pir`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein Komplettset zu kaufen ist sicherlich bequem, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IM SET
        - LINK
    *   - Kepler-Set
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links erwerben.

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schaltplan**

|sch_pir|

Wenn das PIR-Modul eine vorbeigehende Person erkennt, wird GP14 auf "hoch" gesetzt, andernfalls bleibt er "niedrig".

.. note::
    Das PIR-Modul verfügt über zwei Potentiometer: eines zur Einstellung der Empfindlichkeit, das andere zur Anpassung der Erfassungsreichweite. Für optimale Ergebnisse sollten beide Potentiometer ganz nach links gedreht werden.

    |img_PIR_TTE|

**Verdrahtung**

|wiring_pir|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.10_detect_human_movement.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Anschließend klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke auszuwählen.

    * Detaillierte Anleitungen finden Sie unter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Somebody here!")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

Nach dem Ausführen des Programms wird in der Shell "Somebody here!" ausgegeben, wenn das PIR-Modul eine nahe Person erkennt.

**Weitere Informationen**

Das PIR-Modul ist sehr empfindlich. Um es an die Einsatzumgebung anzupassen, sind Einstellungen erforderlich. Richten Sie die Seite mit den beiden Potentiometern auf sich aus und drehen Sie beide Potentiometer ganz nach links. Setzen Sie die Jumperkappe auf den Pin mit L und den mittleren Pin.

.. note::

    * Öffnen Sie die Datei ``2.10_pir_adjustment.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Anschließend klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke auszuwählen.

    * Detaillierte Anleitungen finden Sie unter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    global timer_delay
    timer_delay = utime.ticks_ms()
    print("start")

    def pir_in_high_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_FALLING, handler=pir_in_low_level)    
        intervals = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()
        print("the dormancy duration is " + str(intervals) + "ms")

    def pir_in_low_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 
        intervals2 = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()        
        print("the duration of work is " + str(intervals2) + "ms")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 

Lassen wir uns die Anpassungsmethode anhand der experimentellen Ergebnisse analysieren.

|img_pir_back|

1. Auslösemodus

   Werfen wir einen Blick auf die Pins mit der Jumperkappe in der Ecke.
   Sie ermöglichen dem PIR, in den wiederholbaren oder nicht wiederholbaren Auslösemodus zu wechseln.

   Aktuell ist unsere Jumperkappe mit dem mittleren Pin und dem L-Pin verbunden, was den PIR in den nicht wiederholbaren Auslösemodus versetzt.
   In diesem Modus sendet der PIR bei Erkennung einer Bewegung ein Hochpegelsignal für etwa 2,8 Sekunden an die Hauptsteuerplatine.
   Anhand der ausgegebenen Daten können wir erkennen, dass die Arbeitsdauer stets rund 2800 ms beträgt.

   Als Nächstes ändern wir die Position der unteren Jumperkappe und verbinden sie mit dem mittleren Pin und dem H-Pin, um den PIR in den wiederholbaren Auslösemodus zu versetzen.
   In diesem Modus sendet der PIR ein Hochpegelsignal an die Hauptsteuerplatine, solange innerhalb des Erfassungsbereichs eine Bewegung stattfindet (beachten Sie, dass es sich um eine Bewegung handelt, nicht um ein statisches Verharren vor dem Sensor).
   In den ausgegebenen Daten ist die Arbeitsdauer ein variabler Wert.

#. Verzögerungsanpassung

   Das linke Potentiometer dient zur Einstellung des Intervalls zwischen zwei Arbeitszyklen.
   
   Derzeit haben wir es ganz gegen den Uhrzeigersinn gedreht, was dazu führt, dass der PIR nach Beendigung der Hochpegel-Arbeit eine Ruhezeit von etwa 5 Sekunden einlegen muss. In dieser Zeit erfasst der PIR keine Infrarotstrahlung im Zielbereich mehr.
   Anhand der ausgegebenen Daten können wir erkennen, dass die Ruhezeit immer mindestens 5000 ms beträgt.

   Drehen wir das Potentiometer im Uhrzeigersinn, verlängert sich auch die Ruhezeit. Wenn es ganz im Uhrzeigersinn gedreht wird, kann die Ruhezeit bis zu 300 Sekunden betragen.

#. Entfernungsanpassung

   Das mittlere Potentiometer dient zur Einstellung des Erfassungsbereichs des PIR.
   
   Drehen Sie den Knopf des Entfernungsanpassungspotentiometers **im Uhrzeigersinn**, um den Erfassungsbereich zu erweitern. Der maximale Erfassungsbereich beträgt etwa 0 bis 7 Meter.
   Wird es **gegen den Uhrzeigersinn** gedreht, verringert sich der Erfassungsbereich, und der minimale Erfassungsbereich beträgt etwa 0 bis 3 Meter.
