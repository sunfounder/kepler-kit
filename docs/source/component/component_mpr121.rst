.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_mpr121:

Módulo MPR121
===========================

|img_mpr121|

* **3.3V**: Fuente de alimentación
* **IRQ**: Pin de salida de interrupción con colector abierto, activo bajo
* **SCL**: Reloj I2C
* **SDA**: Datos I2C
* **ADD**: Pin de selección de dirección I2C. Conecta el pin ADDR a VSS, VDD, SDA o SCL; las direcciones I2C resultantes son 0x5A, 0x5B, 0x5C y 0x5D respectivamente.
* **GND**: Tierra
* **0~11**: Electrodos 0~11, los electrodos son sensores táctiles. Normalmente, los electrodos pueden ser simplemente un pedazo de metal o un cable. Sin embargo, dependiendo de la longitud del cable o del material del electrodo, la detección puede ser complicada. Por esta razón, el MPR121 permite configurar lo que se necesita para activar y desactivar un electrodo.

**VISIÓN GENERAL DEL MPR121**

El MPR121 es la segunda generación de controladores de sensores táctiles 
capacitivos tras el lanzamiento inicial de la serie MPR03x. El MPR121 
incluye mejoras significativas, como un mayor número de electrodos, una 
dirección I2C configurable por hardware, un sistema de filtrado ampliado 
con debounce y electrodos completamente independientes con autoconfiguración 
integrada. El dispositivo también cuenta con un 13º canal de detección 
simulado dedicado para la detección de proximidad cercana utilizando las 
entradas de detección multiplexadas.

* `MPR121 Datasheet <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Características**

* Operación de bajo consumo
    • Operación de suministro de 1.71 V a 3.6 V
    • Corriente de suministro de 29 μA a un intervalo de muestreo de 16 ms
    • Corriente de 3 μA en modo de parada
* 12 entradas de detección capacitiva
    • 8 entradas son multifuncionales para controladores LED y GPIO
* Detección táctil completa
    • Autoconfiguración para cada entrada de detección
    • Autocalibración para cada entrada de detección
    • Umbral de toque/liberación y debounce para la detección táctil
* Interfaz I2C, con salida de interrupción
* Paquete QFN de 20 pines de 3 mm x 3 mm x 0.65 mm
* Rango de temperatura de operación: -40°C a +85°C

**Ejemplos**

* :ref:`py_mpr121` (Para usuarios de MicroPython)
* :ref:`py_fruit_piano` (Para usuarios de MicroPython)
* :ref:`ar_mpr121` (Para usuarios de Arduino)
