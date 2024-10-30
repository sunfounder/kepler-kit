.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en temas avanzados sobre Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_led:

2.1 ¡Hola, LED!
===================

Así como imprimir "¡Hola, mundo!" es el primer paso para aprender a programar, controlar un LED mediante programación es la introducción clásica al aprendizaje de la programación física.

* :ref:`cpn_led`

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Esquema**

|sch_led|

Este circuito funciona con un principio simple, y la dirección de la corriente se muestra en la figura. El LED se encenderá después de la resistencia limitadora de corriente de 220 ohmios cuando GP15 emite un nivel alto (3.3v). El LED se apagará cuando GP15 emita un nivel bajo (0v).

**Conexiones**

|wiring_led|

¡Para montar el circuito, sigamos la dirección de la corriente!

1. El LED se alimenta mediante el pin GP15 de la placa Pico W, y el circuito comienza aquí.
#. Para proteger el LED, la corriente debe pasar a través de una resistencia de 220 ohmios. Inserta un extremo de la resistencia en la misma fila que el pin GP15 de Pico W (fila 20 en mi circuito) y el otro extremo en una fila libre de la placa de pruebas (fila 24).

    .. note::
        La resistencia de 220 ohmios tiene bandas de color rojo, rojo, negro, negro y marrón.

#. Si observas el LED, verás que uno de sus pines es más largo que el otro. Conecta el pin más largo a la misma fila que la resistencia y el pin más corto a la fila opuesta de la placa de pruebas.

    .. note::
        El pin más largo es el ánodo, que representa el lado positivo del circuito; el pin más corto es el cátodo, que representa el lado negativo.

        El ánodo debe estar conectado al pin GPIO a través de una resistencia; el cátodo debe estar conectado al pin GND.

#. Usa un cable de puente macho a macho (M2M) para conectar el pin corto del LED al bus negativo de la placa de pruebas.
#. Conecta el pin GND de Pico W al bus negativo de la placa de pruebas usando un cable de puente.


**Código**

.. note::

    * Abre el archivo ``2.1_hello_led.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

Después de ejecutar el código, verás que el LED parpadea.


**¿Cómo funciona?**


La biblioteca machine es necesaria para usar GPIO.

.. code-block:: python

    import machine

La biblioteca contiene todas las instrucciones necesarias para la comunicación entre MicroPython y Pico W. 
Sin esta línea de código, no podremos controlar los GPIO.

Observa la siguiente línea:

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

Aquí definimos el objeto ``led``. Técnicamente, podría tener cualquier nombre, como x, y, banana o cualquier otra cosa.
Para facilitar la lectura del programa, es mejor utilizar un nombre que describa su propósito.

En la segunda parte de esta línea (después del signo igual), llamamos a la función Pin que se encuentra en la biblioteca ``machine``. Sirve para indicar a los pines GPIO de Pico qué hacer.
La función ``Pin`` tiene dos parámetros: el primero (15) representa el pin a configurar;
el segundo parámetro (machine.Pin.OUT) especifica que el pin debe ser de salida en lugar de entrada.

El código anterior "configura" el pin, pero no encenderá el LED. Para esto, necesitamos también "usar" el pin.

.. code-block:: python

    led.value(1)

El pin GP15 ha sido configurado previamente y nombrado ``led``. La función de esta declaración es establecer el valor de ``led`` en 1 para encender el LED.

En resumen, para usar GPIO, estos pasos son necesarios:

* **Importar la biblioteca machine**: Esto es esencial y solo se ejecuta una vez.
* **Configurar GPIO**: Antes de su uso, cada pin debe configurarse.
* **Usar**: Cambiar el estado de funcionamiento del pin asignándole un valor.

Si seguimos los pasos anteriores para escribir un ejemplo, obtendrás un código como este:

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

Ejecuta el código y podrás encender el LED.

A continuación, intentemos agregar una instrucción para apagarlo:

.. code-block:: python

    import machine   
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

Según el código, este programa encenderá primero el LED y luego lo apagará. 
Sin embargo, al ejecutarlo, verás que no ocurre como esperabas.
El LED no emite luz visible. Esto se debe a que la ejecución entre ambas líneas es muy rápida, mucho más de lo que el ojo humano puede percibir. 
Cuando el LED se enciende, no percibimos la luz de inmediato. Esto se soluciona ralentizando el programa.

La segunda línea del programa debería contener la siguiente instrucción:

.. code-block:: python

    import utime

Similar a ``machine``, la biblioteca ``utime`` se importa aquí y maneja todo lo relacionado con el tiempo.
La demora que necesitamos está incluida aquí. Añade una instrucción de pausa entre ``led.value(1)`` y ``led.value(0)`` para que estén separados por 2 segundos.

.. code-block:: python

    utime.sleep(2)

Así es como debería verse ahora el código. 
Veremos que el LED se enciende primero y luego se apaga cuando lo ejecutamos:

.. code-block:: python

    import machine 
    import utime  
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

Finalmente, debemos hacer que el LED parpadee. 
Crea un bucle, reescribe el programa, y será como lo viste al inicio de este capítulo.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`py_syntax_while` 

**Para Aprender Más**


Por lo general, habrá un archivo de API (Interfaz de Programación de Aplicaciones) asociado con la biblioteca. 
Este contiene toda la información necesaria para utilizar la biblioteca, incluyendo descripciones detalladas de funciones, clases, tipos de retorno, tipos de parámetros, etc.

En este artículo usamos las bibliotecas ``machine`` y ``utime`` de MicroPython. Podemos encontrar más formas de utilizarlas aquí:

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

¡Revisa el archivo API para comprender mejor este ejemplo de cómo hacer parpadear el LED!

.. note::

    * Abre el archivo ``2.1_hello_led_2.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)