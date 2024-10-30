.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_potentiometer:

Potenciómetro
===============

|img_pot|

El potenciómetro es un componente resistivo con 3 terminales, y su valor de resistencia se puede ajustar según una variación regular.

Los potenciómetros vienen en diversas formas, tamaños y valores, pero todos tienen lo siguiente en común:

* Tienen tres terminales (o puntos de conexión).
* Disponen de una perilla, tornillo o deslizador que se puede mover para variar la resistencia entre el terminal medio y cualquiera de los terminales externos.
* La resistencia entre el terminal medio y cualquiera de los terminales externos varía de 0 Ω a la resistencia máxima del potenciómetro a medida que se mueve la perilla, tornillo o deslizador.

A continuación se muestra el símbolo de circuito de un potenciómetro.

|img_pot_symbol|

Las funciones del potenciómetro en el circuito son las siguientes:

#. Funcionando como divisor de voltaje

    El potenciómetro es una resistencia ajustable de forma continua. Al ajustar el eje o el mango deslizante del potenciómetro, el contacto móvil se desliza sobre la resistencia. En este punto, se puede obtener un voltaje de salida dependiendo del voltaje aplicado al potenciómetro y el ángulo que haya girado el brazo móvil o el recorrido que haya realizado.

#. Funcionando como reóstato

    Cuando se usa el potenciómetro como reóstato, conecta el pin medio y uno de los otros 2 pines en el circuito. De esta manera, se puede obtener un valor de resistencia que cambia de forma suave y continua dentro del recorrido del contacto móvil.

#. Funcionando como controlador de corriente

    Cuando el potenciómetro actúa como controlador de corriente, el terminal de contacto deslizante debe estar conectado como uno de los terminales de salida.

Si deseas saber más sobre el potenciómetro, consulta: `Potenciómetro - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer.>`_

.. Ejemplo
.. -------------------

.. * :ref:`Turn the Knob` (Para usuarios de MicroPython)
.. * :ref:`Table Lamp` (Para usuarios de C/C++(Arduino))


**Ejemplos**

* :ref:`py_pot` (Para usuarios de MicroPython)
* :ref:`ar_pot` (Para usuarios de Arduino)
* :ref:`per_swing_servo` (Para usuarios de Piper Make)
