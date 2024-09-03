.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 60 : Controllare i Colori di NeoPixel con un Joystick in MicroPython
================================================================================

Questo tutorial tratta il controllo di una striscia LED tramite un joystick utilizzando il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**: Collega il joystick: massa al pin 38, 3.3V al pin 36, VRX al pin GPIO 27, VRY al pin GPIO 26. Collega il Neopixel: massa al pin 38, 5V al pin 40 e dati al pin GPIO 0.
* **Implementazione del Codice**: Importa le librerie necessarie (`machine`, `time`, `math`, `neopixel`). Configura l'ADC per il joystick e Neopixel. Leggi i valori del joystick e calcola gli angoli. Converti gli angoli in valori RGB per il Neopixel.
* **Compito**: Scrivi un programma per controllare il colore e la luminosità del Neopixel in base all'angolo del joystick e alla distanza dal centro.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

