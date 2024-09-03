.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e concorsi festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 12: Creare un LED dimmerabile in Micropython
==========================================================================

Questo tutorial tratta il controllo della luminosità di un LED utilizzando un potenziometro e PWM (Pulse Width Modulation) su Raspberry Pi Pico W:

* **Controllo della luminosità del LED**: Spiega come controllare la luminosità di un LED utilizzando PWM. Discute i segnali digitali, i cicli di lavoro e come la variazione dei cicli di lavoro controlli la luminosità del LED. Introduce il concetto di scalatura esponenziale per rendere la percezione della luminosità del LED più lineare per l'occhio umano.
* **Schema elettrico e configurazione**: Fornisce un diagramma di cablaggio dettagliato per collegare un potenziometro e un LED con una resistenza da 220 Ohm al Raspberry Pi Pico W. Dimostra l'installazione fisica su una breadboard.
* **Spiegazione del codice**: Descrive il codice per configurare PWM su un pin GPIO, leggere il valore analogico da un potenziometro e convertirlo nel corrispondente ciclo di lavoro PWM. Spiega l'uso delle librerie, degli oggetti PWM e delle impostazioni di frequenza.
* **Dimostrazione pratica**: Mostra come misurare e visualizzare il segnale PWM utilizzando un oscilloscopio, illustrando come i diversi cicli di lavoro corrispondano a diverse tensioni medie. Dimostra l'effetto dell'uso della scalatura esponenziale per transizioni di luminosità più fluide.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MCo5nXAKyUU?si=VauJgWRltVnQpwz-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

