.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 46: Costruisci un Inclinometro a 2 Assi con Display Utilizzando l'MPU6050
=======================================================================================
Questo tutorial tratta l'utilizzo del sensore MPU6050 con il Raspberry Pi Pico W per creare un inclinometro a due assi:

* **Setup**:
   - Collega l'MPU6050 e l'OLED 1306 al Raspberry Pi Pico W utilizzando lo schema fornito. Assicurati che tutte le connessioni siano sicure per evitare interferenze elettriche.
* **Concetto**:
   - Misura l'inclinazione del sensore utilizzando i dati dell'accelerometro dell'MPU6050 per calcolare gli angoli di pitch e roll. Usa questi angoli per creare una rappresentazione visiva di una bolla di livello sul display OLED.
* **Equazione**:
   - Calcola gli angoli di pitch e roll utilizzando le seguenti formule:
     - Pitch: \(\text{Pitch} = \arctan\left(\frac{\text{Accelerazione Y}}{\text{Accelerazione Z}}\right)\)
     - Roll: \(\text{Roll} = \arctan\left(\frac{\text{Accelerazione X}}{\text{Accelerazione Z}}\right)\)
   - Converti questi angoli da radianti a gradi.
* **Implementazione del Codice**:
   - Configura le librerie per l'MPU6050 e l'OLED 1306.
   - Misura i valori di accelerazione sugli assi X, Y e Z.
   - Calcola gli angoli di pitch e roll in gradi.
   - Visualizza gli angoli calcolati di pitch e roll sull'OLED insieme a una rappresentazione visiva di una bolla che si muove all'interno di un rettangolo per indicare l'inclinazione.
* **Dimostrazione Pratica**:
   - Testa il sistema inclinando il sensore e osservando il movimento della bolla sul display OLED. Regola la sensibilità del movimento della bolla per rendere l'inclinometro più reattivo.
   - Assicurati che le letture siano accurate e che la bolla si muova fluidamente in base agli angoli di inclinazione.
* **Considerazioni Avanzate**:
   - Affronta la sfida dell'accelerometro che interpreta l'accelerazione e la decelerazione come inclinazione. Pensa a strategie per stabilizzare le letture e prevenire rilevazioni errate dell'inclinazione a causa di vibrazioni o movimenti.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
