.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_syntax_while:

While Loops
====================

L'istruzione ``while`` viene utilizzata per eseguire un programma in un ciclo, ovvero per eseguire un programma in un loop sotto determinate condizioni per gestire lo stesso compito che deve essere ripetutamente processato.

La sua forma di base è:

.. code-block:: python

    while test expression:
        Body of while


Nel ciclo ``while``, viene prima verificata l'espressione di test (``test expression``). Solo quando l'espressione di test restituisce ``True``, si entra nel corpo del ciclo while. Dopo una iterazione, l'espressione di test viene controllata nuovamente. Questo processo continua fino a quando l'espressione di test non restituisce ``False``.

In MicroPython, il corpo del ciclo ``while`` è determinato dall'indentazione.

Il corpo inizia con un'indentazione e termina con la prima riga non indentata.

Python interpreta qualsiasi valore diverso da zero come ``True``. None e 0 sono interpretati come ``False``.

**Diagramma di Flusso del ciclo while**

.. image:: img/while_loop.png



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1


Break Statement
--------------------

Con l'istruzione break possiamo interrompere il ciclo anche se la condizione del while è vera:



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        if x == 6:
            break
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6

Ciclo While con Else
----------------------
Come il ciclo ``if``, anche il ciclo ``while`` può avere un blocco ``else`` opzionale.

Se la condizione nel ciclo ``while`` viene valutata come ``False``, viene eseguita la parte ``else``.



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1
    else:
        print("Game Over")

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1
Game Over