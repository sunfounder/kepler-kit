.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 70:  Esempio di Uscita Pulita da un Programma a Doppio Core in MicroPython
=======================================================================================

Questo tutorial spiega come utilizzare i thread per controllare un servo e un pulsante con il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:

- Collega il filo di controllo del servo al pin GPIO 17, il filo di alimentazione al pin fisico 40, e il filo di massa al pin fisico 38.
- Collega un pulsante al pin GPIO 16 e alla massa.

* **Implementazione del Codice**:

 - Importa le librerie necessarie (`machine`, `time`, `_thread`, `Servo`).
 - Configura i pin per il pulsante e il servo.
 - Implementa un interruttore a levetta per il pulsante per controllare il movimento del servo.
 - Definisci un ciclo principale per rilevare le pressioni del pulsante e alternare il servo tra 0 e 180 gradi.
 - Utilizza il threading per gestire il movimento del servo su un core separato, consentendo un'uscita pulita del programma.

* **Compito**:

 - Modifica il programma per garantire che esca pulitamente anche se interrotto mentre il servo è in movimento.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
