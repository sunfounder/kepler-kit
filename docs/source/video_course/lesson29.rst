.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora en profundidad el apasionante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con el apoyo de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 29: Proyecto Cliente-Servidor Simple para Controlar un LED RGB
=============================================================================

Este tutorial cubre la configuración de un LED RGB controlado de forma remota mediante una Raspberry Pi Pico W y una PC a través de Wi-Fi:

* **Introducción**: El objetivo es controlar un LED RGB en una Raspberry Pi Pico W de forma remota utilizando Wi-Fi.
* **Diagrama de Cableado y Configuración**: Conectar el LED RGB a los pines GPIO 16, 17 y 18, y la OLED a los pines GPIO 2 (SDA) y 3 (SCL).
* **Configuración del Servidor**: Importar bibliotecas, inicializar los pines GPIO, conectarse a Wi-Fi, crear un servidor UDP y mostrar la IP en la pantalla OLED.
* **Configuración del Cliente**: Crear un cliente UDP en la PC para enviar comandos de color al servidor.
* **Demostración Práctica**: Muestra cómo cambiar el color del LED RGB mediante comandos enviados desde la PC, con la OLED mostrando los comandos y la IP.
* **Configuración Final y Pruebas**: Alimentar la Raspberry Pi Pico W con una batería, guardar el código como ``main.py`` y demostrar el funcionamiento inalámbrico.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
