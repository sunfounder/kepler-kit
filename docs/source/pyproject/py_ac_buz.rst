.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_ac_buz:

3.1 Zumbador
==================

El zumbador activo es un típico dispositivo de salida digital, ¡tan fácil de usar como encender un LED!

* :ref:`cpn_buzzer`

**Componentes Requeridos**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí tienes el enlace:

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Zumbador Activo :ref:`cpn_buzzer`
        - 1
        - 

**Esquema**

|sch_buzzer|

Cuando la salida GP15 está en alto, después de la resistencia limitadora de corriente de 1K (para proteger el transistor), el S8050 (transistor NPN) se activa, y el zumbador emite sonido.

El S8050 (transistor NPN) actúa como amplificador de corriente, haciendo que el zumbador suene más fuerte. De hecho, también se podría conectar el zumbador directamente a GP15, pero notarás que el sonido es más débil.

**Conexión**

El kit incluye dos tipos de zumbadores. Necesitamos usar el zumbador activo. Da la vuelta al zumbador; el que tiene la parte trasera sellada (no el PCB expuesto) es el que necesitamos.

|img_buzzer|

El zumbador necesita un transistor para funcionar, aquí utilizamos el S8050 (Transistor NPN).

|wiring_beep|


**Código**

.. note::

    * Abre el archivo ``3.1_beep.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.Pin(15, machine.Pin.OUT)
    while True:
        for i in range(4):
            buzzer.value(1)
            utime.sleep(0.3)
            buzzer.value(0)
            utime.sleep(0.3)
        utime.sleep(1)

Después de ejecutar el código, escucharás un sonido de bip cada segundo.
