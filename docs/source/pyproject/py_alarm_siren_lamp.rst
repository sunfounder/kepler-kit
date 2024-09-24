.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_alarm_lamp:

7.3 Alarmanlagenlampe
=======================

Polizeilichter sind oft im wirklichen Leben (oder in Filmen) zu sehen. In der Regel werden sie zur Verkehrsregelung, als Warnmittel und als wichtiges Sicherheitszubehör für Polizeibeamte, Rettungsfahrzeuge, Feuerwehrautos und Baufahrzeuge eingesetzt. Wenn Sie ihre Lichter sehen oder ihre Sirene hören, sollten Sie vorsichtig sein, denn das bedeutet, dass Sie (oder die Menschen in Ihrer Umgebung) möglicherweise in Gefahr sind.

In diesem Projekt nutzen wir eine LED und einen Summer, um ein kleines Warnlicht zu schaffen, das über einen Schiebeschalter aktiviert wird.

|sirem_alarm|


**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links erwerben.


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
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schaltplan**

|sch_alarm_siren_lamp|

* GP17 ist mit dem mittleren Pin des Schiebeschalters verbunden, parallel dazu sind ein 10K-Widerstand und ein Kondensator (Filter) an GND angeschlossen. Dies ermöglicht dem Schiebeschalter, ein konstant hohes oder niedriges Signal auszugeben, wenn er nach links oder rechts bewegt wird.
* Sobald GP15 hoch ist, leitet der NPN-Transistor und der passive Summer beginnt zu tönen. Dieser Summer wird programmiert, um in der Frequenz allmählich anzusteigen und so einen Sirenenton zu erzeugen.
* An GP16 ist eine LED angeschlossen, die so programmiert ist, dass ihre Helligkeit periodisch wechselt, um eine Sirene zu simulieren.

**Verdrahtung**

|wiring_alarm_siren_lamp|


**Code**

.. note::

    * Öffnen Sie die Datei ``7.3_alarm_siren_lamp.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im unteren rechten Bereich auf den "MicroPython (Raspberry Pi Pico)"-Interpreter zu klicken.

    * Für ausführliche Anleitungen beziehen Sie sich bitte auf :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    # Initialize the PWM for the buzzer (on pin 15) and LED (on pin 16)
    buzzer = machine.PWM(machine.Pin(15))  # PWM for buzzer
    led = machine.PWM(machine.Pin(16))  # PWM for LED
    led.freq(1000)  # Set the frequency of the LED PWM to 1kHz

    # Initialize the switch (on pin 17) as an input pin
    switch = machine.Pin(17, machine.Pin.IN)

    # Function to stop the buzzer by setting the duty cycle to 0%
    def noTone(pin):
        pin.duty_u16(0)  # Set the PWM duty cycle to 0, stopping the sound

    # Function to play a tone on the buzzer with a specified frequency
    def tone(pin, frequency):
        pin.freq(frequency)  # Set the frequency for the buzzer
        pin.duty_u16(30000)  # Set duty cycle to around 50% (30000 out of 65535)

    # Function to map a value from one range to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Interrupt handler function to toggle the bell_flag when the switch is pressed
    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag  # Toggle the bell_flag value
        print(bell_flag)  # Print the current state of bell_flag for debugging
        
        # Change the switch interrupt depending on the state of the bell_flag
        if bell_flag:
            # If bell_flag is True, listen for a falling edge (when switch is released)
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            # If bell_flag is False, listen for a rising edge (when switch is pressed)
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Initialize bell_flag to False (buzzer and LED off by default)
    bell_flag = False

    # Set up an interrupt to detect when the switch is pressed (rising edge)
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Main loop to control the buzzer and LED based on the bell_flag
    while True:
        if bell_flag == True:
            # If bell_flag is True, gradually increase the brightness of the LED
            # and change the buzzer frequency to simulate a bell ringing effect
            for i in range(0, 100, 2):  # Loop from 0 to 100 in steps of 2
                led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))  # Map i to LED brightness
                tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))  # Map i to buzzer frequency
                time.sleep_ms(10)  # Short delay to create a smooth ramp
        else:
            # If bell_flag is False, stop the buzzer and turn off the LED
            noTone(buzzer)  # Stop the buzzer
            led.duty_u16(0)  # Turn off the LED (set duty cycle to 0)


Sobald das Programm läuft, verschieben Sie den Schiebeschalter nach links (bei Ihnen kann es auch rechts sein, je nachdem, wie Ihr Schiebeschalter verdrahtet ist). Der Summer gibt dann einen aufsteigenden Warnton ab und die LED ändert entsprechend ihre Helligkeit; verschieben Sie den Schiebeschalter nach rechts und der Summer und die LED hören auf zu arbeiten.
