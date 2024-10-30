.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_dot_matrix:

Matriz de LED
==========================

|img_led_matrix|

Generalmente, las matrices de LED se pueden clasificar en dos tipos: 
cátodo común (CC) y ánodo común (CA). A simple vista parecen similares, 
pero la diferencia radica en su estructura interna, la cual se puede 
comprobar mediante pruebas. En este kit se utiliza una matriz de LED CA, 
la cual está etiquetada como 788BS en el costado.

Observa la figura a continuación. Los pines están dispuestos en los dos 
extremos en la parte trasera. Tomando como referencia el lado de la etiqueta: 
los pines de este extremo son del 1 al 8, y del otro lado son del 9 al 16.

Vista externa:

|img_788bs_i|

A continuación se muestran las figuras que ilustran su estructura interna. 
En una matriz de LED CA, la FILA representa el ánodo del LED y la COLUMNA es 
el cátodo; es al contrario en una matriz CC. Algo que tienen en común ambos 
tipos es que, para ambas, los pines 13, 3, 4, 10, 6, 11, 15 y 16 son todos 
COLUMNA, mientras que los pines 9, 14, 8, 12, 1, 7, 2 y 5 son todos FILA. 
Si deseas encender el primer LED en la esquina superior izquierda, en una 
matriz de LED CA, solo debes configurar el pin 9 como alto y el pin 13 como 
bajo, mientras que en una CC, configuras el pin 13 como alto y el pin 9 como 
bajo. Si deseas encender toda la primera columna, para CA, configura el pin 
13 como bajo y las FILAS 9, 14, 8, 12, 1, 7, 2 y 5 como alto, mientras que para 
CC, configura el pin 13 como alto y las FILAS 9, 14, 8, 12, 1, 7, 2 y 5 como 
bajo. Observa las siguientes figuras para una mejor comprensión.

Vista interna:

|img_788bs_sche|

Numeración de pines correspondiente a las filas y columnas mencionadas:

=========== ====== ====== ===== ====== ===== ====== ====== ======
**COL**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **13** **3**  **4** **10** **6** **11** **15** **16**
**ROW**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **9**  **14** **8** **12** **1** **7**  **2**  **5**
=========== ====== ====== ===== ====== ===== ====== ====== ======

Además, aquí se utilizan dos chips 74HC595. Uno controla las filas de la 
matriz de LED mientras que el otro controla las columnas.


**Ejemplos**

* :ref:`py_74hc_788bs` (Para usuarios de MicroPython)
* :ref:`py_bubble_level` (Para usuarios de MicroPython)
* :ref:`ar_74hc_788bs` (Para usuarios de Arduino)
