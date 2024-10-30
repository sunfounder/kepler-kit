.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

1.5 Guía rápida de Thonny
==================================

.. _open_run_code_py:

Abrir y ejecutar código directamente
---------------------------------------------

La sección de código en los proyectos te indica exactamente qué código usar, así que haz doble clic en el archivo ``.py`` con el número de serie en la ruta ``kepler-kit-main/micropython/`` para abrirlo.

Sin embargo, primero debes descargar el paquete y cargar la biblioteca, como se describe en :ref:`add_libraries_py`.

#. Abrir código.

    Por ejemplo, ``2.1_hello_led.py``.

    Si haces doble clic sobre él, se abrirá una nueva ventana a la derecha. Puedes abrir más de un código al mismo tiempo.

    |open_code|

#. Selecciona el intérprete correcto

    Usa un cable micro USB para conectar el Pico W a tu computadora y selecciona el intérprete "MicroPython (Raspberry Pi Pico)".

    |sec_inter|

#. Ejecuta el código

    Para ejecutar el script, haz clic en el botón **Run current script** o presiona F5.

    |run_it|

    Si el código contiene alguna información que deba imprimirse, aparecerá en el Shell; de lo contrario, solo aparecerá la siguiente información.

    Haz clic en **View** -> **Edit** para abrir la ventana Shell si no aparece en tu Thonny.

        .. code-block::

            MicroPython vx.xx on xxxx-xx-xx; Raspberry Pi Pico W  With RP2040

            Type "help()" for more information.
            >>> %Run -c $EDITOR_CONTENT

    * La primera línea muestra la versión de MicroPython, la fecha y la información de tu dispositivo.
    * La segunda línea te indica que ingreses "help()" para obtener ayuda.
    * La tercera línea es un comando de Thonny que le indica al intérprete de MicroPython en tu Pico W que ejecute el contenido del área de scripts - "EDITOR_CONTENT".
    * Si aparece algún mensaje después de la tercera línea, generalmente es un mensaje que le pediste a MicroPython que imprimiera o un mensaje de error en el código.

#. Detener la ejecución

    |stop_it|

    Para detener el código en ejecución, haz clic en el botón **Stop/Restart backend**. El comando **%RUN -c $EDITOR_CONTENT** desaparecerá después de detenerse.

#. Guardar o guardar como

    Puedes guardar los cambios realizados en el ejemplo abierto presionando **Ctrl+S** o haciendo clic en el botón **Save** en Thonny.

    El código se puede guardar como un archivo separado en la Raspberry Pi Pico W haciendo clic en **File** -> **Save As**.

    |save_as|

    Selecciona **Raspberry Pi Pico**.

    |sec_pico|

    Luego haz clic en **OK** después de ingresar el nombre del archivo y la extensión **.py**. En la unidad Raspberry Pi Pico W, verás tu archivo guardado.

    |sec_name|

    .. note::
        Independientemente del nombre que le des a tu código, es mejor describir el tipo de código en lugar de usar un nombre sin sentido como ``abc.py``.
        Cuando guardas el código como ``main.py``, se ejecutará automáticamente al encender el dispositivo.


Crear archivo y ejecutarlo
-------------------------------


El código se muestra directamente en la sección de código. Puedes copiarlo en Thonny y ejecutarlo de la siguiente manera.

#. Crear un nuevo archivo

    Abre Thonny IDE y haz clic en el botón **New** para crear un nuevo archivo en blanco.

    |new_file|

#. Copia el código

    Copia el código del proyecto en el IDE de Thonny.

    |copy_file|

#. Selecciona el intérprete correcto

    Conecta el Pico W a tu computadora con un cable micro USB y selecciona el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    |sec_inter|

#. Ejecuta y guarda el código

    Haz clic en **Run Current Script** o simplemente presiona F5 para ejecutarlo. Si tu código no ha sido guardado, aparecerá una ventana preguntando si deseas guardarlo en **Esta computadora** o **Raspberry Pi Pico**.

    |where_save|

    .. note::
        Thonny guarda tu programa en la Raspberry Pi Pico W cuando se lo indicas, por lo que si desconectas el Pico W y lo conectas a otra computadora, tu programa permanecerá intacto.

    Haz clic en OK después de seleccionar la ubicación, nombrar el archivo y añadir la extensión **.py**.

    |sec_name|

    .. note::
        Independientemente del nombre que le des a tu código, es mejor describir el tipo de código en lugar de usar un nombre sin sentido como ``abc.py``.
        Cuando guardas el código como ``main.py``, se ejecutará automáticamente al encender el dispositivo.

    Una vez que tu programa esté guardado, se ejecutará automáticamente y verás la siguiente información en el área de Shell.

    Haz clic en **View** -> **Edit** para abrir la ventana Shell si no aparece en tu Thonny.

    .. code-block::

        MicroPython vx.xx.x on xxxx-xx-xx; Raspberry Pi Pico W With RP2040

        Type "help()" for more information.
        >>> %Run -c $EDITOR_CONTENT

    * La primera línea muestra la versión de MicroPython, la fecha y la información de tu dispositivo.
    * La segunda línea te indica que ingreses "help()" para obtener ayuda.
    * La tercera línea es un comando de Thonny que le indica al intérprete de MicroPython en tu Pico W que ejecute el contenido del área de scripts - "EDITOR_CONTENT".
    * Si aparece algún mensaje después de la tercera línea, generalmente es un mensaje que le pediste a MicroPython que imprimiera o un mensaje de error en el código.

#. Detener la ejecución

    |stop_it|

    Para detener el código en ejecución, haz clic en el botón **Stop/Restart backend**. El comando **%RUN -c $EDITOR_CONTENT** desaparecerá después de detenerse.

#. Abrir archivo

    Aquí tienes dos formas de abrir un archivo de código guardado.

    * La primera forma es hacer clic en el ícono de abrir en la barra de herramientas de Thonny. Como cuando guardas un programa, se te preguntará si deseas abrirlo desde **esta computadora** o **Raspberry Pi Pico**. Por ejemplo, haz clic en **Raspberry Pi Pico** y verás una lista de todos los programas que has guardado en el Pico W.
    * La segunda forma es abrir la vista previa del archivo directamente haciendo clic en **View**-> **File**-> y luego haciendo doble clic en el archivo ``.py`` correspondiente para abrirlo.
