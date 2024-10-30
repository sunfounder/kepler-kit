.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_10_second:

7.5 JUEGO - 10 Segundos
============================


Para poner a prueba tu concentración, vamos a crear un dispositivo de juego. 
Haremos una varita mágica conectando un interruptor de inclinación a un palo. Cuando agites la varita, la pantalla de 4 dígitos empezará a contar, y cuando la vuelvas a agitar, se detendrá. Para ganar, el contador debe detenerse en **10.00**. Puedes jugar con tus amigos para ver quién es el "mago del tiempo".

**Componentes Requeridos**

En este proyecto, necesitamos los siguientes componentes.

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
        - 5 (4 de 220Ω, 1 de 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_tilt`
        - 1
        - 

**Esquema**


|sch_10_second|


* Este circuito se basa en :ref:`py_74hc_4dig` con la adición de un interruptor de inclinación.
* GP16 es alto cuando el interruptor de inclinación está en posición vertical; bajo cuando está inclinado.


**Conexión**

|wiring_game_10_second|

**Código**

.. note::

    * Abre el archivo ``7.5_game_10_second.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    # Códigos del display de 7 segmentos para los dígitos 0-9, en hexadecimal
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    # Definir pines para la comunicación del registro de desplazamiento (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Entrada de Datos Seriales
    rclk = machine.Pin(19, machine.Pin.OUT)  # Reloj de Registro (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Reloj de Registro de Desplazamiento

    # Inicializar lista para almacenar los pines de control de los 4 dígitos
    placePin = []

    # Definir pines de control para cada uno de los cuatro dígitos (ánodos comunes)
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    # Función para seleccionar cuál dígito (0-3) mostrar controlando los pines de ánodo común
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    # Función para limpiar la pantalla enviando '0x00' al registro de desplazamiento
    def clearDisplay():
        hc595_shift(0x00)

    # Función para enviar datos al registro de desplazamiento (74HC595)
    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()

    # Función para mostrar un número en el display de 7 segmentos
    def display(num):
        pickDigit(0)
        hc595_shift(SEGCODE[num % 10])

        pickDigit(1)
        hc595_shift(SEGCODE[num % 100 // 10])

        pickDigit(2)
        hc595_shift(SEGCODE[num % 1000 // 100] + 0x80)

        pickDigit(3)
        hc595_shift(SEGCODE[num % 10000 // 1000])

    # Inicializar el sensor de inclinación en el pin 16
    tilt_switch = machine.Pin(16, machine.Pin.IN)

    # Bandera booleana para controlar si la cuenta debe continuar
    count_flag = False

    # Manejador de interrupción para el interruptor de inclinación, alterna la bandera de cuenta
    def shake(pin):
        global timeStart, count_flag
        count_flag = not count_flag
        if count_flag == True:
            timeStart = time.ticks_ms()

    # Configurar una interrupción en el interruptor de inclinación para detectar movimiento
    tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)

    # Inicializar la variable de conteo a cero
    count = 0

    # Bucle principal para actualizar continuamente la pantalla según el tiempo transcurrido desde que se activó el interruptor de inclinación
    while True:
        if count_flag == True:
            count = int((time.ticks_ms() - timeStart) / 10)
        display(count)


La pantalla de 7 segmentos de 4 dígitos comenzará a contar cuando agites la varita y se detendrá al volver a agitarla.
Ganas si logras detener el contador en 10.00. El juego continuará con una nueva agitación.
