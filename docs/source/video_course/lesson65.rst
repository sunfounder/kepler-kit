.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 65 : Creare una Classe Servo e Metodo in MicroPython
===================================================================================

Questo tutorial tratta la creazione di una classe Servo utilizzando la programmazione orientata agli oggetti (OOP) con il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:
Collega il filo rosso del servo al pin fisico 40 (3.3V), il filo marrone al pin 38 (massa), e il filo di controllo arancione al pin GPIO 17.
* **Classe e Metodi**:
   - Definisci una classe `Servo` per gestire gli oggetti servo.
   - Inizializza il servo con il metodo `__init__`, configurando il pin PWM.
   - Implementa un metodo `pos` per controllare la posizione del servo.
* **Implementazione del Codice**:
   - Importa le librerie necessarie (`machine` e `time`).
   - Crea la classe `Servo` con i metodi `__init__` e `pos`.
   - Crea un oggetto servo e controlla la sua posizione utilizzando il metodo `pos`.
* **Compito**:
   - Rivedi la lezione 36 per i dettagli sul lavoro con i servomotori. Crea una classe Servo che consenta un facile controllo della posizione del servo impostando gli angoli. Implementa un metodo per muovere il servo in base all'input dell'utente.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/OI4MzX7zqGc?si=ReJ76mhOZqUdnL9h" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
