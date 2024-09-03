.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 25: Introduzione all'uso di OLED 1306 in Micropython
=============================================================================

Questo tutorial tratta l'utilizzo del Raspberry Pi Pico W e di un display OLED per progetti portatili:

* **Introduzione**:
 - Sottolinea l'obiettivo: continuare a svincolare i progetti dal desktop rendendoli portatili e più efficienti dal punto di vista energetico.
* **Revisione dei Componenti e Configurazione**:
 - Ricapitola la lezione precedente: utilizzo di una batteria ricaricabile LiPo per alimentare il Raspberry Pi Pico W con un sensore DHT-11, un pulsante e un display LCD.
 - Discute i limiti dell'utilizzo di un display LCD, inclusi il maggiore consumo di energia e le dimensioni maggiori.
* **Introduzione al Display OLED**:
 - Consiglia l'uso di un display OLED piccolo, a basso consumo e ad alto contrasto per progetti portatili.
 - Mostra come collegare il display OLED al Raspberry Pi Pico W utilizzando il bus I2C, specificamente sui pin GPIO 2 (SDA) e 3 (SCL).
* **Installazione della Libreria e Configurazione Iniziale**:
 - Dimostra come installare la libreria SSD1306 per il display OLED.
 - Spiega la configurazione di base del codice, compreso l'import delle librerie necessarie e la creazione degli oggetti I2C e display.
* **Visualizzazione di Testo e Grafica**:
 - Fornisce esempi di codice per visualizzare testo sullo schermo OLED.
 - Mostra come indirizzare i singoli pixel e disegnare linee orizzontali, verticali e arbitrarie.
 - Dimostra come creare e riempire rettangoli sul display.
* **Gestione dell'Energia**:
 - Spiega come accendere e spegnere il display per risparmiare energia della batteria utilizzando comandi software.
* **Dimostrazione Pratica**:
 - Esegue il codice per mostrare testo e grafica sul display OLED.
 - Sottolinea l'elevato contrasto e il basso consumo energetico del display OLED rispetto all'LCD.
* **Compito a Casa**:
 - Assegna un compito: creare un programma che visualizzi il titolo "My Circle" nella parte superiore dello schermo e disegni un cerchio con un raggio di 20 pixel al centro dello schermo.
 - Incoraggia gli spettatori a postare il loro lavoro su YouTube e condividere il link nei commenti.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/6SdNvqofWww?si=ZVxzi5Nm3lP5PniU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
