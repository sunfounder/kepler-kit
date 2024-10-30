.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora en profundidad Raspberry Pi, Arduino y ESP32 junto a otros aficionados.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_neopixel:

3.3 - Tira RGB WS2812
==========================

WS2812 es una fuente de luz LED con control inteligente donde el circuito de 
control y el chip RGB están integrados en un componente de 5050. Internamente, 
incluye un puerto digital de almacenamiento de datos inteligente y un circuito 
de amplificación para la remodelación de la señal. También incorpora un oscilador 
interno de alta precisión y una parte de control de corriente constante programable, 
asegurando que el color de cada punto de píxel sea altamente consistente.

El protocolo de transferencia de datos utiliza un modo de comunicación NZR único. 
Después de que el píxel se enciende y se reinicia, el puerto DIN recibe datos del 
controlador; el primer píxel recoge 24 bits de datos iniciales y los envía a un 
almacenamiento interno, mientras que el resto de los datos se transmiten al siguiente 
píxel en cascada a través del puerto DO, gracias a la circuitería interna de amplificación 
de señal. La tecnología de transmisión con auto-remodelación permite que el número de píxeles en cascada no tenga limitaciones en cuanto a la transmisión de la señal, y depende solo de la velocidad de transmisión de ésta.

* :ref:`cpn_ws2812`

**Componentes necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Esquema**

|sch_ws2812|

**Conexión**

|wiring_ws2812|

.. warning::
    Un aspecto a tener en cuenta es la corriente.

    Aunque se puede utilizar una tira LED con cualquier número de LEDs en el Pico W, la potencia de su pin VBUS es limitada.
    Aquí utilizaremos ocho LEDs, lo cual es seguro.
    Pero si deseas usar más LEDs, necesitarás una fuente de alimentación separada.
    

**Código**

.. note::

    * Puedes abrir el archivo ``3.3_rgb_led_strip.ino`` en la ruta ``kepler-kit-main/arduino/3.3_rgb_led_strip``.
    * O copiar este código en el **Arduino IDE**.
    * Luego selecciona la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.
    * Aquí se utiliza la biblioteca ``Adafruit_NeoPixel``, que puedes instalar desde el **Library Manager**.

      .. image:: img/lib_neopixel.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/efe5d60f-ea0f-4446-bc5b-30c76197fedf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Seleccionemos algunos colores favoritos y mostremos en la tira de LED RGB.

**¿Cómo funciona?**

Declara un objeto de tipo Adafruit_NeoPixel, conectado a ``PIXEL_PIN``, donde hay ``PIXEL_COUNT`` LEDs RGB en la tira.

.. code-block:: arduino

    #define PIXEL_PIN    0
    #define PIXEL_COUNT 8

    // Declaramos nuestro objeto NeoPixel para la tira:
    Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
    // Argumento 1 = Número de píxeles en la tira NeoPixel
    // Argumento 2 = Número de pin de Arduino (la mayoría son válidos)
    // Argumento 3 = Banderas de tipo de píxel, agrega según sea necesario:
    //   NEO_KHZ800  800 KHz bitstream (la mayoría de productos NeoPixel con LEDs WS2812)
    //   NEO_KHZ400  400 KHz (pixeles clásicos 'v1' (no v2) FLORA, controladores WS2811)
    //   NEO_GRB     Pixeles cableados para bitstream GRB (la mayoría de productos NeoPixel)
    //   NEO_RGB     Pixeles cableados para bitstream RGB (pixeles v1 FLORA, no v2)
    //   NEO_RGBW    Pixeles cableados para bitstream RGBW (productos NeoPixel RGBW)

Inicializa el objeto strip y todos los píxeles a 'apagado'.

Funciones
    * ``strip.begin()`` : Inicializa el objeto de la tira NeoPixel (OBLIGATORIO).
    * ``strip.setPixelColor(index, color)`` : Configura el color de un píxel (en RAM), el ``color`` debe ser un valor único de 32 bits 'empaquetado'.
    * ``strip.Color(red, green, blue)`` : Color como un valor de 32 bits 'empaquetado'.
    * ``strip.show()`` : Actualiza la tira con el nuevo contenido.
  
**Aprende más**

Podemos generar colores aleatorios y crear un efecto de luz fluida y colorida.

.. note::

    * Puedes abrir el archivo ``3.3_rgb_led_strip_flowing.ino`` en la ruta ``kepler-kit-main/arduino/3.3_rgb_led_strip_flowing``.
    * O copiar este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a3d7c520-b4f8-4445-9454-5fe7d2a24fd9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

O puedes hacer que esta tira de LED WS2812 realice un ciclo de arcoíris alrededor de la rueda de color (rango 65535).

.. note::

   * Puedes abrir el archivo ``3.3_rgb_led_strip_rainbow.ino`` en la ruta ``kepler-kit-main/arduino/3.3_rgb_led_strip_rainbow``.
   * O copiar este código en el **IDE de Arduino**.
   * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/47d84804-3560-48fa-86df-49f8e2f6ad63/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>   

* ``strip.getPixelColor(index)`` : Consulta el color de un píxel previamente configurado.
* ``strip.ColorHSV(pixelHue)`` : Convierte el tono, la saturación y el valor en un color RGB de 32 bits empaquetado, que puede ser pasado a ``setPixelColor()`` u otras funciones compatibles con RGB.
* ``strip.gamma32()`` : Proporciona un color "más verdadero" antes de asignarlo a cada píxel.

