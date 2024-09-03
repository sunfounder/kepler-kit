.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 18: Controllo di un LED con un Pulsante in Micropython
=============================================================================

Questo tutorial spiega come utilizzare i pulsanti per accendere e spegnere un LED con il Raspberry Pi Pico W:

* **Introduzione**: La lezione inizia con una breve introduzione e una panoramica dell'argomento, concentrandosi sull'uso dei pulsanti per controllare i LED sul Raspberry Pi Pico W.
* **Soluzione del Compito**: Fornisce una soluzione al compito della lezione precedente, che prevedeva la creazione di un interruttore a levetta per un LED utilizzando un pulsante.
* **Configurazione del Circuito**: Mostra il cablaggio di un pulsante al pin GPIO 14 e di un LED al pin GPIO 15 sul Raspberry Pi Pico W. Include il collegamento del pulsante e del LED a una massa comune.
* **Logica dell'Interruttore a Levetta**: Spiega la logica necessaria per alternare lo stato del LED ad ogni pressione e rilascio del pulsante. Introduce i concetti di `stato attuale del pulsante`, `stato precedente del pulsante` e `stato del LED`.
* **Spiegazione del Codice**: Inizializza i pin GPIO per il LED e il pulsante. Utilizza un ciclo while per leggere continuamente lo stato del pulsante. Alterna lo stato del LED in base alle azioni di pressione e rilascio del pulsante. Include istruzioni print per il debug e la verifica degli stati.
* **Dimostrazione Pratica**: Fornisce una dimostrazione passo dopo passo dell'esecuzione del codice, premendo il pulsante e osservando i cambiamenti nello stato del LED.
* **Compito a Casa**: Assegna un nuovo progetto per utilizzare più pulsanti per controllare i colori di un LED RGB. Il compito consiste nello scrivere un programma in cui premendo i pulsanti rosso, verde o blu si cambia il colore del LED RGB di conseguenza.
* **Prossimi Passi**: Annuncia che le lezioni future continueranno a esplorare l'uso dei pulsanti e dei LED, concentrandosi sull'integrazione di questi componenti in progetti più complessi.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/oztHWvrhKNk?si=I83VoID3AKSCUr9x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

