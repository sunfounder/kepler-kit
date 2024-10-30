.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_reed:

2.9 Siente el Magnetismo
================================

El tipo más común de interruptor de láminas contiene un par de láminas metálicas magnetizables y flexibles, cuyas partes finales están separadas por un pequeño espacio cuando el interruptor está abierto.

Un campo magnético, ya sea de un electroimán o de un imán permanente, hará que las láminas se atraigan entre sí, completando así un circuito eléctrico. 
La fuerza de resorte de las láminas hace que se separen y abran el circuito cuando el campo magnético desaparece.

Un ejemplo común de aplicación de un interruptor de láminas es detectar la apertura de una puerta o ventana, para una alarma de seguridad.

* :ref:`cpn_reed`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Esquema**

|sch_reed|

Por defecto, GP14 está en bajo; y subirá a alto cuando el imán esté cerca del interruptor de láminas.

El propósito de la resistencia de 10K es mantener el GP14 en un nivel bajo estable cuando no hay un imán cerca.

**Conexiones**

|wiring_reed|

**Código**

.. note::

    * Abre el archivo ``2.9_feel_the_magnetism.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    reed = machine.Pin(14, machine.Pin.IN)
    while True:
        if reed.value() == 1:
            print("There are magnets here!!")
            utime.sleep(1)

Al ejecutar el código, GP14 se activará en alto cuando un imán esté cerca del interruptor de láminas, de lo contrario, permanecerá en bajo. Es similar al funcionamiento del botón en el capítulo :ref:`py_button`.

**Aprende Más**

Esta vez, probaremos una forma flexible de usar interruptores: las solicitudes de interrupción, o IRQs.

Por ejemplo, estás leyendo un libro página por página, como si un programa estuviera ejecutando un hilo. En ese momento, alguien llega para hacerte una pregunta e interrumpe tu lectura. Esa persona está ejecutando una solicitud de interrupción, pidiéndote que dejes de leer para responder y luego retomes la lectura al terminar.

La solicitud de interrupción en MicroPython funciona de la misma manera, permitiendo que ciertas operaciones interrumpan el programa principal.


.. note::

    * Abre el archivo ``2.9_feel_the_magnetism_irq.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    reed_switch = machine.Pin(14, machine.Pin.IN)

    def detected(pin):
        print("Magnet!")

    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=detected)


Primero, se define una función de retorno llamada ``detected(pin)``, que será el controlador de interrupción. Se ejecutará cuando se active una solicitud de interrupción. Luego, se configura una solicitud de interrupción en el programa principal, la cual contiene dos partes: el ``trigger`` y el ``handler``.

En este programa, ``trigger`` es ``IRQ_RISING``, lo que indica que el valor del pin sube de bajo a alto (es decir, cuando el botón se presiona).

``handler`` es ``detected``, la función de retorno que definimos anteriormente.


* `machine.Pin.irq - Micropython Docs <https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.irq>`_