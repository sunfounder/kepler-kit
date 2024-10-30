.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora a fondo el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 60: Controlar Colores de NeoPixel con un Joystick en MicroPython
=============================================================================

Este tutorial cubre el control de una tira LED mediante un joystick usando la Raspberry Pi Pico W:

* **Configuración de Conexiones**:

    - Conecta la tierra del joystick al pin 38, 3.3V al pin 36, VRX al GPIO 27 y VRY al GPIO 26.
    - Conecta la tierra del Neopixel al pin 38, 5V al pin 40 y el dato al GPIO 0.

* **Implementación de Código**:

    - Importa las bibliotecas (``machine``, ``time``, ``math``, ``neopixel``).
    - Configura el ADC para el joystick y el Neopixel. Lee los valores del joystick y calcula los ángulos.
    - Convierte los ángulos a valores RGB para el Neopixel.

* **Tarea**: Escribe un programa para controlar el color y brillo de Neopixel basado en el ángulo del joystick y su distancia desde el centro.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
