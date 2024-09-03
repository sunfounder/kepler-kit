.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 36: Controllo di un Servo con MicroPython
=============================================================================

Questo tutorial spiega come controllare un motore servo utilizzando il Raspberry Pi Pico W:

* **Controllo del Motore Servo**:
  - Introduzione all'uso del servo motore SG90 con il Raspberry Pi Pico W.
  - Spiegazione dei collegamenti del motore servo: marrone (massa), rosso (alimentazione), arancione (controllo).
  - Importante: non utilizzare il Raspberry Pi Pico W per alimentare servomotori più grandi a causa del rischio di danni.
* **Diagramma di Collegamento e Configurazione**:
  - Istruzioni dettagliate per collegare il servo SG90 al Raspberry Pi Pico W.
  - Utilizzo del pin GPIO 15 per il controllo e creazione di una barra di alimentazione dal pin 1 per la fornitura di 5V.
* **Nozioni di Base sul PWM**:
  - Spiegazione della Modulazione a Larghezza di Impulso (PWM) e del suo ruolo nel controllo della posizione del servo.
  - Calcolo degli impulsi corrispondenti ai diversi angoli del servo (0,5ms per 0 gradi, 2,5ms per 180 gradi).
  - Impostazione della frequenza PWM a 50Hz per soddisfare i requisiti del servo.
* **Spiegazione del Codice**:
  - Tutorial passo-passo per configurare il PWM sul pin GPIO 15.
  - Creazione di una funzione per convertire gli angoli desiderati in valori di duty cycle PWM.
  - Codice di esempio per controllare il servo inserendo gli angoli desiderati.
* **Dimostrazione Pratica**:
  - Esecuzione del codice per muovere il servo a specifici angoli.
  - Assicurarsi di operare il servo in sicurezza evitando di ruotare manualmente il braccio del servo.
* **Compito a Casa**:
  - Integrazione di un potenziometro con il setup per controllare la posizione del servo regolando il potenziometro.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/vAnd0AC6u1Q?si=0VAnHzQFnQlyDqI6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
