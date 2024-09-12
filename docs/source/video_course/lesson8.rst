.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Lezione 8: Condizionali Composti e Istruzioni If in MicroPython
==========================================================================

Questo tutorial tratta l'uso di un potenziometro per controllare tre LED (verde, giallo e rosso) con il Raspberry Pi Pico W e identifica un errore logico critico nell'implementazione precedente:

* **Revisione della Soluzione del Compito**: Riepiloga il compito precedente per trovare il difetto logico nel codice che controllava i LED in base alle letture del potenziometro.
* **Spiegazione dell'Errore Logico**: Spiega l'errore logico nel codice in cui gli stati dei LED potevano sovrapporsi, causando comportamenti indesiderati. Sottolinea l'importanza di garantire che le condizioni logiche siano mutuamente esclusive per evitare tali errori.
* **Esempio di Applicazione Reale**: Illustra i potenziali pericoli degli errori logici utilizzando uno scenario ipotetico di stanze di sterilizzazione UV, dove un controllo errato dei LED potrebbe causare danni.
* **Introduzione ai Condizionali Composti**: Introduce i condizionali composti utilizzando operatori logici (AND, OR) per creare condizioni precise per il controllo dei LED. Dimostra come assicurarsi che ogni condizione sia correttamente implementata per evitare sovrapposizioni.
* **Configurazione del Circuito e Spiegazione del Codice**: Fornisce uno schema di cablaggio dettagliato e la configurazione per collegare il potenziometro e i LED al Raspberry Pi Pico W. Discute il modo corretto di scrivere istruzioni condizionali per controllare i LED in base alle letture del potenziometro.
* **Dimostrazione Pratica**: Mostra il codice rivisto in azione, evidenziando il corretto comportamento dei LED senza sovrapposizioni o condizioni mancate. Sottolinea l'importanza di una pianificazione logica accurata nei progetti di coding.
* **Prossimi Passi**: Anticipa la prossima Lezione sulla simulazione dell'uscita analogica, che amplierà ulteriormente gli strumenti per lavorare con il Raspberry Pi Pico W.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/uTwm3ydI69w?si=2OJPTawMlFfqO_DN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

