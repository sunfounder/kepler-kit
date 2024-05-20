.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_pa_buz:

3.2 Eigener Ton
==========================================

Im vorherigen Projekt haben wir einen aktiven Summer verwendet, diesmal setzen wir einen passiven Summer ein.

Wie der aktive Summer arbeitet auch der passive Summer mit dem Phänomen der elektromagnetischen Induktion. Der Unterschied besteht darin, dass ein passiver Summer keine eigene Schwingungsquelle hat. Daher wird er bei Verwendung von Gleichstromsignalen keinen Ton erzeugen. 
Dies ermöglicht es dem passiven Summer jedoch, seine eigene Schwingungsfrequenz anzupassen und unterschiedliche Töne wie "do, re, mi, fa, sol, la, ti" auszusenden.

Lassen Sie den passiven Summer eine Melodie erklingen!

* :ref:`cpn_buzzer`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Ein Gesamtpaket zu kaufen ist natürlich praktisch, hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch einzeln über die unten stehenden Links erworben werden.

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schaltbild**

|sch_buzzer|

Wird der GP15-Ausgang auf "High" gesetzt, wird nach dem 1K-Strombegrenzungswiderstand (zum Schutz des Transistors) der S8050 (NPN-Transistor) leitend, und der Summer gibt einen Ton ab.

Die Rolle des S8050 (NPN-Transistor) besteht darin, den Strom zu verstärken und somit den Ton des Summers zu erhöhen. Tatsächlich können Sie den Summer auch direkt an GP15 anschließen, dann werden Sie allerdings feststellen, dass der Ton leiser ist.

**Verdrahtung**

|img_buzzer|

Im Kit sind zwei verschiedene Summertypen enthalten; wir verwenden einen passiven Summer (den mit der freiliegenden Leiterplatte auf der Rückseite).

Für den Betrieb des Summers ist ein Transistor erforderlich, hier verwenden wir den S8050.

|wiring_buzzer|

.. 1. Verbinden Sie 3V3 und GND des Pico W mit der Stromschiene des Breadboards.
.. #. Verbinden Sie den Pluspol des Summers mit der positiven Stromschiene.
.. #. Verbinden Sie den Kathodenpin des Summers mit dem **Kollektor**-Anschluss des Transistors.
.. #. Verbinden Sie den **Basis**-Anschluss des Transistors über einen 1kΩ-Widerstand mit dem GP15-Pin.
.. #. Verbinden Sie den **Emitter**-Anschluss des Transistors mit der negativen Stromschiene.



**Code**

.. note::

    * Öffnen Sie die Datei ``3.2_custom_tone.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, unten rechts den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen. 

    * Für ausführliche Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    tone(buzzer,440,250)
    utime.sleep_ms(500)
    tone(buzzer,494,250)
    utime.sleep_ms(500)
    tone(buzzer,523,250)


**Wie funktioniert es?**

Wenn der passive Summer ein digitales Signal erhält, kann er nur die Membran bewegen, ohne einen Ton zu erzeugen.

Daher verwenden wir die Funktion ``tone()`` um ein PWM-Signal zu generieren und den passiven Summer zum Klingen zu bringen.

Diese Funktion hat drei Parameter:

* **pin**, der GPIO-Pin, der den Summer steuert.
* **Frequenz**, die Tonhöhe des Summers wird durch die Frequenz bestimmt. Je höher die Frequenz, desto höher die Tonhöhe.
* **Dauer**, die Dauer des Tons.

Wir nutzen die Funktion ``duty_u16()`` um den Tastgrad auf 30000 (etwa 50%) zu setzen. Es können auch andere Werte sein; wichtig ist nur, ein diskontinuierliches elektrisches Signal zu erzeugen.

**Mehr erfahren**

Wir können den spezifischen Ton gemäß der Grundfrequenz des Klaviers simulieren, um ein vollständiges Musikstück zu spielen.

* `Frequenzen der Klaviertasten - Wikipedia <https://de.wikipedia.org/wiki/Frequenzen_der_gleichstufigen_Stimmung>`_

.. note::

    * Öffnen Sie die Datei ``3.2_custom_tone_2.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, unten rechts den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.

    * Für ausführliche Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    NOTE_C4 = 262
    NOTE_G3 = 196
    NOTE_A3 = 220
    NOTE_B3 = 247

    melody =[NOTE_C4,NOTE_G3,NOTE_G3,NOTE_A3,NOTE_G3,NOTE_B3,NOTE_C4]

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    for note in melody:
        tone(buzzer,note,250)
        utime.sleep_ms(150)
