.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Variablen
==========

Variablen dienen als Behälter zur Speicherung von Datenwerten.

Eine Variable zu erstellen ist sehr einfach. Sie muss lediglich benannt und ihr ein Wert zugewiesen werden. Der Datentyp der Variable muss bei der Zuweisung nicht angegeben werden, da die Variable eine Referenz ist und über die Zuweisung auf Objekte verschiedener Datentypen zugreift.

Die Benennung von Variablen muss folgende Regeln beachten:

* Variablennamen dürfen nur Zahlen, Buchstaben und Unterstriche enthalten
* Das erste Zeichen des Variablennamens muss ein Buchstabe oder Unterstrich sein
* Variablennamen sind groß- und kleinschreibungsempfindlich

Variable erstellen
------------------

In MicroPython gibt es keinen Befehl zur Deklaration von Variablen. Variablen werden erstellt, indem ihnen zum ersten Mal ein Wert zugewiesen wird. Es ist keine spezielle Typdeklaration erforderlich, und der Typ kann sogar nach dem Festlegen der Variable geändert werden.

.. code-block:: python

    x = 8       # x ist vom Typ int
    x = "Lily" # x ist nun vom Typ str
    print(x)

>>> %Run -c $EDITOR_CONTENT
Lily

Typumwandlung (Casting)
-----------------------

Wenn Sie den Datentyp für die Variable spezifizieren möchten, können Sie dies durch Typumwandlung (Casting) tun.

.. code-block:: python

    x = int(5)    # x wird 5 sein
    y = str(5)    # y wird '5' sein
    z = float(5)  # z wird 5.0 sein
    print(x, y, z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Den Typ abfragen
-----------------

Sie können den Datentyp einer Variable mit der Funktion `type()` abfragen.

.. code-block:: python

    x = 5
    y = "Hallo"
    z = 5.0
    print(type(x), type(y), type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

Einfache oder doppelte Anführungszeichen?
-----------------------------------------

In MicroPython können einfache oder doppelte Anführungszeichen verwendet werden, um String-Variablen zu definieren.

.. code-block:: python

    x = "Hallo"
    # ist dasselbe wie
    x = 'Hallo'

Groß- und Kleinschreibung
-------------------------

Variablennamen sind groß- und kleinschreibungsempfindlich.

.. code-block:: python

    a = 5
    A = "Lily"
    # A wird a nicht überschreiben
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 Lily

