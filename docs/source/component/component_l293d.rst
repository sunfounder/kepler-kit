.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_l293d:

IC L293D 
=================

|img_l293d0|

El L293D es un controlador de motor de 4 canales integrado en un chip de alto voltaje y alta corriente. 
Está diseñado para conectarse a niveles lógicos estándar DTL y TTL, y puede manejar cargas inductivas (como bobinas de relés, motores DC, motores paso a paso) y transistores de conmutación de potencia, entre otros. 
Los motores de corriente continua (DC) son dispositivos que convierten la energía eléctrica DC en energía mecánica y se utilizan ampliamente en sistemas de accionamiento eléctrico por su excelente rendimiento en regulación de velocidad.

Observa el diagrama de pines a continuación. El L293D tiene dos pines (Vcc1 y Vcc2) para la fuente de alimentación. 
Vcc2 se utiliza para suministrar energía al motor, mientras que Vcc1 alimenta el chip. Dado que aquí se usa un motor DC de pequeño tamaño, conecta ambos pines a +5V.

|img_l293d1| 

A continuación se muestra la estructura interna del L293D. 
El pin EN es un pin de habilitación y solo funciona con nivel alto; A representa la entrada y Y la salida. 
Puedes ver la relación entre ellos en la parte inferior derecha. 
Cuando el pin EN está en nivel alto, si A es alto, Y produce un nivel alto; si A es bajo, Y produce un nivel bajo. Cuando el pin EN está en nivel bajo, el L293D no funciona.

|img_l293d2|

* `L293D Datasheet <https://cdn-shop.adafruit.com/datasheets/l293d.pdf>`_

**Ejemplos**

* :ref:`py_motor` (Para usuarios de MicroPython)
* :ref:`ar_motor` (Para usuarios de Arduino)
* :ref:`py_pump` (Para usuarios de MicroPython)
* :ref:`ar_pump` (Para usuarios de Arduino)
* :ref:`per_smart_fan` (Para usuarios de Piper Make)
