.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 45: Calcolo dell'Altezza di Caduta di un Oggetto in Caduta Libera
=============================================================================
Questo tutorial copre l'uso del sensore MPU6050 con il Raspberry Pi Pico W per misurare le distanze verticali:

* **Setup**:
   - Collega l'MPU6050 e l'OLED 1306 al Raspberry Pi Pico W utilizzando lo schema fornito. Assicurati che tutte le connessioni siano sicure per evitare interferenze elettriche.
* **Concetto**:
   - Misura le distanze verticali lasciando cadere il sensore e calcolando il tempo di caduta (T_drop). Usa il tempo di caduta libera per calcolare l'altezza da cui è stato lasciato cadere.
* **Equazione**:
   - L'altezza (H) viene calcolata utilizzando la formula: \( H = 16 \times (T_{drop})^2 \). Converti il tempo di caduta da millisecondi a secondi prima di applicare la formula.
* **Implementazione del Codice**:
   - Configura le librerie per l'MPU6050 e l'OLED 1306.
   - Misura l'accelerazione sull'asse Z per rilevare quando il sensore è in caduta libera (misurando 0G).
   - Avvia un timer quando il sensore viene lasciato cadere e fermalo quando tocca il suolo.
   - Visualizza l'altezza calcolata e il tempo di caduta sull'OLED.
* **Dimostrazione Pratica**:
   - Testa il sistema lasciando cadere il sensore da altezze note e verificando l'accuratezza delle misurazioni. Regola se necessario per migliorare la precisione.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
