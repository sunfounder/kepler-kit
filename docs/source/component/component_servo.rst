.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_servo:

Servo
===========

|img_servo|

Un servo generalmente está compuesto por las siguientes partes: carcasa, eje, sistema de engranajes, potenciómetro, motor de corriente continua (DC) y una placa embebida.

Funciona de la siguiente manera: el microcontrolador envía señales PWM al servo, y la placa embebida en el servo recibe las señales a través del pin de señal y controla el motor interno para girar. Como resultado, el motor impulsa el sistema de engranajes y luego mueve el eje después de la desaceleración. El eje y el potenciómetro del servo están conectados. Cuando el eje gira, impulsa al potenciómetro, por lo que el potenciómetro envía una señal de voltaje a la placa embebida. Luego, la placa determina la dirección y la velocidad de rotación en función de la posición actual, permitiendo detenerse exactamente en la posición definida y mantenerse allí.

|img_servo_i|

El ángulo se determina por la duración de un pulso que se aplica al cable de control, lo que se llama Modulación por Ancho de Pulso (PWM). El servo espera recibir un pulso cada 20 ms. La longitud del pulso determinará cuánto gira el motor. Por ejemplo, un pulso de 1.5 ms hará que el motor gire a la posición de 90 grados (posición neutral).
Cuando se envía un pulso al servo de menos de 1.5 ms, el servo gira a una posición y mantiene su eje de salida a ciertos grados en sentido antihorario desde el punto neutral. Cuando el pulso es mayor a 1.5 ms, ocurre lo contrario. La amplitud mínima y máxima del pulso que hará que el servo gire a una posición válida varía en cada servo. Generalmente, el pulso mínimo será de aproximadamente 0.5 ms y el pulso máximo será de 2.5 ms.

|img_servo_duty|

.. Example
.. -------------------

.. :ref:`Swinging Servo`

**Ejemplos**

* :ref:`py_servo` (Para usuarios de MicroPython)
* :ref:`py_somato_controller` (Para usuarios de MicroPython)
* :ref:`ar_servo` (Para usuarios de Arduino)
* :ref:`per_water_tank` (Para usuarios de Piper Make)
* :ref:`per_swing_servo` (Para usuarios de Piper Make)
* :ref:`per_lucky_cat` (Para usuarios de Piper Make)
