.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Lezione 5: Leggere Tensioni Analogiche Utilizzando un Potenziometro
======================================================================

Questo tutorial copre la lettura delle tensioni analogiche utilizzando il SunFounder Kepler Kit per Raspberry Pi Pico W:

* **Lettura della Tensione Analogica**: Spiega l'importanza di leggere le tensioni analogiche per vari input da sensori e input utente, come i potenziometri, per controllare aspetti come il volume o la luminosità.

* **Schema di Collegamento e Configurazione**: Fornisce una spiegazione dettagliata del funzionamento del potenziometro e di come collegarlo al Pico W. Descrive la configurazione delle linee di massa e dei 3,3V e il collegamento del pin centrale del potenziometro al pin GPIO 28.

* **Spiegazione del Codice**: Descrive la scrittura del codice Python per leggere le tensioni analogiche. Copre l'importazione delle librerie necessarie, la configurazione dei pin GPIO, la creazione di un oggetto per il potenziometro e l'utilizzo di un ciclo while per leggere e stampare continuamente i valori di tensione.

* **Conversione Matematica**: Insegna come convertire i valori grezzi dell'ADC (da 0 a 65535) in valori di tensione reali (da 0 a 3,3V) utilizzando equazioni lineari. Dimostra il processo di derivazione dell'equazione della retta da due punti noti e la sua applicazione nel codice.

* **Dimostrazione Pratica**: Mostra il codice in azione, leggendo e convertendo i valori del potenziometro in tensione e visualizzandoli. Discute l'accuratezza e i risultati attesi durante la regolazione del potenziometro.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ODWwErH_iGA?si=EzLxy17TO462G6_r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

