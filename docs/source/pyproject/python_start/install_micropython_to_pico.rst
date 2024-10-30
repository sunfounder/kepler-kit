.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_micropython_on_pico:

1.3 Instalar MicroPython en tu Pico
==========================================

Ahora vamos a instalar MicroPython en la Raspberry Pi Pico. Thonny IDE ofrece una forma muy conveniente de hacerlo con solo un clic.

.. note::
    Si prefieres no actualizar Thonny, también puedes utilizar la herramienta oficial de Raspberry Pi |link_micropython_pi|, simplemente arrastrando y soltando un archivo ``rp2_pico_xxxx.uf2`` en tu Raspberry Pi Pico.

#. Abre Thonny IDE.

    .. image:: img/set_pico1.png

#. Mantén presionado el botón **BOOTSEL** y conecta el Pico a la computadora mediante un cable Micro USB. Suelta el botón **BOOTSEL** una vez que tu Pico se monte como un Dispositivo de Almacenamiento Masivo llamado **RPI-RP2**.

    .. image:: img/bootsel_onboard.png

#. En la esquina inferior derecha, haz clic en el botón de selección del intérprete y selecciona **Instalar Micropython**.

    .. note::
        Si tu versión de Thonny no tiene esta opción, por favor actualiza a la última versión.

    .. image:: img/set_pico2.png

#. En el campo **Target volume**, aparecerá automáticamente el volumen del Pico que acabas de conectar, y en **Micropython variant**, selecciona **Raspberry Pi.Pico W/Pico WH**.

    .. image:: img/set_pico3.png

#. Haz clic en el botón **Install**, espera a que la instalación se complete y luego cierra esta página.

    .. image:: img/set_pico4.png

¡Felicidades, tu Raspberry Pi Pico ya está lista para usarse!
