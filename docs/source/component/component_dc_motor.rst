.. note::

    Ciao, benvenuto nella Community di SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_motor:

Motore DC
===================

|img_dc_motor|

Questo è un motore DC da 3V. Quando applichi un livello alto e uno basso a ciascuno dei 2 terminali, esso inizierà a ruotare.

* **Dimensioni**: 25*20*15MM
* **Tensione di funzionamento**: 1-6V
* **Corrente a vuoto** (3V): 70mA
* **Velocità a vuoto** (3V): 13000RPM
* **Corrente di stallo** (3V): 800mA
* **Diametro dell'albero**: 2mm

Il motore a corrente continua (DC) è un attuatore continuo che trasforma l'energia elettrica in energia meccanica. I motori DC fanno funzionare pompe rotative, ventilatori, compressori, giranti e altri dispositivi producendo una rotazione angolare continua.

Un motore DC è composto da due parti: la parte fissa del motore chiamata **statore** e la parte interna del motore chiamata **rotore** (o **indotto** di un motore DC) che ruota per produrre movimento.
Il segreto per generare movimento è posizionare l'indotto all'interno del campo magnetico del magnete permanente (il cui campo si estende dal polo nord al polo sud). L'interazione tra il campo magnetico e le particelle cariche in movimento (il filo attraversato da corrente genera il campo magnetico) produce la coppia che fa ruotare l'indotto.

|img_dc_motor_sche|

La corrente fluisce dal terminale positivo della batteria attraverso il circuito, attraverso le spazzole in rame fino al commutatore, e quindi all'indotto.
Ma a causa delle due interruzioni nel commutatore, questo flusso si inverte a metà di ogni rotazione completa.
Questa inversione continua trasforma essenzialmente la potenza DC della batteria in AC, permettendo all'indotto di sperimentare la coppia nella giusta direzione al momento giusto per mantenere la rotazione.

* `DC Motor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Fleming's left-hand rule for motors - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_



**Esempio**

* :ref:`py_motor` (For MicroPython User)
* :ref:`ar_motor` (For Arduino User)
* :ref:`per_smart_fan` (For Piper Make User)