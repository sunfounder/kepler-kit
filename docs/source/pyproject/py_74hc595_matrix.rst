.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_74hc_788bs:

5.4 Gráficos 8x8 Píxeles
=============================

La matriz de LEDs es una pantalla de matriz de puntos de baja resolución que utiliza un conjunto de diodos emisores de luz (LEDs) como píxeles para mostrar patrones.

Son lo suficientemente brillantes para ser visibles a plena luz del día y suelen encontrarse en tiendas, carteles, indicadores de tráfico y en pantallas de mensajes variables (como las que tienen algunos vehículos de transporte público).

El kit incluye una matriz de 8x8 puntos con 16 pines. Sus ánodos están conectados en filas y sus cátodos en columnas, lo cual permite controlar estos 64 LEDs en conjunto.

Para encender el primer LED, se debe proporcionar un nivel alto para la Fila1 y un nivel bajo para la Columna1. Para encender el segundo LED, se da un nivel alto para la Fila1 y un nivel bajo para la Columna2, y así sucesivamente. Controlando la corriente a través de cada par de filas y columnas, se puede controlar cada LED de forma individual para mostrar caracteres o imágenes.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Esquema**

|sch_ledmatrix|

La matriz de puntos 8x8 es controlada por dos chips 74HC595, uno controla las filas y el otro controla las columnas, compartiendo los pines G18~G20 para reducir el uso de los puertos de E/S de la placa Pico W.

La Pico W necesita emitir un número binario de 16 bits, donde los primeros 8 bits van al 74HC595 que controla las filas y los últimos 8 bits al que controla las columnas, de esta forma la matriz de puntos puede mostrar un patrón específico.

Q7': Pin de salida en serie, conectado al DS de otro 74HC595 para conectar múltiples 74HC595 en serie.

**Conexión**

Construye el circuito paso a paso, ya que el cableado es complicado.

**Paso 1:** Primero, inserta la Pico W, la matriz de puntos LED y los dos 
chips 74HC595 en la breadboard. Conecta los pines 3.3V y GND de la Pico W 
a las líneas de alimentación de ambos lados de la placa, luego conecta los 
pines 16 y 10 de los dos chips 74HC595 a VCC, y los pines 13 y 8 a GND.

.. note::
   En la imagen de Fritzing, el lado con la etiqueta está en la parte inferior.

|wiring_ledmatrix_4|

**Paso 2:** Conecta el pin 11 de los dos 74HC595 juntos y luego a GP20; 
luego conecta el pin 12 de ambos chips a GP19; finalmente, conecta el pin 14 
del 74HC595 de la izquierda a GP18 y el pin 9 al pin 14 del segundo 74HC595.

|wiring_ledmatrix_3|

**Paso 3:** El 74HC595 a la derecha controla las columnas de la matriz de puntos 
LED. Consulta la tabla de abajo para el mapeo. Los pines Q0-Q7 del 74HC595 están 
mapeados con los pines 13, 3, 4, 10, 6, 11, 15 y 16 respectivamente.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Paso 4:** Ahora conecta las FILAS de la matriz LED. El 74HC595 a la izquierda 
controla las FILAS de la matriz LED. Consulta la tabla de abajo para el mapeo. 
Podemos ver que Q0-Q7 del 74HC595 están mapeados con los pines 9, 14, 8, 12, 1, 
7, 2 y 5 respectivamente.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Código**

.. note::

    * Abre el archivo ``5.4_8x8_pixel_graphics.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)


    glyph = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]

    # Shift the data to 74HC595
    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

Cuando el programa está en ejecución, verás una gráfica de **x** mostrada en la matriz de puntos 8x8.

**¿Cómo funciona?**

Aquí utilizamos dos 74HC595 para proporcionar señales a las filas y columnas de la matriz de puntos.
La forma de proporcionar señales es la misma que en ``hc595_shift(dat)`` de los capítulos anteriores, pero aquí necesitamos escribir un número binario de 16 bits a la vez.
Así que dividimos ``hc595_shift(dat)`` en dos funciones: ``hc595_in(dat)`` y ``hc595_out()``.

.. code-block:: python

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

Luego, en el bucle principal, llamamos a ``hc595_in(dat)`` dos veces, escribimos dos números binarios de 8 bits y después llamamos a ``hc595_out()`` para mostrar un patrón.

Sin embargo, debido a que los LEDs en la matriz tienen polos comunes, controlar múltiples filas o columnas al mismo tiempo puede causar interferencias. Por ello, es necesario activar una columna (o una fila) a la vez, ciclando 8 veces, y usar el principio de imagen residual para que el ojo humano perciba el patrón completo de 8x8.

.. code-block:: python

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

En este ejemplo, la función principal anida un bucle ``for``, y cuando ``i`` es 1, solo la primera línea está activada (el chip de la línea de control obtiene el valor ``0x80``) y se escribe la imagen de la primera línea. 
Cuando ``i`` es 2, se activa la segunda línea (el chip de la línea de control obtiene el valor ``0x40``) y se escribe la imagen de la segunda línea, y así sucesivamente hasta completar las 8 salidas.

Es importante mantener la tasa de actualización para evitar parpadeos, por lo que se debe evitar el uso de ``sleep()`` adicional en el bucle principal siempre que sea posible.

**Para Aprender Más**

Prueba reemplazar ``glyph`` con el siguiente array y observa el resultado:

.. code-block:: python

    glyph1 = [0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF]
    glyph2 = [0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF]
    glyph3 = [0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF]
    glyph4 = [0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF]
    glyph5 = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]
    glyph6 = [0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF]

O puedes intentar crear tus propios gráficos.
