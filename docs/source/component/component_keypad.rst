.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_keypad:

Teclado 4x4
========================

En sistemas con microcontroladores, si se utilizan más teclas, como en un teclado numérico o un teclado de teléfono, generalmente se requieren al menos de 12 a 16 teclas, y se suele emplear un teclado matricial.


El teclado matricial, también llamado teclado de filas, es un teclado que cuenta con cuatro líneas de E/S como filas y cuatro líneas de E/S como columnas. En cada intersección de las líneas de fila y columna hay una tecla. Por lo tanto, el número total de teclas en el teclado es de 4x4. Esta estructura de filas y columnas puede mejorar eficazmente la utilización de los puertos de E/S en un sistema de microcontrolador.


Sus contactos se acceden a través de un conector adecuado para conexión con un cable plano o para inserción en una placa de circuito impreso. 
En algunos teclados, cada botón se conecta a un contacto separado en el conector, mientras que todos los botones comparten una conexión a tierra común.

|img_keypad|

Con mayor frecuencia, los botones están codificados en una matriz, lo que significa que cada uno de ellos conecta un par único de conductores en la matriz. 
Esta configuración es ideal para el sondeo por parte de un microcontrolador, que se puede programar para enviar un pulso de salida a cada una de las cuatro líneas horizontales de forma secuencial. 
Durante cada pulso, verifica las cuatro líneas verticales restantes en secuencia para determinar cuál, si es que alguna, está transmitiendo una señal. 
Se deben agregar resistencias pull-up o pull-down a las líneas de entrada para evitar que los pines del microcontrolador se comporten de manera impredecible cuando no hay señal presente.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Ejemplos**

* :ref:`py_keypad` (Para usuarios de MicroPython)
* :ref:`py_guess_number` (Para usuarios de MicroPython)
* :ref:`ar_keypad` (Para usuarios de Arduino)
