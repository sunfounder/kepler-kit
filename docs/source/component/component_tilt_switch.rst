.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_tilt:

Interruptor de Inclinación
=============================

|img_tilt| 

El interruptor de inclinación que se utiliza aquí es un modelo con una bola de metal en su interior. Se emplea para detectar inclinaciones de un pequeño ángulo.

El principio es muy sencillo. Cuando el interruptor se inclina a cierto ángulo, la bola en su interior rueda y toca los dos contactos conectados a los pines externos, activando así el circuito. De lo contrario, la bola se mantendrá alejada de los contactos, interrumpiendo el circuito.

|img_tilt_symbol|

* `SW520D Tilt Switch Datasheet <https://www.tme.com/Document/f1e6cedd8cb7feeb250b353b6213ec6c/SW-520D.pdf>`_

.. * :ref:`Reading Button Value`


**Example**

* :ref:`py_tilt` (Para usuarios de MicroPython)
* :ref:`py_10_second` (Para usuarios de MicroPython)
* :ref:`ar_tilt` (Para usuarios de Arduino)
* :ref:`per_flowing_leds` (Para usuarios de Piper Make)
