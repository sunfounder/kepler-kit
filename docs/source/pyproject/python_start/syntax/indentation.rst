.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Einrückung
=============

Die Einrückung bezieht sich auf die Leerzeichen am Anfang einer Codezeile. Wie bei standardmäßigen Python-Programmen werden auch MicroPython-Programme üblicherweise von oben nach unten ausgeführt: Es durchläuft jede Zeile der Reihe nach, führt sie im Interpreter aus und fährt dann mit der nächsten Zeile fort. Genauso, als würden Sie sie Zeile für Zeile in der Shell eingeben. Ein Programm, das einfach nur die Befehlsliste Zeile für Zeile durchgeht, ist allerdings nicht sehr intelligent. Daher hat auch MicroPython, genau wie Python, eine eigene Methode zur Steuerung der Reihenfolge seiner Programmausführung: die Einrückung.

Vor einem ``print()``-Aufruf muss mindestens ein Leerzeichen gesetzt werden, sonst erscheint die Fehlermeldung "Ungültige Syntax". Es wird allgemein empfohlen, Leerzeichen durch einheitliches Drücken der Tab-Taste zu standardisieren.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

In einem Codeblock müssen Sie die gleiche Anzahl an Leerzeichen verwenden, sonst wird Python einen Fehler ausgeben.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
