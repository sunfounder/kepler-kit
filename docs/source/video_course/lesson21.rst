.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti a noi oggi stesso!

lezione 21: Misurazioni di Temperatura e Umidità con Interruttore a Pulsante
================================================================================

Questo tutorial spiega come aggiungere un pulsante a bilanciere per alternare tra le letture della temperatura in Fahrenheit e Celsius utilizzando il sensore DHT11 con il Raspberry Pi Pico W:

* **Introduzione**: Introduce il tutorial e ringrazia lo sponsor, SunFounder. Spiega l'obiettivo di aggiungere un pulsante a bilanciere al sistema esistente di misurazione della temperatura e dell'umidità.

* **Riepilogo delle Lezioni Precedenti**: Ripassa la lezione precedente sull'utilizzo del sensore DHT11 e fornisce il contesto per il compito attuale.

**Introduzione ai Componenti e Configurazione del Circuito**:
- Reintroduce il sensore DHT11 e spiega l'aggiunta di un pulsante al circuito.
- Descrive i collegamenti:
  - Sensore DHT11:
    - Pin 1 a 3,3V
    - Pin 2 al pin GPIO 16
    - Pin 4 a massa
  - Pulsante:
    - Una gamba a massa
    - L'altra gamba al pin GPIO 15
* **Spiegazione del Codice**:
  - Importa le librerie necessarie: machine, utime (come time) e DHT.
  - Configura i pin GPIO per il sensore DHT11 e il pulsante.
  - Crea un meccanismo di alternanza per passare tra le unità di temperatura (Celsius e Fahrenheit).
  - Legge lo stato del pulsante e alterna l'unità di temperatura quando il pulsante viene premuto e rilasciato.
  - Misura e converte la temperatura da Celsius a Fahrenheit.
  - Stampa le letture di temperatura e umidità in una singola riga utilizzando `\r` per un output pulito.
  - Affronta i problemi di formattazione per garantire che l'output venga visualizzato correttamente durante il passaggio tra Celsius e Fahrenheit.
* **Dimostrazione Pratica**:
  - Esegue il codice per osservare le letture di temperatura e umidità.
  - Dimostra la funzionalità di alternanza tra Celsius e Fahrenheit quando il pulsante viene premuto.
  - Risolve i problemi di formattazione per garantire un output pulito e coerente.
* **Compito per Casa**:
  - Aggiunge più funzionalità di alternanza al progetto.
  - Implementa ulteriori opzioni per alternare tra la visualizzazione della temperatura in Celsius, Fahrenheit e umidità una alla volta.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MrfIfndX7OM?si=d1WrCY-6Ui7J2DWb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

