.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 23: Sensore di Temperatura e Umidità con Display LCD
=============================================================================

Questo tutorial spiega come creare un progetto di rilevamento della temperatura e umidità utilizzando il Raspberry Pi Pico W, il sensore DHT-11 e un display LCD:

* **Introduzione**: Introduce il tutorial, ringrazia lo sponsor SunFounder e rivede l'obiettivo della lezione, che è quello di creare un progetto di rilevamento della temperatura e umidità con un display LCD.
* **Introduzione ai Componenti e Configurazione**:
 - Descrive i componenti necessari: Raspberry Pi Pico W, sensore DHT-11, pulsante e display LCD 1602.
 - Fornisce uno schema e istruzioni per collegare questi componenti, facendo riferimento alle lezioni precedenti per dettagli sulle istruzioni di cablaggio.
* **Installazione della Libreria**:
 - Guida su come scaricare e installare la libreria necessaria per il display LCD 1602 da toptechboy.com.
 - Fornisce istruzioni per salvare e importare la libreria in Thonny IDE.
* **Spiegazione del Codice**:
 - Descrive come configurare il sensore DHT-11 e il pulsante utilizzando i pin GPIO.
 - Introduce una variabile flag per passare da Celsius a Fahrenheit.
 - Spiega il codice per la lettura della temperatura e dell'umidità dal sensore DHT-11.
 - Dettaglia l'implementazione di una funzione di commutazione per passare da Celsius a Fahrenheit.
 - Spiega come visualizzare le letture sia sulla console che sul display LCD.
* **Dimostrazione Pratica**:
 - Mostra il programma in azione, visualizzando le letture di temperatura e umidità sul display LCD.
 - Dimostra la funzionalità di commutazione per passare da Celsius a Fahrenheit.
 - Affronta i potenziali problemi di sovrapposizione del testo sul display LCD aggiungendo spazi e utilizzando `LCD.clear()` per cancellare lo schermo prima di scrivere nuovo testo.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/2DZo1JeVWMk?si=mceO0XqYqT3aBpU7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

