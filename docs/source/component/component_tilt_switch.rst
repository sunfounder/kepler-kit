.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_tilt:

Interruttore a Inclinazione
=============================

|img_tilt| 

L'interruttore a inclinazione utilizzato qui è un modello a sfera con una piccola sfera metallica all'interno. Viene impiegato per rilevare inclinazioni di piccolo angolo.

Il principio di funzionamento è molto semplice. Quando l'interruttore viene inclinato di un certo angolo, la sfera all'interno rotola verso il basso e tocca i due contatti collegati ai pin esterni, attivando così i circuiti. Altrimenti, la sfera rimane lontana dai contatti, interrompendo i circuiti.

|img_tilt_symbol|

* `SW520D Tilt Switch Datasheet <https://www.tme.com/Document/f1e6cedd8cb7feeb250b353b6213ec6c/SW-520D.pdf>`_

.. * :ref:`Lettura del Valore del Pulsante`


**Esempio**

* :ref:`py_tilt` (For MicroPython User)
* :ref:`py_10_second` (For MicroPython User)
* :ref:`ar_tilt` (For Arduino User)
* :ref:`per_flowing_leds` (For Piper Make User)