.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_thermistor:

Termistore
===============

|img_thermistor|

Un termistore è un tipo di resistore la cui resistenza è fortemente dipendente dalla temperatura, molto più di quanto accade nei resistori standard. Il termine è una combinazione delle parole "thermal" e "resistor". I termistori sono ampiamente utilizzati come limitatori di corrente di spunto, sensori di temperatura (tipicamente di tipo a coefficiente di temperatura negativo o NTC), protezioni autoripristinanti contro il sovracorrente e elementi riscaldanti autoregolanti (tipicamente di tipo a coefficiente di temperatura positivo o PTC).

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Ecco il simbolo elettronico del termistore.

|img_thermistor_symbol|

Esistono due tipi fondamentali opposti di termistori:

* Con i termistori NTC, la resistenza diminuisce all'aumentare della temperatura, solitamente a causa di un aumento degli elettroni di conduzione provocato dall'agitazione termica dalla banda di valenza. Un NTC è comunemente usato come sensore di temperatura, o in serie con un circuito come limitatore di corrente di spunto.
* Con i termistori PTC, la resistenza aumenta all'aumentare della temperatura, solitamente a causa delle maggiori agitazioni del reticolo termico, in particolare quelle dovute alle impurità e alle imperfezioni. I termistori PTC sono comunemente installati in serie con un circuito e utilizzati per proteggere dalle condizioni di sovracorrente, come fusibili ripristinabili.

In questo kit utilizziamo un termistore NTC. Ogni termistore ha una resistenza nominale. Qui è di 10k ohm, che viene misurata a 25 gradi Celsius.

Ecco la relazione tra la resistenza e la temperatura:

    RT = RN * expB(1/TK - 1/TN)   

* **RT** è la resistenza del termistore NTC quando la temperatura è TK. 
* **RN** è la resistenza del termistore NTC alla temperatura nominale TN. Qui, il valore numerico di RN è 10k.
* **TK** è una temperatura in Kelvin e l'unità è K. Qui, il valore numerico di TK è 273,15 + gradi Celsius.
* **TN** è una temperatura nominale in Kelvin; anche l'unità è K. Qui, il valore numerico di TN è 273,15 + 25.
* E **B(beta)**, la costante del materiale del termistore NTC, è anche chiamata indice di sensibilità termica con un valore numerico di 3950.      
* **exp** è l'abbreviazione di esponenziale, e la base e è un numero naturale pari a circa 2,7.

Converti questa formula TK=1/(ln(RT/RN)/B+1/TN) per ottenere la temperatura in Kelvin, a cui sottrarre 273,15 per ottenere i gradi Celsius.

Questa relazione è una formula empirica. È precisa solo quando la temperatura e la resistenza rientrano nell'intervallo effettivo.

.. Esempio
.. -------------------

.. :ref:`Termometro`


**Esempio**

* :ref:`py_temp` (For MicroPython User)
* :ref:`py_room_temp` (For MicroPython User)
* :ref:`ar_temp` (For Arduino User)