.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

1.1 Introducción a MicroPython
======================================

MicroPython es una implementación de software de un lenguaje de programación en gran medida compatible con Python 3, escrito en C y optimizado para ejecutarse en microcontroladores.

MicroPython incluye un compilador de Python a bytecode y un intérprete de ese bytecode en tiempo de ejecución. Ofrece al usuario un prompt interactivo (REPL) para ejecutar comandos compatibles de forma inmediata. Además, incorpora una selección de bibliotecas esenciales de Python y módulos que proporcionan acceso a nivel bajo de hardware.

* Referencia: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

La historia comienza aquí
--------------------------------

Las cosas cambiaron en 2013, cuando Damien George lanzó una campaña de financiamiento (Kickstarter).

Damien era estudiante de pregrado en la Universidad de Cambridge y un apasionado programador de robótica. Su objetivo era reducir el entorno de Python de una máquina en gigabytes a una en kilobytes. Su campaña en Kickstarter fue para respaldar su desarrollo mientras convertía su prueba de concepto en una implementación terminada.

MicroPython cuenta con el respaldo de una comunidad diversa de Pythonistas comprometidos con el éxito del proyecto.

Además de probar y apoyar la base de código, los desarrolladores han proporcionado tutoriales, bibliotecas de código y adaptaciones para hardware, permitiendo a Damien centrarse en otros aspectos del proyecto.

* Referencia: `realpython <https://realpython.com/micropython/>`_

¿Por qué MicroPython?
---------------------------

Aunque la campaña original en Kickstarter lanzó MicroPython como una placa de desarrollo "pyboard" con STM32F4, MicroPython es compatible con muchas arquitecturas de productos basados en ARM. Los puertos principales soportados incluyen ARM Cortex-M (varias placas STM32, TI CC3200/WiPy, placas Teensy, la serie Nordic nRF, SAMD21 y SAMD51), ESP8266, ESP32, PIC de 16 bits, Unix, Windows, Zephyr y JavaScript.

En segundo lugar, MicroPython permite una retroalimentación rápida. Esto es posible porque puedes usar REPL para ingresar comandos de manera interactiva y obtener respuestas inmediatas. Incluso puedes ajustar el código y ejecutarlo de inmediato en lugar de seguir el ciclo de escribir-compilar-subir-ejecutar.

Si bien Python tiene las mismas ventajas, algunas placas de microcontroladores, como la Raspberry Pi Pico, son pequeñas, simples y tienen poca memoria para ejecutar Python en su totalidad. Es por eso que MicroPython ha evolucionado, conservando las principales características de Python y agregando nuevas funcionalidades para trabajar con estas placas de microcontroladores.

A continuación, aprenderás a instalar MicroPython en la Raspberry Pi Pico.

* Referencia: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* Referencia: `realpython <https://realpython.com/micropython/>`_
