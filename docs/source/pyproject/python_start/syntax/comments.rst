.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Commenti
===============

I commenti nel codice ci aiutano a comprendere meglio il codice, rendono l'intero codice più leggibile e consentono di commentare parti del codice durante i test, in modo che tali parti non vengano eseguite.

Commento su una singola linea
---------------------------------

I commenti su una singola linea in MicroPython iniziano con # e il testo successivo viene considerato un commento fino alla fine della riga. I commenti possono essere posizionati prima o dopo il codice.

.. code-block:: python

    print("hello world") #This is a annotationhello world

>>> %Run -c $EDITOR_CONTENT
hello world

I commenti non sono necessariamente testo utilizzato per spiegare il codice. È anche possibile commentare parte del codice per impedire a MicroPython di eseguire quel codice.

.. code-block:: python

    #print("Can't run it！")
    print("hello world") #This is a annotationhello world

>>> %Run -c $EDITOR_CONTENT
hello world

Commento su più linee
------------------------------

Se vuoi commentare su più linee, puoi usare più segni #.

.. code-block:: python

    #This is a comment
    #written in
    #more than just one line
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Oppure, puoi utilizzare stringhe su più linee.

Poiché MicroPython ignora i letterali di stringa che non vengono assegnati a variabili, puoi aggiungere più linee di stringhe (triple virgolette) nel codice e inserire i commenti al loro interno:

.. code-block:: python

    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Finché la stringa non è assegnata a una variabile, MicroPython la ignorerà dopo aver letto il codice e la tratterà come se fosse un commento su più linee.

