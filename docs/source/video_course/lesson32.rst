.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora en profundidad el apasionante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con el apoyo de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 32: Proyecto de Estación Meteorológica Portátil
=============================================================================

Este tutorial cubre la creación de una estación meteorológica portátil usando la Raspberry Pi Pico W:

* **Conexión a Wi-Fi**: Importar bibliotecas, crear un objeto WLAN y conectar a Wi-Fi.
* **Obtención de Datos Meteorológicos**: Utilizar la API de OpenWeatherMap para recuperar datos meteorológicos en tiempo real, requiriendo una clave de API.
* **Análisis de Datos JSON**: Extraer temperatura, humedad, presión, horas de amanecer y atardecer de la respuesta en JSON.
* **Visualización de Datos en OLED**: Configurar y conectar una pantalla OLED, usar la biblioteca ``ssd1306`` y actualizar los datos meteorológicos en pantalla en un bucle.
* **Alimentación del Dispositivo**: Alimentar la Raspberry Pi Pico W con una batería para hacerla portátil.
* **Explicación del Código**: Inicializar la OLED, conectar a Wi-Fi, obtener y mostrar datos meteorológicos, y configurar un bucle para actualizaciones periódicas.
* **Tarea**: Agregar un LED RGB para indicar condiciones meteorológicas basadas en la temperatura, humedad o velocidad del viento.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
