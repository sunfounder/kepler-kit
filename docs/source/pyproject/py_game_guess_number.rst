.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_guess_number:

7.7 Adivina el Número
===========================


"Adivina el Número" es un divertido juego en el que tú y tus amigos ingresan números (0-99). Con cada número ingresado, el rango se reduce hasta que alguien acierta el número secreto. Luego, el jugador pierde y recibe un castigo.

Por ejemplo, si el número secreto es 51 (desconocido para los jugadores), y el jugador 1 ingresa 50, el rango cambia a 50-99; si el jugador 2 ingresa 70, el rango se ajusta a 50-70; si el jugador 3 ingresa 51, ¡pierde el juego! Los números se ingresan a través de un teclado y los resultados se muestran en una pantalla LCD.

|guess_number|

**Componentes Requeridos**

Para este proyecto, necesitaremos los siguientes componentes.

Es conveniente adquirir un kit completo; aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N.º
        - COMPONENTE
        - CANTIDAD
        - ENLACE

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cable Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Varios
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Esquema**

|sch_guess_number|

Este circuito está basado en :ref:`py_keypad` con la adición de un LCD I2C 1602 para mostrar los números ingresados.

**Conexión**

|wiring_game_guess_number|

Para facilitar la conexión, en el diagrama anterior, la fila de columnas del teclado matricial y las resistencias de 10K están conectadas a los mismos agujeros donde están ubicados G10 ~ G13.


**Código**

.. note::

    * Abre el archivo ``7.7_game_guess_number.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import time
    import urandom

    # Inicializar comunicación I2C para el LCD1602
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Crear objeto LCD para controlar el LCD1602
    lcd = LCD(i2c)

    # Mapeo de caracteres para el teclado matricial 4x4
    characters = [["1", "2", "3", "A"], 
                ["4", "5", "6", "B"], 
                ["7", "8", "9", "C"], 
                ["*", "0", "#", "D"]]

    # Definir pines de fila para el teclado
    pin = [21, 20, 19, 18]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    # Definir pines de columna para el teclado
    pin = [13, 12, 11, 10]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

    # Función para leer una tecla del teclado
    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if col[j].value() == 1:
                    key.append(characters[i][j])
            row[i].low()
        if key == []:
            return None
        else:
            return key

    # Inicializar y reiniciar variables del juego (valor de punto aleatorio, límites superior/inferior)
    def init_new_value():
        global pointValue, upper, count, lower
        pointValue = int(urandom.uniform(0, 99))
        print(pointValue)
        upper = 99
        lower = 0
        count = 0
        return False

    # Función para mostrar información del juego en el LCD
    def lcd_show(result):
        lcd.clear()
        if result == True:
            string = "GAME OVER!\n"
            string += "Point is " + str(pointValue)  
        else:
            string = "Enter number: " + str(count) + "\n"
            string += str(lower) + " < Point < " + str(upper)
        lcd.message(string)
        return

    # Procesar la suposición del jugador y actualizar el límite superior o inferior
    def number_processing():
        global upper, count, lower
        if count > pointValue:
            if count < upper:
                upper = count
        elif count < pointValue:
            if count > lower:
                lower = count
        elif count == pointValue:
            return True
        count = 0
        return False

    # Configuración y bucle principal del juego
    string = "Presiona A para Iniciar!"
    lcd.message(string)
    result = init_new_value()

    # Bucle principal para gestionar la entrada y actualizar el LCD
    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        
        if current_key != None:
            if current_key == ["A"]:
                result = init_new_value()
            elif current_key == ["D"]:
                result = number_processing()
            elif current_key[0] in list("1234567890") and count < 10:
                count = count * 10 + int(current_key[0])
            lcd_show(result)
        time.sleep(0.1)

* Después de ejecutar el código, presiona ``A`` para iniciar el juego. Se genera un número aleatorio como ``punto`` pero no se muestra en el LCD, y tu objetivo es adivinarlo.
* El número que ingresas aparece al final de la primera línea hasta que se realiza la verificación final (presiona ``D`` para iniciar la comparación).
* El rango del número ``punto`` se muestra en la segunda línea. Debes ingresar un número dentro del rango indicado.
* Si adivinas correctamente el número, aparecerá ``GAME OVER!``.

.. note::
    Si el código y las conexiones son correctos, pero el LCD aún no muestra contenido, ajusta el potenciómetro en la parte posterior para aumentar el contraste.

