.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_pir:

Modulo Sensore di Movimento PIR
==================================

|img_pir|

Il sensore PIR rileva la radiazione di calore infrarosso, che può essere utilizzata per rilevare la presenza di organismi che emettono radiazione di calore infrarosso.

Il sensore PIR è diviso in due slot collegati a un amplificatore differenziale. Quando un oggetto stazionario si trova davanti al sensore, i due slot ricevono la stessa quantità di radiazione e l'uscita è zero. Quando un oggetto in movimento si trova davanti al sensore, uno degli slot riceve più radiazione rispetto all'altro, causando fluttuazioni nell'uscita, alta o bassa. Questo cambiamento nella tensione di uscita è il risultato del rilevamento del movimento.

|img_PIR_working_principle|

Dopo che il modulo di rilevamento è stato cablato, c'è un'inizializzazione di un minuto. Durante l'inizializzazione, il modulo emetterà segnali 0~3 volte a intervalli. Successivamente, il modulo entrerà in modalità standby. Si prega di mantenere lontane dalla superficie del modulo le sorgenti di luce e altre fonti di interferenza per evitare malfunzionamenti causati dal segnale di interferenza. Sarebbe meglio utilizzare il modulo in assenza di vento, poiché anche il vento può interferire con il sensore.

|img_pir_back|

**Regolazione della Distanza**

Ruotando il pomello del potenziometro di regolazione della distanza in senso orario, il raggio di rilevamento aumenta, e il raggio massimo di rilevamento è di circa 0-7 metri. Se lo si ruota in senso antiorario, il raggio di rilevamento diminuisce, con un minimo di circa 0-3 metri.

**Regolazione del Ritardo**

Ruotando il pomello del potenziometro di regolazione del ritardo in senso orario, si può aumentare il ritardo di rilevamento. Il ritardo massimo di rilevamento può arrivare fino a 300s. Al contrario, ruotandolo in senso antiorario, è possibile ridurre il ritardo fino a un minimo di 5s.

**Due Modalità di Attivazione**

È possibile scegliere diverse modalità utilizzando il ponticello.

* **H**: Modalità di attivazione ripetibile, dopo aver rilevato il corpo umano, il modulo emette un livello alto. Durante il successivo periodo di ritardo, se qualcuno entra nel raggio di rilevamento, l'uscita rimarrà al livello alto.
* **L**: Modalità di attivazione non ripetibile, emette un livello alto quando rileva il corpo umano. Dopo il ritardo, l'uscita passerà automaticamente da livello alto a livello basso.

.. Esempio 
.. -------------------

.. :ref:`Intruder Alarm`


**Esempio**

* :ref:`py_pir` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`ar_pir` (For Arduino User)
* :ref:`per_lucky_cat` (For Piper Make User)