.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _syntax_list:

Listen
===================

Listen dienen dazu, mehrere Elemente in einer einzigen Variable zu speichern und werden mit eckigen Klammern erstellt:

.. code-block:: python

    B_Liste = ["Blossom", "Bubbles", "Buttercup"]
    print(B_Liste)


Listenelemente sind veränderbar, geordnet und erlauben doppelte Werte.
Die Elemente der Liste sind indiziert, wobei das erste Element den Index [0], das zweite den Index [1] usw. hat.

.. code-block:: python

    C_Liste = ["Rot", "Blau", "Grün", "Blau"]
    print(C_Liste)            # Duplikate erlaubt
    print(C_Liste[0]) 
    print(C_Liste[1])         # geordnet
    C_Liste[2] = "Lila"       # veränderbar
    print(C_Liste)

>>> %Run -c $EDITOR_CONTENT
['Rot', 'Blau', 'Grün', 'Blau']
Rot
Blau
['Rot', 'Blau', 'Lila', 'Blau']


Eine Liste kann unterschiedliche Datentypen enthalten:

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    print(A_Liste)

>>> %Run -c $EDITOR_CONTENT
['Banane', 255, False, 3.14]


Listenlänge
------------------
Um herauszufinden, wie viele Elemente in der Liste enthalten sind, verwenden Sie die Funktion len().

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    print(len(A_Liste))

>>> %Run -c $EDITOR_CONTENT
4

Listenelemente überprüfen
---------------------------

Drucken Sie das zweite Element der Liste aus:

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    print(A_Liste[1])

>>> %Run -c $EDITOR_CONTENT
[255]

Drucken Sie das letzte Element der Liste aus:

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    print(A_Liste[-1])

>>> %Run -c $EDITOR_CONTENT
[3.14]

Drucken Sie das zweite und dritte Element aus:

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    print(A_Liste[1:3])

>>> %Run -c $EDITOR_CONTENT
[255, False]


Listen-Elemente ändern
----------------------
Ändere das zweite und dritte Element:

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    A_Liste[1:3] = [True, "Orange"] 
    print(A_Liste)

>>> %Run -c $EDITOR_CONTENT
['Banane', True, 'Orange', 3.14]

Ersetze das zweite Element durch zwei Werte:

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14]
    A_Liste[1:2] = [True, "Orange"] 
    print(A_Liste)

>>> %Run -c $EDITOR_CONTENT
['Banane', True, 'Orange', False, 3.14]


Listenelemente hinzufügen
---------------------------

Mit der append()-Methode ein Element hinzufügen:

.. code-block:: python

    C_Liste = ["Rot", "Blau", "Grün"]
    C_Liste.append("Orange")
    print(C_Liste)

>>> %Run -c $EDITOR_CONTENT
['Rot', 'Blau', 'Grün', 'Orange']

Ein Element an der zweiten Position einfügen:

.. code-block:: python

    C_Liste = ["Rot", "Blau", "Grün"]
    C_Liste.insert(1, "Orange")
    print(C_Liste)

>>> %Run -c $EDITOR_CONTENT
['Rot', 'Orange', 'Blau', 'Grün']


Listenelemente entfernen
---------------------------

Die remove()-Methode entfernt das angegebene Element.

.. code-block:: python

    C_Liste = ["Rot", "Blau", "Grün"]
    C_Liste.remove("Blau")
    print(C_Liste)

>>> %Run -c $EDITOR_CONTENT
['Rot', 'Grün']

Die pop()-Methode entfernt das Element am angegebenen Index. Wenn kein Index angegeben wird, entfernt die pop()-Methode das letzte Element.

.. code-block:: python

    A_Liste = ["Banane", 255, False, 3.14, True, "Orange"]
    A_Liste.pop(1)
    print(A_Liste)
    A_Liste.pop()
    print(A_Liste)

>>> %Run -c $EDITOR_CONTENT
255
['Banane', False, 3.14, True, 'Orange']
'Orange'
['Banane', False, 3.14, True]

Das Schlüsselwort ``del`` entfernt ebenfalls den angegebenen Index:

.. code-block:: python

    C_Liste = ["Rot", "Blau", "Grün"]
    del C_Liste[1]
    print(C_Liste)

>>> %Run -c $EDITOR_CONTENT
['Rot', 'Grün']

Die clear()-Methode leert die Liste. Die Liste bleibt bestehen, hat aber keinen Inhalt mehr.

.. code-block:: python

    C_Liste = ["Rot", "Blau", "Grün"]
    C_Liste.clear()
    print(C_Liste)

>>> %Run -c $EDITOR_CONTENT
[]
