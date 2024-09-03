.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Funzioni
===============

In MicroPython, una funzione è un insieme di istruzioni correlate che svolgono un compito specifico.

Le funzioni aiutano a suddividere il nostro programma in blocchi modulari più piccoli. Man mano che il nostro programma cresce, le funzioni lo rendono più organizzato e gestibile.

Inoltre, evitano duplicazioni e rendono il codice riutilizzabile.

Creare una Funzione
----------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* Una funzione è definita utilizzando la parola chiave ``def``.

* Un nome funzione per identificare univocamente la funzione. La denominazione delle funzioni segue le stesse regole della denominazione delle variabili.
    
   * Può contenere solo numeri, lettere e underscore.
   * Il primo carattere deve essere una lettera o un underscore.
   * Case sensitive.

* Parametri (argomenti) attraverso i quali passiamo i valori a una funzione. Sono facoltativi.

* I due punti (:) segnano la fine dell'intestazione della funzione.

* Docstring facoltativa, utilizzata per descrivere la funzione. Solitamente utilizziamo le virgolette triple in modo che la docstring possa essere estesa su più righe.

* Una o più istruzioni valide in Micropython che costituiscono il corpo della funzione. Le istruzioni devono avere lo stesso livello di indentazione (di solito 4 spazi).

* Ogni funzione necessita di almeno un'istruzione, ma se per qualche motivo c'è una funzione che non contiene alcuna istruzione, inserisci l'istruzione pass per evitare errori.

* Un'istruzione ``return`` facoltativa per restituire un valore dalla funzione.


Chiamare una Funzione
-------------------------

Per chiamare una funzione, aggiungi parentesi dopo il nome della funzione.



.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

L'istruzione return
--------------------------

L'istruzione return viene utilizzata per uscire da una funzione e tornare al punto in cui è stata chiamata.

**Sintassi di return**

.. code-block:: python

    return [expression_list]

L'istruzione può contenere un'espressione che viene valutata e restituisce un valore. Se non c'è un'espressione nell'istruzione, o l'istruzione ``return`` stessa non esiste nella funzione, la funzione restituirà un oggetto ``None``.

.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
La tua prima funzione
None

Qui, ``None`` è il valore di ritorno, poiché non è stata utilizzata l'istruzione ``return``.

Argomenti
---------------

Le informazioni possono essere passate alla funzione come argomenti.

Specifica gli argomenti tra parentesi dopo il nome della funzione. Puoi aggiungere quanti argomenti vuoi, basta separarli con una virgola.



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!


Numero di Argomenti
*************************

Per impostazione predefinita, una funzione deve essere chiamata con il numero corretto di argomenti. Significa che se la tua funzione si aspetta 2 parametri, devi chiamare la funzione con 2 argomenti, né più né meno.



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

Qui, la funzione benvenuto() ha 2 parametri.

Poiché abbiamo chiamato questa funzione con due argomenti, la funzione viene eseguita senza errori.

Se viene chiamata con un numero diverso di argomenti, l'interprete visualizzerà un messaggio di errore.

Di seguito è riportata la chiamata a questa funzione, che contiene un solo argomento e nessun argomento e i rispettivi messaggi di errore.

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


Argomenti Predefiniti
*************************

In MicroPython, possiamo utilizzare l'operatore di assegnazione (=) per fornire un valore predefinito al parametro.

Se chiamiamo la funzione senza argomento, utilizza il valore predefinito.



.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Ciao Lily, Benvenuta in Cina!

In questa funzione, il parametro ``nome`` non ha un valore predefinito ed è richiesto (obbligatorio) durante la chiamata.

D'altra parte, il valore predefinito del parametro ``msg`` è "Benvenuta in Cina!". Pertanto, è facoltativo durante la chiamata. Se viene fornito un valore, sovrascriverà il valore predefinito.

Qualsiasi numero di argomenti nella funzione può avere un valore predefinito. Tuttavia, una volta che c'è un argomento predefinito, tutti gli argomenti alla sua destra devono avere anche valori predefiniti.

Ciò significa che gli argomenti non predefiniti non possono seguire gli argomenti predefiniti. 

Ad esempio, se definiamo l'intestazione della funzione sopra come:

.. code-block:: python

    def welcome(name = "Lily", msg):

Riceveremo il seguente messaggio di errore:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument


Argomenti a Parole Chiave
****************************

Quando chiamiamo una funzione con determinati valori, questi valori ​​vengono assegnati agli argomenti in base alla loro posizione.

Ad esempio, nella funzione benvenuto() sopra, quando l'abbiamo chiamata come benvenuto("Lily", "Benvenuta in Cina"), il valore "Lily" viene assegnato a ``nome`` e analogamente "Benvenuta in Cina" al parametro ``msg``.

MicroPython consente di chiamare funzioni con argomenti a parole chiave. Quando chiamiamo la funzione in questo modo, l'ordine (posizione) degli argomenti può essere modificato. 

.. code-block:: python

    # keyword arguments
    welcome(name = "Lily",msg = "Welcome to China!")

    # keyword arguments (out of order)
    welcome(msg = "Welcome to China！",name = "Lily") 

    #1 positional, 1 keyword argument
    welcome("Lily", msg = "Welcome to China!")

Come possiamo vedere, possiamo mescolare argomenti posizionali e argomenti a parole chiave durante le chiamate di funzione. Ma dobbiamo ricordare che gli argomenti a parole chiave devono venire dopo gli argomenti posizionali.

Avere un argomento posizionale dopo un argomento a parole chiave risulterà in un errore. 

Ad esempio, se la chiamata alla funzione avviene come segue:

.. code-block:: python

    welcome(name="Lily","Welcome to China!")

Risulterà in un errore:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg


Argomenti Arbitrari
**********************

A volte, se non conosciamo in anticipo il numero di argomenti che verranno passati alla funzione. 

Nella definizione della funzione, possiamo aggiungere un asterisco (*) prima del nome del parametro.



.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        #names is a tuple with arguments
        for name in names:
            print("Welcome to China!", name)
            
    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

Qui, abbiamo chiamato la funzione con più argomenti. Questi argomenti vengono inseriti in una tupla prima di essere passati alla funzione. 

All'interno della funzione, utilizziamo un ciclo for per recuperare tutti gli argomenti.

Ricorsione
----------------
In Python, sappiamo che una funzione può chiamare altre funzioni. È anche possibile che la funzione chiami se stessa. Questi tipi di costrutti sono chiamati funzioni ricorsive.

Questo ha il vantaggio di poter scorrere i dati per raggiungere un risultato.

Lo sviluppatore dovrebbe fare molta attenzione con la ricorsione poiché può essere abbastanza facile scrivere una funzione che non termina mai, o una che utilizza quantità eccessive di memoria o potenza del processore. Tuttavia, quando scritta correttamente, la ricorsione può essere un approccio molto efficiente e matematicamente elegante alla programmazione.



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

In questo esempio, ric_funzione() è una funzione che abbiamo definito per chiamare se stessa ("ricorsione"). Usiamo la variabile ``i`` come dato e verrà decrementata (-1) ogni volta che ricorriamo. Quando la condizione non è maggiore di 0 (cioè 0), la ricorsione termina.

Per i nuovi sviluppatori, potrebbe volerci del tempo per capire come funziona e il modo migliore per farlo è testare e modificare il codice.

**Vantaggi della Ricorsione**

* Le funzioni ricorsive rendono il codice pulito ed elegante.
* Un compito complesso può essere suddiviso in sotto-problemi più semplici utilizzando la ricorsione.
* La generazione di sequenze è più semplice con la ricorsione che utilizzando alcune iterazioni nidificate.

**Svantaggi della Ricorsione**

* A volte la logica dietro la ricorsione è difficile da seguire.
* Le chiamate ricorsive sono costose (inefficienti) poiché consumano molta memoria e tempo.
* Le funzioni ricorsive sono difficili da debug.

