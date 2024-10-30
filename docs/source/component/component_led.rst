.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_led:

LED
==========

|img_led|

El diodo emisor de luz (LED) es un tipo de componente semiconductor que puede convertir energía eléctrica en energía luminosa a través de uniones PN. Según la longitud de onda, se puede clasificar en diodo láser, diodo emisor de luz infrarroja y diodo emisor de luz visible, comúnmente conocido como LED.

El diodo tiene conductividad unidireccional, por lo que la corriente fluye en la dirección que indica la flecha en el símbolo del circuito. Solo se debe aplicar una tensión positiva en el ánodo y una negativa en el cátodo para que el LED se encienda.

|img_led_symbol|

Un LED tiene dos pines. El pin más largo es el ánodo y el más corto es el cátodo. Es importante no conectarlos al revés. Hay una caída de voltaje directa fija en el LED, por lo que no se puede conectar directamente al circuito, ya que el voltaje de la fuente de alimentación puede superar esta caída y causar que el LED se queme. La caída de voltaje directa para los LEDs rojos, amarillos y verdes es de 1.8 V, mientras que para los blancos es de 2.6 V. La mayoría de los LEDs pueden soportar una corriente máxima de 20 mA, por lo que es necesario conectar una resistencia limitadora de corriente en serie.

La fórmula para calcular el valor de la resistencia es la siguiente:

    R = (Vsupply – VD)/I

**R** representa el valor de la resistencia limitadora, **Vsupply** es el voltaje de la fuente de alimentación, **VD** es la caída de voltaje y **I** es la corriente de trabajo del LED.

Aquí tienes una introducción detallada sobre los LEDs: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

.. **Ejemplos**

.. * :ref:`Hello, Breadboard!` (Para usuarios de MicroPython)
.. * :ref:`fading_led_micropython` (Para usuarios de MicroPython)
.. * :ref:`fading_led_arduino` (Para usuarios de C/C++ (Arduino))
.. * :ref:`hello_led_arduino` (Para usuarios de C/C++ (Arduino))

**Ejemplos**

* :ref:`py_led` (Para usuarios de MicroPython)
* :ref:`py_fade` (Para usuarios de MicroPython)
* :ref:`py_alarm_lamp` (Para usuarios de MicroPython)
* :ref:`py_traffic_light` (Para usuarios de MicroPython)
* :ref:`py_reversing_aid` (Para usuarios de MicroPython)
* :ref:`ar_led` (Para usuarios de Arduino)
* :ref:`ar_fade` (Para usuarios de Arduino)
* :ref:`per_blink` (Para usuarios de Piper Make)
* :ref:`per_button` (Para usuarios de Piper Make)
* :ref:`per_service_bell` (Para usuarios de Piper Make)
* :ref:`per_reversing_system` (Para usuarios de Piper Make)
* :ref:`per_reaction_game` (Para usuarios de Piper Make)
