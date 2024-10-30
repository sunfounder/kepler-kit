.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _setup_pico_arduino:

1.3 Configuración del Raspberry Pi Pico W (Importante)
========================================================

1. Instalación del Firmware UF2
-----------------------------------

Cuando conectas por primera vez el Raspberry Pi Pico W, o mantienes presionado el botón BOOTSEL al insertarlo, el dispositivo aparecerá como una unidad sin asignarse a un puerto COM. Esto hace que no sea posible cargar código.

Para solucionar esto, necesitas instalar el firmware UF2. Este firmware es compatible con MicroPython y también se puede usar con el Arduino IDE.

1. Descarga el Firmware UF2 desde el enlace a continuación.

    * :download:`Raspberry Pi Pico W UF2 Firmware <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Conecta tu Raspberry Pi Pico W a tu computadora usando un cable Micro USB. Tu Pico W se montará como un dispositivo de almacenamiento masivo llamado **RPI-RP2**.

    .. image:: img/install_pico_plugin.png

3. Arrastra y suelta el firmware UF2 descargado en la unidad **RPI-RP2**.

    .. image:: img/install_pico_uf2.png

4. Después de esto, la unidad **RPI-RP2** desaparecerá, y podrás continuar con los siguientes pasos.


2. Instalación del Paquete de Placas
---------------------------------------

Para programar el Raspberry Pi Pico W, necesitarás instalar el paquete correspondiente en el Arduino IDE. Aquí tienes una guía paso a paso:

1. En la ventana del **Administrador de Placas**, busca **pico**. Haz clic en el botón **Instalar** para comenzar la instalación. Esto instalará el paquete **Arduino Mbed OS RP2040 Boards**, que incluye soporte para el Raspberry Pi Pico W.

    .. image:: img/install_pico.png

2. Durante el proceso, aparecerán algunas ventanas emergentes solicitando la instalación de controladores específicos. Selecciona **"Instalar"**.

    .. image:: img/install_pico_sa.png

3. Al finalizar, recibirás una notificación indicando que la instalación se ha completado.

3. Selección de la Placa y el Puerto
----------------------------------------

1. Para seleccionar la placa adecuada, ve a **Herramientas** -> **Placa** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico**.

    .. image:: img/install_pico_tool_board.png

2. Si tu Raspberry Pi Pico W está conectado a la computadora, selecciona el puerto correcto yendo a **Herramientas** -> **Puerto**.

    .. image:: img/install_pico_tool_port.png

3. Arduino 2.0 ofrece una nueva función de selección rápida. Para el Raspberry Pi Pico W, que normalmente no se reconoce automáticamente, haz clic en **Seleccionar otra placa y puerto**.

    .. image:: img/install_pico_select.png

4. Escribe **Raspberry Pi Pico** en la barra de búsqueda, selecciónalo cuando aparezca, elige el puerto adecuado y haz clic en **OK**.

    .. image:: img/install_pico_board.png

5. Podrás volver a seleccionarlo fácilmente más adelante a través de esta ventana de acceso rápido.

    .. image:: img/install_pico_quick.png

6. Cualquiera de estos métodos te permitirá configurar correctamente la placa y el puerto. Ya estás listo para cargar código en el Raspberry Pi Pico W.

4. Cargar Código
---------------------

Ahora veamos cómo cargar código en tu Raspberry Pi Pico W.

1. Abre cualquier archivo ``.ino`` o usa el boceto en blanco que aparece. Luego, haz clic en el botón **Cargar**.

    .. image:: img/install_pico_upload.png

2. Espera a que aparezca el mensaje de carga, como se muestra a continuación.

    .. image:: img/install_pico_upload_dot.png

3. Mantén presionado el botón **BOOTSEL**, desconecta rápidamente tu Raspberry Pi Pico W y vuelve a conectarlo.

    .. image:: img/led_onboard.png 

    .. note::
        
        * Este paso es crucial, especialmente para los usuarios que usan el Arduino IDE por primera vez. Si omites este paso, la carga fallará.

        * Una vez que cargues el código con éxito, tu Pico W será reconocido por la computadora. En el futuro, simplemente conéctalo a la computadora.

4. Aparecerá un mensaje indicando que la carga se ha realizado con éxito.

    .. image:: img/install_pico_upload_done.png
