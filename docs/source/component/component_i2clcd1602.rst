.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_i2c_lcd:

I2C LCD1602
==============

|i2c_lcd1602|

* **GND**: Tierra
* **VCC**: Fuente de voltaje, 5V.
* **SDA**: Línea de datos en serie. Conectar a VCC a través de una resistencia pull-up.
* **SCL**: Línea de reloj en serie. Conectar a VCC a través de una resistencia pull-up.

Como todos sabemos, aunque las pantallas LCD y otras similares mejoran enormemente la interacción hombre-máquina, comparten una debilidad común. Al conectarse a un controlador, ocupan múltiples pines de IO del controlador, que no siempre cuenta con suficientes puertos externos. Esto también limita otras funciones del controlador.

Por esta razón, se desarrolló el LCD1602 con un módulo I2C para solucionar el problema. El módulo I2C tiene un chip integrado PCF8574 que convierte datos seriales I2C en datos paralelos para la pantalla LCD.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**Dirección I2C**

La dirección por defecto es generalmente 0x27, aunque en algunos casos puede ser 0x3F.

Tomando la dirección por defecto 0x27 como ejemplo, la dirección del dispositivo puede modificarse cortocircuitando las almohadillas A0/A1/A2; en el estado por defecto, A0/A1/A2 es 1, y si se cortocircuita la almohadilla, A0/A1/A2 será 0.

|i2c_address|

**Retroiluminación/Contraste**

La retroiluminación se puede habilitar mediante un capuchón de puente; para deshabilitarla, simplemente retira el capuchón. El potenciómetro azul en la parte posterior se utiliza para ajustar el contraste (la relación de brillo entre el blanco más brillante y el negro más oscuro).

|back_lcd1602|

* **Capuchón de puente**: La retroiluminación se puede habilitar con este capuchón; retíralo para deshabilitar la retroiluminación.
* **Potenciómetro**: Se utiliza para ajustar el contraste (la claridad del texto mostrado), aumentando en sentido horario y disminuyendo en sentido antihorario.




**Ejemplos**

* :ref:`py_lcd` (Para usuarios de MicroPython)
* :ref:`py_room_temp` (Para usuarios de MicroPython)
* :ref:`py_guess_number` (Para usuarios de MicroPython)
* :ref:`ar_lcd` (Para usuarios de Arduino)
