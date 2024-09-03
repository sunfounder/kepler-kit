.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_pir:

2.10 - Rileva il movimento umano
=========================================

Il sensore passivo a infrarossi (sensore PIR) è un sensore comune che può misurare la luce infrarossa (IR) emessa dagli oggetti nel suo campo visivo.
In parole semplici, rileva la radiazione infrarossa emessa dal corpo, permettendo così di rilevare il movimento di persone e altri animali.
Più specificamente, segnala alla scheda di controllo principale che qualcuno è entrato nella tua stanza.

:ref:`cpn_pir`

**Componenti necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK PER L'ACQUISTO
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - INTRODUZIONE COMPONENTE	
        - QUANTITÀ
        - LINK PER L'ACQUISTO

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

**Schema elettrico**

|sch_pir|

Quando il modulo PIR rileva il passaggio di una persona, GP14 sarà alto, altrimenti sarà basso.

**Cablaggio**

|wiring_pir|

**Codice**

.. note::

   * Puoi aprire il file ``2.10_detect_human_movement.ino`` nel percorso ``kepler-kit-main/arduino/2.10_detect_human_movement``. 
   * Oppure copia questo codice nell'**Arduino IDE**.

   
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/bb3ff9f1-127d-4279-84b9-cba28b9667e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    
Dopo l'esecuzione del programma, se il modulo PIR rileva la presenza di qualcuno nelle vicinanze, il Serial Monitor stamperà "Somebody here!" 

**Approfondimenti**

Il PIR è un sensore molto sensibile. Per adattarlo all'ambiente di utilizzo, 
è necessario regolarlo. Con i 2 potenziometri rivolti verso di te, 
ruota entrambi i potenziometri in senso antiorario fino in fondo e inserisci il cappuccio del ponticello sul pin con L e il pin centrale.

|img_pir_back|

1. Modalità di trigger

    Osserviamo i pin con il cappuccio del ponticello nell'angolo.
    Questo permette al PIR di entrare in modalità di trigger ripetibile o non ripetibile.

    Al momento, il nostro cappuccio del ponticello collega il pin centrale e il pin L, il che mette il PIR in modalità di trigger non ripetibile.
    In questa modalità, quando il PIR rileva il movimento dell'organismo, invierà un segnale di alto livello per circa 2,8 secondi alla scheda di controllo principale.
    .. Nei dati stampati possiamo vedere che la durata del lavoro sarà sempre intorno ai 2800 ms.

    Successivamente, modifichiamo la posizione del cappuccio del ponticello inferiore collegandolo al pin centrale e al pin H per mettere il PIR in modalità di trigger ripetibile.
    In questa modalità, quando il PIR rileva il movimento dell'organismo (nota che deve essere movimento, non statico davanti al sensore), finché l'organismo continua a muoversi all'interno dell'area di rilevamento, il PIR continuerà a inviare un segnale di alto livello alla scheda di controllo principale.
    .. Nei dati stampati possiamo vedere che la durata del lavoro è un valore incerto.

#. Regolazione del ritardo

    Il potenziometro a sinistra viene utilizzato per regolare l'intervallo tra due operazioni.

    Attualmente, lo ruotiamo completamente in senso antiorario, il che fa sì che il PIR debba entrare in una fase di riposo di circa 5 secondi dopo aver completato l'invio del segnale di alto livello. Durante questo tempo, il PIR non rileverà più la radiazione infrarossa nell'area target.
    .. Nei dati stampati possiamo vedere che la durata del riposo non è mai inferiore a 5000 ms.

    Se ruotiamo il potenziometro in senso orario, anche il tempo di riposo aumenterà. Quando è ruotato completamente in senso orario, il tempo di riposo sarà fino a 300s.

#. Regolazione della distanza

    Il potenziometro centrale viene utilizzato per regolare il range di rilevamento del PIR.

    Ruota la manopola del potenziometro di regolazione della distanza **in senso orario** per aumentare il range di rilevamento, con un range massimo di circa 0-7 metri.
    Se ruota **in senso antiorario**, il range di rilevamento si riduce, con un range minimo di circa 0-3 metri.
