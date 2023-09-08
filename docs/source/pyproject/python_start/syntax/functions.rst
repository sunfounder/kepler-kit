Funktionen
==============

In MicroPython ist eine Funktion eine Gruppe von verwandten Anweisungen, die eine bestimmte Aufgabe ausführen.

Funktionen helfen dabei, unser Programm in kleinere, modulare Blöcke zu zerlegen. Je umfangreicher unser Projekt wird, desto übersichtlicher und handhabbarer wird es durch die Verwendung von Funktionen.

Zudem vermeiden Funktionen Duplikate und machen den Code wiederverwendbar.

Eine Funktion erstellen
-------------------------

.. code-block::

    def funktions_name(parameter): 
        """Dokumentationszeichenfolge"""
        Anweisung(en)

* Eine Funktion wird mit dem Schlüsselwort ``def`` definiert.

* Ein Funktionsname zur eindeutigen Identifizierung der Funktion. Die Benennung von Funktionen und Variablen folgt denselben Regeln:
    
   * Darf nur Zahlen, Buchstaben und Unterstriche enthalten.
   * Das erste Zeichen muss ein Buchstabe oder Unterstrich sein.
   * Groß- und Kleinschreibung wird unterschieden.

* Parameter (Argumente), über die Werte an eine Funktion übergeben werden. Diese sind optional.

* Der Doppelpunkt (:) markiert das Ende der Funktionskopfzeile.

* Eine optionale Dokumentationszeichenfolge, die in der Regel durch dreifache Anführungszeichen mehrzeilig gestaltet werden kann, dient zur Beschreibung der Funktion.

* Eine oder mehrere gültige MicroPython-Anweisungen, die den Funktionskörper bilden. Die Anweisungen müssen die gleiche Einrückungsebene haben (in der Regel 4 Leerzeichen).

* Jede Funktion benötigt mindestens eine Anweisung. Sollte aus irgendeinem Grund eine Funktion keine Anweisung enthalten, verwenden Sie bitte die Anweisung ``pass``, um Fehler zu vermeiden.

* Eine optionale ``return``-Anweisung, um einen Wert aus der Funktion zurückzugeben.


Eine Funktion aufrufen
---------------------------

Um eine Funktion aufzurufen, fügen Sie Klammern hinter den Funktionsnamen.

.. code-block:: python

    def meine_funktion():
        print("Deine erste Funktion")

    meine_funktion()

>>> %Run -c $EDITOR_CONTENT
Deine erste Funktion

Die return-Anweisung
-----------------------

Die ``return``-Anweisung wird verwendet, um eine Funktion zu verlassen und an die Stelle zurückzukehren, von der aus sie aufgerufen wurde.

**Syntax von return**

.. code-block:: python

    return [Ausdrucksliste]

Die Anweisung kann einen Ausdruck enthalten, der ausgewertet wird und einen Wert zurückgibt. Wenn in der Anweisung kein Ausdruck enthalten ist oder die ``return``-Anweisung in der Funktion selbst nicht vorhanden ist, gibt die Funktion ein ``None``-Objekt zurück.

.. code-block:: python

    def meine_funktion():
            print("Deine erste Funktion")

    print(meine_funktion())

>>> %Run -c $EDITOR_CONTENT
Deine erste Funktion
None

In diesem Fall ist ``None`` der Rückgabewert, da die ``return``-Anweisung nicht verwendet wird.

Argumente
-------------

Informationen können der Funktion als Argumente übergeben werden.

Geben Sie die Argumente in Klammern hinter dem Funktionsnamen an. Sie können so viele Argumente hinzufügen wie nötig, trennen Sie diese einfach durch Kommas.

.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!


Anzahl der Argumente
*************************

Standardmäßig muss eine Funktion mit der korrekten Anzahl an Argumenten aufgerufen werden. Das heißt, wenn Ihre Funktion zwei Parameter erwartet, müssen Sie die Funktion auch mit genau zwei Argumenten aufrufen, weder mehr noch weniger.

.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

Hier hat die Funktion welcome() zwei Parameter.

Da wir diese Funktion mit zwei Argumenten aufgerufen haben, wird sie fehlerfrei ausgeführt.

Wird sie jedoch mit einer abweichenden Anzahl an Argumenten aufgerufen, gibt der Interpreter eine Fehlermeldung aus.

Folgende Aufrufe der Funktion, die entweder ein oder gar kein Argument enthalten, erzeugen jeweils eine entsprechende Fehlermeldung.

.. code-block::

    welcome("Lily")＃Only one argument

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃No arguments

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


Standardargumente
*************************

In MicroPython können wir den Zuweisungsoperator (=) verwenden, um einen Standardwert für den Parameter festzulegen.

Wenn wir die Funktion ohne Argument aufrufen, wird der Standardwert verwendet.

.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

In dieser Funktion ist der Parameter ``name`` zwingend erforderlich, da er keinen Standardwert hat.

Andererseits ist der Standardwert des Parameters ``msg`` "Willkommen in China!". Daher ist er beim Aufruf der Funktion optional. Wird ein Wert angegeben, überschreibt dieser den Standardwert.

In der Funktion können beliebig viele Argumente einen Standardwert haben. Sobald jedoch ein Argument einen Standardwert hat, müssen alle folgenden Argumente ebenfalls Standardwerte haben.

Das bedeutet, dass Standardargumente immer am Ende der Parameterliste stehen müssen.

Zum Beispiel, wenn wir die obenstehende Funktionsdeklaration wie folgt definieren:

.. code-block:: python

    def welcome(name = "Lily", msg):

Dann erhalten wir die folgende Fehlermeldung:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument



Schlüsselwortargumente
**************************

Wenn wir eine Funktion mit bestimmten Werten aufrufen, werden diese Werte basierend auf ihrer Position den Argumenten zugewiesen.

Beispielsweise wird im oben erwähnten Fall der Funktion welcome(), wenn wir sie mit welcome("Lily", "Willkommen in China") aufrufen, der Wert "Lily" dem Parameter ``name`` und entsprechend "Willkommen in China" dem Parameter ``msg`` zugewiesen.

MicroPython ermöglicht das Aufrufen von Funktionen mit Schlüsselwortargumenten. Bei dieser Art des Aufrufs kann die Reihenfolge der Argumente variiert werden. 

.. code-block:: python

    # Schlüsselwortargumente
    welcome(name = "Lily", msg = "Willkommen in China!")

    # Schlüsselwortargumente (in unterschiedlicher Reihenfolge)
    welcome(msg = "Willkommen in China!", name = "Lily") 

    # Ein Positionsargument, ein Schlüsselwortargument
    welcome("Lily", msg = "Willkommen in China!")

Wie zu sehen ist, können Positionsargumente und Schlüsselwortargumente in Funktionsaufrufen gemischt werden. Es ist jedoch wichtig, dass die Schlüsselwortargumente immer nach den Positionsargumenten stehen.

Ein Positionsargument nach einem Schlüsselwortargument führt zu einem Fehler.

Zum Beispiel resultiert der folgende Funktionsaufruf in einem Fehler:

.. code-block:: python

    welcome(name="Lily", "Willkommen in China!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: positional argument follows keyword argument


Beliebige Argumente
********************

Manchmal wissen wir im Voraus nicht, wie viele Argumente an die Funktion übergeben werden.

In der Funktionsdefinition können wir ein Sternchen (*) vor dem Parameternamen setzen.

.. code-block:: python

    def welcome(*names):
        """Diese Funktion begrüßt alle Personen
        im Namens-Tupel"""
        for name in names:
            print("Willkommen in China!", name)
            
    welcome("Lily", "John", "Wendy")

>>> %Run -c $EDITOR_CONTENT
Willkommen in China! Lily
Willkommen in China! John
Willkommen in China! Wendy

Hier haben wir die Funktion mit mehreren Argumenten aufgerufen, die in ein Tupel verpackt und dann an die Funktion übergeben werden.

Innerhalb der Funktion verwenden wir eine Schleife, um alle Argumente abzurufen.


Rekursion
----------------

In Python ist es bekanntlich möglich, dass eine Funktion andere Funktionen aufruft. Sie kann sogar sich selbst aufrufen. Solche Konstrukte werden als rekursive Funktionen bezeichnet.

Dies hat den Vorteil, dass man durch Daten iterieren kann, um ein Ergebnis zu erreichen.

Entwickler sollten bei der Verwendung von Rekursion sehr vorsichtig sein, da leicht eine Funktion entstehen kann, die niemals endet oder übermäßig viel Speicher bzw. Prozessorleistung verbraucht. Bei korrekter Implementierung kann Rekursion jedoch ein sehr effizienter und mathematisch eleganter Ansatz zur Programmierung sein.

.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

In diesem Beispiel ruft rec_func() sich selbst auf ("Rekursion"). Wir verwenden die Variable ``i`` als Datenwert, der bei jedem Rekursionsschritt um 1 verringert wird. Wenn die Bedingung nicht größer als 0 ist (also 0), endet die Rekursion.

Für neue Entwickler kann es etwas Zeit in Anspruch nehmen, die Funktionsweise zu verstehen; der beste Weg zur Überprüfung ist das Ausprobieren und Anpassen.

**Vorteile der Rekursion**

* Rekursive Funktionen machen den Code sauber und elegant.
* Komplexe Aufgaben können durch Rekursion in einfachere Teilprobleme zerlegt werden.
* Die Erzeugung von Sequenzen ist mit Rekursion einfacher als mit verschachtelten Schleifen.

**Nachteile der Rekursion**

* Manchmal ist die Logik hinter der Rekursion schwer nachzuvollziehen.
* Rekursive Aufrufe sind ressourcenintensiv, da sie viel Speicher und Zeit verbrauchen.
* Rekursive Funktionen sind schwer zu debuggen.
