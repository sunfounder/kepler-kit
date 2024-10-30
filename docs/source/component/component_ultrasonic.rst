.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_ultrasonic:

Módulo Ultrasónico
================================

|ultrasonic_pic|

* **TRIG**: Entrada de Pulso de Disparo
* **ECHO**: Salida de Pulso de Eco
* **GND**: Tierra
* **VCC**: Suministro de 5V

Este es el sensor de distancia ultrasónico HC-SR04, que proporciona mediciones sin contacto desde 2 cm hasta 400 cm con una precisión de hasta 3 mm. El módulo incluye un transmisor ultrasónico, un receptor y un circuito de control.

Solo necesitas conectar 4 pines: VCC (alimentación), Trig (disparo), Echo (recepción) y GND (tierra) para que sea fácil de usar en tus proyectos de medición.

**Características**

* Voltaje de funcionamiento: DC5V
* Corriente de trabajo: 16mA
* Frecuencia de trabajo: 40Hz
* Rango máximo: 500cm
* Rango mínimo: 2cm
* Señal de entrada de disparo: pulso TTL de 10uS
* Señal de salida de eco: señal de nivel TTL de entrada proporcional al rango
* Conector: XH2.54-4P
* Dimensiones: 46x20.5x15 mm

**Principio**

Los principios básicos son los siguientes:

* Usar IO para disparar una señal de nivel alto de al menos 10us.

* El módulo envía una ráfaga de 8 ciclos de ultrasonido a 40 kHz y detecta si se recibe una señal de pulso.

* El eco generará una salida de nivel alto si se devuelve una señal; la duración del nivel alto es el tiempo desde la emisión hasta el retorno.

* Distancia = (tiempo de nivel alto x velocidad del sonido (340M/S)) / 2

|ultrasonic_prin|

Fórmula:

* us / 58 = distancia en centímetros
* us / 148 = distancia en pulgadas
* distancia = tiempo de nivel alto x velocidad (340M/S) / 2

.. note::

    Este módulo no debe conectarse cuando se enciende, si es necesario, deja que el GND del módulo se conecte primero. De lo contrario, afectará el funcionamiento del módulo.

    El área del objeto a medir debe ser de al menos 0.5 metros cuadrados y lo más plana posible. De lo contrario, afectará los resultados.


**Example**

* :ref:`py_ultrasonic` (Para usuarios de MicroPython)
* :ref:`py_reversing_aid` (Para usuarios de MicroPython)
* :ref:`ar_ultrasonic` (Para usuarios de Arduino)
* :ref:`per_reversing_system` (Para usuarios de Piper Make)
