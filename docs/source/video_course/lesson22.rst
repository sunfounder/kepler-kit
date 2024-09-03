.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 22: Utilizzo di un Display LCD con il Pico W
=============================================================================

Questo tutorial spiega come collegare e utilizzare un display LCD 1602 con il Raspberry Pi Pico W:

* **Introduzione**: Introduce il tutorial, ringrazia lo sponsor SunFounder e spiega l'obiettivo di aggiungere un display LCD al progetto con il Raspberry Pi Pico W per un uso mobile.

* **Introduzione ai Componenti e Configurazione**:
- Descrive i componenti necessari: display LCD 1602 e cavi femmina-maschio.
- Dettaglia i collegamenti:
  - Pin del display LCD 1602 al Raspberry Pi Pico W:
    - Ground al pin 38
    - VCC (5V) al pin più a destra
    - SDA (dati) al pin GPIO 6
    - SCL (clock) al pin GPIO 7

* **Installazione della Libreria**:
 - Guida su come scaricare e installare la libreria necessaria per il display LCD 1602 da toptechboy.com.
 - Fornisce istruzioni per salvare e importare la libreria in Thonny IDE.

* **Spiegazione del Codice**:
 - Descrive la creazione di un oggetto LCD e la scrittura di testo sul display.
 - Fornisce un programma di esempio che chiede il nome dell'utente e visualizza un messaggio di benvenuto sull'LCD.
 - Affronta i potenziali problemi di sovrapposizione del testo utilizzando `LCD.clear()` per cancellare lo schermo prima di scrivere un nuovo testo.

* **Dimostrazione Pratica**:
 - Mostra il programma in azione, visualizzando i nomi sul display LCD.
 - Spiega come regolare il contrasto dell'LCD utilizzando un potenziometro sul retro del display.

* **Compito per Casa**:
 - Assegna il compito di integrare il display LCD con il progetto del sensore di temperatura e umidità DHT11 della lezione 21.
 - Insegna a visualizzare la temperatura in Celsius o Fahrenheit in base a un pulsante di commutazione e a visualizzare l'umidità sul display LCD.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/liwMc01LOIA?si=ZRpzb2YskRgxd3Kn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

