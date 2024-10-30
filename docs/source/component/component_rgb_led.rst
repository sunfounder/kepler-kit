.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_rgb:

LED RGB
=================

|img_rgb|

Los LEDs RGB emiten luz en varios colores. Un LED RGB combina tres LEDs (rojo, verde y azul) dentro de una carcasa plástica transparente o semitransparente. Puede mostrar diferentes colores al variar el voltaje de entrada de los tres pines y superponerlos, lo que, según cálculos, puede generar hasta 16,777,216 colores diferentes.

|img_rgb_light|

Los LEDs RGB se pueden clasificar en anodo común y cátodo común. En este kit, se utiliza el último. El **cátodo común**, o CC, significa que los cátodos de los tres LEDs están conectados. Una vez que lo conectes a GND y enchufes los tres pines, el LED emitirá el color correspondiente.

Su símbolo de circuito se muestra en la figura.

|img_rgb_symbol|

Un LED RGB tiene 4 pines: el pin más largo es el cátodo común, que usualmente se conecta a GND; el pin de la izquierda junto al más largo es el rojo, y los otros dos a la derecha son el verde y el azul.

|img_rgb_pin|

**Características**

* Color: Tricolor (Rojo/Verde/Azul)
* Cátodo Común
* Lente Redonda Clara de 5mm
* Voltaje Directo: Rojo: DC 2.0 - 2.2V; Azul y Verde: DC 3.0 - 3.2V (IF=20mA)
* LED RGB DIP de 0.06 Vatios
* Luminancia Hasta un 20% Más Brillante
* Ángulo de Visión: 30°

.. Example
.. -------------------

.. :ref:`Colorful Light`


**Ejemplos**

* :ref:`py_rgb` (Para usuarios de MicroPython)
* :ref:`py_fruit_piano` (Para usuarios de MicroPython)
* :ref:`ar_rgb` (Para usuarios de Arduino)
* :ref:`per_rainbow_light` (Para usuarios de Piper Make)
