.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_4_dit_7_segment:

Pantalla de 7 segmentos de 4 dígitos
========================================

La pantalla de 7 segmentos de 4 dígitos consiste en cuatro pantallas de 7 segmentos que funcionan juntas.

|img_4-digit-sche|

La pantalla de 7 segmentos de 4 dígitos funciona de manera independiente. 
Utiliza el principio de persistencia visual humana para mostrar rápidamente 
los caracteres de cada uno de los segmentos en un bucle, formando cadenas continuas.

Por ejemplo, cuando se muestra "1234" en la pantalla, el "1" aparece en el 
primer segmento de 7, mientras que "234" no se muestra. Tras un breve periodo 
de tiempo, el segundo segmento muestra "2", mientras que los segmentos 1º, 
3º y 4º permanecen apagados, y así sucesivamente. Los cuatro dígitos se muestran 
de manera secuencial. Este proceso es muy corto (típicamente 5 ms), y debido al 
efecto de post-resplandor óptico y el principio de persistencia de la visión, 
podemos ver los cuatro caracteres al mismo tiempo.

|img_4-digit-sche-ca| 

**Códigos de Visualización** 

Para ayudarte a comprender cómo las pantallas de 7 segmentos (cátodo común) muestran números, hemos elaborado la siguiente tabla. Los números corresponden al rango de 0-F mostrados en la pantalla de 7 segmentos; (DP) GFEDCBA se refiere al conjunto de LED correspondiente configurado en 0 o 1. Por ejemplo, 00111111 significa que DP y G están configurados en 0, mientras que los demás están en 1. Por lo tanto, el número 0 se muestra en la pantalla de 7 segmentos, mientras que el código HEX corresponde al número hexadecimal.

.. list-table:: Glyph Code
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

**Ejemplos**

* :ref:`py_74hc_4dig` (Para usuarios de MicroPython)
* :ref:`py_passage_counter` (Para usuarios de MicroPython)
* :ref:`py_10_second` (Para usuarios de MicroPython)
* :ref:`py_traffic_light` (Para usuarios de MicroPython)
* :ref:`ar_74hc_4dig` (Para usuarios de Arduino)
