.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e a esclusive anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e concorsi festivi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 11: Comprendere e controllare un LED RGB in MicroPython
==========================================================================

Questo tutorial tratta il controllo di un LED RGB utilizzando il SunFounder Kepler Kit e Raspberry Pi Pico W:

* **Controllo del LED RGB**: Spiega come controllare i colori del LED RGB utilizzando PWM (Pulse Width Modulation). Discute la struttura del LED RGB, che contiene tre LED (rosso, verde e blu) con una massa comune. Sottolinea l'importanza di utilizzare resistenze limitatrici di corrente separate per ciascun canale di colore per prevenire interferenze.
* **Schema elettrico e configurazione**: Fornisce un diagramma di cablaggio dettagliato per collegare il LED RGB e le resistenze necessarie al Raspberry Pi Pico W. Dimostra l'installazione fisica su una breadboard, inclusi i collegamenti per i canali rosso, verde e blu ai pin GPIO 13, 14 e 15, rispettivamente.
* **Spiegazione del codice**: Descrive il codice per configurare il PWM su ciascun pin GPIO e controllare la luminosità di ciascun canale di colore. Copre la configurazione della frequenza PWM, del ciclo di lavoro e l'inizializzazione dei pin GPIO per i canali rosso, verde e blu.
* **Dimostrazione pratica**: Mostra come eseguire il codice per cambiare il colore del LED RGB. Dimostra come accendere e spegnere singoli canali di colore e regolare i livelli di luminosità.
* **Compito a casa**: Invita gli utenti a creare un programma che richieda all'utente di inserire un colore (rosso, verde, blu, ciano, magenta, giallo, arancione o bianco) e regolare il LED RGB per visualizzare il colore specificato. Incoraggia gli utenti a combinare e abbinare i valori PWM per ottenere una rappresentazione accurata del colore.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/yZkx-KWbATY?si=p85rQXYb6YGoEe9L" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

