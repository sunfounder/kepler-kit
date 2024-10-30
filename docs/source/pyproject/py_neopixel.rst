.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones durante festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_neopixel:

3.3 Tira de LED RGB
======================

El WS2812 es una fuente de luz LED de control inteligente que integra el 
circuito de control y el chip RGB en un solo componente 5050. Incluye un 
puerto de datos digital inteligente, un circuito de transmisión de señal 
con amplificación y un oscilador interno de precisión, además de una sección 
de control de corriente constante programable, garantizando una consistencia 
alta en el color de los puntos de luz.

El protocolo de transmisión de datos utiliza el modo de comunicación NZR de 
un solo hilo. Después del reinicio de alimentación del píxel, el puerto DIN 
recibe datos del controlador; el primer píxel recopila los primeros 24 bits 
de datos, los envía al puerto interno y los demás datos, amplificados por el 
circuito de reshaping interno, se envían al siguiente píxel en cascada a través 
del puerto DO. Cada vez que se transmite un píxel, la señal se reduce en 24 bits. 
La tecnología de transmisión de reshaping automático permite un número ilimitado de píxeles en cascada, dependiendo únicamente de la velocidad de transmisión de la señal.

* :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Esquema**

|sch_ws2812|

**Conexiones**

|wiring_ws2812|

.. warning::
    Ten en cuenta el consumo de corriente.

    Aunque se puede usar la tira de LED con cualquier cantidad de LEDs en la Pico W, la potencia de su pin VBUS es limitada.
    Aquí usaremos ocho LEDs, lo cual es seguro.
    Pero si deseas utilizar más LEDs, necesitarás añadir una fuente de alimentación independiente.
    

**Código**

.. note::

    * Abre el archivo ``3.3_rgb_led_strip.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

    * Aquí necesitas usar la biblioteca llamada ``ws2812.py``, verifica si ha sido cargada en Pico W. Para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812

    ws = WS2812(machine.Pin(0),8)

    ws[0] = [64,154,227]
    ws[1] = [128,0,128]
    ws[2] = [50,150,50]
    ws[3] = [255,30,30]
    ws[4] = [0,128,255]
    ws[5] = [99,199,0]
    ws[6] = [128,128,128]
    ws[7] = [255,100,0]
    ws.write()


¡Seleccionemos algunos colores favoritos y mostrémonos en la tira de LED RGB!


**¿Cómo funciona?**

En la biblioteca ws2812, hemos integrado funciones relacionadas en la clase WS2812.

Puedes usar la tira de LED RGB con la siguiente declaración.

.. code-block:: python

    from ws2812 import WS2812

Declara un objeto de tipo WS2812, llamado "ws", que está conectado a "pin", y que contiene un "número" de LEDs RGB en la tira WS2812.

.. code-block:: python

    ws = WS2812(pin,number)

ws es un objeto de tipo array, cada elemento corresponde a un LED RGB en la tira WS2812, por ejemplo, ws[0] es el primero y ws[7] es el octavo.

Podemos asignar valores de color a cada LED RGB, estos valores deben ser en color de 24 bits (representados con seis dígitos hexadecimales) o una lista de 3 valores RGB de 8 bits.

Por ejemplo, el valor rojo es "0xFF0000" o "[255,0,0]".

.. code-block:: python

    ws[i] = color value

Luego utiliza esta declaración para escribir el color en la tira de LEDs y encenderla.

.. code-block:: python

    ws.write()

También puedes usar la siguiente declaración directamente para hacer que todos los LEDs se iluminen con el mismo color.

.. code-block:: python

    ws.write_all(color value)


**Aprende Más**

Podemos generar colores aleatorios y hacer un flujo de luz colorida.

.. note::

    * Abre el archivo ``3.3_rgb_led_strip_2.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812
    import utime
    import urandom

    ws = WS2812(machine.Pin(0),8)

    def flowing_light():
        for i in range(7,0,-1):
            ws[i] = ws[i-1]
        ws[0] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write()
        utime.sleep_ms(80)

    while True:
        flowing_light()
        print(ws[0])