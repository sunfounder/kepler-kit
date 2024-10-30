.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora en profundidad el apasionante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con el apoyo de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 45: Cálculo de Altura a partir de un Objeto en Caída Libre
=============================================================================

Este tutorial cubre el uso del sensor MPU6050 con la Raspberry Pi Pico W para medir distancias verticales:

* **Configuración**: Conecta el MPU6050 y el OLED 1306 a la Raspberry Pi Pico W, asegurando conexiones firmes para reducir el ruido.
* **Concepto**: Mide la distancia vertical calculando el tiempo de caída libre (T_drop) y utilízalo para determinar la altura desde la que fue soltado.
* **Ecuación**: Calcula la altura (H) con \( H = 16 \times (T_{drop})^2 \), convirtiendo el tiempo de milisegundos a segundos.
* **Implementación del Código**: Configura las bibliotecas, mide la aceleración en el eje Z para detectar 0G, inicia un temporizador durante la caída libre y muestra la altura y el tiempo de caída en el OLED.
* **Demostración Práctica**: Prueba el sensor dejándolo caer desde alturas conocidas y ajusta según sea necesario para mayor precisión.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
