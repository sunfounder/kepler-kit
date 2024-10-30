.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_micro_switch:

Microinterruptor
========================

|img_micro_switch|

La construcción de un microinterruptor es bastante simple. Las partes principales del interruptor son:

|img_micro_switch2|

* 1. Émbolo (Actuador)
* 2. Cubierta
* 3. Pieza móvil
* 4. Soporte
* 5. Caja
* 6. Terminal NO: normalmente abierto
* 7. Terminal NC: normalmente cerrado
* 8. Contacto
* 9. Brazo móvil

Después de que un microinterruptor hace contacto físico con un objeto, sus contactos cambian de posición. El principio básico de funcionamiento es el siguiente:

Cuando el émbolo está en la posición de reposo o liberado:

* El circuito normalmente cerrado puede conducir corriente.
* El circuito normalmente abierto está eléctricamente aislado.

Cuando el émbolo es presionado o activado:

* El circuito normalmente cerrado se abre.
* El circuito normalmente abierto se cierra.

|img_micro_switch1|

**Ejemplos**

* :ref:`py_micro` (Para usuarios de MicroPython)
* :ref:`ar_micro` (Para usuarios de Arduino)
* :ref:`per_service_bell` (Para usuarios de Piper Make)
