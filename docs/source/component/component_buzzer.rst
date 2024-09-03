.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_buzzer:

Cicalino
============


Il cicalino è un tipo di dispositivo elettronico con una struttura integrata, alimentato da corrente continua, ampiamente utilizzato in computer, stampanti, fotocopiatrici, allarmi, giocattoli elettronici, dispositivi elettronici per automobili, telefoni, timer e altri prodotti elettronici o dispositivi vocali.

I cicalini possono essere suddivisi in due categorie: attivi e passivi (vedi l'immagine seguente). Se si gira il cicalino in modo che i pin siano rivolti verso l'alto, quello con una scheda verde è un cicalino passivo, mentre quello racchiuso in un nastro nero è un cicalino attivo.

|img_buzzer|

La differenza tra un cicalino attivo e uno passivo:

Un cicalino attivo ha una sorgente di oscillazione integrata, quindi emetterà suoni una volta alimentato. Un cicalino passivo, invece, non dispone di una tale sorgente e non emetterà alcun suono se si utilizza una corrente continua; è necessario utilizzare onde quadre con una frequenza compresa tra 2K e 5K per farlo funzionare. Il cicalino attivo è spesso più costoso di quello passivo a causa dei vari circuiti oscillanti integrati.

Di seguito è riportato il simbolo elettrico di un cicalino. Ha due pin con poli positivo e negativo. Il simbolo + sulla superficie indica l'anodo, mentre l'altro è il catodo.

|img_buzzer_symbol|

Puoi controllare i pin del cicalino, quello più lungo è l'anodo e quello più corto è il catodo. Non invertire le connessioni, altrimenti il cicalino non emetterà suoni.

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Esempio
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**Esempio**

* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)
* :ref:`per_service_bell` (For Piper Make User)
* :ref:`per_reversing_system` (For Piper Make User)
* :ref:`per_reaction_game` (For Piper Make User)