.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en temas más avanzados sobre Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_led_bar:

2.2 Visualización del Nivel
================================

En el primer proyecto simplemente hicimos parpadear un LED. Para este proyecto, usaremos una Barra de LED, que contiene 10 LEDs en una carcasa plástica, comúnmente utilizada para mostrar niveles de potencia o de volumen.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Componentes Necesarios**

Para este proyecto, necesitaremos los siguientes componentes.

Es más conveniente adquirir un kit completo, aquí tienes el enlace:

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Esquema**


|sch_ledbar|

La Barra de LED cuenta con 10 LEDs, cada uno de los cuales puede controlarse individualmente. El ánodo de cada LED está conectado a GP6*GP15, mientras que el cátodo se conecta a una resistencia de 220 ohmios y luego a tierra (GND).

**Conexiones**

|wiring_ledbar|

**Código**

.. note::

    * Abre el archivo ``2.2_display_the_level.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

En la Barra de LED, verás que los LEDs se encienden y apagan secuencialmente mientras el programa está en ejecución.

**¿Cómo funciona?**

La Barra de LED consta de diez LEDs controlados por diez pines, por lo que debemos definir estos pines. El proceso sería muy tedioso si los definiéramos uno por uno. Aquí utilizamos ``listas``.

.. note::
    Las listas de Python son uno de los tipos de datos más versátiles, que nos permiten trabajar con múltiples elementos a la vez. Se crean colocando elementos dentro de corchetes [], separados por comas.

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

La línea anterior define una lista llamada ``pin`` que contiene los diez 
elementos ``6,7,8,9,10,11,12,13,14,15``. Podemos usar el operador de 
índice [] para acceder a un elemento de una lista. En Python, los índices 
comienzan en 0. Así, una lista de 10 elementos tendrá índices de 0 a 9. 
En este caso, ``pin[0]`` es ``6`` y ``pin[4]`` es ``10``.

Luego, declaramos una lista vacía ``led`` que usaremos para definir diez objetos LED.

.. code-block:: python

    led = []    

Debido a que la lista inicialmente tiene una longitud de 0, no se pueden realizar operaciones directas en ella, como imprimir ``led[0]``. Es necesario agregar nuevos elementos.

.. code-block:: python

    led.append(None)

El método ``append()`` agrega el primer elemento a la lista ``led``, que ahora tiene una longitud de 1. ``led[0]`` se convierte en un elemento válido, aunque actualmente su valor es ``None`` (lo que significa nulo).

A continuación, definimos ``led[0]``, el LED conectado al pin 6, como el primer objeto LED.

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

Ahora se ha definido el primer objeto LED.

Como puedes ver, hemos creado la lista de diez números de pines llamada **pin**, que podemos utilizar para simplificar las operaciones masivas.

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

Usamos una instrucción ``for`` para que todos los 10 pines ejecuten la declaración anterior.

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`syntax_list`
* :ref:`syntax_forloop`

Usa otro bucle ``for`` para hacer que los diez LEDs de la Barra de LED cambien de estado uno por uno.

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

El código se completa colocando el fragmento anterior en un bucle ``while``.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)


