.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _projects_arduino:

Proyectos Arduino
======================

Esta sección introduce la programación con Arduino usando el Pico W, guiándote en el proceso de configurar el IDE de Arduino, instalar las bibliotecas necesarias y construir proyectos emocionantes. Con explicaciones detalladas y ejercicios prácticos, dominarás tanto la programación básica como avanzada de hardware basada en Arduino.

**Código Fuente**

* :download:`Kit SunFounder Kepler <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* O revisa el código en `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_


1. Primeros Pasos
------------------------
Configura el IDE de Arduino y prepárate para programar tu Pico W. Aprende cómo instalar el IDE, configurar la placa Pico W y agregar las bibliotecas esenciales para tus proyectos.  


.. toctree::
    :maxdepth: 1

    arduino_start/install_arduino_ide
    arduino_start/introduce_ide
    arduino_start/install_pico_w
    arduino_start/add_libraries_ar 

2. Salida e Entrada
-----------------------
Trabaja con LEDs, sensores y botones para aprender los fundamentos de controlar dispositivos de salida y recolectar datos del mundo físico. Estos ejercicios fundamentales establecerán una base sólida en la programación con Arduino.  

.. toctree::
    :maxdepth: 1

    ar_led
    ar_led_bar
    ar_fade
    ar_rgb
    ar_button
    ar_tilt
    ar_slide
    ar_micro
    ar_reed
    ar_pir
    ar_pot
    ar_photoresistor
    ar_temp
    ar_water
    ar_transistor
    ar_relay

3. Sonido, Pantalla y Movimiento
-------------------------------------
Explora cómo crear efectos de sonido, mostrar datos y controlar el movimiento. Este capítulo incluye proyectos con zumbadores, LEDs NeoPixel, pantallas LCD, motores, bombas y servos para dar vida a tu hardware.  

.. toctree::
    :maxdepth: 1

    ar_ac_buz
    ar_pa_buz
    ar_neopixel
    ar_lcd
    ar_motor
    ar_pump
    ar_servo


4. Controlador
---------------------
Utiliza controladores como joysticks, teclados y sensores táctiles para agregar funciones interactivas a tus proyectos. Aprende a procesar entradas de estos dispositivos y traducirlas en salidas creativas.  


.. toctree::
    :maxdepth: 1

    ar_joystick
    ar_keypad
    ar_mpr121

5. Microchip
---------------------
Descubre el poder de los registros de desplazamiento 74HC595 para un control avanzado de LEDs, pantallas de 7 segmentos y módulos de matriz de puntos. Este capítulo cubre técnicas eficientes para manejar múltiples salidas con menos pines.  

.. toctree::
    :maxdepth: 1

    ar_74hc595_led
    ar_74hc595_7seg
    ar_74hc595_4dig
    ar_74hc595_matrix

6. Avanzado
----------------
Adéntrate en módulos y conceptos avanzados, como la medición de distancia con ultrasonidos, sensores ambientales con DHT11, seguimiento de movimiento con MPU6050, y comunicación inalámbrica con RFID y controles remotos IR.  

.. toctree::
    :maxdepth: 1

    ar_ultrasonic
    ar_dht11
    ar_mpu6050
    ar_irremote
    ar_rfid
