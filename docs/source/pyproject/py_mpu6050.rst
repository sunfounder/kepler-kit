.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones durante festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_mpu6050:

6.3 Seguimiento de Movimiento de 6 Ejes
==========================================

El MPU-6050 es un dispositivo de seguimiento de movimiento de 6 ejes (que combina un giroscopio de 3 ejes y un acelerómetro de 3 ejes).

Un acelerómetro es una herramienta que mide la aceleración propia. Por ejemplo, un acelerómetro en reposo en la superficie de la Tierra medirá una aceleración debido a la gravedad terrestre, apuntando hacia arriba (por definición) con un valor aproximado de g ≈ 9.81 m/s².

Los acelerómetros tienen múltiples aplicaciones en la industria y la ciencia, como en sistemas de navegación inercial para aeronaves y misiles, y para mantener las imágenes verticales en tabletas y cámaras digitales, entre otros.

Los giroscopios se utilizan para medir la orientación y la velocidad angular de un dispositivo. Sus aplicaciones incluyen sistemas antivuelco 
y de airbags para automóviles, sistemas de detección de movimiento para dispositivos inteligentes, sistemas de estabilización de actitud para drones, entre otros.

* :ref:`cpn_mpu6050`


**Componentes Necesarios**

Para este proyecto, necesitaremos los siguientes componentes.

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

**Esquema**

|sch_mpu6050|

**Conexiones**

|wiring_mpu6050|

**Código**

.. note::

    * Abre el archivo ``6.3_6axis_motion_tracking.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

    * Aquí necesitas usar las bibliotecas ``imu.py`` y ``vector3d.py``. Verifica si han sido cargadas en Pico W. Para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.5)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.5)

Una vez que el programa esté en ejecución, podrás ver los valores del acelerómetro de 3 ejes y del giroscopio de 3 ejes que se mostrarán en pantalla en un ciclo. Gira el MPU6050 al azar, y verás cómo cambian estos valores en consecuencia. 

Para facilitar la visualización de los cambios, puedes comentar una de las líneas ``print`` y concentrarte en un conjunto de datos.

La unidad de valor de aceleración es m/s², y la unidad de valor del giroscopio es °/s.

**¿Cómo funciona?**

En la biblioteca imu, hemos integrado las funciones relevantes en la clase ``MPU6050``. 

MPU6050 es un módulo I2C y requiere un conjunto de pines I2C para inicializarse.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin

    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

Posteriormente, podrás obtener los valores de aceleración y velocidad angular en tiempo real en ``mpu.accel.x``, ``mpu.accel.y``, ``mpu.accel.z``, ``mpu.gyro.x``, ``mpu.gyro.y``, ``mpu.gyro.z``.

.. code-block:: python

    while True:
        print("x: %s, y: %s, z: %s"%(mpu.accel.x, mpu.accel.y, mpu.accel.z))
        time.sleep(0.5)
        print("A: %s, B: %s, Y: %s"%(mpu.gyro.x, mpu.gyro.y, mpu.gyro.z))
        time.sleep(0.5)
