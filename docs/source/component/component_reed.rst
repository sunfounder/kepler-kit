.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_reed:

Interruptor de Láminas (Reed Switch)
=========================================

|img_reed|

El interruptor de láminas es un interruptor eléctrico que se activa mediante un campo magnético aplicado. Fue inventado por Walter B. Ellwood de Bell Telephone Laboratories en 1936 y patentado en los Estados Unidos el 27 de junio de 1940 bajo el número de patente 2264746.

El principio de funcionamiento de un interruptor de láminas es muy sencillo. Dos láminas (generalmente hechas de hierro y níquel) que se superponen en los puntos finales están selladas dentro de un tubo de vidrio, con las dos láminas separadas por un pequeño espacio (solo unos pocos micrones). El tubo de vidrio está lleno de un gas inerte de alta pureza (como nitrógeno), y algunos interruptores de láminas están diseñados con un vacío en su interior para mejorar su rendimiento de alta tensión.

Las láminas actúan como conductores de flujo magnético. Cuando el interruptor no está en operación, las dos láminas no están en contacto; al pasar a través de un campo magnético generado por un imán permanente o una bobina electromagnética, el campo magnético aplicado provoca que las dos láminas adopten polaridades opuestas en sus extremos. Cuando la fuerza magnética supera la fuerza de resorte de las láminas, estas se juntan, cerrando el circuito. Cuando el campo magnético se debilita o desaparece, las láminas se separan debido a su propia elasticidad, abriendo el circuito nuevamente.

|img_reed_sche|

* `Reed Switch - Wikipedia <https://en.wikipedia.org/wiki/Reed_switch>`_

**Ejemplos**


* :ref:`py_reed` (Para usuarios de MicroPython)
* :ref:`ar_reed` (Para usuarios de Arduino)
