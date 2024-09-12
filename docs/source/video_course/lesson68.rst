.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 68:  Esempio di Multithreading con MicroPython su Due Core con LED e Servo
=======================================================================================

Questo tutorial tratta il controllo di un servo e di LED con il Raspberry Pi Pico W utilizzando entrambi i core:

* **Configurazione dei collegamenti**: Collega il LED rosso al GPIO 15, il LED verde al GPIO 14, il servo al GPIO 17, l'alimentazione al pin 40 e la massa al pin 38.
* **Implementazione del codice**: Importa ``machine``, ``time``, ``_thread`` e ``Servo``. Configura i pin per i LED e il servo. Definisci la funzione ``other_core`` per far lampeggiare i LED in base alla direzione del servo.
* **Compito a casa**: Modifica il codice per far lampeggiare il LED rosso per il movimento del servo in senso orario e il LED verde per il movimento in senso antiorario.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/n2eQTw9axHg?si=TRVLEM1EqyD_DefA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

