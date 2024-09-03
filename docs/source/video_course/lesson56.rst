.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 56: Utilizzare un Joystick con MicroPython
=============================================================================

Questo tutorial tratta l'utilizzo di un joystick con il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:
   - Collega il cavo di massa, 3.3V, VRX al pin GPIO 27 e VRY al pin GPIO 26.
* **Implementazione del Codice**:
   - Importa le librerie necessarie (`machine`, `time`, `math`).
   - Configura l'ADC per gli assi del joystick.
   - Leggi e stampa i valori del joystick per comprendere il range e il comportamento.
* **Calibrazione**:
   - Regola le letture per renderle più intuitive, convertendole su una scala da -100 a +100 per una più facile interpretazione.
* **Compito**:
   - Scrivi un programma per calibrare il joystick in modo che la posizione centrale legga (0,0) e i bordi leggano ±100.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/0W8XSJhGux0?si=DO3JL-oMiMfbXF_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

