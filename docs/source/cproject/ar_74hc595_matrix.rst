.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_74hc_788bs:

5.4 - Grafica a 8x8 Pixel
=============================

La matrice LED è un display a matrice di punti a bassa risoluzione. Utilizza una griglia di diodi emettitori di luce come pixel per visualizzare schemi.

Sono abbastanza luminosi da essere visibili alla luce solare esterna, e puoi vederli in alcuni negozi, cartelloni pubblicitari, insegne e display a messaggi variabili (come quelli sui veicoli del trasporto pubblico).

In questo kit è utilizzata una matrice di punti 8x8 con 16 pin. Gli anodi sono collegati in righe e i catodi sono collegati in colonne (a livello di circuito), il che consente di controllare questi 64 LED.

Per accendere il primo LED, è necessario fornire un livello alto per la Riga 1 e un livello basso per la Colonna 1. Per accendere il secondo LED, è necessario fornire un livello alto per la Riga 1 e un livello basso per la Colonna 2, e così via.
Controllando la corrente attraverso ciascuna coppia di righe e colonne, è possibile controllare individualmente ciascun LED per visualizzare caratteri o immagini.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Schema Elettrico**

|sch_ledmatrix|

La matrice di punti 8x8 è controllata da due chip 74HC595, uno per le righe e uno per le colonne, mentre questi due chip condividono G18~G20, il che consente di risparmiare notevolmente i pin I/O della scheda Pico W.

Pico W deve emettere un numero binario a 16 bit alla volta, i primi 8 bit sono inviati al 74HC595 che controlla le righe e gli ultimi 8 bit sono inviati al 74HC595 che controlla le colonne, in modo che la matrice di punti possa visualizzare un modello specifico.

Q7': Pin di uscita in serie, collegato a DS di un altro 74HC595 per collegare più 74HC595 in serie.

**Cablaggio**

Costruisci il circuito. Poiché il cablaggio è complicato, procediamo
passo dopo passo.

**Passo 1:**  Per prima cosa, inserisci il Pico W, la matrice LED
e due chip 74HC595 nella breadboard. Collega il 3.3V e il GND del
Pico W ai fori sui due lati della scheda, quindi collega i pin 16 e
10 dei due chip 74HC595 a VCC, il pin 13 e il pin 8 a GND.

.. note::
   Nell'immagine Fritzing sopra, il lato con l'etichetta è in basso.

|wiring_ledmatrix_4|

**Passo 2:** Collega il pin 11 dei due chip 74HC595 insieme, e poi a
GP20; poi il pin 12 dei due chip, e a GP19; infine, il pin 14 del
74HC595 sul lato sinistro a GP18 e il pin 9 a pin 14 del secondo
74HC595.

|wiring_ledmatrix_3|

**Passo 3:** Il 74HC595 sul lato destro controlla le colonne della
matrice LED. Consulta la tabella sottostante per la mappatura. Pertanto, i pin Q0-Q7
del 74HC595 sono mappati rispettivamente ai pin 13, 3, 4, 10, 6, 11, 15 e 16.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Passo 4:** Ora collega le righe della matrice LED. Il 74HC595 sul
lato sinistro controlla le righe della matrice LED. Consulta la tabella 
sottostante per la
mappatura. Possiamo vedere che i pin Q0-Q7 del 74HC595 sul lato sinistro 
sono mappati rispettivamente ai pin 9, 14, 8, 12, 1, 7, 2 e 5.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Codice**

.. note::

    * Puoi aprire il file ``5.4_8x8_pixel_graphics.ino`` nel percorso ``kepler-kit-main/arduino/5.4_8x8_pixel_graphics``.
    * Oppure copia questo codice nell'**Arduino IDE**.


    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3682592-17d4-4690-a730-1c0a6fcbd353/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



Una volta avviato il programma, vedrai un grafico a forma di **x** visualizzato sulla matrice di punti 8x8.



**Come funziona?**

Qui utilizziamo due 74HC595 per fornire segnali alle righe e alle colonne della matrice.
Il metodo di fornitura dei segnali è lo stesso di ``shiftOut()`` nei capitoli precedenti, tranne per il fatto che qui dobbiamo scrivere un numero binario a 16 bit alla volta.

Il ciclo principale chiama ``shiftOut()`` due volte, scrive due numeri binari a 8 bit e poi li invia al bus, in modo che un motivo possa essere visualizzato.

Tuttavia, poiché i LED nella matrice di punti utilizzano poli comuni, controllare più righe/colonne contemporaneamente creerà interferenze reciproche (ad esempio, se (1,1) e (2,2) sono accesi contemporaneamente, anche (1,2) e (2,1) si illumineranno inevitabilmente insieme).
Pertanto, è necessario attivare una colonna (o una riga) alla volta, ciclando 8 volte, e utilizzare il principio dell'immagine residua per far sì che l'occhio umano fonda 8 schemi, in modo da ottenere un'immagine contenente 8x8 informazioni.



.. code-block:: arduino

   for(int num = 0; num <=8; num++)
   {
      digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
      shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
      shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
      //return the latch pin high to signal chip that it 
      //no longer needs to listen for information
      digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
   }

In questo esempio, la funzione principale annida un ciclo ``for``, e quando ``i`` è 1, viene attivata solo la prima riga (il chip nel controllo della riga ottiene il valore ``0x80``) e viene scritta l'immagine della prima riga.
Quando ``i`` è 2, viene attivata la seconda riga (il chip nel controllo della riga ottiene il valore ``0x40``) e viene scritta l'immagine della seconda riga. E così via, completando 8 uscite.

A proposito, come per il display a 7 segmenti a 4 cifre, è necessario mantenere la frequenza di aggiornamento per evitare lo sfarfallio percepito dall'occhio umano, quindi è consigliabile evitare di utilizzare ``sleep()`` nel ciclo principale.


**Approfondimenti**

Prova a sostituire ``datArray`` con il seguente array e vedi quali immagini appaiono!

.. code-block:: arduino

   int datArray1[] = {0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF};
   int datArray2[] = {0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF};
   int datArray3[] = {0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF};
   int datArray4[] = {0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF};
   int datArray5[] = {0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF};
   int datArray6[] = {0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF};

Oppure, prova a disegnare le tue grafiche.
