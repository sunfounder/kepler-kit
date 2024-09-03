.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

If Else
==============

Il processo decisionale è necessario quando vogliamo eseguire un codice solo se una certa condizione è soddisfatta.

if
---------------------
.. code-block:: python

    if test expression:
        statement(s)

Qui, il programma valuta l'``espressione di test`` ed esegue l'``istruzione`` solo quando l'``espressione di test`` è Vera.

Se l'``espressione di test`` è Falsa, l'``istruzione(i)`` non verrà eseguita.

In MicroPython, l'indentazione definisce il corpo dell'istruzione ``if``. Il corpo inizia con un'indentazione e termina con la prima riga non indentata.

Python interpreta i valori diversi da zero come "Vero". None e 0 sono interpretati come "Falso".

**Diagramma di flusso dell'istruzione if**

.. image:: img/if_statement.png

**Esempio**

.. code-block:: python

    num = 8
    if num > 0:
        print(num, "is a positive number.")
    print("End with this line")

>>> %Run -c $EDITOR_CONTENT
8 is a positive number.
End with this line



if...else
-----------------------

.. code-block:: python

    if test expression:
        Body of if
    else:
        Body of else

L'istruzione ``if..else`` valuta l'``espressione di test`` ed eseguirà il corpo dell'``if`` solo quando la condizione di test è ``Vera``.

Se la condizione è ``Falsa``, viene eseguito il corpo dell'``else``. L'indentazione viene utilizzata per separare i blocchi.

**Diagramma di flusso dell'istruzione if...else**

.. image:: img/if_else.png

**Esempio**

.. code-block:: python

    num = -8
    if num > 0:
        print(num, "is a positive number.")
    else:
        print(num, "is a negative number.")

>>> %Run -c $EDITOR_CONTENT
-8 is a negative number.



if...elif...else
--------------------

.. code-block:: python

    if test expression:
        Body of if
    elif test expression:
        Body of elif
    else: 
        Body of else

``Elif`` è l'abbreviazione di ``else if``. Consente di verificare più espressioni.

Se la condizione dell'``if`` è Falsa, viene verificata la condizione del successivo blocco elif, e così via.

Se tutte le condizioni sono ``False``, viene eseguito il corpo dell'``else``.

Viene eseguito solo uno dei diversi blocchi ``if...elif...else`` in base alle condizioni.

Il blocco ``if`` può avere solo un blocco ``else``. Ma può avere più blocchi ``elif``.

**Diagramma di flusso dell'istruzione if...elif...else**

.. image:: img/if_elif_else.png

**Esempio**

.. code-block:: python

    x = 10
    y = 9

    if x > y:
        print("x is greater than y")
    elif x == y:
        print("x and y are equal")
    else:
        print("x is greater than y")

>>> %Run -c $EDITOR_CONTENT
x is greater than y


If annidati
---------------------

Possiamo inserire un'istruzione if all'interno di un'altra istruzione if, e in tal caso si parla di if annidati.

**Esempio**

.. code-block:: python

    x = 67

    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

>>> %Run -c $EDITOR_CONTENT
Above ten,
and also above 20!