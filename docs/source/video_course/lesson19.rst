.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 19: Controllo di un LED RGB con Pulsanti in Micropython
=============================================================================

Questo tutorial spiega come utilizzare più pulsanti per controllare i canali RGB di un LED sul Raspberry Pi Pico W:

* **Introduzione**: La lezione inizia con una panoramica, concentrandosi sull'uso di tre pulsanti per controllare i canali rosso, verde e blu di un LED RGB sul Raspberry Pi Pico W.
* **Soluzione del Compito**: Fornisce una soluzione al compito della lezione precedente, che prevedeva la creazione di tre interruttori a levetta per un LED RGB utilizzando pulsanti.
* **Configurazione del Circuito**: Mostra il cablaggio di tre pulsanti e di un LED RGB al Raspberry Pi Pico W. Ogni pulsante è collegato a un pin GPIO, e i canali del LED RGB sono collegati tramite resistori a pin GPIO separati. Viene stabilita una linea di massa per completare il circuito.
* **Spiegazione del Codice**: 
 - Inizializza i pin GPIO per il LED RGB e i pulsanti.
 - Crea oggetti per ogni canale del LED e per i pulsanti, impostandoli come ingressi o uscite a seconda delle necessità.
 - Definisce variabili per gli stati dei pulsanti e degli LED.
 - Implementa la logica per alternare i canali del LED in base alla pressione e al rilascio dei pulsanti.
 - Dimostra come scrivere e organizzare il codice in modo metodico, garantendo una denominazione coerente delle variabili per una maggiore leggibilità e facilità di debug.
* **Dimostrazione Pratica**: 
 - Fornisce una dimostrazione passo dopo passo dell'esecuzione del codice, premendo i pulsanti e osservando i cambiamenti nei canali del LED RGB.
 - Mostra come testare la funzionalità dei pulsanti e verificare che ciascun pulsante alterni correttamente il proprio canale LED.
 - Discute le tecniche di debug per identificare e correggere errori nel codice o nel circuito.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3CiBd7sW5KE?si=I66ycByUwVMi8251" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

