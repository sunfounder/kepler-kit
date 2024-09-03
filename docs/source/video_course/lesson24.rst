.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 24: Alimentare Progetti Portatili con una Batteria Ricaricabile LiPo
================================================================================

Questo tutorial spiega come alimentare un progetto con Raspberry Pi Pico W utilizzando una batteria ricaricabile LiPo, rendendo il progetto portatile:

* **Introduzione**: Introduce il tutorial, ringrazia lo sponsor SunFounder e rivede l'obiettivo della lezione: rendere portatile il progetto del sensore di temperatura e umidità DHT-11.
* **Revisione dei Componenti e Configurazione**:
 - Ricapitola la configurazione del progetto precedente: Raspberry Pi Pico W, sensore DHT-11, pulsante e display LCD 1602.
 - Discute la necessità di rimuovere il cavo USB e alimentare il progetto utilizzando una batteria LiPo.
* **Installazione della Libreria**:
 - Guida gli spettatori su come installare la libreria per il display LCD 1602 se non l'hanno già fatto.
* **Spiegazione del Codice**:
 - Descrive la necessità di salvare il programma come `main.py` in modo che venga eseguito automaticamente quando il Pico W è alimentato.
 - Mostra come salvare il codice e verificarne il funzionamento.
* **Alimentazione del Progetto con una Batteria**:
 - Introduce la batteria ricaricabile LiPo e il portabatteria del kit SunFounder Kepler.
 - Dettaglia il collegamento della batteria al Pico W utilizzando un modulo di gestione dell'alimentazione incluso nel kit.
 - Spiega come regolare la connessione di alimentazione del display LCD da 5V (pin 40) a 3,7V (pin 39) a causa dell'uscita della batteria.
 - Mostra la configurazione e verifica che il progetto funzioni correttamente con l'alimentazione a batteria.
* **Regolazioni e Dimostrazione**:
 - Dimostra come regolare il contrasto del display LCD per una visualizzazione ottimale quando alimentato dalla batteria.
 - Mostra il progetto funzionante correttamente, compresa la commutazione tra Fahrenheit e Celsius.
* **Conclusione e Prossimi Passi**:
 - Incoraggia gli spettatori a verificare che il loro progetto funzioni e introduce l'idea di utilizzare un display OLED per le lezioni future.
 - Raccomanda di acquistare un display OLED per un setup più compatto ed efficiente dal punto di vista energetico.
 - Anticipa le lezioni future focalizzate sulla creazione di progetti portatili e dispiegabili con funzionalità avanzate.
* **Compiti a Casa e Note Finali**:
 - Suggerisce agli spettatori di ordinare il display OLED per prepararsi alle prossime lezioni.
 - Conclude con i promemoria di mettere mi piace, commentare, iscriversi e condividere il video.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/NhfkOEmZoLQ?si=jxNyNl9DCKlqr4PJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
