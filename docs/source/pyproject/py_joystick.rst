.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora más a fondo sobre Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas post-venta y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_joystick:

4.1 Controlar el Joystick
================================

Si juegas a muchos videojuegos, ya estarás muy familiarizado con el joystick. 
Se usa comúnmente para mover personajes, rotar la pantalla, entre otras funciones.

El principio detrás de la capacidad del joystick para permitir que la computadora 
interprete nuestras acciones es muy simple. Se puede pensar que está compuesto por 
dos potenciómetros perpendiculares entre sí. Estos potenciómetros miden el valor 
analógico del joystick en sentido vertical y horizontal, generando un valor (x, y) 
en un sistema de coordenadas en ángulo recto.

El joystick de este kit también incluye una entrada digital que se activa cuando se presiona el joystick.

* :ref:`cpn_joystick`

**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

Es mucho más conveniente adquirir un kit completo. Aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ARTÍCULOS EN ESTE KIT
        - ENLACE
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

También puedes adquirirlos por separado en los enlaces siguientes.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Esquema**

|sch_joystick|

El pin SW está conectado a una resistencia pull-up de 10K para obtener un nivel alto estable en el pin SW (eje Z) cuando el joystick no está presionado; de lo contrario, el pin SW estaría en estado suspendido y el valor de salida podría variar entre 0 y 1.

**Conexiones**

|wiring_joystick|


**Código**

.. note::

    * Abre el archivo ``4.1_toggle_the_joystick.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200)    

Después de ejecutar el programa, la consola Shell imprimirá los valores x, y, z del joystick.


* Los valores de los ejes x e y son valores analógicos que varían de 0 a 65535.
* El valor del eje Z es un valor digital con un estado de 1 o 0.
