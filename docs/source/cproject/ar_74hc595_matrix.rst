.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_74hc_788bs:

5.4 - Gráficos en Matriz de 8x8 Píxeles
=============================================

La matriz de LEDs es una pantalla de baja resolución que utiliza una disposición de diodos emisores de luz como píxeles para mostrar patrones.

Son lo suficientemente brillantes como para ser visibles bajo la luz del sol y se pueden ver en tiendas, carteles, letreros y pantallas de mensajes variables (como las de vehículos de transporte público).

En este kit se utiliza una matriz de puntos de 8x8 con 16 pines. Sus ánodos están conectados en filas y los cátodos en columnas, lo cual permite controlar estos 64 LEDs de manera conjunta.

Para encender el primer LED, debes proporcionar un nivel alto en la Fila1 y un nivel bajo en la Columna1. Para encender el segundo LED, debes establecer un nivel alto en la Fila1 y un nivel bajo en la Columna2, y así sucesivamente. 
Controlando la corriente a través de cada par de filas y columnas, es posible controlar cada LED individualmente para mostrar caracteres o imágenes.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

Es muy conveniente adquirir un kit completo, aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ITEMS EN ESTE KIT
        - LINK DE COMPRA
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCCIÓN DEL COMPONENTE
        - CANTIDAD
        - LINK DE COMPRA

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

La matriz de puntos de 8x8 es controlada por dos chips 74HC595, uno de ellos controla las filas y el otro las columnas, compartiendo ambos los pines G18~G20, lo que permite ahorrar significativamente los puertos I/O de la placa Pico W.

Pico W necesita emitir un número binario de 16 bits a la vez: los primeros 8 bits se asignan al 74HC595 que controla las filas y los últimos 8 bits al 74HC595 que controla las columnas, permitiendo que la matriz de puntos muestre un patrón específico.

Q7': Pin de salida en serie, conectado al DS de otro 74HC595 para encadenar múltiples 74HC595 en serie.

**Conexión**

Construye el circuito. Dado que el cableado es complejo, vamos a realizarlo paso a paso.

**Paso 1:** Primero, inserta la Pico W, la matriz de LEDs y los dos chips 74HC595 en 
la protoboard. Conecta el 3.3V y GND de la Pico W a las ranuras de ambos lados de la 
protoboard, luego conecta el pin 16 y el 10 de ambos chips 74HC595 a VCC, y el pin 13 y el 8 a GND.

.. note::
   En la imagen de Fritzing anterior, el lado con la etiqueta está en la parte inferior.

|wiring_ledmatrix_4|

**Paso 2:** Conecta el pin 11 de ambos 74HC595 y luego a GP20; después, conecta el pin 12 
de ambos chips a GP19; a continuación, el pin 14 del 74HC595 en el lado izquierdo a GP18 y 
el pin 9 al pin 14 del segundo 74HC595.

|wiring_ledmatrix_3|

**Paso 3:** El 74HC595 en el lado derecho es el que controla las columnas de la 
matriz de LEDs. Consulta la siguiente tabla para ver la correspondencia. Por lo 
tanto, los pines Q0-Q7 del 74HC595 están asignados a los pines 13, 3, 4, 10, 6, 
11, 15 y 16, respectivamente.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Paso 4:** Ahora conecta las filas de la matriz de LEDs. El 74HC595 en el lado 
izquierdo controla las filas de la matriz de LEDs. Consulta la tabla a continuación 
para ver la correspondencia. Podemos ver que Q0-Q7 del 74HC595 en el lado izquierdo 
están asignados a los pines 9, 14, 8, 12, 1, 7, 2 y 5, respectivamente.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Código**

.. note::

    * Puedes abrir el archivo ``5.4_8x8_pixel_graphics.ino`` en la ruta ``kepler-kit-main/arduino/5.4_8x8_pixel_graphics``.
    * O copia este código en el **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.



.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3682592-17d4-4690-a730-1c0a6fcbd353/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



Una vez que el programa esté en ejecución, verás una gráfica en forma de **x** en la matriz de puntos de 8x8.



**¿Cómo funciona?**

Aquí utilizamos dos 74HC595 para proporcionar señales a las filas y columnas de 
la matriz de puntos. El método de transmisión de señales es el mismo que en ``shiftOut()`` en los capítulos anteriores, con la diferencia de que aquí necesitamos escribir un número binario de 16 bits a la vez.

El bucle principal llama a ``shiftOut()`` dos veces, escribe dos números binarios de 8 bits y luego los envía al bus, permitiendo así que se muestre un patrón.

Sin embargo, dado que los LEDs en la matriz de puntos utilizan polos comunes, controlar 
varias filas o columnas al mismo tiempo puede provocar interferencias (por ejemplo, si 
(1,1) y (2,2) están encendidos al mismo tiempo, (1,2) y (2,1) también se iluminarán involuntariamente). Por lo tanto, es necesario activar una columna (o una fila) a la vez, realizar el ciclo 8 veces y utilizar el principio de postimagen para que el ojo humano perciba 8 patrones como un solo patrón con la información de una matriz de 8x8.

.. code-block:: arduino

   for(int num = 0; num <=8; num++)
   {
      digitalWrite(STcp,LOW); // mantén ST_CP en bajo mientras se transmite
      shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
      shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
      // vuelve a poner en alto el pin de enganche para señalar al chip que 
      // ya no necesita escuchar información
      digitalWrite(STcp,HIGH); // lleva ST_CP a alto para guardar los datos
   }

En este ejemplo, la función principal anida un bucle ``for``, y cuando ``i`` es 1, solo se activa la primera línea (el chip de la línea de control obtiene el valor ``0x80``) y se escribe la imagen de la primera línea.
Cuando ``i`` es 2, se activa la segunda línea (el chip de la línea de control obtiene el valor ``0x40``) y se escribe la imagen de la segunda línea. Así sucesivamente, completando las 8 salidas.

Como en la pantalla de 7 segmentos de 4 dígitos, se debe mantener la tasa de refresco para evitar parpadeos percibidos por el ojo humano, por lo que se recomienda evitar el uso de ``sleep()`` en el bucle principal siempre que sea posible.


**Aprende Más**

Prueba reemplazar ``datArray`` con el siguiente arreglo y observa qué imágenes aparecen.

.. code-block:: arduino

   int datArray1[] = {0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF};
   int datArray2[] = {0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF};
   int datArray3[] = {0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF};
   int datArray4[] = {0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF};
   int datArray5[] = {0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF};
   int datArray6[] = {0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF};

O bien, intenta dibujar tus propios gráficos.
