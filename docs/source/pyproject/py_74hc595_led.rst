.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_74hc_led:

5.1 Microchip - 74HC595
===========================

Un circuito integrado (IC) es un dispositivo electrónico en miniatura que agrupa componentes como transistores, resistencias, condensadores, inductores y otros, fabricados en una o varias obleas de semiconductores o sustratos dieléctricos. Estos componentes se interconectan para formar una estructura con las funciones necesarias, avanzando la tecnología de componentes electrónicos hacia la miniaturización, bajo consumo, inteligencia y alta fiabilidad.

Los inventores de los circuitos integrados son Jack Kilby (basado en germanio (Ge)) y Robert Noyce (basado en silicio (Si)).

Este kit incluye el circuito integrado 74HC595, que permite ahorrar considerablemente el uso de pines GPIO. Específicamente, permite reemplazar 8 pines 
para la salida de señales digitales escribiendo un número binario de 8 bits.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`cpn_74hc595`

**Componentes Requeridos**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí tienes el enlace:

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
        - :ref:`cpn_resistor`
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Esquema**

|sch_74hc_led|

* Cuando MR (pin10) está en nivel alto y OE (pin13) en nivel bajo, los datos se ingresan en el flanco ascendente de SHcp y pasan al registro de memoria. 
* Si los dos relojes están conectados juntos, el registro de desplazamiento siempre está un pulso antes que el registro de memoria.
* En el registro de memoria hay un pin de entrada de desplazamiento en serie (Ds), un pin de salida en serie (Q) y un botón de reinicio asincrónico (nivel bajo).
* El registro de memoria saca una salida de bus paralelo de 8 bits en tres estados. 
* Cuando OE está habilitado (nivel bajo), los datos en el registro de memoria se envían al bus (Q0 ~ Q7).

**Conexión**

.. El 74HC595 es un CI de 16 pines con una muesca semicircular en un lado (normalmente en el lado izquierdo de la etiqueta). Con la muesca hacia arriba, sus pines están dispuestos según el diagrama a continuación.

.. Consulta el diagrama para construir el circuito.

|wiring_74hc_led|

.. 1. Conecta 3V3 y GND del Pico W a las líneas de alimentación de la breadboard.
.. #. Inserta el 74HC595 cruzando la brecha central de la breadboard.
.. #. Conecta el pin GP0 del Pico W al pin DS (pin 14) del 74HC595 con un cable de puente.
.. #. Conecta el pin GP1 del Pico W al pin STcp (pin 12) del 74HC595.
.. #. Conecta el pin GP2 del Pico W al pin SHcp (pin 11) del 74HC595.
.. #. Conecta el pin VCC (pin 16) y el pin MR (pin 10) del 74HC595 a la línea de alimentación positiva.
.. #. Conecta el pin GND (pin 8) y el pin CE (pin 13) del 74HC595 a la línea de alimentación negativa.
.. #. Inserta 8 LEDs en la breadboard, y conecta los pines de ánodo a los pines Q0~Q1 (15, 1, 2, 3, 4, 5, 6, 7) del 74HC595.
.. #. Conecta los cátodos de los LEDs con una resistencia de 220Ω en serie a la línea de alimentación negativa.

**Código**

.. note::

    * Abre el archivo ``5.1_microchip_74hc595.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha. 

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)

    num = 0

    for i in range(16):
        if i < 8:
            num = (num<<1) + 1
        elif i>=8:
            num = (num & 0b01111111)<<1
        hc595_shift(num)
        print("{:0>8b}".format(num))
        time.sleep_ms(200)

Cuando el programa se está ejecutando, ``num`` se escribe en el chip 74HC595 como un número binario de ocho bits para controlar el encendido y apagado de los 8 LEDs. Podemos ver el valor actual de ``num`` en el shell.


**¿Cómo funciona?**

``hc595_shift()`` hace que el 74HC595 emita 8 señales digitales. Emite el último bit del número binario a Q0, y el primer bit a Q7. En otras palabras, escribir el número binario “00000001” hará que Q0 emita un nivel alto y Q1~Q7 emitan nivel bajo.
