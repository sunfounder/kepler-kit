.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros apasionados y explora a fondo el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a nuevos anuncios y adelantos de productos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 71: Permitir que el Hilo Complete la Tarea Antes de Terminar
===================================================================================

Este tutorial cubre la terminación ordenada de un programa multihilo en la Raspberry Pi Pico W:

* **Configuración de Cableado**: Conecta el control del servo al GPIO 17, la alimentación al pin 40 y la tierra al pin 38. Conecta el botón al GPIO 16 y a tierra.
* **Implementación de Código**: Importa ``machine``, ``time``, ``_thread`` y ``Servo``. Configura los pines para el botón y el servo. Implementa un interruptor para el movimiento del servo, usando hilos para salidas limpias.
* **Manejo de Terminación Ordenada**: Usa una variable global ``running`` para gestionar la ejecución del bucle. Implementa un bloqueo para controlar las secciones críticas. Asegura que el servo complete su movimiento antes de terminar.
* **Tarea**: Modifica el programa para manejar más componentes o sensores, asegurando una terminación ordenada en todos los casos.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/Xm3chr1-hkY?si=ITIUvlqKF6UdOsq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
