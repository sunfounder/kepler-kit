.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 31: Progetto Stazione Meteo Remota senza Sensori
=============================================================================

Questo tutorial tratta la creazione di una stazione meteorologica senza sensori utilizzando il Raspberry Pi Pico W:

* **Connessione al WiFi**: Importa le librerie e connetti il dispositivo al WiFi utilizzando un oggetto WLAN.
* **Recupero dei dati meteorologici**: Utilizza l'API di OpenWeatherMap per ottenere dati meteorologici in tempo reale, richiedendo una chiave API.
* **Parsing dei dati JSON**: Estrae temperatura, umidità, pressione, orari di alba e tramonto dalla risposta JSON.
* **Spiegazione del codice**: Usa ``urequests.get()`` per recuperare i dati, converti l'orario Unix e regola le unità di pressione.
* **Visualizzazione dei dati meteorologici**: Stampa temperatura, umidità, pressione, condizioni e velocità del vento.
* **Compito a casa**: Aggiungi un display e crea una stazione meteorologica portatile alimentata a batteria.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

