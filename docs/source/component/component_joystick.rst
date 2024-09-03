.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_joystick:

Modulo Joystick
=======================

|img_joystick_pic|

L'idea di base di un joystick è quella di tradurre il movimento di una leva in informazioni elettroniche che un computer può elaborare.

Per comunicare al computer una gamma completa di movimenti, 
un joystick deve misurare la posizione della leva su due assi: l'asse X (da sinistra a destra) e l'asse Y (su e giù). 
Proprio come nella geometria di base, le coordinate X-Y determinano esattamente la posizione della leva.

Per determinare la posizione della leva, il sistema di controllo del joystick monitora semplicemente la posizione di ciascun asse. 
Il design convenzionale del joystick analogico fa questo con due potenziometri, o resistori variabili.

Il joystick ha anche un ingresso digitale che si attiva quando il joystick viene premuto.

|img_joystick|


*  `Joystick - Wikipedia <https://en.wikipedia.org/wiki/Analog_stick>`_


**Esempio**


* :ref:`py_joystick` (Per utenti MicroPython)
* :ref:`ar_joystick` (Per utenti Arduino)
