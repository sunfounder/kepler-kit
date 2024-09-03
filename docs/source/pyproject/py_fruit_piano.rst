.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_fruit_piano:

7.9 Pianoforte con la Frutta
================================


La conduttività elettrica si trova in molti oggetti metallici, così come nel corpo umano e nella frutta.
Questa proprietà può essere sfruttata per creare un progetto divertente: un pianoforte fatto con la frutta.
In altre parole, trasformiamo la frutta in tastiere che possono suonare musica semplicemente toccandole.

|fruit_piano|

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schema**

|sch_fruit_piano| 

Per trasformare la frutta in un tasto di pianoforte, è necessario collegare gli elettrodi dell'MPR121 alla frutta (ad esempio, inserendo l'elettrodo nel manico della banana).

All'inizio, l'MPR121 si inizializza e ogni elettrodo ottiene un valore basato sulla carica corrente; quando un conduttore (come il corpo umano) tocca un elettrodo, la carica si sposta e si riequilibra.
Di conseguenza, il valore dell'elettrodo cambia rispetto al valore iniziale, segnalando alla scheda di controllo principale che è stato toccato.
Durante questo processo, assicurati che il cablaggio di ciascun elettrodo sia stabile in modo che la carica sia bilanciata durante l'inizializzazione.


**Cablaggio**


|wiring_fruit_piano| 


**Codice**


.. note::

    * Apri il file ``7.9_fruit_piano.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`. 
    
    * Qui devi usare la libreria chiamata ``mpr121.py``, verifica se è stata caricata su Pico W; per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time
    import urandom

    # mpr121
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)


    # buzzer
    NOTE_A3 = 220
    NOTE_B3 = 247
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523
    NOTE_D5 = 587
    NOTE_E5 = 659

    buzzer = machine.PWM(machine.Pin(15))
    note = [NOTE_A3,NOTE_B3,NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5,NOTE_D5,NOTE_E5]

    def tone(pin,frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def noTone(pin):
        pin.duty_u16(0)


    # rgb led
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(12))
    blue = machine.PWM(machine.Pin(11))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


    def lightup():
        red.duty_u16(int(urandom.uniform(0, 65535)))
        green.duty_u16(int(urandom.uniform(0, 65535)))
        blue.duty_u16(int(urandom.uniform(0, 65535)))


    def dark():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)    

    # main project
    lastState=mpr.get_all_states()
    touchMills=time.ticks_ms()
    beat=500

    while True:
        currentState=mpr.get_all_states()
        if currentState != lastState:
            for i in range(12):
                if i in list(currentState) and not i in list(lastState):
                    tone(buzzer,note[i])
                    lightup()
                    touchMills=time.ticks_ms()
        if time.ticks_diff(time.ticks_ms(),touchMills)>=beat or len(currentState) == 0:
            noTone(buzzer)
            dark()
        lastState = currentState

Non toccare la frutta prima che il programma sia in esecuzione per evitare di ottenere un riferimento non corretto durante l'inizializzazione.
Dopo l'avvio del programma, tocca delicatamente la frutta, il buzzer emetterà il tono corrispondente e la luce RGB lampeggerà una volta in modo casuale.
