.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_l293d:

IC L293D 
=================

|img_l293d0|

L293D è un driver motore a 4 canali integrato con chip ad alta tensione e alta corrente. 
È progettato per connettersi ai livelli logici standard DTL, TTL e pilotare carichi induttivi (come bobine di relè, motori DC, Stepper Motor) e transistor di commutazione di potenza, ecc. 
I motori DC sono dispositivi che trasformano l'energia elettrica continua in energia meccanica. Sono ampiamente utilizzati nella trasmissione elettrica per la loro eccellente prestazione nella regolazione della velocità.

Guarda la figura dei pin qui sotto. L293D ha due pin (Vcc1 e Vcc2) per l'alimentazione. 
Vcc2 viene utilizzato per alimentare il motore, mentre Vcc1 per alimentare il chip. Poiché qui viene utilizzato un motore DC di piccole dimensioni, collega entrambi i pin a +5V.

|img_l293d1| 

Di seguito è riportata la struttura interna di L293D. 
Il pin EN è un pin di abilitazione e funziona solo con livello alto; A sta per ingresso e Y per uscita. 
Puoi vedere la relazione tra loro in basso a destra. 
Quando il pin EN è a livello alto, se A è alto, Y emette un livello alto; se A è basso, Y emette un livello basso. Quando il pin EN è a livello basso, L293D non funziona.

|img_l293d2|

* `L293D Datasheet <https://cdn-shop.adafruit.com/datasheets/l293d.pdf>`_

**Esempio**

* :ref:`py_motor` (For MicroPython User)
* :ref:`ar_motor` (For Arduino User)
* :ref:`py_pump` (For MicroPython User)
* :ref:`ar_pump` (For Arduino User)
* :ref:`per_smart_fan` (For Piper Make User)