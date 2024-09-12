.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 29: Progetto Client-Server per il Controllo Remoto di un LED RGB
=============================================================================

Questo tutorial spiega come configurare un LED RGB controllato da remoto tramite Wi-Fi utilizzando un Raspberry Pi Pico W e un PC:

* **Introduzione**:
  - L'obiettivo è controllare un LED RGB su un Raspberry Pi Pico W da remoto tramite Wi-Fi utilizzando un PC.
* **Diagramma di Cablaggio e Configurazione**:
  - I canali rosso, verde e blu del LED RGB sono collegati rispettivamente ai pin GPIO 16, 17 e 18.
  - Il display OLED è collegato tramite I2C ai pin GPIO 2 (SDA) e 3 (SCL).
* **Configurazione del Server (Raspberry Pi Pico W)**:
  - Importa le librerie: `socket`, `time`, `network`, `machine`, `ssd1306`.
  - Inizializza i pin GPIO per il LED RGB e il display OLED.
  - Connettiti al Wi-Fi e ottieni un indirizzo IP.
  - Crea un socket server UDP e associa l'indirizzo IP a una porta.
  - Visualizza l'indirizzo IP e la porta sul display OLED.
  - Ascolta i comandi in arrivo, decodificali e visualizza il comando e l'indirizzo del mittente.
* **Configurazione del Client (PC)**:
  - Importa la libreria `socket`.
  - Definisci l'indirizzo del server e la porta.
  - Crea un socket client UDP.
  - Richiedi l'input dell'utente per il colore del LED, codifica il comando e invialo al server.
  - Attendi e stampa la risposta del server.
* **Dimostrazione Pratica**:
  - Dimostra l'invio di comandi dal client per cambiare il colore del LED RGB sul server.
  - Il display OLED mostra i comandi ricevuti e l'indirizzo IP del mittente.
* **Configurazione Finale e Test**:
  - Scollega il Raspberry Pi Pico W dalla USB e alimentalo con una batteria.
  - Salva il codice come `main.py` per eseguirlo all'avvio.
  - Dimostra il funzionamento completamente wireless inviando comandi dal PC e osservando i cambiamenti del LED RGB e gli aggiornamenti sul display OLED.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

