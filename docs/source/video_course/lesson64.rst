.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 64: Esempio di Programmazione Orientata agli Oggetti in MicroPython con LED
==========================================================================================

Questo tutorial tratta la programmazione orientata agli oggetti (OOP) con il Raspberry Pi Pico W, focalizzandosi sul controllo dei LED:

* **Configurazione dei Collegamenti**: Collega un LED rosso al pin GPIO 15 e un LED verde al pin GPIO 14, utilizzando resistenze da 330 ohm verso massa.
* **Classi e Metodi**:
   1. Definisci una classe `LED` per gestire gli oggetti LED.
   2. Inizializza il LED con il metodo `__init__`, configurando il pin.
   3. Implementa un metodo `blink` per controllare il lampeggio del LED.
* **Implementazione del Codice**:
   1. Importa le librerie necessarie (`machine` e `time`).
   2. Crea la classe `LED` con i metodi `__init__` e `blink`.
   3. Crea istanze per i LED rosso e verde.
   4. Utilizza un ciclo per far lampeggiare i LED secondo i parametri specificati.
* **Compito**: Crea una classe per un Servomotore, che permetta un facile controllo della sua posizione. La classe dovrebbe includere metodi per l'inizializzazione del Servomotore e per impostare il suo angolo. Consulta la Lezione 36 per i dettagli sul lavoro con i Servomotori in MicroPython.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3wyCL9QK_uY?si=G0GXEHqdo2jQ_F-5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

