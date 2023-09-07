Kommentare
=============

Kommentare im Code helfen uns, den Code zu verstehen, machen den gesamten Code lesefreundlicher und ermöglichen es, während des Testens Teile des Codes auszukommentieren, sodass diese Teile nicht ausgeführt werden.

Einzeilige Kommentare
----------------------------

Einzeilige Kommentare in MicroPython beginnen mit einem #, und der darauf folgende Text wird bis zum Ende der Zeile als Kommentar betrachtet. Kommentare können vor oder nach dem Code platziert werden.

.. code-block:: python

    print("Hallo Welt")  # Das ist ein Kommentar
>>> %Run -c $EDITOR_CONTENT
Hallo Welt

Kommentare sind nicht zwangsläufig Text, der dazu dient, den Code zu erklären. Sie können auch Teile des Codes auskommentieren, um zu verhindern, dass MicroPython den Code ausführt.

.. code-block:: python

    #print("Wird nicht ausgeführt!")
    print("Hallo Welt")  # Das ist ein Kommentar

>>> %Run -c $EDITOR_CONTENT
Hallo Welt

Mehrzeilige Kommentare
------------------------------

Wenn Sie mehrere Zeilen kommentieren möchten, können Sie mehrere # Zeichen verwenden.

.. code-block:: python

    # Das ist ein Kommentar
    # der über mehrere 
    # Zeilen geht
    print("Hallo Welt!")

>>> %Run -c $EDITOR_CONTENT
Hallo Welt!

Alternativ können Sie auch mehrzeilige Zeichenketten verwenden.

Da MicroPython Zeichenfolgen, die keiner Variablen zugewiesen werden, ignoriert, können Sie mehrzeilige Zeichenketten (Dreifach-Anführungszeichen) zum Code hinzufügen und dort Kommentare einfügen:

.. code-block:: python

    """
    Das ist ein Kommentar
    der über mehrere 
    Zeilen geht
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Solange die Zeichenfolge keiner Variablen zugewiesen ist, wird MicroPython sie nach dem Lesen des Codes ignorieren und so behandeln, als hätten Sie einen mehrzeiligen Kommentar verfasst.
