.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 20: Utilizzo del Sensore di Temperatura e Umidità DHT11 in MicroPython
======================================================================================

Questo tutorial copre la misurazione di temperatura e umidità utilizzando il sensore DHT11 con il Raspberry Pi Pico W:

* **Introduzione**: Introduce la lezione, focalizzandosi sull'uso del sensore DHT11 per misurare temperatura e umidità.
* **Riepilogo delle Lezioni Precedenti**: Ripassa le competenze fondamentali apprese nelle lezioni precedenti, come scrittura digitale, scrittura analogica con PWM, lettura digitale e lettura analogica.
* **Introduzione ai Componenti**: Introduce il sensore DHT11 dal kit SunFounder Kepler e mostra come trovarlo all'interno del kit.
* **Configurazione del Circuito**:
  - Stabilisce le linee di massa e alimentazione sulla breadboard.
  - Collega il sensore DHT11 al Raspberry Pi Pico W:
    - Il pin 1 del sensore al 3.3V.
    - Il pin 2 del sensore al pin GPIO 16 (pin fisico 21).
    - Il pin 4 del sensore a massa.
* **Spiegazione del Codice**:
  - Importa le librerie necessarie: machine, utime (come time) e DHT.
  - Configura il pin GPIO per l'input dati con una resistenza di pull-down.
  - Inizializza il sensore DHT11.
  - Entra in un ciclo infinito per misurare e stampare continuamente temperatura e umidità.
  - Spiega come formattare l'output stampato per visualizzare temperatura e umidità in una singola linea usando `\r`.
* **Dimostrazione Pratica**:
  - Esegue il codice e osserva le letture di temperatura e umidità in tempo reale.
  - Discute l'importanza di non utilizzare metodi che potrebbero causare condensa sul sensore per testare le variazioni nelle letture.
* **Formattazione dell'Output**:
  - Dimostra come formattare l'output per mostrare la temperatura in gradi Celsius e l'umidità in percentuale.
  - Spiega come stampare il simbolo dei gradi utilizzando i codici dei caratteri ASCII.
* **Compito per Casa**:
  - Aggiungi un pulsante al circuito.
  - Modifica il codice per alternare tra la visualizzazione della temperatura in Celsius e Fahrenheit quando il pulsante viene premuto.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KYEidJFYPto?si=5vAk5sl-VyEqYIfs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

