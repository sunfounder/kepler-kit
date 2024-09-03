.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_bubble_level:

7.12 Livella Digitale a Bolla
==================================

Una `bubble Level <https://en.wikipedia.org/wiki/Spirit_level>`_, è uno strumento progettato per indicare se una superficie è orizzontale (in piano) o verticale (a piombo). Esistono diversi tipi di livelle utilizzate da carpentieri, muratori, posatori di mattoni, altri operai edili, topografi, montatori e altri lavoratori del metallo, così come in alcuni lavori fotografici e videografici.

Qui realizzeremo una livella digitale a bolla utilizzando l'MPU6050 e una matrice LED 8x8. Quando inclini l'MPU6050, anche la bolla sulla matrice LED si inclinerà.

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Schema**

|sch_bubble_level|

L'MPU6050 rileva i valori di accelerazione in ogni direzione e calcola l'angolo di assetto.

Di conseguenza, il programma disegna un punto 2x2 sulla matrice LED basandosi sui dati dei due chip 74HC595.

Con il cambiamento dell'angolo di assetto, il programma invia dati diversi ai chip 74HC595, e la posizione del punto cambia, creando l'effetto di una bolla.

**Cablaggio**

|wiring_digital_bubble_level| 

**Codice**

.. note::

    * Apri il file ``7.12_digital_bubble_level.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.
    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra. 

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.
    * Qui è necessario utilizzare le librerie ``imu.py`` e ``vector3d.py``, verifica se sono state caricate su Pico W; per un tutorial dettagliato, fai riferimento a :ref:`add_libraries_py`.

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050


    ### mpu6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # get rotary angle
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    def get_angle():
        y_angle=get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
        x_angle=get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z) 
        return x_angle,y_angle

    ### led matrix display
    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    def display(glyph):
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

    # data transformation
    def matrix_2_glyph(matrix):
        glyph= [0 for i in range(8)] # glyph code for display()
        for i in range(8):
            for j in range(8):
                glyph[i]+=matrix[i][j]<<j
        return glyph

    def clamp_number(val, min, max):
        return min if val < min else max if val > max else val

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Calculate the position of the bubble
    sensitivity=4          # The higher the number, the more sensitive
    matrix_range=7         # The size of the matrix is 8, so the coordinate range is 0~7
    point_range=matrix_range-1     # The x, y value of the bubble's marker point (upper left point) should be between 0-6
    def bubble_position():
        x,y=get_angle()
        x=int(clamp_number(interval_mapping(x,-90,90,0-sensitivity,point_range+sensitivity),0,point_range))
        y=int(clamp_number(interval_mapping(y,-90,90,point_range+sensitivity,0-sensitivity),0,point_range))
        return [x,y]

    # Drop the bubble into empty matrix
    def drop_bubble(matrix,bubble):
        matrix[bubble[0]][bubble[1]]=0
        matrix[bubble[0]+1][bubble[1]]=0
        matrix[bubble[0]][bubble[1]+1]=0
        matrix[bubble[0]+1][bubble[1]+1]=0
        return matrix

    while True:
        matrix= [[1 for i in range(8)] for j in range(8)]  # empty matrix
        bubble=bubble_position() # bubble coordinate
        matrix=drop_bubble(matrix,bubble) # drop the bubble into empty matrix
        display(matrix_2_glyph(matrix)) # show matrix

Una volta eseguito il programma, posiziona la breadboard su una superficie livellata.
Un punto apparirà al centro della matrice LED (se non è al centro, l'MPU6050 potrebbe non essere in piano).
Quando inclini la breadboard, il punto si sposterà nella direzione in cui l'hai inclinata.
