.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_74hc595:

74HC595
===========

|img_74hc595|

Il 74HC595 è composto da un registro a scorrimento a 8 bit e un registro di memoria con uscite parallele a tre stati. Converte l'input seriale in output parallelo, permettendoti di risparmiare le porte IO di un MCU.

* Quando MR (pin10) è a livello alto e OE (pin13) è a livello basso, i dati vengono inseriti sul fronte di salita di SHcp e vanno al registro di memoria attraverso il fronte di salita di SHcp.
* Se i due clock sono collegati insieme, il registro a scorrimento è sempre un impulso in anticipo rispetto al registro di memoria.
* Nel registro di memoria sono presenti un pin di ingresso a scorrimento seriale (Ds), un pin di uscita seriale (Q) e un pulsante di reset asincrono (livello basso).
* Il registro di memoria emette un bus parallelo a 8 bit e in tre stati.
* Quando OE è abilitato (livello basso), i dati nel registro di memoria vengono emessi al bus (Q0 ~ Q7).

* `74HC595 Datasheet <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

|img_74jc595_pin|

Pin del 74HC595 e loro funzioni:

* **Q0-Q7**: Pin di uscita dati paralleli a 8 bit, in grado di controllare direttamente 8 LED o 8 pin di un display a 7 segmenti.
* **Q7'**: Pin di uscita seriale, collegato a DS di un altro 74HC595 per connettere più 74HC595 in serie.
* **MR**: Pin di reset, attivo a livello basso.
* **SHcp**: Ingresso della sequenza temporale del registro a scorrimento. Sul fronte di salita, i dati nel registro a scorrimento si spostano successivamente di un bit, ovvero i dati in Q1 si spostano in Q2, e così via. Sul fronte di discesa, i dati nel registro a scorrimento rimangono invariati.
* **STcp**: Ingresso della sequenza temporale del registro di memoria. Sul fronte di salita, i dati nel registro a scorrimento vengono trasferiti al registro di memoria.
* **CE**: Pin di abilitazione dell'uscita, attivo a livello basso.
* **DS**: Pin di ingresso dati seriali.
* **VCC**: Tensione di alimentazione positiva.
* **GND**: Massa.

.. Esempio
.. -------------------

.. :ref:`Microchip - :ref:`cpn_74hc595``

**Esempio**

* :ref:`py_74hc_led` (For MicroPython User)
* :ref:`py_74hc_7seg` (For MicroPython User)
* :ref:`py_74hc_4dig` (For MicroPython User)
* :ref:`py_74hc_788bs` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`py_10_second` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`py_bubble_level` (For MicroPython User)
* :ref:`ar_74hc_led` (For Arduino User)
* :ref:`ar_74hc_7seg` (For Arduino User)
* :ref:`ar_74hc_4dig` (For Arduino User)
* :ref:`ar_74hc_788bs` (For Arduino User)