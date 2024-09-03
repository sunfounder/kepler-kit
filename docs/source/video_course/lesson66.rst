.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 66 : Crea le Tue Librerie in Micropython
===================================================================================

Questo tutorial tratta la creazione e l'uso di una libreria Servo con il Raspberry Pi Pico W:

* **Configurazione dei Collegamenti**:
   - Collega il filo rosso del servo al pin fisico 40 (3.3V), il filo marrone al pin 38 (massa), e il filo di controllo arancione al pin GPIO 17.
* **Classe e Metodi**:
   - Definisci una classe `Servo` per gestire gli oggetti servo.
   - Inizializza il servo con il metodo `__init__`, configurando il pin PWM.
   - Implementa un metodo `pos` per controllare la posizione del servo.
* **Creazione della Libreria**:
   - Scrivi il codice della classe `Servo` e salvalo come file di libreria (`ServoLib.py`).
   - Crea una directory `lib` sul Raspberry Pi Pico W e salva il file della libreria in questa directory.
* **Implementazione del Codice**:
   - Importa le librerie necessarie (`machine`, `time` e `ServoLib`).
   - Crea un oggetto servo utilizzando la classe `Servo` dalla libreria `ServoLib`.
   - Controlla la posizione del servo chiamando il metodo `pos` con gli angoli desiderati.
* **Compito**:
   - Crea una libreria simile per un altro componente, come un LED, per semplificarne l'uso in progetti futuri.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/lz_Gp-zDtKI?si=VHgvS20YVqfft8LY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

