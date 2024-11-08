.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_somato_controller:


7.11 Controlador Somatosensorial
=====================================

Si has visto muchas películas de robots, probablemente hayas visto imágenes como esta:
El protagonista gira su muñeca y el robot gigante lo sigue; agita el puño, y el robot lo imita, ¡es muy impresionante!

El uso de esta tecnología ya es común en universidades e institutos de investigación, y la llegada del 5G ampliará enormemente sus áreas de aplicación. Un ejemplo típico es el robot quirúrgico Da Vinci para cirugías remotas.

Un sistema robótico de este tipo se compone generalmente de dos módulos: un módulo de captura de movimiento humano y un módulo de accionamiento del brazo robótico (en algunos casos también incluye un módulo de comunicación de datos).

Aquí utilizamos el MPU6050 para implementar la captura de movimiento humano (colocándolo en un guante) y el servo para representar el movimiento del brazo robótico.

**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

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
        - :ref:`cpn_mpu6050`
        - 1
        - 
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Esquemático**

|sch_somato|

El MPU6050 calcula el ángulo de actitud en función de los valores de aceleración en cada dirección.

El programa controlará el servo para que adopte el ángulo de deflexión correspondiente a medida que cambia el ángulo de actitud.

**Conexiones**

|wiring_somatosensory_controller| 

**Código**

.. note::

    * Abre el archivo ``7.11_somatosensory_controller.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.
    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.
    * Aquí necesitas usar los archivos ``imu.py`` y ``vector3d.py``, verifica que se hayan subido a Pico W. Consulta el tutorial detallado en :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time
    import math

    # Inicializar comunicación I2C para el acelerómetro MPU6050
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # Inicializar PWM para el servo en el pin 15 con una frecuencia de 50Hz
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    # Función para mapear un valor de un rango a otro
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Función para calcular la distancia euclidiana entre dos puntos
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))

    # Función para calcular la rotación a lo largo del eje y
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)

    # Función para calcular la rotación a lo largo del eje x
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)

    # Función para controlar el servo en función del ángulo
    # Mapea el ángulo (0-180) al ciclo de trabajo PWM para el control del servo
    def servo_write(pin, angle):
        pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)  # Mapea el ángulo al ancho de pulso en ms (0.5ms a 2.5ms)
        duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))  # Convierte el ancho de pulso al ciclo de trabajo PWM (0-65535)
        pin.duty_u16(duty)  # Establece el ciclo de trabajo para el PWM del servo

    # Definir el número de lecturas para promediar y suavizar el movimiento
    times = 25

    # Bucle principal
    while True:
        total = 0
        # Realizar múltiples lecturas para promediar el ángulo y suavizar
        for i in range(times):
            angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)  # Obtener el valor de rotación en el eje y del acelerómetro
            total += angle  # Acumular las lecturas

        average_angle = int(total / times)  # Calcular el ángulo promedio
        # Mapear el ángulo promedio (-90 a 90) al rango de movimiento del servo (0 a 180 grados)
        servo_write(servo, interval_mapping(average_angle, -90, 90, 0, 180))

        time.sleep(0.1)  # Pequeño retraso para reducir el temblor en el movimiento del servo


Al ejecutar el programa, el servo girará de izquierda a derecha a medida que inclines el MPU6050 (o giras la muñeca si está montado en un guante).
