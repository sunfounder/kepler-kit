.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_lcd:

3.4 - Display a Cristalli Liquidi
======================================

LCD1602 è un display a cristalli liquidi di tipo carattere, in grado di 
visualizzare contemporaneamente 32 caratteri (16x2).

Come ben sappiamo, sebbene LCD e altri display arricchiscano notevolmente 
l'interazione uomo-macchina, condividono una debolezza comune. Quando vengono 
collegati a un controller, occupano molte porte IO del controller, che spesso 
non dispone di così tante porte esterne. Questo limita altre funzioni del 
controller. Per risolvere questo problema, è stato sviluppato LCD1602 con un 
bus I2C.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

|pin_i2c|

In questo progetto, utilizzeremo l'interfaccia I2C0 per controllare l'LCD1602 e visualizzare il testo.

**Componenti Necessari**

In questo progetto, ci servono i seguenti componenti.

È sicuramente conveniente acquistare un intero kit, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK PER L'ACQUISTO
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - INTRODUZIONE COMPONENTE	
        - QUANTITÀ
        - LINK PER L'ACQUISTO

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

**Cablaggio**

|wiring_lcd|

**Codice**

.. note::

    * Puoi aprire il file ``3.4_liquid_crystal_display.ino`` nel percorso ``kepler-kit-main/arduino/3.4_liquid_crystal_display``. 
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * Qui viene utilizzata la libreria ``LiquidCrystal_I2C``. Si prega di fare riferimento a :ref:`add_libraries_ar` per aggiungerla all'IDE di Arduino.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1f464967-5937-473a-8a0d-8e4577c85e7d/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Dopo l'esecuzione del programma, sarai in grado di vedere due righe di testo apparire sull'LCD a turno, e poi scomparire.

.. note:: 
    Se il codice e il cablaggio sono corretti, ma l'LCD non visualizza ancora contenuti, puoi girare il potenziometro sul retro per aumentare il contrasto.

**Come Funziona**

Chiamando la libreria ``LiquidCrystal_I2C.h``, puoi facilmente gestire l'LCD.

.. code-block:: arduino

    #include "LiquidCrystal_I2C.h"

**Funzioni della Libreria**

.. code-block:: arduino

    LiquidCrystal_I2C(uint8_t lcd_Addr,uint8_t lcd_cols,uint8_t lcd_rows)

Crea una nuova istanza della classe ``LiquidCrystal_I2C`` che rappresenta un particolare LCD collegato alla tua scheda Arduino.

- **lcd_Addr**: L'indirizzo dell'LCD è di default 0x27.
- **lcd_cols**: L'LCD1602 ha 16 colonne.
- **lcd_rows**: L'LCD1602 ha 2 righe.

.. code-block:: arduino

    void init()

Inizializza l'LCD.

.. code-block:: arduino

    void backlight()

Accendi la retroilluminazione (opzionale).

.. code-block:: arduino

    void nobacklight()

Spegni la retroilluminazione (opzionale).

.. code-block:: arduino

    void display()

Accendi il display LCD.

.. code-block:: arduino

    void nodisplay()

Spegni rapidamente il display LCD.

.. code-block:: arduino

    void clear()

Cancella il display e posiziona il cursore a zero.

.. code-block:: arduino

    void setCursor(uint8_t col,uint8_t row)

Imposta la posizione del cursore a colonna e riga.

.. code-block:: arduino

    void print(data,BASE)

Stampa testo sull'LCD.

- **data**: I dati da stampare (char, byte, int, long o stringa).
- **BASE (opzionale)**: La base in cui stampare i numeri: BIN per binario (base 2), DEC per decimale (base 10), OCT per ottale (base 8), HEX per esadecimale (base 16).

**Scopri di più**

Carica il codice sul Pico W, il contenuto che inserisci nel monitor seriale verrà stampato sull'LCD.

.. note::

   * Puoi aprire il file ``3.4_liquid_crystal_display_2.ino`` nel percorso ``kepler-kit-main/arduino/3.4_liquid_crystal_display_2``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631e0380-d594-4a8b-9bac-eb0688079b97/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Oltre a leggere dati dai componenti elettronici, il Pico W
può leggere i dati inseriti nel monitor della porta seriale, e puoi
utilizzare ``Serial.read()`` come controller dell'esperimento del circuito.

Avvia la comunicazione seriale in ``setup()`` e imposta il baud rate a 9600.

.. code-block:: arduino

    Serial.begin(9600);

Lo stato del monitor seriale viene giudicato in ``loop()``, e l'elaborazione delle informazioni avverrà solo quando i dati verranno ricevuti.

.. code-block:: arduino

    if (Serial.available() > 0){}

Cancella lo schermo.

.. code-block:: arduino

    lcd.clear();

Leggi il valore inserito nel monitor seriale e memorizzalo nella variabile incomingByte.

.. code-block:: arduino

    char incomingByte = Serial.read();

Visualizza ogni carattere sull'LCD e salta il carattere di nuova riga.

.. code-block:: arduino

    while (Serial.available() > 0) {
        char incomingByte=Serial.read();
        if(incomingByte==10){break;}// skip the line-feed character
        lcd.print(incomingByte);// display each character to the LCD  
    } 


* `Serial Read <https://www.arduino.cc/reference/en/language/functions/communication/serial/read/>`_
