.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_light_theremin:

7.1 Theremin a Luce
=========================

Il theremin è uno strumento musicale elettronico che non richiede contatto fisico. In base alla posizione della mano del musicista, produce diverse tonalità.

La sua sezione di controllo è solitamente composta da due antenne metalliche che rilevano la posizione delle mani del thereminista, una controllando gli oscillatori e l'altra il volume. I segnali elettrici del theremin vengono amplificati e inviati a un altoparlante.

Non possiamo riprodurre lo stesso strumento tramite Pico W, ma possiamo usare un fotoresistore e un cicalino passivo per ottenere un effetto simile.

* `Theremin - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE	
        - QUANTITÀ
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cavo Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Diversi
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
        - Cicalino :ref:`cpn_buzzer`
        - 1
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schema Elettrico**

|sch_light_theremin|

Prima di iniziare il progetto, muovi la mano su e giù sopra il fotoresistore per calibrare l'intervallo di intensità luminosa. Il LED collegato al GP16 viene utilizzato per indicare il tempo di debug: si accende per indicare l'inizio del debug e si spegne per indicarne la fine.

Quando GP15 emette un livello alto, il transistor S8050 (NPN) conduce e il cicalino passivo inizia a suonare.

Quando la luce è più intensa, il valore di GP28 è più piccolo; viceversa, è più grande quando la luce è più debole.
Programmando il valore del fotoresistore per influenzare la frequenza del cicalino passivo, è possibile simulare un dispositivo fotosensibile.

**Collegamenti**

|wiring_light_theremin|


**Codice**

.. note::

    * Apri il file ``7.1_light_theremin.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # Initialize LED, photoresistor, and buzzer
    led = machine.Pin(16, machine.Pin.OUT)  # LED on pin 16
    photoresistor = machine.ADC(28)  # Photoresistor on ADC pin 28
    buzzer = machine.PWM(machine.Pin(15))  # Buzzer on pin 15 with PWM

    # Variables to store the highest and lowest light readings for calibration
    light_low = 65535 
    light_high = 0 

    # Function to map one range of values to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Function to play a tone on the buzzer at a specified frequency for a set duration
    def tone(pin, frequency, duration):
        pin.freq(frequency)  # Set buzzer frequency
        pin.duty_u16(30000)  # Set duty cycle to around 50%
        utime.sleep_ms(duration)  # Play the tone for the specified duration
        pin.duty_u16(0)  # Turn off the tone by setting duty cycle to 0

    # Calibrate the photoresistor by finding the highest and lowest light values over 5 seconds
    timer_init_start = utime.ticks_ms()  # Get the current time (start time)
    led.value(1)  # Turn on LED to indicate calibration is in progress
    while utime.ticks_diff(utime.ticks_ms(), timer_init_start) < 5000:  # Run calibration for 5 seconds
        light_value = photoresistor.read_u16()  # Read the light value from the photoresistor
        if light_value > light_high:  # Track the maximum light value
            light_high = light_value
        if light_value < light_low:  # Track the minimum light value
            light_low = light_value
    led.value(0)  # Turn off the LED after calibration

    # Main loop to read light levels and play corresponding tones
    while True:
        light_value = photoresistor.read_u16()  # Read the current light value from the photoresistor
        pitch = int(interval_mapping(light_value, light_low, light_high, 50, 6000))  # Map light value to a pitch range
        if pitch > 50:  # Only play tones if the pitch is above a minimum threshold
            tone(buzzer, pitch, 20)  # Play the corresponding pitch for 20ms
        utime.sleep_ms(10)  # Small delay between readings



Non appena il programma viene eseguito, il LED si accenderà e avrai cinque secondi per calibrare l'intervallo di rilevamento del fotoresistore.

Questo è dovuto ai diversi ambienti luminosi in cui potremmo trovarci quando lo utilizziamo (ad esempio, diverse intensità luminose a mezzogiorno e al crepuscolo), nonché all'altezza della nostra mano sopra il fotoresistore. È necessario impostare l'altezza massima e minima della tua mano dal fotoresistore, che è anche l'altezza alla quale suonerai lo strumento.

Dopo cinque secondi, il LED si spegnerà e potrai muovere le mani sopra il fotoresistore e suonare.
