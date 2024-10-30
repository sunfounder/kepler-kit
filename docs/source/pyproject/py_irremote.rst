.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_irremote:

6.4 Control Remoto IR
==========================

En la electrónica de consumo, los controles remotos se utilizan para operar dispositivos como televisores y reproductores de DVD. 
En algunos casos, los controles remotos permiten a las personas operar dispositivos que están fuera de su alcance, como aires acondicionados centrales.

El receptor IR es un componente con una fotocélula diseñada para recibir luz infrarroja. 
Se usa casi siempre para la detección de controles remotos; cada televisor y reproductor de DVD tiene uno de estos en su parte frontal para recibir la señal IR del control remoto. 
Dentro del control remoto, hay un LED IR que emite pulsos infrarrojos para indicar al televisor que se encienda, apague o cambie de canal.

* :ref:`cpn_ir_receiver`

**Componentes Requeridos**

Para este proyecto, necesitaremos los siguientes componentes.

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Esquema**

|sch_irrecv|

**Conexión**

|wiring_irrecv|

**Código**

.. note::

    * Abre el archivo ``6.4_ir_remote_control.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.
    
    * Aquí necesitas usar las bibliotecas en la carpeta ``ir_rx``. Verifica que se hayan subido a Pico W; para un tutorial detallado, consulta :ref:`add_libraries_py`.

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.print_error import print_error
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

    # Función de retorno de llamada del usuario
    def callback(data, addr, ctrl):
        if data < 0:  # El protocolo NEC envía códigos de repetición.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instanciar receptor
    ir.error_function(print_error)  # Mostrar información de depuración

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()


El nuevo control remoto tiene una pieza de plástico en el extremo para aislar la batería interna. Debes retirar esta pieza para alimentar el control al usarlo.
Una vez que el programa esté en ejecución, al presionar el control remoto, la consola Shell imprimirá la tecla que has presionado.

**¿Cómo funciona?**

Este programa parece ligeramente complicado, pero en realidad realiza las funciones básicas del receptor IR con solo unas pocas líneas.

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    # Función de retorno de llamada del usuario
    def callback(data, addr, ctrl):
        if data < 0:  # El protocolo NEC envía códigos de repetición.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instanciar receptor

Aquí se instancia un objeto ``ir`` que lee en cualquier momento las señales recibidas por el receptor IR.

El resultado se registra en ``data`` dentro de la función de retorno de llamada.

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

Si el receptor IR recibe valores duplicados (por ejemplo, al presionar una tecla sin soltarla), entonces data < 0 y este dato necesita ser filtrado.

De lo contrario, data contendría un valor utilizable, pero en un código no legible directamente, y la función ``decodeKeyValue(data)`` se utiliza para decodificarlo.

.. code-block:: python

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

Si presionamos la tecla **1**, el receptor IR emite un valor como ``0x0C``, que necesita ser decodificado para corresponder a la tecla específica.

A continuación, se incluyen algunas funciones de depuración. Son importantes, pero no están relacionadas con el efecto que necesitamos lograr, así que simplemente las dejamos en el programa.

.. code-block:: python

    from ir_rx.print_error import print_error

    ir.error_function(print_error) # Mostrar información de depuración

Finalmente, usamos un bucle vacío como programa principal. Y empleamos try-except para que el programa salga con el objeto ``ir`` finalizado.

.. code-block:: python

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()



* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_