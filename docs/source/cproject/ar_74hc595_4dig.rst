.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_74hc_4dig:

5.3 - Contatore di Tempo
================================

Il display a 4 cifre e 7 segmenti è costituito da quattro display a 7 segmenti 
che funzionano insieme.

Il display a 4 cifre e 7 segmenti funziona indipendentemente. Utilizza il 
principio della persistenza visiva umana per visualizzare rapidamente i 
caratteri di ciascun segmento in un ciclo, formando stringhe continue.

Ad esempio, quando sul display appare "1234", viene visualizzato "1" sul 
primo segmento, mentre "234" non è visibile. Dopo un breve intervallo, il 
secondo segmento mostra "2", mentre il 1°, 3° e 4° segmento non mostrano 
nulla, e così via, il display a quattro cifre mostra le cifre in sequenza. 
Questo processo è molto rapido (tipicamente 5ms), e grazie all'effetto di 
persistenza ottica e al principio della persistenza visiva, possiamo vedere 
tutte e quattro le cifre contemporaneamente.

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
        - Alcuni
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Schema Elettrico**

|sch_4dig|

Qui il principio di cablaggio è sostanzialmente lo stesso di :ref:`ar_74hc_led`, l'unica differenza è che Q0-Q7 sono collegati ai pin da a a g del display a 4 cifre e 7 segmenti.

Poi G10 ~ G13 selezioneranno quale display a 7 segmenti attivare.

**Cablaggio**


|wiring_4dig|

**Codice**

.. note::

    * Puoi aprire il file ``5.3_time_counter.ino`` nel percorso ``kepler-kit-main/arduino/5.3_time_counter``.
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0e97386e-417e-4f53-a026-5f37e36deba4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo l'esecuzione del programma, vedrai il display a 4 cifre e 7 segmenti diventare un contatore e il numero aumenterà di 1 ogni secondo.


**Come funziona?**

L'invio di segnali a ciascun display a 7 segmenti avviene nello stesso modo di :ref:`ar_74hc_7seg`, utilizzando la funzione ``hc595_shift()``.
Il punto cruciale del display a 4 cifre e 7 segmenti è attivare selettivamente ciascun display a 7 segmenti. Il codice associato è il seguente.

.. code-block:: arduino

    const int placePin[4] = {13,12,11,10}; 

    void setup ()
    {
        for (int i = 0; i<4;i++){
            pinMode(placePin[i],OUTPUT);
        }
    }

    void loop()
    { 
        pickDigit(0);
        hc595_shift(count%10/1);
        
        pickDigit(1);
        hc595_shift(count%100/10);
        
        pickDigit(2);
        hc595_shift(count%1000/100);
        
        pickDigit(3);
        hc595_shift(count%10000/1000);
    }

    void pickDigit(int digit){
        for(int i = 0; i < 4; i++){
            digitalWrite(placePin[i],HIGH);
        }
        digitalWrite(placePin[digit],LOW);
    }

Qui, quattro pin (GP10, GP11, GP12, GP13) vengono utilizzati per controllare ciascun segmento del display a 4 cifre e 7 segmenti individualmente.
Quando lo stato di questi pin è ``LOW``, il display a 7 segmenti corrispondente è attivo; quando lo stato è ``HIGH``, il display a 7 segmenti non funziona.


Qui la funzione ``pickDigit(digit)`` viene utilizzata per disattivare tutti i display a 7 segmenti e poi attivare un determinato segmento singolarmente.
Successivamente, ``hc595_shift()`` viene utilizzato per scrivere il codice di 8 bit corrispondente per il display a 7 segmenti.

Il display a 4 cifre e 7 segmenti deve essere attivato continuamente a turno in modo che possiamo vedere visualizzate tutte e quattro le cifre, il che significa che il programma principale non può facilmente aggiungere codice che influenzi la temporizzazione.

Tuttavia, è necessario aggiungere una funzione di temporizzazione a questo esempio, se aggiungiamo un ``delay (1000)``, potremo rilevare l'illusione dei quattro display a 7 segmenti che funzionano contemporaneamente, esponendo il fatto che solo un display a 7 segmenti alla volta si illumina.

Pertanto, utilizzare la funzione ``millis()`` è un ottimo modo per farlo.

.. code-block:: arduino

    void setup ()
    {
        timerStart = millis();
    }

    void loop()
    {
        unsigned int count = (millis()-timerStart)/1000;
    }

La funzione ``millis()`` ottiene il numero di millisecondi trascorsi dall'inizio del programma corrente. Registriamo il primo valore temporale come ``timerStart``; 

poi, quando dobbiamo ottenere nuovamente il tempo, richiamiamo la funzione ``millis()`` e sottraiamo ``timerStart`` dal valore per ottenere da quanto tempo il programma è in esecuzione.

Infine, converti questo valore temporale e lascia che il display a 4 cifre e 7 segmenti lo mostri.


* `millis() <https://www.arduino.cc/reference/en/language/functions/time/millis/>`_
