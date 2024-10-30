.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_rgb:

2.4 Luz Colorida
==============================================

Como sabemos, la luz puede superponerse. Por ejemplo, al mezclar luz azul y verde se obtiene luz cian, mientras que al combinar luz roja y verde obtenemos luz amarilla. Esto se denomina “Método Aditivo de Mezcla de Colores”.

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Basándonos en este método, podemos usar los tres colores primarios para mezclar luz visible de cualquier color, ajustando las proporciones. Por ejemplo, el naranja se puede obtener con más rojo y menos verde.

En este capítulo, usaremos un LED RGB para explorar el misterio de la mezcla aditiva de colores.

Un LED RGB es equivalente a encapsular un LED rojo, uno verde y uno azul bajo una misma carcasa, 
compartiendo un cátodo común. Al proporcionar señal eléctrica a cada ánodo, se puede visualizar el color correspondiente. Cambiando la intensidad de la señal en cada ánodo, es posible generar diversos colores.

* :ref:`cpn_rgb`

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
        - :ref:`cpn_resistor`
        - 3 (1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Esquemático**

|sch_rgb|

Los pines PWM GP13, GP14 y GP15 controlan respectivamente los pines rojo, verde y azul del LED RGB, y el pin de cátodo común se conecta a GND. Esto permite que el LED RGB muestre un color específico al superponer luces en estos pines con diferentes valores PWM.

**Conexiones**

|img_rgb_pin|

El LED RGB tiene 4 pines: el pin largo es el cátodo común, que generalmente se conecta a GND; el pin a la izquierda junto al más largo es el rojo; y los dos pines de la derecha son verde y azul.

|wiring_rgb|

**Código**

.. note::

    * Abre el archivo ``2.4_colorful_light.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
        return rgb_value

    def color_set(red_value,green_value,blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255,128,0)

Aquí, puedes elegir tu color favorito en un software de dibujo (como Paint) y visualizarlo en el LED RGB.

|img_take_color|

Escribe el valor RGB en ``color_set()``, y verás cómo el LED RGB ilumina los colores que deseas.



**¿Cómo funciona?**

Para permitir que los tres colores primarios trabajen juntos, hemos definido la función ``color_set()``.

Actualmente, los píxeles en hardware de computadoras suelen utilizar representaciones de 24 bits. Cada color primario se divide en 8 bits, y el rango del valor del color es de 0 a 255. Existen 256 combinaciones posibles para cada uno de los tres colores primarios (¡no olvides contar el 0!), resultando en 256 x 256 x 256 = 16,777,216 colores. La función ``color_set()`` también utiliza la notación de 24 bits, permitiéndote seleccionar un color con mayor facilidad.

Y dado que el rango de valores de ``duty_u16()`` es de 0 a 65535 (en lugar de 0 a 255) cuando se envían señales al LED RGB a través de PWM, hemos definido las funciones ``color_to_duty()`` e ``interval_mapping()`` para mapear los valores de color a los valores de ciclo de trabajo.
