.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_tilt:

2.6 - ¡Inclínalo!
==========================

|img_tilt|

El interruptor de inclinación es un dispositivo de 2 pines con una bola de metal en su interior. Cuando está en posición vertical, los dos pines se conectan entre sí; al inclinar el interruptor, los dos pines se desconectan.


**Componentes Necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**Esquema**

|sch_tilt|

Cuando el interruptor está en posición vertical, GP14 se establece en alto; al inclinarlo, GP14 se establece en bajo.

La resistencia de 10K sirve para mantener GP14 en un estado bajo estable cuando el interruptor de inclinación está inclinado.

* :ref:`cpn_tilt`

**Conexión**

|wiring_tilt|

**Código**

.. note::

    * Puedes abrir el archivo ``2.6_tilt_it.ino`` en la ruta ``kepler-kit-main/arduino/2.4_colorful_light``. 
    * O copia este código en **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/0421b002-a697-4f22-a965-0e62e8dc3abf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>




Cuando el programa se esté ejecutando, al inclinar la breadboard (interruptor de inclinación), aparecerá en la consola el mensaje "¡El interruptor funciona!".
