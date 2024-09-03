.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_joystick:

4.1 Utilizzo del Joystick
================================

Se giochi molto ai videogiochi, allora dovresti essere molto familiare 
con il Joystick. Di solito è utilizzato per muovere il personaggio, 
ruotare lo schermo, ecc.

Il principio alla base della capacità del Joystick di permettere al computer 
di leggere le nostre azioni è molto semplice. Può essere considerato come 
composto da due potenziometri perpendicolari tra loro. Questi due potenziometri 
misurano il valore analogico del joystick in senso verticale e orizzontale, 
risultando in un valore (x,y) in un sistema di coordinate rettangolari planari.

Il joystick di questo kit ha anche un input digitale, che viene attivato quando 
il joystick viene premuto.

* :ref:`cpn_joystick`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 



**Schema Elettrico**

|sch_joystick|

Il pin SW è collegato a una resistenza di pull-up da 10K, il motivo è quello di ottenere un livello logico stabile sul pin SW (asse Z) quando il joystick non è premuto; altrimenti, il pin SW sarebbe in uno stato sospeso e il valore in uscita potrebbe variare tra 0 e 1.

**Collegamenti**

|wiring_joystick|


**Codice**

.. note::

    * Apri il file ``4.1_toggle_the_joystick.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200)    

Dopo l'esecuzione del programma, la Shell stamperà i valori x,y,z del joystick.


* I valori degli assi x e y sono valori analogici che variano da 0 a 65535.
* L'asse Z è un valore digitale con uno stato di 1 o 0.
