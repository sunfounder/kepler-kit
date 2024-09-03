.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 35: Stazione Meteorologica Remota con Indicatore di Temperatura RGB
=============================================================================

Questo tutorial spiega come integrare un LED RGB per visualizzare i dati di temperatura in una stazione meteorologica utilizzando il Raspberry Pi Pico W:

* **Panoramica del Progetto**:
  - Costruisci una stazione meteorologica remota utilizzando Raspberry Pi Pico W, un display OLED e un LED RGB per mostrare visivamente la temperatura.
* **Conversione da HSV a RGB**:
  - Converte i valori di temperatura in colori utilizzando la ruota dei colori HSV.
  - Mappa le temperature da -20°F (viola profondo) a 120°F (rosso) agli angoli corrispondenti sulla ruota dei colori.
* **Configurazione del Circuito**:
  - Collega il display OLED e il LED RGB al Raspberry Pi Pico W.
  - Configura i pin GPIO e il PWM per il LED RGB.
* **Codifica**:
  - Recupera i dati di temperatura, calcola l'angolo della tonalità, convertilo in valori RGB e applicali al LED RGB.
  - Integra la libreria di conversione da HSV a RGB nel codice della stazione meteorologica.
* **Dimostrazione**:
  - Visualizza i dati di temperatura sul display OLED e sul LED RGB.
  - Salva ed esegui il codice, rendendo il setup portatile con alimentazione a batteria.
* **Conclusione**:
  - Personalizza il progetto regolando le mappature dei colori e i range di temperatura.
  - Incoraggiamento a iscriversi, commentare e condividere il tutorial.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/c9tQHyQWIYk?si=ORHsIXt8eBGeXDdp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

