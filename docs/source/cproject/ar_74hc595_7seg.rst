.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_74hc_7seg:

5.2 - Visualización de Números
=================================

Las pantallas LED de segmentos son visibles en numerosos dispositivos de la 
vida cotidiana. Por ejemplo, en un aire acondicionado se usan para mostrar la temperatura, o en un indicador de tráfico, para mostrar un temporizador.

La pantalla LED de segmentos es, en esencia, un dispositivo formado por 8 LEDs, de los cuales 7 LEDs en forma de tira forman un "8" y hay un LED adicional, más pequeño y punteado, como punto decimal. Estos LEDs están etiquetados como a, b, c, d, e, f, g y dp. Cada uno tiene su propio pin de ánodo y comparten un cátodo común. La ubicación de los pines se muestra en la figura a continuación.

|img_7seg_cathode|

Esto significa que necesita ser controlado por 8 señales digitales simultáneas para funcionar completamente, y el 74HC595 puede realizar esta función.

* :ref:`cpn_7_segment`


**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

Es muy conveniente adquirir un kit completo, aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ITEMS EN ESTE KIT
        - LINK DE COMPRA
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCCIÓN DEL COMPONENTE
        - CANTIDAD
        - LINK DE COMPRA

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

**Conexión**

|wiring_74hc_7seg|

.. list-table:: Conexiones
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segment Display
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

**Código**

.. note::

    * Puedes abrir el archivo ``5.2_number_display.ino`` en la ruta ``kepler-kit-main/arduino/5.2_number_display``.
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/a237801f-40d7-4920-80fb-a349307b1e05/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Cuando el programa esté en ejecución, podrás ver cómo la Pantalla LED de Segmentos muestra los números del 0 al 9 en secuencia.

**¿Cómo funciona?**

La función ``shiftOut()`` hace que el 74HC595 emita 8 señales digitales. Esta emite el último bit del número binario en Q0, y el primer bit en Q7. Es decir, al escribir el número binario "00000001", Q0 emitirá un nivel alto y Q1~Q7 emitirán un nivel bajo.

Supongamos que la pantalla de 7 segmentos debe mostrar el número "1". En este caso, necesitamos escribir un nivel alto para b y c, y un nivel bajo para a, d, e, f, g y dp. Esto corresponde al número binario "00000110". Para mayor legibilidad, utilizaremos la notación hexadecimal "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

De manera similar, podemos mostrar otros números en la Pantalla LED de Segmentos de la misma manera. La siguiente tabla muestra los códigos correspondientes a cada número.

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

Escribe estos códigos en ``shiftOut()`` para que la Pantalla LED de Segmentos muestre los números correspondientes.
