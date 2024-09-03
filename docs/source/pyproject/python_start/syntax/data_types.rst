.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Tipi di Dati
===============

Tipi di Dati Incorporati
----------------------------
MicroPython dispone dei seguenti tipi di dati:

* Tipo Testo: str
* Tipi Numerici: int, float, complex
* Tipi Sequenza: list, tuple, range
* Tipo Mappatura: dict
* Tipi Set: set, frozenset
* Tipo Booleano: bool
* Tipi Binari: bytes, bytearray, memoryview

Ottenere il Tipo di Dato
-----------------------------
Puoi ottenere il tipo di dato di qualsiasi oggetto utilizzando la funzione ``type()``:



.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

Impostare il Tipo di Dato
------------------------------
In MicroPython non è necessario impostare esplicitamente il tipo di dato, poiché viene determinato automaticamente quando assegni un valore alla variabile.



.. code-block:: python

    x = "welcome"
    y = 45
    z = ["apple", "banana", "cherry"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>> 

Impostare un Tipo di Dato Specifico
------------------------------------------

Se desideri specificare il tipo di dato, puoi utilizzare le seguenti funzioni costruttore:

.. list-table:: 
    :widths: 25 10
    :header-rows: 1

    *   - Esempio
        - Tipo di Dato
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hello World")
        - str
    *   - x = list(("apple", "banana", "cherry"))
        - list
    *   - x = tuple(("apple", "banana", "cherry"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("apple", "banana", "cherry"))
        - set
    *   - x = frozenset(("apple", "banana", "cherry"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

Puoi stamparne alcuni per vedere il risultato.



.. code-block:: python

    a = float(20.5)
    b = list(("apple", "banana", "cherry"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['apple', 'banana', 'cherry']
True
>>> 

Conversione di Tipo
-------------------------
Puoi convertire un tipo di dato in un altro usando i metodi int(), float() e complex():
La conversione in Python si effettua quindi utilizzando funzioni costruttore:

* int() - costruisce un numero intero a partire da un letterale intero, un letterale float (rimuovendo tutte le cifre decimali) o un letterale stringa (purché la stringa rappresenti un numero intero)
* float() - costruisce un numero float a partire da un letterale intero, un letterale float o un letterale stringa (purché la stringa rappresenti un numero intero o un float)
* str() - costruisce una stringa da un'ampia varietà di tipi di dati, inclusi stringhe, letterali interi e letterali float



.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

Nota: Non puoi convertire numeri complessi in un altro tipo di numero.
