.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_bubble_level:

7.12 Nivel de Burbuja Digital
=============================

Un `bubble Level <https://en.wikipedia.org/wiki/Spirit_level>`_ es un instrumento diseñado para indicar si una superficie está horizontal (nivelada) o vertical (aplomada). Existen diferentes tipos de niveles de burbuja utilizados por carpinteros, albañiles, topógrafos, y trabajadores en diversas áreas de la construcción y el metal. También se usa en fotografía y videografía para medir la inclinación.

Aquí creamos un nivel de burbuja digital utilizando el MPU6050 y una matriz LED 8x8. Al inclinar el MPU6050, la “burbuja” en la matriz LED se desviará en la misma dirección.

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

**Esquema**

|sch_bubble_level|

El MPU6050 obtiene los valores de aceleración en cada dirección y calcula el ángulo de inclinación.

El programa dibuja un punto de 2x2 en la matriz LED utilizando datos de los dos chips 74HC595. 

A medida que el ángulo de inclinación cambia, el programa envía diferentes datos a los chips 74HC595 y cambia la posición del punto, creando un efecto de burbuja.

**Conexión**

|wiring_digital_bubble_level|

**Código**

.. note::

    * Abre el archivo ``7.12_digital_bubble_level.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.
    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.
    * Aquí necesitas las bibliotecas ``imu.py`` y ``vector3d.py``; verifica si han sido cargadas en Pico W. Para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050

    # Inicializar comunicación I2C con el sensor MPU6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # Función para calcular la distancia entre dos puntos
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))

    # Función para calcular la rotación en el eje y
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)

    # Función para calcular la rotación en el eje x
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)

    # Función para obtener los ángulos actuales del sensor MPU6050
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle

    # Inicializar los pines del registro de desplazamiento para controlar la matriz LED
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)

    # Función para desplazar datos en el registro de desplazamiento
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    # Función para sacar los datos del registro de desplazamiento a la matriz LED
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    # Función para mostrar un glifo (matriz 8x8) en la matriz LED
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()

    # Convierte una matriz 2D en un glifo que se puede mostrar en la matriz LED
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph

    # Limita un valor entre un mínimo y un máximo especificado
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val

    # Mapea un valor de un rango a otro
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Calcula la posición de la burbuja en la matriz según las lecturas del MPU6050
    sensitivity = 4  # Sensibilidad del movimiento de la burbuja
    matrix_range = 7  # Tamaño de la matriz es 8x8, así que el rango es 0-7
    point_range = matrix_range - 1  # La posición de la burbuja debe estar entre 0 y 6

    # Función para calcular la posición de la burbuja basada en los datos del sensor
    def bubble_position():
        y, x = get_angle()  # Obtener los ángulos actuales de rotación
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]

    # Coloca la burbuja (representada apagando LEDs 2x2) en la matriz
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix

    # Bucle principal
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # Crear una matriz vacía (todos los LEDs encendidos)
        bubble = bubble_position()  # Obtener la posición actual de la burbuja según los datos del sensor
        matrix = drop_bubble(matrix, bubble)  # Colocar la burbuja en la matriz
        display(matrix_2_glyph(matrix))  # Mostrar la matriz en la pantalla LED
        time.sleep(0.1)  # Añadir un pequeño retraso para ralentizar las actualizaciones

Una vez que el programa esté en ejecución, coloca la protoboard en una 
superficie nivelada. Aparecerá un punto en el centro de la matriz LED 
(si no está centrado, es posible que el MPU6050 no esté nivelado). 
Al inclinar la protoboard, el punto se desplazará en la dirección de la inclinación.
