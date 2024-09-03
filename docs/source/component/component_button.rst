.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_button:

Pulsante
============

|img_button|

I pulsanti sono componenti comuni utilizzati per controllare dispositivi elettronici. Sono generalmente usati come interruttori per collegare o interrompere i circuiti. Anche se i pulsanti sono disponibili in diverse dimensioni e forme, quello utilizzato qui è un mini-pulsante da 6 mm come mostrato nelle immagini seguenti.
Il pin 1 è collegato al pin 2 e il pin 3 al pin 4. Quindi è sufficiente collegare uno qualsiasi dei pin 1 e 2 al pin 3 o 4.

Di seguito è riportata la struttura interna di un pulsante. Il simbolo a destra in basso viene solitamente utilizzato per rappresentare un pulsante nei circuiti.

|img_button_symbol|

Poiché il pin 1 è collegato al pin 2 e il pin 3 al pin 4, quando il pulsante viene premuto, i 4 pin vengono collegati, chiudendo così il circuito.

|img_button2|

.. Esempi
.. -------------------

.. :ref:`Lettura del valore del pulsante`

**Esempio**

* :ref:`py_button` (For MicroPython User)
* :ref:`ar_button` (For Arduino User)
* :ref:`per_button` (For Piper Make User)
* :ref:`per_rainbow_light` (For Piper Make User)
* :ref:`per_drum_kit` (For Piper Make User)
* :ref:`per_reaction_game` (For Piper Make User)