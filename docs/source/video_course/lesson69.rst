.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora más a fondo el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 69: Cerrar Limpia y Correctamente los Hilos de MicroPython al Terminar el Programa
================================================================================================

Este tutorial cubre el control de un servo y LEDs en la Raspberry Pi Pico W utilizando ambos núcleos:

* **Configuración de Cableado**: Conecta el LED rojo al GPIO 15, el LED verde al GPIO 14 y el servo al GPIO 17, con alimentación en el pin 40 y tierra en el pin 38.
* **Implementación de Código**: Importa ``machine``, ``time``, ``_thread`` y ``Servo``. Configura los pines para los LEDs y el servo. Define ``other_core`` para hacer parpadear los LEDs según el movimiento del servo. Crea un bucle para controlar el servo y los LEDs.
* **Tarea**: Modifica el código para que el LED rojo parpadee en sentido horario y el LED verde en sentido antihorario al mover el servo.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
