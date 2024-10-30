.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_relay:

2.16 Controla Otro Circuito
=================================

En nuestra vida cotidiana, podemos encender o apagar una lámpara con solo presionar un interruptor.
Pero, ¿qué sucede si quieres controlar la lámpara con el Pico W para que se apague automáticamente después de diez minutos?

Un relé puede ayudarte a lograr esta idea.

Un relé es en realidad un tipo especial de interruptor, que es controlado por un lado del circuito (generalmente un circuito de baja tensión) y se utiliza para controlar el otro lado del circuito (generalmente un circuito de alta tensión). Esto hace posible modificar nuestros electrodomésticos para ser controlados mediante un programa, convirtiéndolos en dispositivos inteligentes o incluso conectándolos a Internet.

.. warning::
    Modificar electrodomésticos puede ser peligroso; no lo intentes a la ligera. Realízalo siempre bajo la supervisión de profesionales.

* :ref:`cpn_relay`

Aquí solo usaremos un circuito simple alimentado por un módulo de alimentación en la protoboard para mostrar cómo controlarlo mediante un relé.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Conexiones**

Primero, construye un circuito de baja tensión para controlar un relé.
Para manejar el relé se requiere una alta corriente, por lo que se necesita un transistor; en este caso, usaremos el S8050.

|sch_relay_1|

|wiring_relay_1|

Un diodo (diodo de continuidad) se utiliza aquí para proteger el circuito. El cátodo es el extremo con la banda plateada y está conectado a la fuente de alimentación, mientras que el ánodo se conecta al transistor.

Cuando la entrada de voltaje cambia de Alto (5V) a Bajo (0V), el transistor pasa de saturación (amplificación, saturación y corte) a corte, y de repente no hay paso para que fluya corriente a través de la bobina.

En este punto, si este diodo de continuidad no existe, la bobina generará una potencial autoinducido en ambos extremos, varias veces mayor que el voltaje de alimentación, lo cual, sumado al voltaje de la fuente, es suficiente para quemar el transistor.

Al agregar el diodo, la bobina y el diodo forman instantáneamente un nuevo circuito alimentado por la energía almacenada en la bobina para descargar, evitando así que el voltaje excesivo dañe componentes como transistores en el circuito.

* :ref:`cpn_diode`
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

En este punto, el programa está listo para ejecutarse. Después de iniciar, escucharás el sonido de “tik tok”, que es el sonido de la bobina del contactor dentro del relé activándose y desactivándose.

Luego, conecta los dos extremos del circuito de carga a los pines 3 y 6 del relé respectivamente.

..(Toma como ejemplo el circuito simple alimentado por el módulo de alimentación de la protoboard descrito en el artículo anterior).

|sch_relay_2|

|wiring_relay_2|

En este punto, el relé podrá controlar el encendido y apagado del circuito de carga.

**Código**

.. note::

    * Abre el archivo ``2.16_control_another_circuit.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    relay = machine.Pin(15, machine.Pin.OUT)
    while True:
        relay.value(1)
        utime.sleep(2)
        relay.value(0)
        utime.sleep(2)

Cuando se ejecuta el código, el relé cambiará el estado operativo del circuito controlado cada dos segundos.
Puedes comentar manualmente una de las líneas para aclarar la correspondencia entre el circuito del relé y el circuito de carga.


**Aprende Más**


El pin 3 del relé está normalmente abierto y solo se activa cuando la bobina del contactor está operando; el pin 4 está normalmente cerrado y se activa cuando la bobina del contactor está energizada.
El pin 1 está conectado al pin 6 y es el terminal común del circuito de carga.

Al cambiar un extremo del circuito de carga del pin 3 al pin 4, podrás obtener el estado operativo exactamente opuesto.
