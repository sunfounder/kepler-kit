.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_pir:

2.10 Rilevamento del Movimento Umano
========================================

Il sensore a infrarossi passivo (sensore PIR) è un sensore comune che 
può misurare la luce infrarossa (IR) emessa dagli oggetti nel suo campo 
visivo. In parole semplici, rileva la radiazione infrarossa emessa dal 
corpo, permettendo di rilevare il movimento di persone e altri animali. 
Più specificamente, comunica alla scheda di controllo principale che 
qualcuno è entrato nella tua stanza.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Schema Elettrico**

|sch_pir|

Quando il modulo PIR rileva una persona di passaggio, il pin GP14 diventerà alto, altrimenti rimarrà basso.

.. note::
    Il modulo PIR ha due potenziometri: uno regola la sensibilità, l'altro la distanza di rilevamento. Per far funzionare al meglio il modulo PIR, è necessario ruotarli entrambi completamente in senso antiorario.

    |img_PIR_TTE|

**Collegamenti**

|wiring_pir|

**Codice**

.. note::

    * Apri il file ``2.10_detect_human_movement.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Somebody here!")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

Dopo l'esecuzione del programma, se il modulo PIR rileva qualcuno nelle vicinanze, la Shell stamperà "Qualcuno è qui!"

**Per Saperne di Più**

Il PIR è un sensore molto sensibile. Per adattarlo all'ambiente di utilizzo, è necessario regolarlo. Con la parte con i 2 potenziometri rivolta verso di te, ruota entrambi i potenziometri completamente in senso antiorario e inserisci il cappuccio del ponticello sul pin con la L e il pin centrale.


.. note::

    * Apri il file ``2.10_pir_adjustment.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

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

Analizziamo il metodo di regolazione insieme ai risultati sperimentali.

|img_pir_back|

1. Modalità di Attivazione

    Osserviamo i pin con il cappuccio del ponticello nell'angolo.
    Permette al PIR di entrare in modalità di attivazione ripetibile o non ripetibile.

    Attualmente, il nostro cappuccio del ponticello collega il Pin centrale e il Pin L, il che rende il PIR in modalità di attivazione non ripetibile.
    In questa modalità, quando il PIR rileva il movimento dell'organismo, invierà un segnale di livello alto per circa 2,8 secondi alla scheda di controllo principale.
    Possiamo vedere nei dati stampati che la durata del lavoro sarà sempre intorno ai 2800 ms.

    Successivamente, modifichiamo la posizione del cappuccio del ponticello inferiore e lo colleghiamo al Pin centrale e al Pin H per mettere il PIR in modalità di attivazione ripetibile.
    In questa modalità, quando il PIR rileva il movimento dell'organismo (nota che si tratta di movimento, non di stasi davanti al sensore), fintanto che l'organismo continua a muoversi entro il raggio di rilevamento, il PIR continuerà a inviare un segnale di livello alto alla scheda di controllo principale.
    Possiamo vedere nei dati stampati che la durata del lavoro è un valore incerto.

#. Regolazione del Ritardo

    Il potenziometro a sinistra serve per regolare l'intervallo tra due operazioni.
    
    Attualmente, lo ruotiamo completamente in senso antiorario, il che fa sì che il PIR necessiti di un tempo di sospensione di circa 5 secondi dopo aver terminato l'invio del lavoro ad alto livello. Durante questo tempo, il PIR non rileverà più la radiazione infrarossa nell'area target.
    Possiamo vedere nei dati stampati che la durata della dormienza non è mai inferiore a 5000 ms.

    Se ruotiamo il potenziometro in senso orario, anche il tempo di sospensione aumenterà. Quando viene ruotato completamente in senso orario, il tempo di sospensione sarà fino a 300s.

#. Regolazione della Distanza

    Il potenziometro centrale serve per regolare il raggio di rilevamento del PIR.

    Ruota la manopola del potenziometro di regolazione della distanza **in senso orario** per aumentare il raggio di rilevamento, e il raggio massimo di rilevamento è di circa 0-7 metri.
    Se ruota **in senso antiorario**, il raggio di rilevamento diminuisce, e il raggio minimo di rilevamento è di circa 0-3 metri.
