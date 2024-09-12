.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 59: Controllare un Servo con un Joystick
=============================================================================

Questo tutorial tratta il controllo di un servo tramite un joystick utilizzando il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**: Collega il joystick: massa al pin 38, 3.3V al pin 36, VRX al pin GPIO 27, VRY al pin GPIO 26. Collega il servo: 5V al pin 40, massa al pin 38 e controllo al pin GPIO 15.
* **Implementazione del Codice**: Importa le librerie necessarie (`machine`, `time`, `math`). Configura l'ADC per gli assi del joystick e il PWM per il servo. Leggi e stampa i valori del joystick per la calibrazione e il calcolo dell'angolo.
* **Calibrazione e Controllo**: Converti i valori grezzi dell'ADC su una scala da -100 a +100. Calcola l'angolo del joystick utilizzando la trigonometria. Mappa l'angolo al valore PWM appropriato per il servo.
* **Compito**: Scrivi un programma per controllare un servomotore in base all'angolo del joystick, assicurando un tracciamento accurato tra 0 e 180 gradi.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
