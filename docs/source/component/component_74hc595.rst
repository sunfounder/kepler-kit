.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_74hc595:

74HC595
===========

|img_74hc595|

El 74HC595 consta de un registro de desplazamiento de 8 bits y un registro de almacenamiento con salidas paralelas de tres estados. Convierte la entrada serial en salida paralela para que puedas ahorrar puertos de IO en un MCU.

* Cuando MR (pin 10) está en nivel alto y OE (pin 13) está en nivel bajo, los datos se introducen en el flanco ascendente de SHcp y se transfieren al registro de memoria a través del flanco ascendente de SHcp.
* Si los dos relojes están conectados juntos, el registro de desplazamiento siempre está un pulso antes que el registro de memoria.
* Hay un pin de entrada de desplazamiento serial (Ds), un pin de salida serial (Q) y un botón de reinicio asíncrono (nivel bajo) en el registro de memoria.
* El registro de memoria tiene una salida paralela de 8 bits y en tres estados.
* Cuando OE está habilitado (nivel bajo), los datos en el registro de memoria se envían al bus (Q0 ~ Q7).

* `74HC595 Datasheet <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

|img_74jc595_pin|

Pines del 74HC595 y sus funciones:

* **Q0-Q7**: Pines de salida de datos paralelos de 8 bits, capaces de controlar directamente 8 LEDs o 8 pines de una pantalla de 7 segmentos.
* **Q7'**: Pin de salida en serie, conectado a DS de otro 74HC595 para conectar múltiples 74HC595 en serie.
* **MR**: Pin de reinicio, activo en nivel bajo.
* **SHcp**: Entrada de secuencia temporal del registro de desplazamiento. En el flanco ascendente, los datos en el registro de desplazamiento se desplazan un bit sucesivamente, es decir, los datos en Q1 se mueven a Q2, y así sucesivamente. En el flanco descendente, los datos en el registro de desplazamiento permanecen sin cambios.
* **STcp**: Entrada de secuencia temporal del registro de almacenamiento. En el flanco ascendente, los datos en el registro de desplazamiento se mueven al registro de memoria.
* **CE**: Pin de habilitación de salida, activo en nivel bajo.
* **DS**: Pin de entrada de datos seriales.
* **VCC**: Voltaje de alimentación positivo.
* **GND**: Tierra.

.. Example
.. -------------------

.. :ref:`Microchip - :ref:`cpn_74hc595``

**Ejemplos**

* :ref:`py_74hc_led` (Para usuarios de MicroPython)
* :ref:`py_74hc_7seg` (Para usuarios de MicroPython)
* :ref:`py_74hc_4dig` (Para usuarios de MicroPython)
* :ref:`py_74hc_788bs` (Para usuarios de MicroPython)
* :ref:`py_passage_counter` (Para usuarios de MicroPython)
* :ref:`py_10_second` (Para usuarios de MicroPython)
* :ref:`py_traffic_light` (Para usuarios de MicroPython)
* :ref:`py_bubble_level` (Para usuarios de MicroPython)
* :ref:`ar_74hc_led` (Para usuarios de Arduino)
* :ref:`ar_74hc_7seg` (Para usuarios de Arduino)
* :ref:`ar_74hc_4dig` (Para usuarios de Arduino)
* :ref:`ar_74hc_788bs` (Para usuarios de Arduino)
