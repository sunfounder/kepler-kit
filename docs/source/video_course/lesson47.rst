.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y profundiza en el fascinante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 47: Mejora de Datos del Sensor con un Filtro de Paso Bajo
=============================================================================

Este tutorial cubre el uso del sensor MPU6050 con la Raspberry Pi Pico W para crear un inclinómetro de dos ejes estable mediante la implementación de un filtro de paso bajo:

* **Configuración**: Conecta el MPU6050 a la Raspberry Pi Pico W.
* **Concepto**: Mide la inclinación utilizando datos del acelerómetro, abordando errores causados por la aceleración.
* **Filtro de Paso Bajo**: Implementa un filtro para suavizar los datos utilizando la ecuación: ``\(\text{nuevo valor} = \text{confianza} \times \text{medición} + (1 - \text{confianza}) \times \text{valor anterior}\)``.
* **Código**: Mide X, Y, Z, filtra los ángulos de pitch y roll, y muestra los resultados.
* **Tarea**: Prueba el filtro de paso bajo y experimenta con diferentes valores de confianza.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
