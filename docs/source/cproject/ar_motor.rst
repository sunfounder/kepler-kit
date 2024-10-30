.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_motor:

3.5 - Pequeño Ventilador
=============================

Ahora utilizaremos el TA6586 para controlar el motor de corriente continua (DC) y hacer que gire en sentido horario y antihorario.
Dado que el motor DC requiere una corriente relativamente alta, por razones de seguridad, usaremos un módulo de alimentación para suministrar energía al motor.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - Batería 18650
        - 1
        -  
    *   - 9
        - Soporte para batería
        - 1
        - 

**Esquema**

|sch_motor|

**Conexión**

.. note::

    * Dado que los motores de corriente continua requieren una corriente alta, utilizamos aquí un módulo cargador de Li-po para alimentar el motor por razones de seguridad.
    * Asegúrate de que el módulo cargador de Li-po esté conectado como se muestra en el diagrama. De lo contrario, un cortocircuito podría dañar la batería y el circuito.

|wiring_motor|

**Código**

.. note::

    * Puedes abrir el archivo ``3.5_small_fan.ino`` en la ruta ``kepler-kit-main/arduino/3.5_small_fan``.
    * O copia este código en el **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Una vez que el programa esté en ejecución, el motor girará hacia adelante y hacia atrás en un patrón regular.

.. note::

    * Si no puedes cargar el código nuevamente, en esta ocasión debes conectar el pin **RUN** en el Pico W a GND con un cable para reiniciarlo, y luego desconectar este cable para ejecutar el código nuevamente.
    * Esto se debe a que el motor opera con mucha corriente, lo cual puede hacer que el Pico W se desconecte de la computadora.

    |wiring_run_reset|
