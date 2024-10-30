.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_ws2812:

Tira de LEDs RGB WS2812 de 8 LEDs
=======================================

|img_ws2812|

La tira de LEDs RGB WS2812 de 8 LEDs está compuesta por 8 LEDs RGB. 
Solo se requiere un pin para controlar todos los LEDs. Cada LED RGB tiene un chip WS2812, que se puede controlar de forma independiente. 
Puede realizar una visualización de brillo de 256 niveles y una reproducción de color real completa con 16,777,216 colores. 
Al mismo tiempo, el píxel contiene un circuito amplificador de señal con retención de datos digitales e interfaz inteligente, 
y un circuito de conformado de señal integrado para garantizar de manera efectiva la consistencia del color en los puntos de luz del píxel.

Es flexible, puede acoplarse, doblarse y cortarse libremente, y su parte posterior está equipada con cinta adhesiva, lo que permite fijarla en superficies irregulares y su instalación en espacios reducidos.

**Características**

* Voltaje de Trabajo: DC5V
* IC: Un IC controla un LED RGB
* Consumo: 0.3w por LED
* Temperatura de Trabajo: -15-50°C
* Color: RGB a todo color
* Tipo de RGB: 5050RGB (IC integrado WS2812B)
* Grosor de la Tira de Luz: 2mm
* Cada LED se puede controlar individualmente

**Introducción al WS2812B**

* `WS2812B Datasheet <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

El WS2812B es una fuente de luz LED de control inteligente que integra el circuito de control y el chip RGB en 
un paquete de componentes 5050. Incluye un puerto de datos digitales con retención de datos y un circuito de amplificación 
y conformado de señal. También tiene un oscilador interno de precisión y un control de corriente constante programable de 12V, 
garantizando de manera efectiva la consistencia del color en los puntos de luz de los píxeles.

El protocolo de transferencia de datos utiliza un modo de comunicación NZR simple. Después del reinicio del pixel, 
el puerto DIN recibe los datos del controlador, el primer píxel recoge los primeros 24 bits de datos y los envía al latch de datos interno. 
Los datos restantes, que son conformados por el circuito de amplificación interna, se envían al siguiente píxel en cascada a través del puerto DO. 
Después de la transmisión por cada píxel, la señal reduce 24 bits. La tecnología de transmisión de auto conformado permite que el número de píxeles en cascada no esté limitado, 
dependiendo solo de la velocidad de transmisión de la señal.

El LED tiene un bajo voltaje de manejo, es ecológico y de bajo consumo energético, con alta luminosidad, amplio ángulo de dispersión, buena consistencia, bajo consumo, larga vida útil, entre otras ventajas. 
El chip de control integrado en el LED simplifica el circuito, reduce el tamaño y facilita la instalación.

.. Example
.. -------------------

.. :ref:`Tira de LEDs RGB`


**Ejemplos**

* :ref:`py_neopixel` (Para usuarios de MicroPython)
* :ref:`py_music_player` (Para usuarios de MicroPython)
* :ref:`ar_neopixel` (Para usuarios de Arduino)
* :ref:`per_flowing_leds` (Para usuarios de Piper Make)
