.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_dht11:

6.2 Temperatura - Humedad
=======================================

La temperatura y la humedad están estrechamente relacionadas tanto en términos 
de física como en la vida cotidiana de las personas. La temperatura y la humedad 
del entorno afectan directamente la función termorreguladora y la transferencia 
de calor en el cuerpo humano. Esto, a su vez, puede influir en el estado mental 
y la capacidad de concentración, afectando así nuestra eficiencia en el estudio 
y el trabajo.

La temperatura es una de las siete magnitudes físicas básicas en el Sistema 
Internacional de Unidades, utilizada para medir el grado de calor o frío de un 
objeto. La escala Celsius es una de las más utilizadas en el mundo, y se 
representa con el símbolo "℃".

La humedad es la concentración de vapor de agua presente en el aire. En la vida 
diaria se usa comúnmente la humedad relativa del aire, expresada en %HR. La 
humedad relativa está directamente relacionada con la temperatura. Para un 
volumen de gas sellado, a mayor temperatura, menor es la humedad relativa, y a 
menor temperatura, mayor es la humedad relativa.

|img_Dht11|

Este kit incluye un sensor digital básico de temperatura y humedad, el **DHT11**. Utiliza un sensor capacitivo de humedad y un termistor para medir el aire circundante y emite una señal digital en los pines de datos (no se requieren pines de entrada analógica).

* :ref:`cpn_dht11`

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Esquema**

|sch_dht11|

**Conexión**

|wiring_dht11|

**Código**

.. note::

    * Abre el archivo ``6.2_temperature_humidity.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`. 
    
    * Aquí necesitas usar la biblioteca llamada ``dht.py``; por favor verifica si ha sido cargada en el Pico W. Para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    from machine import Pin
    import utime as time
    from dht import DHT11, InvalidPulseCount

    pin = Pin(16, Pin.IN)
    sensor = DHT11(pin)
    time.sleep(5)  # retraso inicial

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')




Después de ejecutar el código, verás en la consola los valores de temperatura y humedad continuamente, y a medida que el programa se ejecute de forma estable, estos valores se volverán cada vez más precisos.

**¿Cómo funciona?**

En la biblioteca dht, hemos integrado la funcionalidad relevante en la clase ``DHT11``.

.. code-block:: python

    from dht import DHT11, InvalidPulseCount

Inicializa el objeto ``DHT11``. Este dispositivo solo necesita una entrada digital para ser usado.

.. code-block:: python

    pin = Pin(16, Pin.IN)
    sensor = DHT11(pin)

Usa ``sensor.measure()`` para leer la temperatura y la humedad actuales, que se almacenarán en ``sensor.temperature`` y ``sensor.humidity``. Luego se imprimen en pantalla.
Finalmente, como la tasa de muestreo del DHT11 es de 1Hz, se necesita un ``time.sleep(1)`` en el bucle.

.. code-block:: python

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')
