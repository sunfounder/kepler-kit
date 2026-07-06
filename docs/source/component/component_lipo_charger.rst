.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_lipo_charger:

Modulo Caricatore Li-po
=================================================


|lipo_module|

Questo è un modulo caricatore Li-po progettato per Raspberry Pi Pico/Pico H/Pico W. Basta collegarlo e inserire il Pico nel breadboard come mostrato di seguito, quindi connettere la batteria all'altra estremità e sei pronto per usarlo.

Quando colleghi il Pico W con un cavo USB a un computer o a una presa, la spia del modulo caricatore Li-po si accende, indicando che la batteria verrà caricata contemporaneamente. Quando scolleghi il cavo USB, il Pico W sarà alimentato dalla batteria, così il tuo progetto potrà continuare a funzionare.


.. note::
    Per alcuni computer con prestazioni scarse, a volte se colleghi il tuo Pico W al computer con questo modulo di ricarica collegato, potrebbe causare il mancato riconoscimento del Pico W da parte del computer.

    Il motivo è che dopo il collegamento, durante la ricarica della batteria, la tensione della porta USB si abbassa, causando un'alimentazione insufficiente al Pico W per essere riconosciuto dal computer.
    
    In questo caso, è necessario scollegare il modulo di ricarica Li-Po e poi ricollegare il Pico W.

|lipo_wire|

**Caratteristiche**

* Tensione di ingresso: 5V
* Tensione di uscita: 3.3V
* Dimensioni: 20mmx7mm
* Modello di interfaccia: PH2.0
* È disponibile un portabatterie da 1A abbinato e una Power Pack da 800mAh da utilizzare insieme.


**Schema**

|sch_lipo_charger|
