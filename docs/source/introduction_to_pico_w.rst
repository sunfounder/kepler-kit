.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso exclusivo**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!
.. _cpn_pico_w:

Conociendo el Pico W
=======================================

|pico_w_side|

El Raspberry Pi Pico W añade conectividad inalámbrica a la exitosa línea de 
productos Raspberry Pi Pico. Construido en torno a nuestra plataforma de silicio 
RP2040, los productos Pico aportan nuestros valores distintivos de alto rendimiento, 
bajo costo y facilidad de uso al espacio de los microcontroladores.

El Raspberry Pi Pico W ofrece soporte para LAN inalámbrica 802.11 b/g/n de 2.4GHz, 
con una antena integrada y certificación de cumplimiento modular. Puede operar 
tanto en modo estación como en modo punto de acceso. El acceso completo a la 
funcionalidad de red está disponible tanto para desarrolladores de C como de 
MicroPython. El Raspberry Pi Pico W combina el RP2040 con 2MB de memoria flash y 
un chip de alimentación que soporta voltajes de entrada de 1.8 a 5.5V. Proporciona 
26 pines GPIO, tres de los cuales pueden funcionar como entradas analógicas, con pads pasantes 
de 0.1” de separación y bordes acastillados. El Raspberry Pi Pico W está disponible como unidad 
individual o en bobinas de 480 unidades para ensamblaje automatizado.

**Características**

* Formato de 21 mm x 51 mm
* Chip microcontrolador RP2040 diseñado por Raspberry Pi en el Reino Unido
* Procesador de doble núcleo Arm Cortex-M0+, con reloj flexible que funciona hasta 133 MHz
* 264 kB de SRAM en chip
* 2 MB de flash QSPI en placa
* LAN inalámbrica 802.11n de 2.4GHz
* 26 pines GPIO multifuncionales, incluyendo 3 entradas analógicas
* 2 x UART, 2 x controladores SPI, 2 x controladores I2C, 16 x canales PWM
* 1 x controlador y PHY USB 1.1, con soporte para host y dispositivo
* 8 x máquinas de estado PIO (I/O programable) para soporte de periféricos personalizados
* Voltaje de entrada soportado de 1.8-5.5V CC
* Temperatura de operación de -20°C a +70°C
* Módulo acastillado que permite soldar directamente a placas portadoras
* Programación por arrastre y caída utilizando almacenamiento masivo a través de USB
* Modos de bajo consumo y reposo
* Reloj interno preciso
* Sensor de temperatura
* Bibliotecas de enteros y punto flotante aceleradas en chip

**Pines de Pico**

|pico_pin|

.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - Nombre
        - Descripción
        - Función
    *   - GP0-GP28
        - Pines de entrada/salida de uso general
        - Actúan como entrada o salida y no tienen un propósito fijo.
    *   - GND
        - Tierra a 0 voltios
        - Varios pines GND alrededor del Pico W para facilitar el cableado.
    *   - RUN
        - Habilita o deshabilita tu Pico
        - Inicia y detiene tu Pico W desde otro microcontrolador.
    *   - GPxx_ADCx
        - Entrada/salida de uso general o entrada analógica
        - Se utiliza como entrada analógica así como entrada o salida digital, pero no ambas al mismo tiempo.
    *   - ADC_VREF
        - Referencia de voltaje para el convertidor analógico-digital (ADC)
        - Un pin de entrada especial que establece un voltaje de referencia para cualquier entrada analógica.
    *   - AGND
        - Tierra a 0 voltios para el convertidor analógico-digital (ADC)
        - Una conexión a tierra especial para usar con el pin ADC_VREF.
    *   - 3V3(O)
        - Alimentación de 3.3 voltios
        - Una fuente de energía de 3.3V, el mismo voltaje que utiliza tu Pico W internamente, generado a partir de la entrada VSYS.
    *   - 3v3(E)
        - Habilita o deshabilita la alimentación
        - Enciende o apaga la alimentación de 3V3(O), también puede apagar tu Pico W.
    *   - VSYS
        - Alimentación de 2-5 voltios
        - Un pin conectado directamente a la fuente de alimentación interna del Pico, que no se puede apagar sin también apagar el Pico W.
    *   - VBUS
        - Alimentación de 5 voltios
        - Una fuente de alimentación de 5 V tomada del puerto micro USB de tu Pico, y utilizada para alimentar hardware que necesita más de 3.3 V.

El mejor lugar para encontrar todo lo que necesitas para comenzar con tu Raspberry Pi Pico W es `aquí <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`_

O puedes hacer clic en los siguientes enlaces:

* `Raspberry Pi Pico W product brief <https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf>`_
* `Raspberry Pi Pico W datasheet <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf>`_
* `Getting started with Raspberry Pi Pico: C/C++ development <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `API-level Doxygen documentation for the Raspberry Pi Pico C/C++ SDK <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2040 datasheet <https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf>`_
* `Hardware design with RP2040 <https://datasheets.raspberrypi.org/rp2040/hardware-design-with-rp2040.pdf>`_
* `Raspberry Pi Pico W design files <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEP file <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
