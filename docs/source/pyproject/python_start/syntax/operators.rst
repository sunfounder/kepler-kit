.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Operatori
==============

Gli operatori vengono utilizzati per eseguire operazioni su variabili e valori.

* :ref:`Arithmetic operators`

* :ref:`Assignment operators`

* :ref:`Comparison operators`

* :ref:`Logical operators`

* :ref:`Identity operators`

* :ref:`Membership operators`

* :ref:`Bitwise operators`

Operatori aritmetici
------------------------

Puoi utilizzare gli operatori aritmetici per eseguire alcune operazioni matematiche comuni.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operatore
        - Nome
    *   - ``+``
        - Addizione
    *   - ``-``
        - Sottrazione
    *   - ``*``
        - Moltiplicazione
    *   - ``/``
        - Divisione
    *   - ``%``
        - Modulo
    *   - ``**``
        - Esponenziazione
    *   - ``//``
        - Divisione intera



.. code-block:: python

    x = 5
    y = 3

    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x % y
    f = x ** y
    g = x // y

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)

>>> %Run -c $EDITOR_CONTENT
8
2
15
1.666667
2
125
1
8
2
15
>>> 

Operatori di assegnazione
----------------------------

Gli operatori di assegnazione vengono utilizzati per assegnare valori alle variabili.

.. list-table:: 
    :widths: 10 30 30
    :header-rows: 1

    *   - Operatore
        - Esempio
        - Equivalente a
    *   - ``=``
        - a = 6
        - a =6
    *   - ``+=``
        - a += 6
        - a = a + 6
    *   - ``-=``
        - a -= 6
        - a = a - 6
    *   - ``*=``
        - a \*= 6
        - a = a * 6
    *   - ``/=``
        - a /= 6
        - a = a / 6
    *   - ``%=``
        - a %= 6
        - a = a % 6
    *   - ``**=``
        - a \*\*= 6
        - a = a ** 6
    *   - ``//=``
        - a //= 6
        - a = a // 6
    *   - ``&=``
        - a &= 6
        - a = a & 6
    *   - ``|=``
        - a \|= 6
        - a = a | 6
    *   - ``^=``
        - a ^= 6
        - a = a ^ 6
    *   - ``>>=``
        - a >>= 6
        - a = a \>\> 6
    *   - ``<<=``
        - a <<= 6
        - a = a << 6



.. code-block:: python

    a = 6

    a *= 6
    print(a)

>>> %Run test.py
36
>>> 

Operatori di confronto
--------------------------

Gli operatori di confronto vengono utilizzati per confrontare due valori.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operatore
        - Nome
    *   - ``==``
        - Uguale
    *   - ``!=``
        - Diverso
    *   - ``<``
        - Minore di
    *   - ``>``
        - Maggiore di
    *   - ``>=``
        - Maggiore o uguale a
    *   - ``<=``
        - Minore o uguale a




.. code-block:: python

    a = 6
    b = 8

    print(a>b)

>>> %Run test.py
False
>>> 

Restituisce **False**, perché **a** è minore di **b**.

Operatori logici
--------------------

Gli operatori logici vengono utilizzati per combinare dichiarazioni condizionali.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operatore
        - Descrizione
    *   - ``and``
        - Restituisce True se entrambe le dichiarazioni sono vere
    *   - ``or``
        - Restituisce True se una delle dichiarazioni è vera
    *   - ``not``
        - Inverte il risultato, restituisce False se il risultato è vero

.. code-block:: python

    a = 6
    print(a > 2 and a < 8)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Operatori di identità
-------------------------

Gli operatori di identità vengono utilizzati per confrontare gli oggetti, non se sono uguali, ma se sono effettivamente lo stesso oggetto, con la stessa posizione in memoria.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operatore
        - Descrizione
    *   - ``is``
        - Restituisce True se entrambe le variabili sono lo stesso oggetto
    *   - ``is not``
        - Restituisce True se entrambe le variabili non sono lo stesso oggetto

.. code-block:: python

    a = ["hello", "welcome"]
    b = ["hello", "welcome"]
    c = a

    print(a is c)
    # restituisce True perché c è lo stesso oggetto di a

    print(a is b)
    # restituisce False perché a non è lo stesso oggetto di b, anche se hanno lo stesso contenuto

    print(a == b)
    # restituisce True perché a è uguale a b

>>> %Run -c $EDITOR_CONTENT
True
False
True
>>> 

Operatori di appartenenza
------------------------------

Gli operatori di appartenenza vengono utilizzati per verificare se una sequenza è presente in un oggetto.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operatore
        - Descrizione
    *   - ``in``
        - Restituisce True se una sequenza con il valore specificato è presente nell'oggetto
    *   - ``not in``
        - Restituisce True se una sequenza con il valore specificato non è presente nell'oggetto

.. code-block:: python

    a = ["hello", "welcome", "Goodmorning"]

    print("welcome" in a)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Operatori bit a bit
------------------------

Gli operatori bit a bit vengono utilizzati per confrontare numeri (binari).

.. list-table:: 
    :widths: 10 20 50
    :header-rows: 1

    *   - Operatore
        - Nome
        - Descrizione
    *   - ``&``
        - AND
        - Imposta ogni bit a 1 se entrambi i bit sono 1
    *   - ``|``
        - OR
        - Imposta ogni bit a 1 se uno dei due bit è 1
    *   - ``^``
        - XOR
        - Imposta ogni bit a 1 se solo uno dei due bit è 1
    *   - ``~``
        - NOT
        - Inverte tutti i bit
    *   - ``<<``
        - Shift a sinistra con riempimento di zeri
        - Sposta a sinistra inserendo zeri da destra e fa cadere i bit più a sinistra
    *   - ``>>``
        - Shift a destra con segno
        - Sposta a destra inserendo copie del bit più a sinistra da sinistra, e fa cadere i bit più a destra

.. code-block:: python

    num = 2

    print(num & 1)
    print(num | 1)
    print(num << 1)

>>> %Run -c $EDITOR_CONTENT
0
3
4
>>>