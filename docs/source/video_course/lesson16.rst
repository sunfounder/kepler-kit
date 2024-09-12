.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e a contenuti esclusivi.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 16: Sequenza di Colori in LED RGB con Micropython
=============================================================================

Questo tutorial tratta l'uso dei cicli for in MicroPython con il Raspberry Pi Pico W per controllare un LED RGB:

* **Introduzione**: La Lezione inizia con una breve introduzione e una panoramica, concentrandosi sull'uso dei cicli for e della modulazione di larghezza di impulso (PWM) per controllare la luminosità e il colore di un LED RGB.
* **Configurazione del Circuito**: Mostra il cablaggio del LED RGB al Raspberry Pi Pico W, utilizzando i pin GPIO 13, 14 e 15 rispettivamente per i canali rosso, verde e blu. Sottolinea l'importanza di utilizzare resistori di limitazione della corrente da 330 Ohm.
* **Configurazione PWM**: Spiega come impostare i canali PWM per ciascun colore del LED, stabilendo una frequenza di 1000 Hz per garantire transizioni fluide senza sfarfallii visibili.
* **Inserimento della Sequenza di Colori**: Mostra come richiedere all'utente una sequenza di colori e catturare l'input. Utilizza un ciclo for per memorizzare i colori definiti dall'utente in un array, assicurandosi che l'input venga convertito in minuscolo per coerenza.
* **Logica di Controllo dei Colori**: Dettaglia la logica per impostare la luminosità di ciascun colore del LED in base all'input dell'utente. Implementa istruzioni if per assegnare i valori PWM per creare diversi colori, tra cui rosso, verde, blu, ciano, magenta, giallo, arancione e spento.
* **Ciclo Continuo per Visualizzare i Colori**: Utilizza un ciclo while true per scorrere continuamente la sequenza di colori definita dall'utente. Aggiunge istruzioni sleep per controllare la durata di visualizzazione di ciascun colore.
* **Dimostrazione Pratica**: Fornisce una dimostrazione passo dopo passo dell'esecuzione del codice, inserendo una sequenza di colori e osservando il LED RGB visualizzare i colori nell'ordine specificato.
* **Prossimi Passi**: Annuncia che la prossima Lezione tratterà l'uso dei pulsanti con il Raspberry Pi Pico W per leggere ingressi digitali, completando l'apprendimento dei metodi di input e output prima di passare a componenti più avanzati.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VivNlgYg3wY?si=ECUsRAWanIAShyxk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

