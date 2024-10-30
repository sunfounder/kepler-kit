.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora a fondo el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 59: Control de un Servo con un Joystick
=============================================================================

Este tutorial cubre cómo controlar un servo con un joystick utilizando la Raspberry Pi Pico W:

* **Configuración de Conexiones**: Conecta la tierra del joystick al pin 38, 3.3V al pin 36, VRX al GPIO 27 y VRY al GPIO 26. Conecta el 5V del servo al pin 40, tierra al pin 38 y el control al GPIO 15.
* **Implementación de Código**: Importa ``machine``, ``time`` y ``math``. Configura el ADC para el joystick y PWM para el servo. Lee e imprime los valores del joystick.
* **Calibración y Control**: Escala los valores del ADC de -100 a +100. Calcula el ángulo del joystick y mapea este ángulo al PWM del servo.
* **Tarea**: Escribe un código para controlar el servo en función del ángulo del joystick (0-180 grados).

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
