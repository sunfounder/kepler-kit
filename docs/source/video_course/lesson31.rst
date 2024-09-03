.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 31: Progetto Stazione Meteo Remota senza Sensori
=============================================================================

Questo tutorial spiega come creare una stazione meteo senza sensori utilizzando il Raspberry Pi Pico W:

* **Connessione al WiFi**:
 - Importa le librerie necessarie.
 - Crea un oggetto WLAN e connettiti alla rete WiFi.
* **Recupero Dati Meteo**:
 - Utilizza l'API di OpenWeatherMap per ottenere dati meteo in tempo reale.
 - Ottieni una chiave API da OpenWeatherMap iscrivendoti per un account gratuito.
* **Analisi dei Dati JSON**:
 - Estrai informazioni meteo rilevanti come temperatura, umidità, pressione barometrica, orari di alba e tramonto.
* **Spiegazione del Codice**:
 - Usa `urequests.get()` per ottenere dati JSON dall'endpoint API.
 - Converti l'ora Unix epoch in ora locale per l'alba e il tramonto.
 - Converti la pressione barometrica da HPA ad atmosfere.
* **Visualizzazione dei Dati Meteo**:
 - Stampa informazioni meteo come temperatura, umidità, pressione barometrica, condizioni atmosferiche e velocità del vento.
* **Compito per Casa**:
 - Migliora il progetto aggiungendo un display per mostrare le informazioni meteo.
 - Crea una stazione meteo portatile alimentata a batteria.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

