.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Datentypen
===========

Eingebaute Datentypen
---------------------
MicroPython unterstützt die folgenden Datentypen:

* Texttyp: str
* Numerische Typen: int, float, complex
* Sequenztypen: list, tuple, range
* Abbildungstyp: dict
* Mengentypen: set, frozenset
* Boolescher Typ: bool
* Binärtypen: bytes, bytearray, memoryview

Den Datentyp ermitteln
-----------------------------
Mit der Funktion ``type()`` können Sie den Datentyp eines beliebigen Objekts herausfinden:

.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

Datentyp setzen
----------------------
In MicroPython muss der Datentyp nicht explizit festgelegt werden; er wird automatisch bei der Wertzuweisung an eine Variable bestimmt:

.. code-block:: python

    x = "willkommen"
    y = 45
    z = ["Apfel", "Banane", "Kirsche"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>> 

Spezifischen Datentyp festlegen
----------------------------------
Möchten Sie den Datentyp explizit angeben, können Sie die folgenden Konstruktorfunktionen verwenden:

.. list-table:: 
    :widths: 25 10
    :header-rows: 1

    *   - Beispiel
        - Datentyp
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hallo Welt")
        - str
    *   - x = list(("Apfel", "Banane", "Kirsche"))
        - list
    *   - x = tuple(("Apfel", "Banane", "Kirsche"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("Apfel", "Banane", "Kirsche"))
        - set
    *   - x = frozenset(("Apfel", "Banane", "Kirsche"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

Einige von ihnen können Sie ausgeben, um das Ergebnis zu sehen.

.. code-block:: python

    a = float(20.5)
    b = list(("Apfel", "Banane", "Kirsche"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['Apfel', 'Banane', 'Kirsche']
Wahr
>>> 

Typumwandlung
----------------
Mit den Methoden int(), float() und complex() können Sie von einem Typ in einen anderen konvertieren. In Python erfolgt das Casting mithilfe von Konstruktorfunktionen:

* int() - erstellt eine Ganzzahl aus einem Ganzzahl-, Fließkomma- oder Zeichenliteral (vorausgesetzt, die Zeichenfolge stellt eine ganze Zahl dar)
* float() - erstellt eine Fließkommazahl aus einem Ganzzahl-, Fließkomma- oder Zeichenliteral (vorausgesetzt, die Zeichenfolge stellt eine Fließkommazahl oder eine ganze Zahl dar)
* str() - erstellt eine Zeichenfolge aus einer Vielzahl von Datentypen, einschließlich Zeichenfolgen, Ganzzahl- und Fließkommaliteralen

.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

Hinweis: Komplexe Zahlen können nicht in einen anderen Zahlenwert umgewandelt werden.
