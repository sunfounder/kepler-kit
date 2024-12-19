.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_joystick:

4.1 - Activación del Joystick
================================

Si juegas muchos videojuegos, entonces seguramente estás muy familiarizado con el joystick.
Normalmente se usa para mover al personaje, rotar la pantalla, etc.

El principio detrás de cómo el joystick permite que la computadora lea nuestras acciones es muy simple.
Se puede imaginar como dos potenciómetros perpendiculares entre sí.
Estos dos potenciómetros miden el valor analógico del joystick en las direcciones vertical y horizontal, generando así un valor (x,y) en un sistema de coordenadas rectangulares.

El joystick de este kit también tiene una entrada digital, que se activa al presionar el joystick.

* :ref:`cpn_joystick`

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Esquema**

|sch_joystick|

El pin SW está conectado a una resistencia pull-up de 10K, la razón es poder obtener un nivel alto estable en el pin SW (eje Z) cuando el joystick no está presionado; de lo contrario, el pin SW estaría en un estado flotante y el valor de salida podría variar entre 0 y 1.

**Conexión**

|wiring_joystick|

**Código**

.. note::

    * Puedes abrir el archivo ``4.1_toggle_the_joystick.ino`` en la ruta ``kepler-kit-main/arduino/4.1_toggle_the_joystick``.
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/dfe53878-7cb4-4543-bb97-7f5ef5aad15a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el programa, la consola imprimirá los valores de x, y, z del joystick.


* Los valores del eje X y del eje Y son valores analógicos que varían de 0 a 1023.
* El eje Z es un valor digital con un estado de 1 o 0.
