.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_passage_counter:

7.4 Contador de Pasajeros
==================================

Para centros comerciales, cadenas de tiendas, aeropuertos, estaciones, museos y otros espacios públicos como salas de exposición, el flujo de personas es un dato indispensable.

Por ejemplo, en aeropuertos y estaciones, se necesita controlar estrictamente el número de personas 
para garantizar la seguridad y el flujo fluido. Además, se puede analizar cuándo hay más visitantes 
en centros comerciales y tiendas, cuántas compras genera cada usuario, entre otros. De este modo, se pueden estudiar los hábitos de consumo y aumentar las ventas.

Los contadores de pasajeros ayudan a comprender el funcionamiento de estos espacios públicos y a organizar sus operaciones de forma eficiente.

Crearemos un contador de pasajeros sencillo utilizando un sensor PIR y una pantalla de 7 segmentos de 4 dígitos.

**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

Es muy conveniente adquirir un kit completo; aquí tienes el enlace:

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

    *   - SN
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
        - 4(220Ω)
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Esquema**

|sch_passager_counter| 

* Este circuito se basa en el :ref:`py_74hc_4dig` con la adición de un módulo PIR.
* El PIR enviará una señal alta de aproximadamente 2.8 segundos cuando alguien pase frente a él.
* El módulo PIR tiene dos potenciómetros: uno ajusta la sensibilidad y el otro la distancia de detección. Para mejorar el rendimiento del módulo PIR, ajusta ambos potenciómetros completamente en sentido antihorario.

    |img_PIR_TTE|

**Conexiones**

|wiring_passager_counter|

**Código**

.. note::

    * Abre el archivo ``7.4_passenger_counter.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    # Inicializa el sensor PIR en el pin 16, configurado como entrada
    pir_sensor = machine.Pin(16, machine.Pin.IN)

    # Códigos de 7 segmentos para los dígitos 0-9, usando hexadecimal para representar los segmentos LED
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    # Define los pines para la comunicación con el registro de desplazamiento (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Entrada de datos en serie
    rclk = machine.Pin(19, machine.Pin.OUT)  # Reloj del registro (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Reloj del registro de desplazamiento

    # Inicializa la lista para almacenar los pines de control de 4 dígitos
    placePin = []

    # Define los pines de control para cada uno de los cuatro dígitos (ánodos comunes)
    pin = [10,13,12,11] # Números de pines para la pantalla de 4 dígitos
    for i in range(4):
        placePin.append(None)  # Reserva espacio en la lista
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Inicializa el pin como salida

    # Inicializa el contador para rastrear eventos de detección de movimiento
    count = 0

    # Función para seleccionar qué dígito (0-3) mostrar controlando los pines de ánodo común
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Apaga todos los dígitos
        placePin[digit].value(0)  # Enciende el dígito seleccionado

    # Función para limpiar la pantalla enviando '0x00' al registro de desplazamiento
    def clearDisplay():
        hc595_shift(0x00)

    # Función para enviar datos al registro de desplazamiento (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Baja el latch para preparar el desplazamiento de datos
        time.sleep_us(200)  # Pequeña demora para estabilidad de sincronización
        for bit in range(7, -1, -1):  # Bucle a través de cada bit (MSB primero)
            srclk.low()  # Prepara el siguiente bit
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extrae el bit actual de los datos
            sdi.value(value)  # Establece el valor de la línea de datos
            time.sleep_us(200)
            srclk.high()  # Pulso en el reloj de desplazamiento para almacenar el bit
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulso en el reloj del registro para mover los datos a la salida

    # Manejador de interrupción para el sensor PIR, activado en detección de movimiento (flanco ascendente)
    # Incrementa el contador de movimiento cada vez que se detecta el sensor
    def motion_detected(pin):
        global count
        count = count + 1  # Incrementa el conteo al detectar movimiento

    # Configura una interrupción para detectar movimiento usando el sensor PIR
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # Bucle principal para actualizar continuamente la pantalla de 7 segmentos con el conteo actual
    while True:
        # Actualiza el primer dígito (unidades)
        pickDigit(0)
        hc595_shift(SEGCODE[count % 10])

        # Actualiza el segundo dígito (decenas)
        pickDigit(1)
        hc595_shift(SEGCODE[count % 100 // 10])

        # Actualiza el tercer dígito (centenas)
        pickDigit(2)
        hc595_shift(SEGCODE[count % 1000 // 100])

        # Actualiza el cuarto dígito (millares)
        pickDigit(3)
        hc595_shift(SEGCODE[count % 10000 // 1000])

Cuando se ejecuta el código, el número en la pantalla de 4 dígitos de 7 segmentos aumentará en uno cada vez que alguien pase frente al módulo PIR.
