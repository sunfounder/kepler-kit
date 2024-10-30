.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_buzzer:

Buzzer
============


Como un tipo de zumbador electrónico con una estructura integrada, los zumbadores, que funcionan con corriente continua (DC), se utilizan ampliamente en computadoras, impresoras, fotocopiadoras, alarmas, juguetes electrónicos, dispositivos electrónicos automotrices, teléfonos, temporizadores y otros productos electrónicos o dispositivos de voz.

Los zumbadores se pueden clasificar en activos y pasivos (ver la imagen a continuación). Gira el zumbador de forma que los pines queden hacia arriba; el zumbador con una placa de circuito verde es un zumbador pasivo, mientras que el que está cubierto con una cinta negra es un zumbador activo.

|img_buzzer|

Diferencias entre un zumbador activo y uno pasivo:

Un zumbador activo tiene una fuente de oscilación incorporada, por lo que emitirá sonidos cuando se energice. Pero un zumbador pasivo no tiene dicha fuente, por lo que no emitirá sonido si se utilizan señales de corriente continua (DC); en cambio, necesitas usar ondas cuadradas cuya frecuencia esté entre 2K y 5K para hacerlo funcionar. El zumbador activo suele ser más caro que el pasivo debido a los múltiples circuitos de oscilación que tiene integrados.

A continuación se muestra el símbolo eléctrico de un zumbador. Tiene dos pines con polos positivo y negativo. El símbolo "+" en la superficie representa el ánodo y el otro es el cátodo.

|img_buzzer_symbol|

Puedes comprobar los pines del zumbador: el más largo es el ánodo y el más corto es el cátodo. No los conectes de forma incorrecta, de lo contrario, el zumbador no emitirá sonido.

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Example
.. -------------------

.. :ref:`Alarma de Intruso`

.. :ref:`Tono Personalizado`

**Ejemplos**

* :ref:`py_ac_buz` (Para usuarios de MicroPython)
* :ref:`py_pa_buz` (Para usuarios de MicroPython)
* :ref:`py_light_theremin` (Para usuarios de MicroPython)
* :ref:`py_alarm_lamp` (Para usuarios de MicroPython)
* :ref:`py_music_player` (Para usuarios de MicroPython)
* :ref:`py_fruit_piano` (Para usuarios de MicroPython)
* :ref:`py_reversing_aid` (Para usuarios de MicroPython)
* :ref:`ar_ac_buz` (Para usuarios de Arduino)
* :ref:`ar_pa_buz` (Para usuarios de Arduino)
* :ref:`per_service_bell` (Para usuarios de Piper Make)
* :ref:`per_reversing_system` (Para usuarios de Piper Make)
* :ref:`per_reaction_game` (Para usuarios de Piper Make)
