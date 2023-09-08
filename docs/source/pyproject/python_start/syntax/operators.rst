Operatoren
============

Operatoren dienen zur Durchführung von Operationen auf Variablen und Werten.

* :ref:`Arithmetische Operatoren`

* :ref:`Zuweisungsoperatoren`

* :ref:`Vergleichsoperatoren`

* :ref:`Logische Operatoren`

* :ref:`Identitätsoperatoren`

* :ref:`Mitgliedschaftsoperatoren`

* :ref:`Bitweise Operatoren`

Arithmetische Operatoren
---------------------------
Mit arithmetischen Operatoren können Sie gängige mathematische Operationen durchführen.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Bezeichnung
    *   - ``+``
        - Addition
    *   - ``-``
        - Subtraktion
    *   - ``*``
        - Multiplikation
    *   - ``/``
        - Division
    *   - ``%``
        - Modulo
    *   - ``**``
        - Potenzierung
    *   - ``//``
        - Ganzzahlige Division



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

Zuweisungsoperatoren
---------------------

Zuweisungsoperatoren werden verwendet, um Werte Variablen zuzuweisen.

.. list-table:: 
    :widths: 10 30 30
    :header-rows: 1

    *   - Operator
        - Beispiel
        - Entsprechend
    *   - ``=``
        - a = 6
        - a = 6
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
        - a = a \*\* 6
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
        - a = a >> 6
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


Vergleichsoperatoren
------------------------
Vergleichsoperatoren werden verwendet, um zwei Werte miteinander zu vergleichen.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Bezeichnung
    *   - ``==``
        - Gleich
    *   - ``!=``
        - Ungleich
    *   - ``<``
        - Kleiner als
    *   - ``>``
        - Größer als
    *   - ``>=``
        - Größer oder gleich
    *   - ``<=``
        - Kleiner oder gleich




.. code-block:: python

    a = 6
    b = 8

    print(a > b)

>>> %Run test.py
False
>>> 

Gibt **False** zurück, weil **a** kleiner als **b** ist.

Logische Operatoren
-----------------------

Logische Operatoren werden verwendet, um Bedingungsanweisungen zu kombinieren.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Beschreibung
    *   - ``and``
        - Gibt True zurück, wenn beide Aussagen wahr sind
    *   - ``or``
        - Gibt True zurück, wenn eine der Aussagen wahr ist
    *   - ``not``
        - Kehrt das Ergebnis um, gibt False zurück, wenn das Ergebnis wahr ist

.. code-block:: python

    a = 6
    print(a > 2 and a < 8)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Identitätsoperatoren
------------------------

Identitätsoperatoren dienen zum Vergleich von Objekten, nicht ob sie gleich sind, sondern ob es sich tatsächlich um dasselbe Objekt mit demselben Speicherort handelt.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Beschreibung
    *   - ``is``
        - Gibt True zurück, wenn beide Variablen dasselbe Objekt sind
    *   - ``is not``
        - Gibt True zurück, wenn beide Variablen nicht dasselbe Objekt sind

.. code-block:: python

    a = ["hello", "welcome"]
    b = ["hello", "welcome"]
    c = a

    print(a is c)
    # Gibt True zurück, da c dasselbe Objekt wie a ist

    print(a is b)
    # Gibt False zurück, da a nicht dasselbe Objekt wie b ist, auch wenn sie denselben Inhalt haben

    print(a == b)
    # Gibt True zurück, da a gleich b ist

>>> %Run -c $EDITOR_CONTENT
True
False
True
>>> 


Mitgliedschaftsoperatoren
----------------------------
Mitgliedschaftsoperatoren werden verwendet, um zu testen, ob eine Sequenz in einem Objekt enthalten ist.

.. list-table:: 
    :widths: 10 30
    :header-rows: 1

    *   - Operator
        - Beschreibung
    *   - ``in``
        - Gibt True zurück, wenn eine Sequenz mit dem angegebenen Wert im Objekt vorhanden ist
    *   - ``not in``
        - Gibt True zurück, wenn eine Sequenz mit dem angegebenen Wert nicht im Objekt vorhanden ist

.. code-block:: python

    a = ["hello", "welcome", "Goodmorning"]

    print("welcome" in a)

>>> %Run -c $EDITOR_CONTENT
True
>>> 

Bitweise Operatoren
------------------------

Bitweise Operatoren werden zum Vergleichen von (binären) Zahlen verwendet.

.. list-table:: 
    :widths: 10 20 50
    :header-rows: 1

    *   - Operator
        - Name
        - Beschreibung
    *   - ``&``
        - UND
        - Setzt jedes Bit auf 1, wenn beide Bits 1 sind
    *   - ``|``
        - ODER
        - Setzt jedes Bit auf 1, wenn eines von zwei Bits 1 ist
    *   - ``^``
        - XOR
        - Setzt jedes Bit auf 1, wenn nur eines von zwei Bits 1 ist
    *   - ``~``
        - NICHT
        - Kehrt alle Bits um
    *   - ``<<``
        - Zero-fill Linksschiebung
        - Verschiebt nach links, indem von rechts Nullen eingefügt werden und die am weitesten links stehenden Bits herausfallen
    *   - ``>>``
        - Signierte Rechtsschiebung
        - Verschiebt nach rechts, indem Kopien des am weitesten links stehenden Bits von links eingefügt werden und die am weitesten rechts stehenden Bits herausfallen

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

