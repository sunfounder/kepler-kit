Print()
=====================

Die Funktion ``print()`` gibt die angegebene Nachricht auf dem Bildschirm oder einem anderen Standardausgabegerät aus. Die Nachricht kann eine Zeichenkette oder ein beliebiges anderes Objekt sein. Das Objekt wird vor der Ausgabe auf dem Bildschirm in eine Zeichenkette umgewandelt.

Mehrere Objekte ausgeben:



.. code-block:: python

    print("Willkommen!", "Viel Spaß!")

>>> %Run -c $EDITOR_CONTENT
Willkommen! Viel Spaß!

Tupel ausgeben:



.. code-block:: python

    x = ("Birne", "Apfel", "Traube")
    print(x)

>>> %Run -c $EDITOR_CONTENT
('Birne', 'Apfel', 'Traube')

Zwei Nachrichten ausgeben und das Trennzeichen festlegen:



.. code-block:: python

    print("Hallo", "wie geht's?", sep="---")

>>> %Run -c $EDITOR_CONTENT
Hallo---wie geht's?
