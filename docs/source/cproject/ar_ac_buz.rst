.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_ac_buz:

3.1 - Zumbador
==================

El zumbador activo es un dispositivo de salida digital típico, ¡tan fácil de usar como encender un LED!

* :ref:`cpn_buzzer`

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Zumbador activo :ref:`cpn_buzzer`
        - 1
        - 

**Esquema**

|sch_buzzer|

Cuando la salida de GP15 está en alto, la corriente pasa a través de la resistencia limitadora de 1K (para proteger el transistor), lo que hace que el S8050 (transistor NPN) conduzca y que el zumbador emita sonido.

El papel del transistor S8050 (NPN) es amplificar la corriente para que el sonido del zumbador sea más fuerte. De hecho, también puedes conectar el zumbador directamente a GP15, pero notarás que el sonido será más débil.

**Conexión**

El kit incluye dos tipos de zumbadores. 
Necesitamos usar el zumbador activo. Gira los zumbadores: el que tiene la parte posterior sellada (sin PCB expuesto) es el que necesitamos.

|img_buzzer|

El zumbador requiere un transistor para funcionar correctamente, aquí usamos el S8050 (Transistor NPN).

|wiring_beep|

**Código**

.. note::

    * Puedes abrir el archivo ``3.1_beep.ino`` en la ruta ``kepler-kit-main/arduino/3.1_beep``. 
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bf2c5d-9890-4f3a-b02a-119c2f6b0bf1/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el código, escucharás un pitido cada segundo.
