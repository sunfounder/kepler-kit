.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_button:

2.5 Lectura del Valor del Botón
==============================================

Estos pines tienen tanto funciones de entrada como de salida, como indica su nombre GPIO (Entrada/Salida de propósito general). Anteriormente, utilizamos la función de salida; en este capítulo, usaremos la función de entrada para leer el valor del botón.

* :ref:`cpn_button`

**Componentes Requeridos**

En este proyecto, necesitamos los siguientes componentes.

Es conveniente adquirir un kit completo; aquí tienes el enlace:

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Esquema**

|sch_button|

Cuando un lado del pin del botón está conectado a 3.3V y el otro lado del pin está conectado a GP14, al presionar el botón, GP14 se encontrará en un estado alto. Sin embargo, cuando el botón no está presionado, GP14 queda en un estado suspendido y puede estar en alto o bajo. Para garantizar un nivel bajo estable cuando el botón no está presionado, es necesario conectar GP14 a GND mediante una resistencia de pull-down de 10K.

**Conexión**

|wiring_button|



.. Sigamos la dirección del circuito para armarlo paso a paso.

.. 1. Conecta el pin 3V3 de Pico W al bus positivo de la breadboard.
.. #. Inserta el botón en la breadboard, atravesando la línea divisoria central.


.. note::
    Un botón de cuatro pines tiene forma de H. Sus dos pines izquierdos o dos pines derechos están conectados, lo que significa que al cruzar el espacio central, conecta dos medias filas con el mismo número de fila. (Por ejemplo, en mi circuito, E23 y F23 están conectados, al igual que E25 y F25).

    Hasta que se presione el botón, los pines izquierdo y derecho están separados, y la corriente no puede fluir de un lado a otro.

.. #. Usa un cable puente para conectar uno de los pines del botón al bus positivo (en mi caso, el pin superior derecho).
.. #. Conecta el otro pin (superior izquierdo o inferior izquierdo) a GP14 con un cable puente.
.. #. Usa una resistencia de 10K para conectar el pin en la esquina superior izquierda del botón al bus negativo.
.. #. Conecta el bus de energía negativo de la breadboard a GND del Pico.

**Código**

.. note::

    * Abre el archivo ``2.5_read_button_value.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

Al ejecutar el código, el shell imprimirá "¡Has presionado el botón!".

**Modo de Trabajo Pull-Up**

A continuación se muestra la conexión y el código cuando usas el botón en modo pull-up.

|sch_button_pullup|

|wiring_button_pullup|

La única diferencia en comparación con el modo pull-down es que la resistencia de 10K está conectada a 3.3V y el botón está conectado a GND. Así, cuando el botón es presionado, GP14 tendrá un nivel bajo, lo cual es lo opuesto al valor obtenido en el modo pull-down.  
Solo debes cambiar el código a ``if button.value() == 0:``.

También puedes consultar la referencia aquí:

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_