.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

lesson 48: Misurare la Rotazione Utilizzando i Giroscopi dell'MPU6050
=============================================================================

Questo tutorial tratta l'utilizzo del sensore MPU6050 con il Raspberry Pi Pico W per creare un inclinometro stabile combinando i dati dell'accelerometro e del giroscopio:

* **Setup**:
   - Collega l'MPU6050 al Raspberry Pi Pico W utilizzando lo schema fornito.
* **Concetto**:
   - Misura l'inclinazione utilizzando sia i dati dell'accelerometro che quelli del giroscopio.
   - Affronta gli errori causati dal rumore dell'accelerazione e dalla deriva del giroscopio.
* **Filtro Passa-Basso**:
   - Uniforma i dati dell'accelerometro per ridurre il rumore.
* **Integrazione del Giroscopio**:
   - Calcola gli angoli di inclinazione utilizzando la velocità di rotazione.
   - Aggiorna continuamente gli angoli di pitch, roll e yaw.
* **Combinazione dei Dati**:
   - Fonde i dati dell'accelerometro e del giroscopio per minimizzare rumore e deriva.
* **Compiti a Casa**:
   - Implementa e affina il metodo descritto per una misurazione stabile dell'inclinazione.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/XZIJasvCB44?si=hx0Ulyd0pTnro8sd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

