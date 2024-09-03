.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Lezione 7: Controllare 3 LED con un Potenziometro in Micropython
====================================================================

Questo tutorial copre l'uso di un potenziometro per controllare tre LED (verde, giallo e rosso) con il Raspberry Pi Pico W:

* **Revisione della Soluzione del Compito**: Riepiloga il compito precedente di collegare un potenziometro e tre LED e mappare le letture del potenziometro da 0 a 100 per controllare i LED in base ai valori di ingresso.
* **Configurazione del Circuito**: Fornisce uno schema di cablaggio dettagliato e la configurazione per collegare il potenziometro e i LED al Raspberry Pi Pico W. Include la creazione di binari di massa e 3,3 V e il collegamento dei componenti ai pin GPIO appropriati.
* **Lettura e Mappatura dei Valori del Potenziometro**: Dimostra come leggere i valori analogici dal potenziometro e mapparli dal loro intervallo originale (432 a 65.535) a una scala da 0 a 100 utilizzando equazioni matematiche.
* **Logica Condizionale per il Controllo dei LED**: Implementa istruzioni if per controllare i LED in base alle letture del potenziometro: LED verde per valori tra 0 e 79. LED giallo per valori tra 80 e 94. LED rosso per valori tra 95 e 100.
* **Dimostrazione Pratica**: Mostra il circuito funzionante e il codice in azione, con i LED che si accendono in base alla posizione del potenziometro.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/YqvcSnGd_HQ?si=igsP6I-k3FhYA7Go" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

