.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_led:

2.1 Ciao, LED! 
=======================================

Proprio come stampare "Hello, world!" è il primo passo per imparare a programmare, usare un programma per accendere un LED è l'introduzione tradizionale alla programmazione fisica.

* :ref:`cpn_led`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE	
        - QUANTITÀ
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cavo Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Diversi
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schema Elettrico**

|sch_led|

Questo circuito funziona su un principio semplice, e la direzione della corrente è mostrata nella figura. Il LED si accenderà dopo la resistenza limitatrice di corrente da 220 ohm quando GP15 emette un livello alto (3,3V). Il LED si spegnerà quando GP15 emette un livello basso (0V).

**Collegamenti**

|wiring_led|

Per costruire il circuito, seguiamo la direzione della corrente!

1. Il LED è alimentato dal pin GP15 della scheda Pico W, e il circuito inizia qui.
#. Per proteggere il LED, la corrente deve passare attraverso una resistenza da 220 ohm. Un'estremità della resistenza dovrebbe essere inserita nella stessa fila del pin GP15 del Pico W (fila 20 nel mio circuito), e l'altra estremità dovrebbe essere inserita nella fila libera della breadboard (fila 24).

    .. note::
        L'anello colorato della resistenza da 220 ohm è rosso, rosso, nero, nero e marrone.

#. Se prendi il LED, vedrai che uno dei suoi terminali è più lungo dell'altro. Collega il terminale più lungo alla stessa fila della resistenza e il terminale più corto alla stessa fila dall'altra parte del divario centrale della breadboard.

    .. note::
        Il terminale più lungo è l'anodo, che rappresenta il lato positivo del circuito; il terminale più corto è il catodo, che rappresenta il lato negativo.

        L'anodo deve essere collegato al pin GPIO attraverso una resistenza; il catodo deve essere collegato al pin GND.

#. Usa un cavetto maschio-maschio (M2M) per collegare il pin corto del LED al bus negativo di alimentazione della breadboard.
#. Collega il pin GND del Pico W al bus negativo di alimentazione utilizzando un jumper.


**Codice**

.. note::

    * Apri il file ``2.1_hello_led.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

Dopo l'esecuzione del codice, vedrai il LED lampeggiare.


**Come funziona?**

La libreria machine è necessaria per utilizzare i GPIO.

.. code-block:: python

    import machine

La libreria contiene tutte le istruzioni necessarie per la comunicazione tra MicroPython e Pico W.
In assenza di questa riga di codice, non saremo in grado di controllare alcun GPIO.

La prossima cosa da notare è questa riga:

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

Qui viene definito l'oggetto ``led``. Tecnicamente, può avere qualsiasi nome, come x, y, banana, Michael_Jackson o qualsiasi carattere. 
Per garantire che il programma sia facile da leggere, è meglio usare un nome che descriva lo scopo.

Nella seconda parte di questa riga (la parte dopo il segno di uguale), chiamiamo la funzione Pin che si trova nella libreria ``machine``. Viene utilizzata per dire ai pin GPIO del Pico cosa fare.
Una funzione ``Pin`` ha due parametri: il primo (15) rappresenta il pin da impostare; 
Il secondo parametro (machine.Pin.OUT) specifica che il pin deve essere un'uscita piuttosto che un ingresso.

Il codice sopra ha "impostato" il pin, ma non accenderà il LED. Per fare questo, dobbiamo anche "usare" il pin.

.. code-block:: python

    led.value(1)

Il pin GP15 è stato impostato in precedenza e nominato ``led``. La funzione di questa istruzione è impostare il valore di ``led`` a 1 per accendere il LED.

In sintesi, per utilizzare i GPIO, questi passaggi sono necessari:

* **importare la libreria machine**: Questo è necessario, e viene eseguito solo una volta.
* **Impostare i GPIO**: Prima dell'uso, ogni pin deve essere impostato.
* **Usare**: Cambia lo stato operativo del pin assegnandogli un valore.

Se seguiamo i passaggi sopra per scrivere un esempio, otterremo un codice simile a questo:

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

Eseguilo e sarai in grado di accendere il LED.

Ora, proviamo ad aggiungere l'istruzione per spegnere il LED:

.. code-block:: python

    import machine   
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

In base alla riga di codice, questo programma accenderà prima il LED, poi lo spegnerà.
Ma quando lo usi, scoprirai che non è così.
Non c'è alcuna luce proveniente dal LED. Questo è dovuto alla velocità di esecuzione molto rapida tra le due righe, molto più veloce di quanto l'occhio umano possa percepire.
Quando il LED si accende, non percepiamo immediatamente la luce. Questo può essere risolto rallentando il programma.

La seconda riga del programma dovrebbe contenere la seguente istruzione:

.. code-block:: python

    import utime

Similmente a ``machine``, qui viene importata la libreria ``utime``, che gestisce tutto ciò che riguarda il tempo.
I ritardi che dobbiamo usare sono inclusi in questa. Aggiungi un'istruzione di ritardo tra ``led.value(1)`` e ``led.value(0)`` e separali di 2 secondi.

.. code-block:: python

    utime.sleep(2)

Ecco come dovrebbe apparire il codice ora.
Vedremo che il LED si accende prima e poi si spegne quando lo eseguiamo:

.. code-block:: python

    import machine 
    import utime  
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

Infine, dovremmo fare in modo che il LED lampeggi.
Crea un ciclo, riscrivi il programma e sarà quello che hai visto all'inizio di questo capitolo.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`py_syntax_while` 


**Scopri di più**

Di solito, ci sarà un file API (Application Programming Interface) associato alla libreria. 
Contiene tutte le informazioni necessarie per utilizzare questa libreria, comprese descrizioni dettagliate delle funzioni, classi, tipi di ritorno, tipi di parametri, ecc.

In questo articolo, abbiamo utilizzato le librerie ``machine`` e ``utime`` di MicroPython, possiamo trovare ulteriori modi per utilizzarle qui.

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

Leggi il file API per comprendere questo esempio di lampeggio del LED!

.. note::

    * Apri il file ``2.1_hello_led_2.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)