.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _projects_micropython:

Proyectos MicroPython
======================

En esta sección, explorarás los fundamentos de MicroPython, desde su historia hasta la instalación en el Pico W. También te sumergirás en la sintaxis básica y trabajarás en numerosos proyectos prácticos diseñados para ayudarte a dominar MicroPython paso a paso.

Recomendamos leer los capítulos en orden para maximizar tu experiencia de aprendizaje.  


**Código Fuente**

* :download:`Kit SunFounder Kepler <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* O revisa el código en `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_


1. Primeros Pasos
------------------------
Aprende los conceptos básicos de MicroPython y configura tu entorno de desarrollo, incluyendo la instalación de Thonny, la carga de MicroPython en el Pico W y la exploración de su sintaxis básica.  


.. toctree::
    :maxdepth: 1


    python_start/introduction_micropython
    python_start/install_thonny
    python_start/install_micropython_to_pico
    python_start/upload_libraries
    python_start/quick_guide_thonny
    python_start/syntax/micropython_basic_syntax



2. Salida e Entrada
----------------------
Descubre cómo trabajar con dispositivos de salida como LEDs y dispositivos de entrada como botones y sensores. Este capítulo introduce los fundamentos de la computación física con proyectos prácticos.  


.. toctree::
    :maxdepth: 1

    py_led
    py_led_bar
    py_fade
    py_rgb
    py_button
    py_tilt
    py_slide
    py_micro
    py_reed
    py_pir
    py_pot
    py_photoresistor
    py_temp
    py_water
    py_transistor
    py_relay

3. Sonido, Pantalla y Movimiento
--------------------------------------
Domina módulos como zumbadores, LEDs NeoPixel, pantallas LCD y actuadores como motores, bombas y servos. Crea proyectos interactivos que produzcan sonido, visuales y movimiento.  

.. toctree::
    :maxdepth: 1

    py_ac_buz
    py_pa_buz
    py_neopixel
    py_lcd
    py_motor
    py_pump
    py_servo

4. Controlador
----------------------
Aprende cómo usar controladores como joysticks, teclados y sensores táctiles para agregar interactividad y complejidad a tus proyectos.  

.. toctree::
    :maxdepth: 1

    py_joystick
    py_keypad
    py_mpr121

5. Microchip
--------------
Sumérgete en proyectos basados en microchips usando registros de desplazamiento 74HC595. Controla LEDs, pantallas de 7 segmentos, matrices de puntos y más con técnicas avanzadas.  

.. toctree::
    :maxdepth: 1

    py_74hc595_led
    py_74hc595_7seg
    py_74hc595_4dig
    py_74hc595_matrix

6. Avanzado
--------------------
Lleva tus proyectos al siguiente nivel con componentes avanzados como sensores ultrasónicos, módulos de temperatura y humedad DHT11, giroscopios MPU6050 y lectores RFID.  


.. toctree::
    :maxdepth: 1

    py_ultrasonic
    py_dht11
    py_mpu6050
    py_irremote
    py_rfid

7. Proyectos Divertidos
----------------------------

Pon tus habilidades en práctica construyendo aplicaciones emocionantes y del mundo real como theremins de luz, contadores de pasajeros, reproductores de música RFID y controladores somatosensoriales. Estos proyectos son tanto divertidos como educativos.  


.. toctree::
    :maxdepth: 1

    py_light_theremin
    py_room_temp_meter
    py_alarm_siren_lamp
    py_passenger_counter
    py_game_10_second
    py_traffic_light
    py_game_guess_number
    py_rfid_music_player
    py_fruit_piano
    py_reversing_aid
    py_somatosensory_controller
    py_digital_bubble_level

8. Proyectos IoT
------------------------
Conecta tu Pico W a internet y explora el mundo del IoT (Internet de las Cosas). Construye proyectos como CheerLights, monitores de clima, sistemas de comunicación basados en MQTT e incluso un sistema de monitoreo de plantas.  

.. toctree::
    :maxdepth: 1

    iotproject/1.access
    iotproject/2.cheerlight
    iotproject/3.ifttt_mail
    iotproject/4.openweather
    iotproject/5.mqtt_pub
    iotproject/6.mqtt_sub
    iotproject/7.web_page
    iotproject/8.anvil
    iotproject/9.sunfounder_controller
    iotproject/10.plant_monitor
