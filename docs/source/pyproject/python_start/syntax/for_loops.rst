.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _syntax_forloop:

Cicli For
==============

Il ciclo ``for`` può attraversare qualsiasi sequenza di elementi, come una lista o una stringa.

Il formato sintattico del ciclo for è il seguente:

.. code-block:: python

    for val in sequence:
        Body of for


Qui, ``val`` è una variabile che ottiene il valore dell'elemento nella sequenza in ciascuna iterazione.

Il ciclo continua fino a quando non raggiungiamo l'ultimo elemento della sequenza. Usa l'indentazione per separare il corpo del ciclo ``for`` dal resto del codice.

**Diagramma di flusso del ciclo for**

.. image:: img/for_loop.png




.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 10

L'istruzione break
-------------------------

Con l'istruzione break possiamo interrompere il ciclo prima che 
abbia attraversato tutti gli elementi:



.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        if sum == 6:
            break
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 6

L'istruzione continue
--------------------------------------------

Con l'istruzione ``continue`` possiamo interrompere l'iterazione corrente del ciclo e continuare con la successiva:



.. code-block:: python

    numbers = [1, 2, 3, 4]

    for val in numbers:
        if val == 3:
            continue
        print(val)

>>> %Run -c $EDITOR_CONTENT
1
2
4

La funzione range()
--------------------------------------------

Possiamo usare la funzione range() per generare una sequenza di numeri. range(6) produrrà numeri tra 0 e 5 (6 numeri).

Possiamo anche definire inizio, fine e passo come range(inizio, fine, passo). Se non specificato, il passo predefinito è 1.

In un certo senso, l'oggetto range è "pigro" perché quando creiamo l'oggetto, non genera ogni numero che "contiene". Tuttavia, questo non è un iteratore perché supporta le operazioni in, len e ``__getitem__``.

Questa funzione non memorizzerà tutti i valori in memoria; sarebbe inefficiente. Quindi ricorderà l'inizio, la fine, il passo e genererà il numero successivo durante il percorso.

Per forzare questa funzione a restituire tutti gli elementi, possiamo usare la funzione list().



.. code-block:: python

    print(range(6))

    print(list(range(6)))

    print(list(range(2, 6)))

    print(list(range(2, 10, 2)))

>>> %Run -c $EDITOR_CONTENT
range(0, 6)
[0, 1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 4, 6, 8]


Possiamo usare ``range()`` in un ciclo ``for`` per iterare su una sequenza di numeri. Può essere combinato con la funzione len() per usare l'indice e attraversare la sequenza.



.. code-block:: python

    fruits = ['pear', 'apple', 'grape']

    for i in range(len(fruits)):
        print("I like", fruits[i])
        
>>> %Run -c $EDITOR_CONTENT
I like pear
I like apple
I like grape

Else nel ciclo For
--------------------------------

Il ciclo ``for`` può anche avere un blocco ``else`` opzionale. Se gli elementi nella sequenza utilizzata per il ciclo sono esauriti, viene eseguita la parte ``else``.

La parola chiave ``break`` può essere utilizzata per interrompere il ciclo ``for``. In questo caso, la parte ``else`` verrà ignorata.

Pertanto, se non si verifica alcuna interruzione, verrà eseguita la parte ``else`` del ciclo ``for``.



.. code-block:: python

    for val in range(5):
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1
2
3
4
Finito

Il blocco else NON verrà eseguito se il ciclo viene interrotto da un'istruzione break.



.. code-block:: python


    for val in range(5):
        if val == 2: break
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1

