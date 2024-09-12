.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 30: Progetto per Connettere il Tuo Raspberry Pi Pico W a Internet
=============================================================================

Questo tutorial spiega come connettere il Raspberry Pi Pico W a Internet e recuperare dati dalle API:

**Introduzione**:
- L'obiettivo è connettere il Raspberry Pi Pico W a Internet e ottenere dati in tempo reale dalle API.
- Nessuna configurazione hardware aggiuntiva necessaria.

**Connessione al WiFi**:
- Importa le librerie necessarie: `network`, `time`, `urequests`.
- Crea un oggetto WLAN e connettiti alla rete WiFi.
- Assicurati che la connessione sia avvenuta con successo prima di procedere.

**Recupero Dati dalle API**:
- Introduzione ai file JSON e alla loro struttura (array, dizionari, elementi nidificati).
- API di esempio utilizzata: Recupero di dati in tempo reale sugli astronauti nello spazio.
- Analizza e stampa la struttura dei dati per comprenderne il formato.

**Spiegazione del Codice**:
- Usa `urequests.get()` per ottenere dati JSON da un endpoint API specificato.
- Analizza i dati JSON per estrarre informazioni rilevanti.
- Esempio: Elenco dei nomi degli astronauti attualmente nello spazio e delle loro rispettive navicelle spaziali.

**Dimostrazione Pratica**:
- Esempio di codice per recuperare e visualizzare i dati sugli astronauti.
- Dimostra come navigare nelle strutture JSON nidificate per estrarre dati specifici.
- Esempio di output: Numero di astronauti, loro nomi e navicelle spaziali.

**Compito per Casa**:
- Trova un set di dati in tempo reale interessante (ad esempio, meteo, prezzi delle azioni, terremoti).
- Recupera e analizza i dati utilizzando il Raspberry Pi Pico W.
- Visualizza o utilizza i dati in modo significativo (ad esempio, stazione meteo senza sensori).


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/5xXHo1xhc-g?si=kdpYgB6P7KoUU2Xa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
