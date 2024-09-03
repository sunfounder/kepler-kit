.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_resistor:

Resistenza
=============

|img_res|

Una resistenza è un elemento elettronico che può limitare la corrente in un ramo di un circuito. 
Una resistenza fissa è un tipo di resistenza il cui valore non può essere modificato, mentre quello di un potenziometro o di una resistenza variabile può essere regolato.

Ecco due simboli comunemente utilizzati per rappresentare una resistenza nei circuiti. Normalmente, il valore della resistenza è indicato su di essa. Quindi, se vedi questi simboli in un circuito, essi rappresentano una resistenza.

|img_res_symbol|

**Ω** è l'unità di misura della resistenza e le unità maggiori includono KΩ, MΩ, ecc. 
La loro relazione è mostrata di seguito: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Normalmente, il valore della resistenza è indicato su di essa.

Quando si utilizza una resistenza, è importante conoscerne il valore. Ecco due metodi: puoi osservare le bande colorate sulla resistenza o utilizzare un multimetro per misurare la resistenza. È consigliato il primo metodo, poiché è più conveniente e veloce.

|img_res_card|

Come mostrato nella scheda, ogni colore rappresenta un numero.

.. list-table::

   * - Nero
     - Marrone
     - Rosso
     - Arancione
     - Giallo
     - Verde
     - Blu
     - Viola
     - Grigio
     - Bianco
     - Oro
     - Argento
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0,1
     - 0,01

Le resistenze a 4 e 5 bande sono frequentemente utilizzate, con 4 o 5 bande colorate. 

Normalmente, quando prendi una resistenza, potresti avere difficoltà a decidere da quale estremità iniziare a leggere i colori. 
Il trucco è che lo spazio tra la quarta e la quinta banda è generalmente più ampio.

Pertanto, puoi osservare lo spazio tra due bande colorate a un'estremità della resistenza; 
se è più grande rispetto agli altri spazi tra le bande, puoi iniziare a leggere dal lato opposto.

Vediamo come leggere il valore di resistenza di una resistenza a 5 bande come mostrato di seguito.

|img_220ohm|

Quindi, per questa resistenza, il valore deve essere letto da sinistra a destra. 
Il valore dovrebbe essere nel seguente formato: 1a Banda 2a Banda 3a Banda x 10^Moltiplicatore (Ω) e la tolleranza ammessa è ± Tolleranza%. 
Pertanto, il valore di resistenza di questa resistenza è 2(rosso) 2(rosso) 0(nero) x 10^0(nero) Ω = 220 Ω, 
e la tolleranza ammessa è ± 1% (marrone).

.. list-table:: Banda dei colori delle resistenze comuni
    :header-rows: 1

    * - :ref:`cpn_resistor` 
      - Banda dei colori  
    * - 10Ω   
      - marrone nero nero argento marrone
    * - 100Ω   
      - marrone nero nero nero marrone
    * - 220Ω 
      - rosso rosso nero nero marrone
    * - 330Ω 
      - arancione arancione nero nero marrone
    * - 1kΩ 
      - marrone nero nero marrone marrone
    * - 2kΩ 
      - rosso nero nero marrone marrone
    * - 5.1kΩ 
      - verde marrone nero marrone marrone
    * - 10kΩ 
      - marrone nero nero rosso marrone 
    * - 100kΩ 
      - marrone nero nero arancione marrone 
    * - 1MΩ 
      - marrone nero nero verde marrone 

Puoi saperne di più sulle resistenze su Wiki: `Resistor - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.
