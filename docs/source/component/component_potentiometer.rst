.. note::

    Ciao, benvenuto nella Community SunFounder per appassionati di Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_potentiometer:

Potenziometro
==================

|img_pot|

Il potenziometro è un componente resistivo con 3 terminali e il suo valore di resistenza può essere regolato in base a una variazione regolare.

I potenziometri sono disponibili in varie forme, dimensioni e valori, ma hanno tutti in comune le seguenti caratteristiche:

* Hanno tre terminali (o punti di connessione).
* Possiedono una manopola, una vite o un cursore che può essere spostato per variare la resistenza tra il terminale centrale e uno dei terminali esterni.
* La resistenza tra il terminale centrale e uno dei terminali esterni varia da 0 Ω alla resistenza massima del potenziometro mentre la manopola, la vite o il cursore vengono spostati.

Qui di seguito è riportato il simbolo del potenziometro nel circuito.

|img_pot_symbol|

Le funzioni del potenziometro nel circuito sono le seguenti:

#. Funzione di divisore di tensione

    Il potenziometro è una resistenza regolabile in modo continuo. Quando si regola l'albero o la maniglia scorrevole del potenziometro, il contatto mobile scivola sulla resistenza. In questo momento, può essere emessa una tensione a seconda della tensione applicata al potenziometro e dell'angolo a cui il braccio mobile è stato ruotato o del percorso che ha compiuto.

#. Funzione di reostato

    Quando il potenziometro viene utilizzato come reostato, collegare il pin centrale e uno degli altri 2 pin nel circuito. In questo modo è possibile ottenere un valore di resistenza che varia in modo fluido e continuo entro il percorso del contatto mobile.

#. Funzione di regolatore di corrente

    Quando il potenziometro agisce come regolatore di corrente, il terminale di contatto scorrevole deve essere collegato come uno dei terminali di uscita.

Se vuoi saperne di più sul potenziometro, consulta: `Potentiometro - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer.>`_

.. Esempio
.. -------------------

.. * :ref:`Turn the Knob` (Per utenti MicroPython)
.. * :ref:`Table Lamp` (Per utenti C/C++(Arduino))


**Esempio**

* :ref:`py_pot` (For MicroPython User)
* :ref:`ar_pot` (For Arduino User)
* :ref:`per_swing_servo` (For Piper Make User)