.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 58: Determinare la Posizione Angolare di un Joystick in MicroPython
=================================================================================

Questo tutorial tratta la calibrazione di un joystick con il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**: Collega la massa al pin 38, 3.3V al pin 36, VRX al pin GPIO 27, VRY al pin GPIO 26.
* **Implementazione del Codice**: Importa le librerie necessarie. Configura l'ADC per gli assi del joystick e leggi i valori per la calibrazione.
* **Calibrazione**: Converti i valori grezzi dell'ADC su una scala da -100 a +100. Usa la trigonometria per calcolare l'angolo del joystick.
* **Compito**: Scrivi un programma per controllare un servomotore in base all'angolo del joystick, assicurando un tracciamento accurato tra 0 e 180 gradi.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KpDIv0i41Tw?si=PUEInyKbRTIUcvCa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

