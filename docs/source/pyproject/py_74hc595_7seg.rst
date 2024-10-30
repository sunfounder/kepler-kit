.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_74hc_7seg:

5.2 Visualización de Números
=================================

El display de 7 segmentos se puede encontrar en muchos dispositivos cotidianos.
Por ejemplo, en un aire acondicionado, se usa para mostrar la temperatura; en un indicador de tráfico, para mostrar el temporizador.

El display de 7 segmentos es, esencialmente, un dispositivo formado por 8 LEDs: 7 de ellos forman una figura con forma de "8" y un LED adicional más pequeño actúa como punto decimal. Estos LEDs están etiquetados como a, b, c, d, e, f, g y dp. Tienen sus propios pines de ánodo y comparten el cátodo. Sus ubicaciones están ilustradas en la figura a continuación.

|img_7seg_cathode|

Esto significa que necesita ser controlado por 8 señales digitales simultáneamente para funcionar completamente, y el 74HC595 es capaz de manejarlo.

* :ref:`cpn_7_segment`

**Componentes Requeridos**

En este proyecto, necesitaremos los siguientes componentes.

Es bastante conveniente comprar un kit completo; aquí tienes el enlace:

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Esquema**

|sch_74hc_7seg|

Aquí, el principio de cableado es básicamente el mismo que en :ref:`py_74hc_led`, la única diferencia es que Q0-Q7 están conectados a los pines a ~ g del display de 7 segmentos.

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - Display de Segmentos :ref:`cpn_led`
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**Cableado**

.. 1. Conecta 3V3 y GND del Pico W a las líneas de alimentación de la breadboard.
.. #. Inserta el 74HC595 cruzando la brecha central en la breadboard.
.. #. Conecta el pin GP0 del Pico W al pin DS (pin 14) del 74HC595 con un cable.
.. #. Conecta el pin GP1 del Pico W al pin STcp (pin 12) del 74HC595.
.. #. Conecta el pin GP2 del Pico W al pin SHcp (pin 11) del 74HC595.
.. #. Conecta el pin VCC (pin 16) y el pin MR (pin 10) del 74HC595 a la línea de alimentación positiva.
.. #. Conecta el pin GND (pin 8) y el pin CE (pin 13) del 74HC595 a la línea de alimentación negativa.
.. #. Inserta el display de segmentos en la breadboard y conecta una resistencia de 220Ω en serie con el pin GND a la línea de alimentación negativa.
.. #. Sigue la tabla a continuación para conectar el 74HC595 y el display de segmentos.

|wiring_74hc_7seg|

**Código**

.. note::

    * Abre el archivo ``5.2_number_display.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

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
        
    while True:
        for num in range(10):
            hc595_shift(SEGCODE[num])
            time.sleep_ms(500)

Cuando el programa esté en ejecución, verás el display de segmentos LED mostrando los números del 0 al 9 en secuencia.

**¿Cómo funciona?**

``hc595_shift()`` hará que el 74HC595 emita 8 señales digitales.
Emite el último bit del número binario a Q0, y el primer bit a Q7. En otras palabras, escribir el número binario "00000001" hará que Q0 emita un nivel alto y Q1~Q7 emitan un nivel bajo.

Por ejemplo, si el display de 7 segmentos muestra el número "1", necesitamos emitir un nivel alto para los pines b y c, y un nivel bajo para los pines a, d, e, f, g y dp.

|img_1_segment|

Esto significa que necesitamos escribir el número binario "00000110". Para mayor legibilidad, utilizaremos notación hexadecimal como "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

De manera similar, también podemos hacer que el display de segmentos muestre otros números de la misma forma. La siguiente tabla muestra los códigos correspondientes a estos números.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Números
        - Código Binario
        - Código Hexadecimal
    *   - 0
        - 00111111
        - 0x3f
    *   - 1
        - 00000110
        - 0x06
    *   - 2
        - 01011011
        - 0x5b
    *   - 3
        - 01001111
        - 0x4f
    *   - 4
        - 01100110
        - 0x66
    *   - 5
        - 01101101
        - 0x6d
    *   - 6
        - 01111101
        - 0x7d
    *   - 7
        - 00000111
        - 0x07
    *   - 8
        - 01111111
        - 0x7f
    *   - 9
        - 01101111
        - 0x6f

Escribe estos códigos en ``hc595_shift()`` para que el display de segmentos LED muestre los números correspondientes.
