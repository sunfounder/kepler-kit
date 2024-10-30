.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_button:

Botón
==========

|img_button|

Los botones son componentes comunes que se utilizan para controlar dispositivos electrónicos. Generalmente se usan como interruptores para conectar o interrumpir circuitos. Aunque hay botones de diferentes tamaños y formas, el que se utiliza aquí es un mini-botón de 6 mm como se muestra en las siguientes imágenes.
El pin 1 está conectado al pin 2, y el pin 3 al pin 4. Por lo tanto, solo necesitas conectar cualquiera de los pines 1 y 2 con los pines 3 o 4.

A continuación se muestra la estructura interna de un botón. El símbolo en la parte inferior derecha se usa habitualmente para representar un botón en los circuitos.

|img_button_symbol|

Dado que el pin 1 está conectado al pin 2, y el pin 3 al pin 4, cuando se presiona el botón, los 4 pines se conectan, cerrando así el circuito.

|img_button2|

.. Examples
.. -------------------

.. :ref:`Lectura del Valor del Botón`

**Ejemplos**

* :ref:`py_button` (Para usuarios de MicroPython)
* :ref:`ar_button` (Para usuarios de Arduino)
* :ref:`per_button` (Para usuarios de Piper Make)
* :ref:`per_rainbow_light` (Para usuarios de Piper Make)
* :ref:`per_drum_kit` (Para usuarios de Piper Make)
* :ref:`per_reaction_game` (Para usuarios de Piper Make)
