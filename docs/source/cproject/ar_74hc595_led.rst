.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_74hc_led:

5.1 Microchip - 74HC595
=============================

Un circuito integrato (integrated circuit) è un dispositivo elettronico miniaturizzato, rappresentato dalla sigla "IC" nel circuito.

Attraverso un certo processo, i transistor, i resistori, i condensatori, gli induttori e altri componenti e cablaggi necessari in un circuito vengono interconnessi, fabbricati su una o più piccole piastre semiconduttrici o substrati dielettrici, e successivamente racchiusi in un package, diventando una microstruttura con le funzioni del circuito richieste; tutti i componenti sono stati strutturati come un tutt'uno, portando i componenti elettronici verso la micro-miniaturizzazione, il basso consumo energetico, l'intelligenza e l'alta affidabilità.

Gli inventori dei circuiti integrati sono Jack Kilby (circuiti integrati basati sul germanio (Ge)) e Robert Norton Noyce (circuiti integrati basati sul silicio (Si)).

Questo kit è dotato di un IC, il 74HC595, che consente di risparmiare notevolmente l'uso dei pin GPIO.
In particolare, può sostituire 8 pin per l'uscita del segnale digitale scrivendo un numero binario a 8 bit.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`74HC595`

**Componenti Necessari**

In questo progetto, ci servono i seguenti componenti.

È sicuramente conveniente acquistare un intero kit, ecco il link:

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
        - :ref:`cpn_resistor`
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schema Elettrico**

|sch_74hc_led|

* Quando MR (pin10) è a livello alto e OE (pin13) è a livello basso, i dati vengono inseriti nel fronte di salita di SHcp e passano al registro di memoria attraverso il fronte di salita di SHcp. 
* Se i due clock sono collegati insieme, il registro a scorrimento è sempre un impulso prima rispetto al registro di memoria. 
* Nel registro di memoria sono presenti un pin di ingresso seriale (Ds), un pin di uscita seriale (Q) e un pulsante di reset asincrono (a livello basso). 
* Il registro di memoria emette un bus parallelo a 8 bit e in tre stati. 
* Quando OE è abilitato (livello basso), i dati nel registro di memoria vengono emessi sul bus (Q0 ~ Q7).


**Cablaggio**


|wiring_74hc_led|

**Codice**


.. note::

   * Puoi aprire il file ``5.1_microchip_74hc595.ino`` nel percorso ``kepler-kit-main/arduino/5.1_microchip_74hc595``.
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71854882-0c1b-4d09-b3e7-5ef7272f7293/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



Quando il programma è in esecuzione, potrai vedere i LED accendersi uno dopo l'altro.

**Come funziona?**

Dichiara un array, memorizza diversi numeri binari a 8 bit utilizzati per modificare lo stato di funzionamento degli otto LED controllati dal 74HC595.

.. code-block:: arduino

    int datArray[] = {0b00000000, 0b00000001, 0b00000011, 0b00000111, 0b00001111, 0b00011111, 0b00111111, 0b01111111, 0b11111111};

Imposta ``STcp`` a livello basso prima e poi a livello alto. Questo genererà un impulso di salita di ``STcp``.

.. code-block:: arduino

    digitalWrite(STcp,LOW); 

``shiftOut()`` viene utilizzato per spostare un byte di dati un bit alla volta, il che significa trasferire un byte di dati in datArray[num] al registro a scorrimento con il pin DS. MSBFIRST significa spostare a partire dai bit più alti.

.. code-block:: arduino

    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);

Dopo aver eseguito ``digitalWrite(STcp,HIGH)``, il STcp sarà al fronte di salita. A questo punto, i dati nel registro a scorrimento verranno trasferiti al registro di memoria.

.. code-block:: arduino

    digitalWrite(STcp,HIGH);

Un byte di dati verrà trasferito nel registro di memoria dopo 8 volte. Successivamente, i dati del registro di memoria vengono emessi sul bus (Q0-Q7). Ad esempio, shiftout ``B00000001`` accenderà il LED controllato da Q0 e spegnerà i LED controllati da Q1~Q7.

