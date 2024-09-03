.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Variables
=============
Le variabili sono contenitori utilizzati per memorizzare valori di dati.

Creare una variabile è molto semplice. Basta darle un nome e assegnarle un valore. Non è necessario specificare il tipo di dato della variabile al momento dell'assegnazione, perché la variabile è un riferimento e accede a oggetti di diversi tipi di dati attraverso l'assegnazione.

La denominazione delle variabili deve seguire le seguenti regole:

* I nomi delle variabili possono contenere solo numeri, lettere e underscore
* Il primo carattere del nome della variabile deve essere una lettera o un underscore
* I nomi delle variabili sono sensibili alle maiuscole e minuscole

Create Variable
---------------------
In MicroPython non esiste un comando per dichiarare le variabili. Le variabili vengono create quando si assegna loro un valore per la prima volta. Non è necessario utilizzare alcuna dichiarazione di tipo specifico, e si può anche cambiare il tipo dopo aver impostato la variabile.



.. code-block:: python

    x = 8       # x is of type int
    x = "lily" # x is now of type str
    print(x)

>>> %Run -c $EDITOR_CONTENT
lily


Casting
-------------
Se vuoi specificare il tipo di dato per la variabile, puoi farlo tramite il casting.



.. code-block:: python

    x = int(5)    # y will be 5
    y = str(5)    # x will be '5'
    z = float(5)  # z will be 5.0
    print(x,y,z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Get the Type
-------------------
Puoi ottenere il tipo di dato di una variabile con la funzione `type()`.



.. code-block:: python

    x = 5
    y = "hello"
    z = 5.0
    print(type(x),type(y),type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

Single or Double Quotes?
---------------------------

In MicroPython, si possono utilizzare virgolette singole o doppie per definire variabili stringa.



.. code-block:: python

    x = "hello"
    # is the same as
    x = 'hello'

Case-Sensitive
---------------------
I nomi delle variabili sono sensibili alle maiuscole e minuscole.



.. code-block:: python

    a = 5
    A = "lily"
    #A will not overwrite a
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 lily


