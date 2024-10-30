.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_pump:

3.6 Bombeo
=======================

Las pequeñas bombas centrífugas son ideales para proyectos de riego automático de plantas. 
También se pueden utilizar para crear pequeñas fuentes de agua inteligentes.

Su componente de potencia es un motor eléctrico, que se controla de la misma manera que un motor normal.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Conecta el tubo a la salida del motor, sumerge la bomba en agua y enciéndela.
    #. Debes asegurarte de que el nivel del agua siempre esté por encima del motor. Funcionarlo en vacío puede dañar el motor debido a la generación de calor y también generará ruido.
    #. Si estás regando plantas, evita que la tierra sea absorbida, ya que esto podría obstruir la bomba.
    #. Si no sale agua por el tubo, es posible que haya agua residual bloqueando el flujo de aire, en cuyo caso se necesita drenar primero.

**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

Es muy conveniente adquirir un kit completo; aquí tienes el enlace:

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Batería 18650
        - 1
        -  
    *   - 8
        - Portapilas
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Esquema**

|sch_pump|

**Conexiones**

.. note::

    * Dado que la bomba requiere una alta corriente, usamos un módulo de cargador Li-po para alimentar el motor por razones de seguridad.
    * Asegúrate de que el módulo Li-po Charger esté conectado como se muestra en el diagrama. De lo contrario, es probable que un cortocircuito dañe la batería y el circuito.

|wiring_pump|

**Código**

.. note::

    * Abre el archivo ``3.6_pumping.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    while True:
        motor1A.high()
        motor2A.low()

Después de ejecutar el código, la bomba comenzará a funcionar y verás agua fluyendo por el tubo al mismo tiempo.

.. note::

    * Si el motor sigue girando después de hacer clic en el botón de detener, necesitas restablecer el pin **RUN** en el Pico W conectándolo a GND con un cable y luego desconectarlo para ejecutar el código nuevamente.
    * Esto se debe a que el motor está funcionando con una corriente demasiado alta, lo que podría hacer que el Pico W se desconecte de la computadora.

    |wiring_run_reset|