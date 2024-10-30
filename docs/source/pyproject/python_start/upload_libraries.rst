.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _add_libraries_py:

1.4 Cargar las bibliotecas en el Pico
=========================================

En algunos proyectos, necesitarás bibliotecas adicionales. Aquí subiremos estas bibliotecas a la Raspberry Pi Pico W primero, para que luego podamos ejecutar el código directamente.

#. Descarga el código relevante desde el siguiente enlace.

   * :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

#. Abre Thonny IDE, conecta el Pico a tu computadora con un cable micro USB y haz clic en el intérprete "MicroPython (Raspberry Pi Pico).COMXX" en la esquina inferior derecha.

    .. image:: img/sec_inter.png

#. En la barra de navegación superior, haz clic en **View** -> **Files**.

    .. image:: img/th_files.png

#. Cambia la ruta a la carpeta donde descargaste el `code package <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`_ anteriormente, y luego ve a la carpeta ``kepler-kit-main/libs``.

    .. image:: img/th_path.png

#. Selecciona todos los archivos o carpetas en la carpeta ``libs/``, haz clic derecho y selecciona **Upload to**, esto tomará un momento.

    .. image:: img/th_upload.png

#. Ahora verás los archivos que acabas de cargar dentro de la unidad ``Raspberry Pi Pico``.

    .. image:: img/th_done.png
