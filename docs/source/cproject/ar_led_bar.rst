.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_led_bar:

2.2 - Mostrar el Nivel
=============================

El primer proyecto consiste en hacer que un LED parpadee. En este proyecto, utilizaremos el LED Bar Graph, que está compuesto por 10 LEDs empaquetados en una carcasa plástica y se usa generalmente para mostrar niveles de potencia o volumen.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Esquema**

|sch_ledbar|

El LED Bar Graph contiene 10 LEDs, cada uno de los cuales se puede controlar individualmente. Aquí, el ánodo de cada uno de los 10 LEDs está conectado a GP6~GP15, el cátodo está conectado a una resistencia de 220Ω y luego a GND.

**Conexión**

|wiring_ledbar|

**Código**

.. note::

    * Puedes abrir el archivo ``2.2_display_the_level.ino`` en la ruta ``kepler-kit-main/arduino/2.2_display_the_level``.
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/ae60e723-430e-4a58-ac39-566b9d1828e8/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Cuando el programa se ejecuta, verás que los LEDs del LED Bar Graph se encienden y se apagan secuencialmente.

**¿Cómo funciona?**

Cada uno de los diez LEDs en el LED Bar necesita ser controlado por un pin, por lo que definimos estos diez pines.

En el ``setup()``, el bucle for inicializa los pines 6~15 en modo de salida.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        pinMode(i,OUTPUT);
    }   

En el ``loop()``, el bucle for hace que el LED parpadee (enciende por 0.5s y luego apaga por 0.5s) de forma secuencial.

.. code-block:: C

    for(int i=6;i<=15;i++)
    {
        digitalWrite(i,HIGH);
        delay(500);
        digitalWrite(i,LOW);
        delay(500);    
    }