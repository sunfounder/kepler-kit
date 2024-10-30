.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y profundiza en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 68: Ejemplo de Multitarea en MicroPython con LED y Servo
===================================================================================

Este tutorial cubre el control de un servo y LEDs en la Raspberry Pi Pico W usando ambos núcleos:

* **Configuración de Cableado**: Conecta el LED rojo al GPIO 15, el LED verde al GPIO 14, el servo al GPIO 17, alimentación al pin 40, y tierra al pin 38.
* **Implementación de Código**: Importa ``machine``, ``time``, ``_thread`` y ``Servo``. Configura los pines para los LEDs y el servo. Define la función ``other_core`` para hacer parpadear los LEDs según la dirección del servo.
* **Tarea**: Modifica el código para hacer parpadear el LED rojo en movimiento horario y el LED verde en movimiento antihorario del servo.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/n2eQTw9axHg?si=TRVLEM1EqyD_DefA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
