.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_74hc_4dig:

5.3 Contatore di Tempo
================================

Il display a 7 segmenti a 4 cifre è composto da quattro display a 7 
segmenti che lavorano insieme.

Ogni display a 7 segmenti a 4 cifre funziona indipendentemente. Utilizza 
il principio della persistenza della visione umana per mostrare rapidamente 
i caratteri di ciascun segmento in un ciclo, formando stringhe continue.

Ad esempio, quando sul display appare "1234", viene visualizzato "1" sul 
primo segmento, mentre "234" non è visibile. Dopo un certo periodo di tempo, 
il secondo segmento mostra "2", mentre il 1°, il 3° e il 4° segmento non 
visualizzano nulla, e così via. I quattro display digitali si alternano 
rapidamente. Questo processo è molto breve (tipicamente 5 ms) e, grazie 
all'effetto del post-lume ottico e al principio della persistenza della 
visione, possiamo vedere i quattro caratteri contemporaneamente.

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
        - :ref:`cpn_resistor`
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schema**

|sch_4dig|

Qui il principio di cablaggio è fondamentalmente lo stesso di :ref:`py_74hc_led`, l'unica differenza è che Q0-Q7 sono collegati ai pin da a ~ g del display a 7 segmenti a 4 cifre.

Successivamente, G10 ~ G13 selezioneranno quale display a 7 segmenti attivare.

**Cablaggio**

|wiring_4dig|

**Codice**

.. note::

    * Apri il file ``5.3_time_counter.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()
        time.sleep_us(200)

    while True:
        count = timer1()
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])     

Dopo aver eseguito il programma, vedrai il display a 7 segmenti a 4 cifre trasformarsi in un contatore e il numero aumenterà di 1 ogni secondo.

**Come Funziona?**

L'invio di segnali a ciascun display a 7 segmenti viene effettuato nello stesso modo descritto in :ref:`py_74hc_7seg`, utilizzando la funzione ``hc595_shift()``.
Il punto centrale del display a 7 segmenti a 4 cifre è attivare selettivamente ciascun display a 7 segmenti. Il codice associato è il seguente.

.. code-block:: python

    placePin = []
    pin = [13,12,11,10]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    while True:
        
        hc595_shift(SEGCODE[count%10])
        pickDigit(0)

        hc595_shift(SEGCODE[count%100//10])
        pickDigit(1)
        
        hc595_shift(SEGCODE[count%1000//100])
        pickDigit(2)    
        
        hc595_shift(SEGCODE[count%10000//1000])
        pickDigit(3)   

Qui, quattro pin (GP10, GP11, GP12, GP13) vengono utilizzati per controllare ciascun segmento del display a 7 segmenti a 4 cifre individualmente.
Quando lo stato di questi pin è ``0``, il display a 7 segmenti corrispondente è attivo; quando lo stato è ``1``, il contrario.

La funzione ``pickDigit(digit)`` viene utilizzata per disabilitare tutti e quattro i segmenti e quindi abilitare un determinato segmento individualmente.
Dopo di che, ``hc595_shift()`` viene utilizzato per scrivere il codice di 8 bit corrispondente per il display a 7 segmenti.

Il display a 7 segmenti a 4 cifre deve essere continuamente attivato a turno in modo che possiamo vedere i quattro segmenti visualizzare, il che significa che il programma principale non può facilmente aggiungere codice che influenzi il timing.
Tuttavia, dobbiamo aggiungere una funzione di temporizzazione a questo esempio e, se aggiungiamo un ``sleep(1)``, ci renderemo conto che ha quattro cifre.
Vedremo attraverso l'illusione del display a 7 segmenti a 4 cifre che funziona contemporaneamente, rivelando il fatto che solo un segmento del display è illuminato alla volta.
Utilizzando la funzione ``time.ticks_ms()`` nella libreria ``time`` è un ottimo modo per farlo.

.. code-block:: python

    import time

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    while True:
        count = timer1()


La funzione ``time.ticks_ms()`` ottiene un tempo (non esplicito), e registriamo il primo valore di tempo ottenuto come ``timerStart``.
Successivamente, quando è necessario il tempo, la funzione ``time.ticks_ms()`` viene chiamata di nuovo e il valore viene sottratto da ``timerStart`` per ottenere quanto tempo il programma è stato in esecuzione (in millisecondi).

Infine, converti e visualizza questo valore temporale sul display a 7 segmenti a 4 cifre ed è fatto.

* `Time - MicroPython Docs <https://docs.micropython.org/en/latest/library/time.html>`_