.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_ultrasonic:

6.1 Midiendo Distancia
========================

El módulo de sensor ultrasónico funciona según el principio de sistemas de sonar y radar para determinar la distancia a un objeto.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Esquemático**

|sch_ultrasonic|

**Conexiones**

|wiring_ultrasonic|

**Código**

.. note::

    * Abre el archivo ``6.1_measuring_distance.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.
    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.
    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print ('Distance: %.2f' % dis)
        time.sleep_ms(300)

Una vez que el programa esté en ejecución, la Shell imprimirá la distancia medida por el sensor ultrasónico respecto al obstáculo situado enfrente.

**¿Cómo funciona?**

Los sensores ultrasónicos producen ondas sonoras de alta frecuencia (ultrasonido) que son emitidas por la sonda transmisora. Cuando esta onda ultrasónica impacta un objeto, se refleja como un eco, detectado por la sonda receptora. Calculando el tiempo entre la emisión y la recepción, se puede determinar la distancia. Basado en este principio, se deriva la función ``distance()``.

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

* Las primeras líneas se usan para transmitir una onda ultrasónica de 10us.

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

* Luego, el programa se pausa y registra el tiempo actual cuando se ha emitido la onda ultrasónica.

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

* Posteriormente, el programa se pausa nuevamente. Tras recibir el eco, se registra el tiempo actual otra vez.

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

* Finalmente, basándose en la diferencia de tiempo entre las dos lecturas y la velocidad del sonido (340 m/s), se obtiene el doble de la distancia entre el módulo ultrasónico y el obstáculo (es decir, ida y vuelta de las ondas ultrasónicas). Convirtiendo las unidades a centímetros, obtenemos el valor de retorno que necesitamos.

.. code-block:: python

        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

Toma en cuenta que el sensor ultrasónico pausará el programa cuando esté en funcionamiento, lo cual puede causar algún retraso al escribir proyectos complejos.
