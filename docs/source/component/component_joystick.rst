.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_joystick:

Módulo Joystick
=======================

|img_joystick_pic|

La idea básica de un joystick es traducir el movimiento de la palanca en información electrónica que una computadora pueda procesar.

Para comunicar un rango completo de movimiento a la computadora, 
un joystick necesita medir la posición de la palanca en dos ejes: el eje X (izquierda a derecha) y el eje Y (arriba y abajo). 
Al igual que en la geometría básica, las coordenadas X-Y determinan exactamente la posición de la palanca.

Para determinar la ubicación de la palanca, el sistema de control del joystick simplemente monitorea la posición de cada eje. 
El diseño convencional de un joystick analógico logra esto con dos potenciómetros, o resistencias variables.

El joystick también cuenta con una entrada digital que se activa cuando se presiona hacia abajo.

|img_joystick|


*  `Joystick - Wikipedia <https://en.wikipedia.org/wiki/Analog_stick>`_


**Ejemplos**


* :ref:`py_joystick` (Para usuarios de MicroPython)
* :ref:`ar_joystick` (Para usuarios de Arduino)
