.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 67: Usa Entrambi i Core del Tuo Pi Pico con MicroPython
===================================================================================

Questo tutorial spiega come utilizzare entrambi i core del Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:
   - Collega un LED verde al pin GPIO 14 con una resistenza da 330 ohm a massa.
   - Collega un LED rosso al pin GPIO 15 con una resistenza da 330 ohm a massa.
* **Implementazione del Codice**:
   - Importa le librerie necessarie (`machine`, `time`, `_thread`).
   - Configura i pin per i LED.
   - Definisci i parametri per i tempi di lampeggio dei LED.
   - Crea funzioni per controllare il lampeggio dei LED:
     - `other_core` per il LED rosso sul secondo core.
     - `green_blink` per il LED verde sul core principale.
   - Usa `_thread.start_new_thread` per eseguire `other_core` sul secondo core.
* **Compito**:
   - Collega un servo.
   - Controlla il servo e i LED:
     - Fai lampeggiare il LED rosso quando il servo si muove all'indietro.
     - Fai lampeggiare il LED verde quando il servo si muove in avanti.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mm1EoNqjd4c?si=RHZLX39PpGDbAFuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

