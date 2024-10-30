.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones durante festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_mpr121:

4.3 Teclado de Electrodos
================================

El MPR121 es una excelente opción si deseas agregar una gran cantidad de 
interruptores táctiles a tu proyecto. Este módulo cuenta con electrodos 
que pueden extenderse mediante conductores. Por ejemplo, si conectas los 
electrodos a un plátano, puedes convertirlo en un interruptor táctil.

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Esquema**

|sch_mpr121|

**Conexiones**

|wiring_mpr121|

**Código**

.. note::

    * Abre el archivo ``4.3_electrode_keyboard.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

    * Aquí necesitas usar la biblioteca llamada ``mpr121.py``. Verifica si ha sido cargada en Pico W. Para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # comprobar todas las teclas
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

Una vez que el programa esté en ejecución, puedes tocar los doce electrodos en el MPR121 con la mano, y los electrodos tocados se imprimirán en pantalla.

Puedes extender los electrodos conectando otros conductores como frutas, cables, láminas de aluminio, etc. Esto te permitirá nuevas formas de activar los electrodos.

**¿Cómo funciona?**

En la biblioteca mpr121, hemos integrado la funcionalidad en la clase ``MPR121``.

.. code-block:: python

    from mpr121 import MPR121

MPR121 es un módulo I2C que requiere un conjunto de pines I2C para inicializar el objeto ``MPR121``. En este punto, el estado de los electrodos del módulo se registrará como valores iniciales. Si los electrodos se extienden, será necesario volver a ejecutar el ejemplo para restablecer los valores iniciales.

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

Luego usa ``mpr.get_all_states()`` para leer si los electrodos están activados. Si los electrodos 2 y 3 están activados, se generará el valor ``[2, 3]``.

.. code-block::

    while True:
        value = mpr.get_all_states()
        if len(value) ! = 0:
            print(value)
        time.sleep_ms(100)

También puedes usar ``mpr.is_touched(electrode)`` para detectar un electrodo específico. Cuando se activa, devuelve ``True``; de lo contrario, devuelve ``False``.

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)