.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y profundiza en el fascinante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 46: Construye un Medidor de Inclinación de 2 Ejes con Pantalla Usando el MPU6050
=================================================================================================

Este tutorial cubre el uso del sensor MPU6050 con la Raspberry Pi Pico W para crear un inclinómetro de dos ejes:

* **Configuración**: Conecta el MPU6050 y el OLED 1306 a la Raspberry Pi Pico W.
* **Concepto**: Mide la inclinación usando ángulos de cabeceo (pitch) y balanceo (roll), mostrando el nivel en forma de burbuja en el OLED.
* **Ecuación**: 
   - Pitch: \(\arctan\left(\frac{Y}{Z}\right)\)
   - Roll: \(\arctan\left(\frac{X}{Z}\right)\)
   - Convierte los valores de radianes a grados.
* **Código**: Configura las bibliotecas, mide la aceleración en X, Y, Z, calcula los ángulos y muéstralos en el OLED.
* **Demostración**: Prueba la inclinación y ajusta el movimiento de la burbuja para mayor sensibilidad.
* **Avanzado**: Estabiliza las lecturas de inclinación para evitar errores causados por aceleración o vibraciones.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
