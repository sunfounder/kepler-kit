.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora a fondo el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 57: Calibración de un Joystick en MicroPython
=============================================================================

Este tutorial cubre la calibración de un joystick con la Raspberry Pi Pico W:

* **Configuración de Conexiones**: Conecta tierra al pin 38, 3.3V al pin 36, VRX al pin GPIO 27 y VRY al pin GPIO 26.
* **Implementación de Código**: Importa las librerías ``machine``, ``time``, ``math``; configura el ADC para los ejes del joystick; lee e imprime los valores del joystick.
* **Calibración**: Convierte los valores brutos del ADC a una escala de -100 a +100, ajustando para eliminar el ruido en la posición neutra.
* **Tarea**: Escribe un programa que calcule y reporte el ángulo del joystick en función de su posición.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
