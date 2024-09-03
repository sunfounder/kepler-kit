.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_lcd:

3.4 Display a Cristalli Liquidi
===================================

LCD1602 è un display a cristalli liquidi di tipo carattere, che può 
visualizzare contemporaneamente 32 (16*2) caratteri.

Come sappiamo, sebbene gli LCD e altri display arricchiscano notevolmente 
l'interazione uomo-macchina, condividono una debolezza comune. Quando sono 
collegati a un controller, molte porte di input/output (IO) del controller 
vengono occupate, limitando altre funzioni del controller stesso. Per 
risolvere questo problema, è stato sviluppato l'LCD1602 con un bus I2C.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_


|pin_i2c|

Qui useremo l'interfaccia I2C0 per controllare l'LCD1602 e visualizzare il testo.


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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schema Elettrico**

|sch_lcd|

**Collegamenti**

|wiring_lcd|

**Codice**

.. note::

    * Apri il file ``3.4_liquid_crystal_display.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`. 
    
    * Qui devi usare la libreria chiamata ``lcd1602.py``, verifica se è stata caricata su Pico W, per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.


.. code-block:: python

    from lcd1602 import LCD
    import utime

    lcd = LCD()
    string = " Hello!\n"
    lcd.message(string)
    utime.sleep(2)
    string = "    Sunfounder!"   
    lcd.message(string)
    utime.sleep(2)
    lcd.clear()   

Dopo l'esecuzione del programma, potrai vedere due righe di testo apparire sul display LCD a turno, e poi scomparire.

.. note:: Quando il codice è in esecuzione, se lo schermo è vuoto, puoi regolare il potenziometro sul retro per aumentare il contrasto.

**Come funziona?**

Nella libreria lcd1602, integriamo le funzioni rilevanti dell'lcd1602 nella classe LCD.

Importa la libreria lcd1602

.. code-block:: python

    from lcd1602 import LCD    

Dichiara un oggetto della classe LCD e chiamalo lcd.

.. code-block:: python

    lcd = LCD()

Questa istruzione visualizzerà il testo sul display LCD. Va notato che l'argomento deve essere di tipo stringa. Se vogliamo passare un intero o un float, dobbiamo usare l'istruzione di conversione forzata ``str()``.

.. code-block:: python

    lcd.message(string)


Se chiami questa istruzione più volte, l'lcd sovrapporrà i testi. Questo richiede l'uso della seguente istruzione per cancellare il display.

.. code-block:: python

    lcd.clear()
