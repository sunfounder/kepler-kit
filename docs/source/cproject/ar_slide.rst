.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_slide:

2.7 - Alternar Izquierda y Derecha
======================================

|img_slide|

El interruptor de deslizamiento es un dispositivo de 3 pines, con el pin 2 (central) como pin común. Cuando el interruptor se desliza hacia la izquierda, los dos pines izquierdos se conectan, y cuando se desliza hacia la derecha, se conectan los dos pines derechos.

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Esquema**

|sch_slide|

GP14 recibirá un nivel diferente cuando deslices el interruptor hacia la derecha o la izquierda.

La resistencia de 10K tiene como objetivo mantener GP14 en bajo mientras se desliza (sin deslizarse completamente a la izquierda o completamente a la derecha).

El condensador cerámico de 104 se usa aquí para eliminar el ruido.

* :ref:`cpn_slide_switch`
* :ref:`cpn_capacitor`

**Conexión**

|wiring_slide|

**Código**

.. note::

    * Puedes abrir el archivo ``2.7_toggle_left_right.ino`` en la ruta ``kepler-kit-main/arduino/2.7_toggle_left_right``. 
    * O copia este código en el **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/a20c0733-f234-4d4b-862d-db87f2c249e9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Al ejecutar el programa, el monitor serial mostrará "ON" o "OFF" cuando deslices el interruptor hacia la izquierda o la derecha.
