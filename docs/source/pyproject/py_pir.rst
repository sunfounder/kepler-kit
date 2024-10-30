.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_pir:

2.10 Detección de Movimiento Humano
========================================

El sensor de infrarrojos pasivo (sensor PIR) es un sensor común que puede medir 
la luz infrarroja (IR) emitida por objetos en su campo de visión. En términos 
sencillos, detecta la radiación infrarroja emitida por el cuerpo, permitiendo 
así detectar el movimiento de personas y otros animales. Más específicamente, 
informa a la placa de control principal cuando alguien ha ingresado a tu habitación.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Esquema**

|sch_pir|

Cuando el módulo PIR detecta que alguien pasa, el pin GP14 se activa (nivel alto); de lo contrario, permanece en nivel bajo.

.. note::
    El módulo PIR tiene dos potenciómetros: uno ajusta la sensibilidad y el otro ajusta la distancia de detección. Para que el módulo PIR funcione de manera óptima, gira ambos potenciómetros completamente en sentido antihorario.

    |img_PIR_TTE|

**Conexiones**

|wiring_pir|

**Código**

.. note::

    * Abre el archivo ``2.10_detect_human_movement.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Somebody here!")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

Después de ejecutar el programa, si el módulo PIR detecta a alguien cerca, la Shell imprimirá "¡Alguien está aquí!".

**Aprende Más**

El PIR es un sensor muy sensible. Para adaptarlo al entorno de uso, es necesario ajustarlo. Con los dos potenciómetros mirando hacia ti, gira ambos en sentido antihorario hasta el final e inserta el puente en el pin L y el pin central.


.. note::

    * Abre el archivo ``2.10_pir_adjustment.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    global timer_delay
    timer_delay = utime.ticks_ms()
    print("start")

    def pir_in_high_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_FALLING, handler=pir_in_low_level)    
        intervals = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()
        print("the dormancy duration is " + str(intervals) + "ms")

    def pir_in_low_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 
        intervals2 = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()        
        print("the duration of work is " + str(intervals2) + "ms")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 

Analicemos el método de ajuste junto con los resultados del experimento.

|img_pir_back|

1. Modo de Activación

    Observemos los pines con el puente en la esquina. Permiten que el PIR 
    entre en el modo de activación repetitiva o no repetitiva.

    Actualmente, nuestro puente conecta el Pin central y el Pin L, colocando 
    el PIR en modo de activación no repetitiva. En este modo, cuando el PIR 
    detecta movimiento, envía una señal de alto nivel de aproximadamente 2.8 
    segundos a la placa de control principal. En los datos impresos, la duración 
    de la activación siempre será de alrededor de 2800ms.

    A continuación, cambiaremos la posición del puente inferior y lo conectaremos 
    al Pin central y al Pin H para poner el PIR en modo de activación repetitiva. 
    En este modo, el PIR continuará enviando una señal de alto nivel a la placa de 
    control principal siempre que detecte movimiento dentro de su rango de detección. 
    En los datos impresos, la duración de la activación será variable.

#. Ajuste de Retardo

    El potenciómetro de la izquierda ajusta el intervalo entre dos detecciones consecutivas.
    
    Actualmente, está completamente en sentido antihorario, lo que hace que el PIR tenga un tiempo de inactividad de aproximadamente 5 segundos tras enviar una señal de trabajo de alto nivel. Durante este tiempo, el PIR no detectará radiación infrarroja en el área objetivo. En los datos impresos, la duración de la inactividad será de al menos 5000ms.

    Si giramos el potenciómetro en sentido horario, el tiempo de inactividad aumentará. Al girarlo al máximo en sentido horario, el tiempo de inactividad será de hasta 300 segundos.

#. Ajuste de Distancia

    El potenciómetro central ajusta el rango de distancia de detección del PIR.

    Gira el potenciómetro de ajuste de distancia **en sentido horario** para aumentar el rango de detección; 
    la distancia máxima es de aproximadamente 0-7 metros. Si giras **en sentido antihorario**, el rango de detección disminuye; la distancia mínima es de aproximadamente 0-3 metros.
