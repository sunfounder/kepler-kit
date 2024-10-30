.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_photoresistor:

2.12 Sentir la Luz
=============================

El fotorresistor es un dispositivo típico para entradas analógicas y se utiliza de forma muy similar a un potenciómetro. Su valor de resistencia depende de la intensidad de la luz: cuanto más fuerte sea la luz irradiada, menor será su valor de resistencia; por el contrario, este valor aumenta si la luz es más tenue.

* :ref:`cpn_photoresistor`

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
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Esquema**

|sch_photoresistor|

En este circuito, el resistor de 10K y el fotorresistor están conectados en serie, y la corriente que pasa a través de ellos es la misma. El resistor de 10K actúa como protección, y el GP28 lee el valor después de la conversión de voltaje del fotorresistor.

Cuando aumenta la luz, la resistencia del fotorresistor disminuye, reduciendo su voltaje, por lo que el valor en GP28 disminuirá; si la luz es suficientemente fuerte, la resistencia del fotorresistor se acercará a 0, y el valor de GP28 será cercano a 0. En este caso, el resistor de 10K juega un papel protector, evitando que se conecten directamente 3.3V y GND, lo que provocaría un cortocircuito.

Si colocas el fotorresistor en un entorno oscuro, el valor en GP28 aumentará. En una situación de oscuridad total, la resistencia del fotorresistor será infinita, su voltaje se acercará a 3.3V (el resistor de 10K es despreciable), y el valor de GP28 se acercará al máximo de 65535.

La fórmula de cálculo se muestra a continuación.

    (Vp/3.3V) x 65535 = Ap

**Conexiones**

|wiring_photoresistor|

**Código**

.. note::

    * Abre el archivo ``2.12_feel_the_light.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

Después de ejecutar el programa, la Shell imprimirá los valores del fotorresistor. Puedes iluminarlo con una linterna o cubrirlo con la mano para ver cómo cambia el valor.

