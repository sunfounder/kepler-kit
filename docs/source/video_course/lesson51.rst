.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y profundiza en el fascinante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Lección 51: Medidor de Inclinación Definitivo con el MPU6050
=============================================================================

Este tutorial cubre la creación de un medidor de inclinación preciso usando el sensor MPU6050 y la Raspberry Pi Pico W:

* **Configuración**: Conecta el MPU6050 y la pantalla OLED 1306 a la Raspberry Pi Pico W.
* **Desafíos**: Los datos del acelerómetro son ruidosos y los del giroscopio presentan deriva con el tiempo.
* **Solución**: Utiliza un filtro complementario para combinar los datos del acelerómetro y giroscopio, con corrección de errores para eliminar el error en estado estable.
* **Implementación**: Inicializa los sensores y la OLED. Recoge y filtra los datos, mostrando la inclinación como un nivel de burbuja y un indicador de grados en la OLED.
* **Demostración**: Prueba para obtener lecturas estables de inclinación y balanceo, con operación portátil alimentada por batería.
* **Mejoras Adicionales**: Considera la monitorización inalámbrica o la creación de una carcasa impresa en 3D para mayor portabilidad.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>