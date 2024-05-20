.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

For-Schleifen
================

Die ``for``-Schleife kann über jede Sequenz von Elementen iterieren, beispielsweise über eine Liste oder einen String.

Die Syntax einer ``for``-Schleife ist wie folgt:

.. code-block:: python

    for val in sequenz:
        Schleifenkörper

Hierbei ist ``val`` eine Variable, die in jeder Iteration den Wert des Elements aus der Sequenz annimmt.

Die Schleife wird solange ausgeführt, bis das letzte Element der Sequenz erreicht ist. Durch Einrückung wird der Schleifenkörper vom restlichen Code abgegrenzt.

**Flussdiagramm der for-Schleife**

.. image:: img/for_loop.png



.. code-block:: python

    zahlen = [1, 2, 3, 4]
    summe = 0

    for val in zahlen:
        summe = summe+val
        
    print("Die Summe beträgt", summe)

>>> %Run -c $EDITOR_CONTENT
Die Summe beträgt 10

Die break-Anweisung
-------------------------

Mit der ``break``-Anweisung kann die Schleife beendet werden, bevor alle Elemente durchlaufen wurden:



.. code-block:: python

    zahlen = [1, 2, 3, 4]
    summe = 0

    for val in zahlen:
        summe = summe+val
        if summe == 6:
            break
    print("Die Summe beträgt", summe)

>>> %Run -c $EDITOR_CONTENT
Die Summe beträgt 6

Die continue-Anweisung
--------------------------------------------

Mit der ``continue``-Anweisung kann die aktuelle Iteration der Schleife beendet und mit der nächsten fortgefahren werden:



.. code-block:: python

    zahlen = [1, 2, 3, 4]

    for val in zahlen:
        if val == 3:
            continue
        print(val)

>>> %Run -c $EDITOR_CONTENT
1
2
4

Die range()-Funktion
--------------------------------------------

Mit der ``range()``-Funktion kann eine Zahlenreihe erzeugt werden. ``range(6)`` erzeugt Zahlen von 0 bis 5 (6 Zahlen insgesamt).

Man kann auch Start, Ende und Schrittgröße definieren: ``range(start, stop, step_size)``. Wenn nicht angegeben, wird die Schrittgröße standardmäßig auf 1 gesetzt.

In gewissem Sinne ist das von ``range`` zurückgegebene Objekt "faul", da es bei seiner Erstellung nicht jede darin enthaltene Zahl generiert. Es ist jedoch kein Iterator, da es die Operationen in, len und ``__getitem__`` unterstützt.

Diese Funktion speichert nicht alle Werte im Speicher; das wäre ineffizient. Sie speichert nur Start, Ende und Schrittgröße und generiert die nächste Zahl bei Bedarf.

Um diese Funktion zu zwingen, alle Elemente auszugeben, kann man die ``list()``-Funktion verwenden.



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

Man kann ``range()`` in einer ``for``-Schleife verwenden, um über eine Zahlenreihe zu iterieren. Das kann in Kombination mit der ``len()``-Funktion genutzt werden, um mit dem Index über eine Sequenz zu iterieren.



.. code-block:: python

    früchte = ['Birne', 'Apfel', 'Traube']

    for i in range(len(früchte)):
        print("Ich mag", früchte[i])
        
>>> %Run -c $EDITOR_CONTENT
Ich mag Birne
Ich mag Apfel
Ich mag Traube

Else in For-Schleife
--------------------------------

Die ``for``-Schleife kann auch einen optionalen ``else``-Block haben. Wenn die Elemente der für die Schleife verwendeten Sequenz aufgebraucht sind, wird der ``else``-Teil ausgeführt.

Das ``break``-Schlüsselwort kann verwendet werden, um die ``for``-Schleife zu beenden. In diesem Fall wird der ``else``-Teil ignoriert.

Daher wird der ``else``-Teil der ``for``-Schleife ausgeführt, wenn kein Abbruch erfolgt.



.. code-block:: python

    for val in range(5):
        print(val)
    else:
        print("Fertig")

>>> %Run -c $EDITOR_CONTENT
0
1
2
3
4
Fertig

Der Else-Block wird NICHT ausgeführt, wenn die Schleife durch eine ``break``-Anweisung gestoppt wird.



.. code-block:: python

    for val in range(5):
        if val == 2: break
        print(val)
    else:
        print("Fertig")

>>> %Run -c $EDITOR_CONTENT
0
1

