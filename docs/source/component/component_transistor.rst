.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_transistor:

Transistor
============

|img_NPN&PNP|

Il transistor è un dispositivo a semiconduttore che controlla la corrente tramite la corrente. Funziona amplificando un segnale debole in un segnale di ampiezza maggiore ed è utilizzato anche come interruttore senza contatto.

Un transistor è una struttura a tre strati composta da semiconduttori di tipo P e N. Questi formano le tre regioni interne. La regione centrale, più sottile, è la base; le altre due sono entrambe di tipo N o P: la regione più piccola con una maggioranza intensa di portatori è l'emettitore, mentre l'altra è il collettore. Questa composizione consente al transistor di agire come amplificatore. Da queste tre regioni derivano tre terminali, che sono base (b), emettitore (e) e collettore (c). Formano due giunzioni P-N, cioè la giunzione dell'emettitore e la giunzione del collettore. La direzione della freccia nel simbolo del circuito del transistor indica quella della giunzione dell'emettitore.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

In base al tipo di semiconduttore, i transistor possono essere divisi in due gruppi: NPN e PNP. Dall'abbreviazione, possiamo dedurre che il primo è composto da due semiconduttori di tipo N e uno di tipo P, mentre il secondo è l'opposto. Vedi la figura sotto.

.. note::
    s8550 è un transistor PNP e s8050 è un transistor NPN. Sono molto simili e bisogna fare attenzione nell'identificare le loro etichette.

|img_transistor_symbol|

Quando un segnale ad alto livello passa attraverso un transistor NPN, esso si attiva. Ma un transistor PNP richiede un segnale a basso livello per funzionare. Entrambi i tipi di transistor sono spesso utilizzati per interruttori senza contatto, come in questo esperimento.


* `S8050 Transistor Datasheet <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

Con l'etichetta rivolta verso di noi e i pin rivolti verso il basso, i pin da sinistra a destra sono: emettitore (e), base (b) e collettore (c).

|img_ebc|

.. note::
    * La base è il dispositivo di controllo della corrente per l'alimentazione elettrica più grande.
    * Nel transistor NPN, il collettore è l'alimentazione elettrica più grande e l'emettitore è l'uscita per tale alimentazione, mentre nel transistor PNP è esattamente l'opposto.

.. Esempio
.. -------------------

.. :ref:`Due Tipi di Transistor`

**Esempio**

* :ref:`py_transistor` (For MicroPython User)
* :ref:`py_relay` (For MicroPython User)
* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)
* :ref:`ar_transistor` (For Arduino User)
* :ref:`ar_relay` (For Arduino User)
* :ref:`per_service_bell` (For Piper Make User)
* :ref:`per_reversing_system` (For Piper Make User)
* :ref:`per_reaction_game` (For Piper Make User)