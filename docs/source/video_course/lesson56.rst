.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora a fondo el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 56: Usando un Joystick con MicroPython
=============================================================================

Este tutorial cubre el uso de un joystick con la Raspberry Pi Pico W:

* **Configuración de Conexiones**: Conecta tierra, 3.3V, VRX al pin GPIO 27 y VRY al pin GPIO 26.
* **Implementación de Código**: Importa las librerías ``machine``, ``time``, ``math``; configura el ADC para los ejes del joystick; lee e imprime los valores del joystick.
* **Calibración**: Convierte las lecturas a una escala de -100 a +100 para una interpretación más intuitiva.
* **Tarea**: Escribe un programa para calibrar el joystick de modo que el centro registre (0,0) y los bordes ±100.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/0W8XSJhGux0?si=DO3JL-oMiMfbXF_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
