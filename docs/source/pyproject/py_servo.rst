.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_servo:

3.7 Movimiento Oscilante del Servo
======================================

En este kit, además de un LED y un zumbador pasivo, también hay un dispositivo controlado mediante una señal PWM: el servo.

El servo es un dispositivo de control de posición (ángulo), ideal para sistemas que requieren cambios constantes de ángulo que se mantengan estables. Se utiliza ampliamente en juguetes de control remoto de alta gama, como aviones, modelos de submarinos y robots de control remoto.

¡Ahora intentemos hacer que el servo oscile!

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Esquemático**

|sch_servo|

**Conexiones**

|wiring_servo|

* El cable naranja es la señal y se conecta a GP15.
* El cable rojo es VCC y se conecta a VBUS (5V).
* El cable marrón es GND y se conecta a GND.

.. 1. Inserta el Brazo del Servo en el eje de salida del Servo. Si es necesario, fíjalo con tornillos.
.. #. Conecta **VBUS** (no 3V3) y GND del Pico W al bus de alimentación de la breadboard.
.. #. Conecta el cable rojo del servo al bus positivo de alimentación con un puente.
.. #. Conecta el cable amarillo del servo al pin GP15 con un puente.
.. #. Conecta el cable marrón del servo al bus negativo de alimentación con un puente.

**Código**

.. note::

    * Abre el archivo ``3.7_swinging_servo.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servo_write(pin, angle):
        pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)
        duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))
        pin.duty_u16(duty)

    while True:
        for angle in range(180):
            servo_write(servo, angle)
            utime.sleep_ms(20)
        for angle in range(180, -1, -1):
            servo_write(servo, angle)
            utime.sleep_ms(20)

Cuando el programa se ejecute, veremos el Brazo del Servo oscilar de un lado a otro, entre los ángulos de 0° a 180°.

El programa se ejecutará de manera continua debido al bucle ``while True``; para detenerlo, es necesario presionar el botón de detención.

**¿Cómo funciona?**

Definimos la función ``servo_write()`` para controlar el movimiento del servo.

Esta función tiene dos parámetros:

* ``pin``, el pin GPIO que controla el servo.
* ``angle``, el ángulo de salida del eje.

En esta función, se llama a ``interval_mapping()`` para mapear el rango de ángulos de 0 a 180 en el rango de ancho de pulso de 0.5 a 2.5ms.

.. code-block:: python

    pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)

¿Por qué el rango es 0.5~2.5? Esto está determinado por el modo de funcionamiento del Servo.

:ref:`cpn_servo`

Luego, convertimos el ancho de pulso a período de duty. Dado que ``duty_u16()`` no acepta valores decimales (el valor no puede ser de tipo float), usamos ``int()`` para forzar la conversión de duty a un tipo int.

.. code-block:: python

    duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))

Finalmente, escribimos el valor de duty en ``duty_u16()``.
