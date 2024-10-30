.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora en profundidad el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 70: Ejemplo de Salida Limpia en Programas de Doble Núcleo en MicroPython
===================================================================================

Este tutorial cubre el uso de hilos para controlar un servo y un botón con la Raspberry Pi Pico W:

* **Configuración de Cableado**: Conecta el control del servo al GPIO 17, la alimentación al pin 40 y la tierra al pin 38. Conecta el botón al GPIO 16 y a tierra.
* **Implementación de Código**: Importa ``machine``, ``time``, ``_thread`` y ``Servo``. Configura los pines para el botón y el servo. Implementa un interruptor para controlar la posición del servo. Usa hilos para el movimiento del servo y una salida limpia del programa.
* **Tarea**: Modifica el programa para que salga de manera ordenada, incluso si se interrumpe durante el movimiento del servo.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
