.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_reed:

Interruttore Reed
======================

|img_reed|

L'interruttore Reed è un interruttore elettrico che funziona mediante un campo magnetico applicato. È stato inventato da Walter B. Ellwood dei Bell Telephone Laboratories nel 1936 e brevettato negli Stati Uniti il 27 giugno 1940, con il numero di brevetto 2264746.

Il principio di funzionamento di un interruttore Reed è molto semplice. Due lamelle (di solito realizzate in ferro e nichel, due metalli) che si sovrappongono alle estremità sono sigillate in un tubo di vetro, con le due lamelle che si sovrappongono e sono separate da un piccolo spazio (solo pochi micron). Il tubo di vetro è riempito con un gas inerte ad alta purezza (come l'azoto), e alcuni interruttori Reed sono realizzati per avere un vuoto all'interno per migliorare le loro prestazioni ad alta tensione.

Le lamelle fungono da conduttori di flusso magnetico. Le due lamelle non sono a contatto quando l'interruttore non è in funzione; quando passano attraverso un campo magnetico generato da un magnete permanente o da una bobina elettromagnetica, il campo magnetico applicato provoca la polarizzazione delle due lamelle vicino alle loro estremità, e quando la forza magnetica supera la forza elastica delle lamelle, queste vengono attratte tra loro, chiudendo il circuito; quando il campo magnetico si indebolisce o scompare, le lamelle si rilasciano a causa della loro elasticità, e le superfici di contatto si separano per aprire il circuito.

|img_reed_sche|

* `Reed Switch - Wikipedia <https://en.wikipedia.org/wiki/Reed_switch>`_


**Esempio**

* :ref:`py_reed` (For MicroPython User)
* :ref:`ar_reed` (For Arduino User)