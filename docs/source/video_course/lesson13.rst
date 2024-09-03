.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e concorsi festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

Lezione 13: Colori RGB LED specificati dall'utente utilizzando Micropython
===============================================================================

Questo tutorial tratta il controllo di un LED RGB utilizzando il SunFounder Kepler Kit e Raspberry Pi Pico W:

* **Controllo del LED RGB**: Dimostra come controllare un LED RGB utilizzando PWM (Pulse Width Modulation) per ottenere colori diversi. Spiega la struttura del LED RGB con le sue quattro gambe per rosso, verde, blu e massa.
* **Schema di collegamento e configurazione**: Fornisce uno schema dettagliato per collegare il LED RGB al Raspberry Pi Pico W. Ogni canale di colore (rosso, verde, blu) è collegato a un pin GPIO (13, 14, 15) con una resistenza da 220 Ohm per limitare la corrente.
* **Spiegazione del codice**: Descrive il codice MicroPython per configurare PWM su ogni pin GPIO e controllare la luminosità di ciascun canale colore. Include codice per accendere colori specifici (rosso, verde, blu, ciano, magenta, giallo, arancione, bianco) in base all'input dell'utente.
* **Dimostrazione pratica**: Mostra come eseguire il codice e cambiare il colore del LED RGB. Dimostra il processo di inserimento di un colore e l'osservazione del cambiamento di colore del LED RGB.
* **Compito a casa**: Invita gli utenti a estendere il progetto collegando tre potenziometri per controllare manualmente i colori del LED RGB. Incoraggia gli utenti a combinare i valori dei potenziometri per ottenere qualsiasi colore desiderato.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/FLMPjwXqXVw?si=laOuij3khzBg5Uac" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

