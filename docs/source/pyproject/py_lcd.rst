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

    from machine import I2C, Pin
    from lcd1602 import LCD
    import time

    # Initialize I2C communication;
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for interfacing with the LCD1602 display
    lcd = LCD(i2c)

    # Display the first message on the LCD
    # Use '\n' to create a new line.
    string = "SunFounder\n    LCD Tutorial"
    lcd.message(string)
    # Wait for 2 seconds
    time.sleep(2)
    # Clear the display
    lcd.clear()

    # Display the second message on the LCD
    string = "Hello\n  World!"
    lcd.message(string)
    # Wait for 5 seconds
    time.sleep(5)
    # Clear the display before exiting
    lcd.clear()

Dopo l'esecuzione del programma, potrai vedere due righe di testo apparire sul display LCD a turno, e poi scomparire.

.. note:: Quando il codice è in esecuzione, se lo schermo è vuoto, puoi regolare il potenziometro sul retro per aumentare il contrasto.

**Come funziona?**

#. Configurazione della comunicazione I2C

   Il modulo ``machine`` viene utilizzato per configurare la comunicazione I2C. I pin SDA (Serial Data) e SCL (Serial Clock) vengono definiti (rispettivamente pin 20 e 21), insieme alla frequenza I2C (400kHz).

   .. code-block:: python
      
      from machine import I2C, Pin
      i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

#. Inizializzazione del display LCD

   La classe ``LCD`` del modulo ``lcd1602`` viene istanziata. Questa classe gestisce la comunicazione con il display LCD tramite I2C. Un oggetto ``LCD`` viene creato utilizzando l'oggetto ``i2c``.

   Per ulteriori dettagli sull'utilizzo della libreria ``lcd1602``, fare riferimento a ``lcd1602.py``.

   .. code-block:: python
      
      from lcd1602 import LCD
      lcd = LCD(i2c)

#. Visualizzazione di messaggi sul display LCD

   Il metodo ``message`` dell'oggetto ``LCD`` viene utilizzato per visualizzare il testo sullo schermo. Il carattere ``\n`` crea una nuova riga sul display LCD. La funzione ``time.sleep()`` sospende l'esecuzione per un numero specificato di secondi.

   .. code-block:: python
      
      string = "SunFounder\n    LCD Tutorial"
      lcd.message(string)
      time.sleep(2)
      lcd.clear()

#. Cancellazione del display

   Il metodo ``clear`` dell'oggetto ``LCD`` viene chiamato per cancellare il testo dal display.

   .. code-block:: python
      
      lcd.clear()

#. Visualizzazione di un secondo messaggio

   Viene visualizzato un nuovo messaggio, seguito da una pausa e poi da una cancellazione dello schermo.

   .. code-block:: python
      
      string = "Hello\n  World!"
      lcd.message(string)
      time.sleep(5)
      lcd.clear()
