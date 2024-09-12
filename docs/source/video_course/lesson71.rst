.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 71:  Permettere al Thread di Completare il Compito Prima della Terminazione
========================================================================================

Questo tutorial spiega come terminare in modo ordinato un programma multithread sul Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:

  - Collega il filo di controllo del servo al pin GPIO 17, il filo di alimentazione al pin fisico 40 e il filo di massa al pin fisico 38.
  - Collega un pulsante al pin GPIO 16 e alla massa.

* **Implementazione del Codice**:

  - Importa le librerie necessarie (`machine`, `time`, `_thread`, `Servo`).
  - Configura i pin per il pulsante e il servo.
  - Implementa un interruttore a levetta per il pulsante per controllare il movimento del servo.
  - Definisci un ciclo principale per rilevare le pressioni del pulsante e alternare il servo tra 0 e 180 gradi.
  - Utilizza il threading per gestire il movimento del servo su un core separato, consentendo uscite pulite del programma.

* **Gestione della Terminazione Pulita**:

  - Utilizza una variabile globale `running` per controllare l'esecuzione del ciclo.
  - Implementa un blocco (lock) per garantire che solo una parte del programma venga eseguita alla volta durante le sezioni critiche.
  - Attendi che il movimento del servo sia completato prima di terminare il programma.

* **Compito**:

  - Modifica il programma per gestire componenti o sensori aggiuntivi, garantendo una terminazione pulita in tutti gli scenari.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/Xm3chr1-hkY?si=ITIUvlqKF6UdOsq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
