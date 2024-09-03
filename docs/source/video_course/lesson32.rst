.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 32: Progetto di Stazione Meteo Portatile
=============================================================================

Questo tutorial spiega come creare una stazione meteo portatile utilizzando il Raspberry Pi Pico W:

* **Connessione al WiFi**:
  - Importa le librerie necessarie.
  - Crea un oggetto WLAN e connettiti alla rete WiFi.
* **Recupero dei Dati Meteo**:
  - Usa l'API di OpenWeatherMap per ottenere dati meteo in tempo reale.
  - Ottieni una chiave API da OpenWeatherMap iscrivendoti per un account gratuito.
* **Analisi dei Dati JSON**:
  - Estrai informazioni meteorologiche rilevanti come temperatura, umidità, pressione barometrica, orari di alba e tramonto.
* **Visualizzazione dei Dati su OLED**:
  - Configura un display OLED e collegalo al Raspberry Pi Pico W.
  - Utilizza la libreria `ssd1306` per visualizzare i dati meteo sullo schermo OLED.
  - Crea un loop per aggiornare periodicamente i dati meteo sullo schermo.
* **Alimentazione del Dispositivo**:
  - Collega il Raspberry Pi Pico W a una batteria per un uso portatile.
* **Spiegazione del Codice**:
  - Passa attraverso l'inizializzazione del display OLED e la connessione al WiFi.
  - Recupera e analizza i dati meteo, quindi visualizzali sullo schermo OLED.
  - Implementa un loop per aggiornare i dati meteo ogni pochi minuti.
* **Compito per Casa**:
  - Migliora il progetto aggiungendo un LED RGB per indicare visivamente le condizioni meteorologiche come temperatura, umidità o velocità del vento.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

