.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_7_segment:

Pantalla de 7 segmentos
============================

|img_7seg|

Una pantalla de 7 segmentos es un componente en forma de "8" que agrupa 7 LEDs. Cada LED se denomina segmento; cuando se enciende, un segmento forma parte de un número que se va a mostrar.

Existen dos tipos de conexión de pines: Cátodo Común (CC) y Ánodo Común (CA). Como sugiere el nombre, una pantalla CC tiene todos los cátodos de los 7 LEDs conectados, mientras que una pantalla CA tiene todos los ánodos de los 7 segmentos conectados.

En este kit, utilizamos la pantalla de 7 segmentos de Cátodo Común. A continuación, se muestra el símbolo electrónico correspondiente.

|img_7seg_cathode|

Cada uno de los LEDs en la pantalla tiene un segmento posicional con uno de sus pines de conexión saliendo del paquete de plástico rectangular. Estos pines de LED están etiquetados de "a" a "g", representando cada LED individual. Los demás pines de los LEDs están conectados juntos formando un pin común. Así, polarizando directamente los pines apropiados de los segmentos LED en un orden particular, algunos segmentos se iluminarán y otros permanecerán apagados, mostrando así el carácter correspondiente en la pantalla.


* `Seven-segment Display - Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display>`_

**Códigos de Visualización** 

Para ayudarte a comprender cómo las pantallas de 7 segmentos (Cátodo Común) muestran números, hemos elaborado la siguiente tabla. Los números corresponden al rango de 0-F mostrados en la pantalla de 7 segmentos; (DP) GFEDCBA se refiere al conjunto de LED correspondiente configurado en 0 o 1. Por ejemplo, 00111111 significa que DP y G están configurados en 0, mientras que los demás están en 1. Por lo tanto, el número 0 se muestra en la pantalla de 7 segmentos, mientras que el código HEX corresponde al número hexadecimal.

.. list-table:: Código de Glifos
    :widths: 20 20 20
    :header-rows: 1

    *   - Números	
        - Código Binario
        - Código Hexadecimal  
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f
    *   - A	
        - 01110111	
        - 0x77
    *   - B
        - 01111100	
        - 0x7c
    *   - C	
        - 00111001	
        - 0x39
    *   - D	
        - 01011110	
        - 0x5e
    *   - E	
        - 01111001	
        - 0x79
    *   - F	
        - 01110001	
        - 0x71

.. Example
.. -------------------

.. :ref:`Pantalla de Segmentos LED`



**Ejemplos**

* :ref:`py_74hc_7seg` (Para usuarios de MicroPython)
* :ref:`ar_74hc_7seg` (Para usuarios de Arduino)
