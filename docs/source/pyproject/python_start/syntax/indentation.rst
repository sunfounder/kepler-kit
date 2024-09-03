.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Indentazione
=================

L'indentazione si riferisce agli spazi all'inizio di una riga di codice.
Come nei programmi Python standard, anche i programmi MicroPython vengono eseguiti solitamente dall'alto verso il basso:
Scorre ogni riga a turno, la esegue nell'interprete e poi passa alla riga successiva,
Proprio come se le digitassi una per una nel terminale.
Tuttavia, un programma che semplicemente scorre la lista delle istruzioni riga per riga non è molto intelligente – quindi MicroPython, proprio come Python, ha il suo metodo per controllare la sequenza di esecuzione del programma: l'indentazione.

Devi inserire almeno uno spazio prima di print(), altrimenti apparirà un messaggio di errore "Sintassi non valida". Solitamente, è consigliato standardizzare gli spazi premendo uniformemente il tasto Tab.



.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

Devi usare lo stesso numero di spazi nello stesso blocco di codice, altrimenti Python ti darà un errore.


.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")
            
>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
