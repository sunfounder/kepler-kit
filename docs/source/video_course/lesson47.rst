.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 47: Migliorare i Dati dei Sensori con un Filtro Passa-Basso
=============================================================================
Questo tutorial tratta l'utilizzo del sensore MPU6050 con il Raspberry Pi Pico W per creare un inclinometro a due assi stabile implementando un filtro passa-basso:

* **Setup**:
   - Collega l'MPU6050 al Raspberry Pi Pico W utilizzando lo schema fornito.

* **Concetto**:
   - Misura l'inclinazione utilizzando i dati dell'accelerometro dell'MPU6050 per calcolare gli angoli di pitch e roll.
   - Affronta gli errori causati dall'interpretazione dell'accelerazione come inclinazione.

* **Filtro Passa-Basso**:
   - Implementa un filtro passa-basso per uniformare i dati e ridurre il rumore.
   - Equazione: \(\text{nuovo valore} = \text{confidence sensore} \times \text{misura} + (1 - \text{confidence sensore}) \times \text{vecchio valore}\)
   - Regola il valore di confidence per trovare il miglior equilibrio tra reattività e riduzione del rumore.

* **Codice**:
   - Configura l'MPU6050 per misurare le accelerazioni sugli assi X, Y e Z.
   - Calcola e filtra gli angoli di pitch e roll.
   - Visualizza i valori filtrati.

* **Compiti a Casa**:
   - Implementa e testa il filtro passa-basso.
   - Sperimenta con diversi valori di confidence.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
