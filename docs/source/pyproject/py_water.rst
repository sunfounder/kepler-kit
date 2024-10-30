.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_water:

2.14 Detección del Nivel de Agua
====================================

|img_water_sensor|

El sensor de agua está diseñado para la detección de líquidos y puede usarse ampliamente en la medición de lluvia, nivel de agua e incluso detección de fugas de líquidos.

Mide el nivel de agua a través de una serie de trazos de cables expuestos y paralelos que evalúan el tamaño de las gotas de agua o volumen. El volumen de agua se convierte fácilmente en una señal analógica, y el valor de salida analógico puede ser leído directamente por la placa de control principal para lograr un efecto de alarma de nivel de agua.

.. warning:: 

    El sensor no puede sumergirse completamente en agua; solo la parte donde se encuentran las diez trazas debe estar en contacto con el agua. Además, alimentar el sensor en un ambiente húmedo acelerará la corrosión de la sonda y reducirá la vida útil del sensor, por lo que se recomienda suministrar energía solo al realizar las lecturas.

* :ref:`cpn_water_level`

**Componentes Necesarios**

Para este proyecto, necesitaremos los siguientes componentes.

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Esquemático**

|sch_water|

**Conexiones**

|wiring_water|

**Código**

.. note::

    * Abre el archivo ``2.14_feel_the_water_level.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha. 

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)

    while True:
        value=sensor.read_u16()
        print(value)
        utime.sleep_ms(200)


Después de ejecutar el programa, sumerge lentamente el módulo del sensor de agua en el agua, y a medida que aumenta la profundidad, el Shell imprimirá un valor mayor.

**Para Saber Más**

Existe una forma de usar el módulo de entrada analógica como un módulo digital.

Primero, toma una lectura del sensor de agua en un entorno seco, regístrala y utilízala como valor de umbral. Luego, completa la programación y realiza una nueva lectura del sensor de agua. Cuando la lectura del sensor difiera significativamente de la lectura en un ambiente seco, indicará que está en contacto con un líquido. En otras palabras, al colocar este dispositivo cerca de una tubería de agua, puede detectar si hay una fuga en la tubería.

.. note::

    * Abre el archivo ``2.14_water_level_threshold.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha. 

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    sensor = machine.ADC(28)
    threshold = 30000  # Este valor debe ajustarse según el entorno.

    while True:
        value=sensor.read_u16()
        if value > threshold :
            print("Liquid leakage!")
        utime.sleep_ms(200)
