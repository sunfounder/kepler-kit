.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

If-Else-Anweisungen
======================

Entscheidungsfindung ist erforderlich, wenn ein bestimmter Code nur bei Erfüllung einer bestimmten Bedingung ausgeführt werden soll.

if
--------------------
.. code-block:: python

    if Testausdruck:
        Anweisung(en)

In diesem Fall wertet das Programm den ``Testausdruck`` aus und führt die ``Anweisung`` nur aus, wenn der ``Testausdruck`` wahr ist.

Ist der ``Testausdruck`` falsch, werden die ``Anweisung(en)`` nicht ausgeführt.

In MicroPython signalisiert die Einrückung den Körper der ``if``-Anweisung. Der Körper beginnt mit einer Einrückung und endet mit der ersten nicht eingerückten Zeile.

Python interpretiert Werte ungleich Null als "True". None und 0 werden als "False" interpretiert.

**Flussdiagramm für if-Anweisungen**

.. image:: img/if_statement.png

**Beispiel**

.. code-block:: python

    num = 8
    if num > 0:
        print(num, "ist eine positive Zahl.")
    print("Ende mit dieser Zeile")

>>> %Run -c $EDITOR_CONTENT
8 ist eine positive Zahl.
Ende mit dieser Zeile


if...else
-----------------------

.. code-block:: python

    if Testausdruck:
        Körper von if
    else:
        Körper von else

Die ``if..else``-Anweisung wertet den ``Testausdruck`` aus und führt den Körper von ``if`` nur aus, wenn die Testbedingung ``True`` ist.

Ist die Bedingung ``False``, wird der Körper von ``else`` ausgeführt. Einrückungen dienen zur Abgrenzung der Blöcke.

**Flussdiagramm für if...else-Anweisungen**

.. image:: img/if_else.png

**Beispiel**

.. code-block:: python

    num = -8
    if num > 0:
        print(num, "ist eine positive Zahl.")
    else:
        print(num, "ist eine negative Zahl.")

>>> %Run -c $EDITOR_CONTENT
-8 ist eine negative Zahl.


if...elif...else
--------------------

.. code-block:: python

    if Testausdruck:
        Körper von if
    elif Testausdruck:
        Körper von elif
    else:
        Körper von else

``Elif`` steht für ``else if``. Damit können wir mehrere Ausdrücke prüfen.

Ist die Bedingung des ``if`` falsch, wird die Bedingung des nächsten ``elif``-Blocks geprüft und so weiter.

Sind alle Bedingungen `falsch`, wird der Körper von ``else`` ausgeführt.

Nur einer der ``if...elif...else``-Blöcke wird je nach Bedingung ausgeführt.

Der ``if``-Block kann nur einen ``else``-Block haben, jedoch mehrere ``elif``-Blöcke.

**Flussdiagramm für if...elif...else-Anweisungen**

.. image:: img/if_elif_else.png

**Beispiel**

.. code-block:: python

    x = 10
    y = 9

    if x > y:
        print("x ist größer als y")
    elif x == y:
        print("x und y sind gleich")
    else:
        print("y ist größer als x")

>>> %Run -c $EDITOR_CONTENT
x ist größer als y


Verschachtelte if-Anweisungen
------------------------------

Wir können eine if-Anweisung in eine andere if-Anweisung einbetten; das nennen wir dann eine verschachtelte if-Anweisung.

**Beispiel**

.. code-block:: python

    x = 67

    if x > 10:
        print("Über zehn,")
        if x > 20:
            print("und auch über 20!")
        else:
            print("aber nicht über 20.")

>>> %Run -c $EDITOR_CONTENT
Über zehn,
und auch über 20!
