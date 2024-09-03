.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 69 :  Uscita Pulita dai Thread in MicroPython alla Terminazione del Programma
=========================================================================================

Questo tutorial spiega come controllare un servo e dei LED con il Raspberry Pi Pico W utilizzando entrambi i core:

* **Configurazione dei Collegamenti**:
 - Collega un LED rosso al pin GPIO 15 con una resistenza da 330 ohm a massa.
 - Collega un LED verde al pin GPIO 14 con una resistenza da 330 ohm a massa.
 - Collega il filo di controllo del servo al pin GPIO 17, il filo di alimentazione al pin fisico 40, e il filo di massa al pin fisico 38.
* **Implementazione del Codice**:
 - Importa le librerie necessarie (`machine`, `time`, `_thread`, `Servo`).
 - Configura i pin per i LED e il servo.
 - Definisci una funzione `other_core` per far lampeggiare i LED in base alla direzione del servo utilizzando una variabile globale.
 - Crea un ciclo per muovere il servo e impostare la direzione del LED.
* **Compito**:
 - Estendi il codice per far lampeggiare il LED rosso quando il servo si muove in senso orario e il LED verde quando si muove in senso antiorario.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

