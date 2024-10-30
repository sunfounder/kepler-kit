.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_arduino:

1.1 Instalar Arduino IDE (Importante)
==========================================

El Arduino IDE, conocido como Entorno de Desarrollo Integrado de Arduino, proporciona todo el soporte de software necesario para completar un proyecto con Arduino. Es un software de programación diseñado específicamente para Arduino, creado por el equipo de Arduino, que nos permite escribir programas y cargarlos en la placa Arduino.

El Arduino IDE 2.0 es un proyecto de código abierto. Representa un gran avance respecto a su sólido predecesor, Arduino IDE 1.x, y cuenta con una interfaz renovada, mejoras en el gestor de placas y librerías, depurador, autocompletado y mucho más.

En este tutorial, mostraremos cómo descargar e instalar el Arduino IDE 2.0 en tu computadora con Windows, Mac o Linux.

Requisitos
-------------------

* Windows - Win 10 y versiones más recientes, 64 bits
* Linux - 64 bits
* Mac OS X - Versión 10.14: "Mojave" o más reciente, 64 bits

Descargar el Arduino IDE 2.0
----------------------------

#. Visita la página de |link_download_arduino|.

#. Descarga el IDE para la versión de tu sistema operativo.

    .. image:: img/sp_001.png

Instalación
------------------------------

Windows
^^^^^^^^^^^^^

#. Haz doble clic en el archivo ``arduino-ide_xxxx.exe`` para ejecutar el archivo descargado.

#. Lee el acuerdo de licencia y acéptalo.

    .. image:: img/sp_002.png

#. Elige las opciones de instalación.

    .. image:: img/sp_003.png

#. Selecciona la ubicación de instalación. Se recomienda instalar el software en una unidad diferente a la unidad del sistema.

    .. image:: img/sp_004.png

#. Luego haz clic en Finalizar.

    .. image:: img/sp_005.png

macOS
^^^^^^^^^^^^^^^^

Haz doble clic en el archivo descargado ``arduino_ide_xxxx.dmg`` y sigue las instrucciones para copiar la **Arduino IDE.app** a la carpeta **Aplicaciones**. Verás que el Arduino IDE se instala correctamente en unos segundos.

.. image:: img/macos_install_ide.png
    :width: 800

Linux
^^^^^^^^^^^^

Para el tutorial de instalación del Arduino IDE 2.0 en un sistema Linux, consulta: https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux


Abrir el IDE
-----------------

#. Al abrir Arduino IDE 2.0 por primera vez, se instalarán automáticamente las placas Arduino AVR, las librerías integradas y otros archivos necesarios.

    .. image:: img/sp_901.png

#. Además, es posible que tu firewall o centro de seguridad muestre ventanas emergentes pidiéndote instalar algunos controladores de dispositivos. Por favor, instala todos ellos.

    .. image:: img/sp_104.png

#. ¡Ahora tu Arduino IDE está listo!

    .. note::
        En caso de que alguna instalación no se haya completado debido a problemas de red u otras razones, puedes volver a abrir el Arduino IDE y finalizará el resto de la instalación. La ventana de Salida no se abrirá automáticamente después de que todas las instalaciones estén completas, a menos que hagas clic en Verificar o Subir.
