.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso exclusivo**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
========================

Arduino
---------------------

#. ¿Error al cargar el código en Arduino IDE?
    * Verifica que tu Pico esté reconocido correctamente en el IDE de Arduino; el puerto debería aparecer como COMXX (Raspberry Pi Pico). Para más instrucciones, consulta :ref:`setup_pico_arduino`.
    * Asegúrate de que la placa (Raspberry Pi Pico) o el puerto (COMXX (Raspberry Pi Pico)) estén seleccionados correctamente.
    * Si tu código es correcto y has seleccionado la placa y puerto adecuados, pero la carga aún no es exitosa, puedes hacer clic nuevamente en el icono de **Upload**. Cuando el progreso indique "Upload...", desconecta el cable USB, mantén presionado el botón **BOOTSEL** y vuelve a conectar el USB; el código debería cargarse correctamente.

MicroPython
------------------

#. ¿Cómo abrir y ejecutar el código?
    Para tutoriales detallados, consulta :ref:`open_run_code_py`.

#. ¿Cómo cargar una biblioteca en el Raspberry Pi Pico W?
    Para tutoriales detallados, consulta :ref:`add_libraries_py`.

#. ¿No aparece la opción de MicroPython (Raspberry Pi Pico W) en Thonny IDE?
    * Verifica que tu Pico W esté conectado a tu computadora mediante un cable USB.
    * Asegúrate de haber instalado MicroPython para el Pico W (:ref:`install_micropython_on_pico`).
    * El intérprete de Raspberry Pi Pico W solo está disponible en la versión 3.3.3 o superior de Thonny. Si tienes una versión anterior, actualízala (:ref:`thonny_ide`).
    * Si en este momento tienes el módulo cargador de Li-po en el protoboard, desconéctalo primero y luego vuelve a conectar el Pico W a la computadora.

#. ¿No puedes abrir o guardar el código del Pico W en Thonny IDE?
    * Verifica que tu Pico W esté conectado a tu computadora mediante un cable USB.
    * Asegúrate de haber seleccionado el intérprete como **MicroPython (Raspberry Pi Pico)**.

#. ¿Se puede usar el Raspberry Pi Pico W en Thonny y Arduino al mismo tiempo?
    NO, necesitas realizar algunas operaciones diferentes.

    * Si primero lo usaste en Arduino y ahora quieres usarlo en Thonny IDE, necesitas :ref:`install_micropython_on_pico`.
    * Si primero lo usaste en Thonny y ahora quieres usarlo en Arduino IDE, necesitas :ref:`setup_pico_arduino`.

#. Si tu computadora es Win7 y el Pico W no es detectado.
    * Descarga el controlador USB CDC desde http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver
    * Descomprime el archivo ``amtel_devices_cdc.inf`` en una carpeta llamada ``pico-serial``.
    * Cambia el nombre del archivo ``amtel_devices_cdc.inf`` a ``pico-serial.inf``.
    * Abre y edita ``pico-serial.inf`` en un editor básico como el bloc de notas.
    * Remueve y reemplaza las líneas bajo los siguientes encabezados:

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Cierra y guarda el archivo asegurándote de que mantenga el nombre pico-serial.inf.
    #. Ve a la lista de dispositivos de tu PC, encuentra el pico bajo Puertos, llamado algo como CDC Device. Un signo de exclamación amarillo lo indica.
    #. Haz clic derecho en el dispositivo CDC y actualiza o instala el controlador eligiendo el archivo creado en la ubicación en la que lo guardaste.

Piper Make
------------------

#. ¿Cómo configurar el Pico W en Piper Make?
    Para tutoriales detallados, consulta :ref:`per_setup_pico`.

#. ¿Cómo descargar o importar código?
    Para tutoriales detallados, consulta :ref:`per_save_import`.

#. ¿Cómo conectar el Pico W?
    Para tutoriales detallados, consulta :ref:`connect_pico_per`.

