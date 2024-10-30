.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora más sobre Raspberry Pi, Arduino y ESP32 junto a otros aficionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede a anuncios y adelantos de nuevos productos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_keypad:

4.2 Teclado 4x4
========================

El teclado 4x4, también conocido como teclado matricial, es una matriz de 16 teclas organizadas en un solo panel.

Este tipo de teclado se encuentra en dispositivos que requieren entrada digital, como calculadoras, controles remotos de TV, teléfonos con botones, máquinas expendedoras, cajeros automáticos, cerraduras de combinación y cerraduras digitales de puertas.

En este proyecto, aprenderemos cómo determinar qué tecla se ha presionado y obtener el valor correspondiente.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

Es más conveniente adquirir un kit completo. Aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ARTÍCULOS EN ESTE KIT
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
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Esquema**

|sch_keypad|

Se conectan 4 resistencias pull-down a cada una de las columnas del teclado matricial, de modo que G6 ~ G9 tengan un nivel bajo estable cuando las teclas no están presionadas.

Las filas del teclado (G2 ~ G5) se programan para estar en nivel alto; si alguna de G6 ~ G9 está en nivel alto al ser leída, sabemos qué tecla ha sido presionada.

Por ejemplo, si G6 se lee en alto, entonces se ha presionado la tecla numérica 1; esto es porque los pines de control de la tecla 1 son G2 y G6, y al presionar la tecla, G2 y G6 se conectan y G6 se pone en alto.

**Conexiones**

|wiring_keypad|

Para facilitar el cableado, en el diagrama anterior, la fila de columnas del teclado y las resistencias de 10K se insertan en los agujeros donde se encuentran G6 ~ G9.

**Código**

.. note::

    * Abre el archivo ``4.2_4x4_keypad.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

Una vez que el programa se esté ejecutando, la consola Shell imprimirá las teclas que presionas en el teclado.

**Cómo funciona**

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

Declara cada tecla del teclado matricial en el array ``characters[]`` y define los pines en cada fila y columna.

.. code-block:: python

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

Esta es la parte de la función principal que lee e imprime el valor del botón.

La función ``readKey()`` leerá el estado de cada botón.

Las instrucciones ``if current_key != None`` y ``if current_key == last_key`` 
se usan para verificar si se ha presionado una tecla y el estado de la tecla presionada. 
(Si presionas '3' cuando has presionado '1', la condición es válida.)

Imprime el valor de la tecla presionada cuando la condición es verdadera.

La instrucción ``last_key = current_key`` asigna el estado de cada evaluación 
a un array ``last_key`` para facilitar la siguiente ronda de evaluaciones.

.. code-block:: python

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

Esta función asigna un nivel alto a cada fila sucesivamente, y cuando se presiona el botón, 
la columna en la que se encuentra la tecla obtiene un nivel alto. 
Tras el bucle de doble capa, el valor del botón cuyo estado es 1 se almacena en el array ``key``.

Si presionas la tecla '3':

|img_keypad_pressed|


``row[0]`` se escribe en nivel alto y ``col[2]`` obtiene nivel alto.



``col[0]``, ``col[1]``, ``col[3]`` obtienen nivel bajo.

Hay cuatro estados: 0, 0, 1, 0; y se escribe \'3\' en ``pressed_keys``.

Cuando ``row[1]``, ``row[2]``, ``row[3]`` se escriben en nivel alto, 
``col[0]`` ~ ``col[4]`` obtienen nivel bajo.

El bucle se detiene y se retorna key = \'3\'.

Si presionas las teclas \'1\' y \'3\', se devolverá key = [\'1\',\'3\'].
