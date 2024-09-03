.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_led:

LED
==========

|img_led|

Il diodo emettitore di luce (LED) è un componente a semiconduttore che può convertire l'energia elettrica in energia luminosa attraverso giunzioni PN. In base alla lunghezza d'onda, può essere categorizzato in diodo laser, diodo emettitore di luce infrarossa e diodo emettitore di luce visibile, generalmente noto come LED.

Il diodo ha una conduttività unidirezionale, quindi la corrente fluirà come indicato dalla freccia nel simbolo del circuito. Puoi fornire solo il positivo all'anodo e il negativo al catodo. In questo modo, il LED si illuminerà.

|img_led_symbol|

Un LED ha due pin. Quello più lungo è l'anodo, mentre quello più corto è il catodo. Presta attenzione a non collegarli in modo inverso. Esiste una caduta di tensione diretta nel LED, quindi non può essere collegato direttamente al circuito, poiché la tensione di alimentazione potrebbe superare questa caduta e causare il danneggiamento del LED. La tensione diretta per i LED rossi, gialli e verdi è di 1,8 V, mentre quella per i LED bianchi è di 2,6 V. La maggior parte dei LED può sopportare una corrente massima di 20 mA, quindi è necessario collegare una resistenza limitatrice di corrente in serie.

La formula per calcolare il valore della resistenza è la seguente:

    R = (Vsupply – VD)/I

**R** rappresenta il valore della resistenza limitatrice di corrente, **Vsupply** la tensione di alimentazione, **VD** la caduta di tensione e **I** la corrente di lavoro del LED.

Ecco un'introduzione dettagliata sul LED: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.
.. **Example**

.. * :ref:`Hello, Breadboard!` (For MicroPython User)
.. * :ref:`fading_led_micropython` (For MicroPython User)
.. * :ref:`fading_led_arduino` (For C/C++(Arduino) User)
.. * :ref:`hello_led_arduino` (For C/C++(Arduino) User)

**Esempio**

* :ref:`py_led` (For MicroPython User)
* :ref:`py_fade` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_led` (For Arduino User)
* :ref:`ar_fade` (For Arduino User)
* :ref:`per_blink` (For Piper Make User)
* :ref:`per_button` (For Piper Make User)
* :ref:`per_service_bell` (For Piper Make User)
* :ref:`per_reversing_system` (For Piper Make User)
* :ref:`per_reaction_game` (For Piper Make User)