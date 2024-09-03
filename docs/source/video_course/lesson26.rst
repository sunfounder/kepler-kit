.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 26: Disegnare un Cerchio sul Display OLED 1306
=============================================================================

Questo tutorial tratta il disegno di forme su un display OLED utilizzando il Raspberry Pi Pico W:

* **Introduzione**:
 - Sottolinea l'obiettivo: disegnare un cerchio su un display OLED utilizzando il Raspberry Pi Pico W.
* **Ricapitolazione e Configurazione**:
 - Ricapitola la lezione precedente sull'utilizzo del display OLED 1306 e la configurazione della libreria SSD1306.
 - Discute l'importanza di utilizzare funzioni matematiche per disegnare forme sul display OLED.
* **Disegnare un Cerchio**:
 - Spiega la matematica dietro il disegno di un cerchio utilizzando funzioni trigonometriche: \( x = r \cos(\theta) \) e \( y = r \sin(\theta) \).
 - Converte i gradi in radianti per l'uso nei linguaggi di programmazione.
 - Mostra come centrare il cerchio sul display OLED regolando le coordinate x e y.
 - Fornisce un esempio di codice passo-passo per disegnare un cerchio iterando su 360 gradi e calcolando le posizioni x e y.
* **Migliorare il Disegno del Cerchio**:
 - Dimostra come disegnare un cerchio pieno iterando su un intervallo di raggi.
 - Mostra come disegnare un cerchio parziale o un arco regolando l'intervallo di angoli.
* **Dimostrazione Pratica**:
 - Esegue il codice per mostrare il disegno di un cerchio e di un cerchio pieno sul display OLED.
 - Spiega come ottimizzare la velocità di disegno aggiornando il display solo dopo che tutti i punti sono stati calcolati.
* **Compito a Casa**:
 - Assegna un compito: creare un programma che disegni una forma di "patatina galleggiante" sul display OLED.
 - Incoraggia gli spettatori a scoprire la matematica dietro la forma e a postare il loro lavoro su YouTube.




**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VgCcBm_Ms3E?si=J175coTlAdw2EMZ_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
