.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 37: Controllare un Servo con un Potenziometro in MicroPython
=============================================================================
Questo tutorial spiega come controllare un motore servo utilizzando un potenziometro con il Raspberry Pi Pico W:

* **Controllo del Motore Servo**:
  - Collega il motore servo SG90 al Raspberry Pi Pico W.
  - Filo marrone a massa, filo rosso a alimentazione (5V), filo arancione al pin GPIO 15 per il controllo.
* **Configurazione dei Collegamenti**:
  - Collega il potenziometro: alimentazione a 3.3V, massa alla barra di massa e segnale al pin GPIO 26.
* **Nozioni di Base sul PWM**:
  - Utilizza la Modulazione a Larghezza di Impulso (PWM) per controllare la posizione del servo.
  - Imposta la frequenza PWM a 50Hz per il servo.
* **Spiegazione del Codice**:
  - Configura il PWM sul pin GPIO 15.
  - Converte le letture del potenziometro in angoli del servo.
  - Viene fornito un esempio di codice per muovere il servo in base all'input del potenziometro.
* **Dimostrazione Pratica**:
  - Esegui il codice per controllare il servo con il potenziometro.
  - Evita di ruotare manualmente il braccio del servo per prevenire danni.
* **Idee Applicative**:
  - Controlla servomotori più grandi con un alimentatore esterno per progetti più avanzati.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/iiJasGsLTrQ?si=f-avwQIJNypRuh4t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
