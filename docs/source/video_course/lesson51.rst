.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 51: Dispositivo Definitivo per Pitch e Roll Utilizzando l'MPU6050
=============================================================================

Questo tutorial copre la creazione di un inclinometro preciso utilizzando il sensore MPU6050 e il Raspberry Pi Pico W:

* **Setup**:
   - Collega l'MPU6050 e l'OLED 1306 al Raspberry Pi Pico W utilizzando lo schema fornito.
* **Sfide**:
   - I dati grezzi dell'accelerometro sono rumorosi.
   - I dati del giroscopio derivano nel tempo.
* **Soluzione**:
   - Combina i dati dell'accelerometro e del giroscopio utilizzando un filtro complementare per ottenere misurazioni dell'inclinazione accurate, veloci e a basso rumore.
   - Implementa la correzione degli errori per gestire gli errori stazionari.
* **Implementazione**:
   - Inizializza l'MPU6050 e l'OLED 1306.
   - Raccogli i dati sia dall'accelerometro che dal giroscopio.
   - Applica un filtro complementare per combinare i dati a breve termine del giroscopio con quelli a lungo termine dell'accelerometro.
   - Aggiungi una correzione degli errori per compensare eventuali derive nelle misurazioni.
   - Visualizza i risultati sullo schermo OLED, mostrando sia informazioni qualitative (livella a bolla) che quantitative (lettura in gradi) sull'inclinazione.
* **Dimostrazione**:
   - L'inclinometro viene testato per mostrare letture di pitch e roll stabili e accurate anche in presenza di vibrazioni.
   - Il dispositivo è reso portatile utilizzando un pacco batteria, consentendo di operare senza fili.
* **Miglioramenti Aggiuntivi**:
   - Si suggerisce di rendere il dispositivo wireless per il monitoraggio remoto o di progettare una custodia stampata in 3D per la portabilità.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
