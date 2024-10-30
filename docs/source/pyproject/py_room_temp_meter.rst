.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_room_temp:

7.2 Medidor de Temperatura Ambiental
=========================================

Utilizando un termistor y una pantalla LCD1602 I2C, podemos crear un medidor de temperatura ambiental.

Este proyecto es muy sencillo y se basa en :ref:`py_temp`, añadiendo la pantalla LCD1602 para mostrar la temperatura.


**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

Es muy conveniente adquirir un kit completo; aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE	
        - CANTIDAD
        - ENLACE

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cable Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Varios
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Esquemático**

|sch_room_temp|

**Conexiones**

|wiring_room_temp|

**Código**

.. note::

    * Abre el archivo ``7.2_room_temperature_meter.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import math

    # Inicializar el termistor (ADC en el pin 28) y la pantalla LCD
    thermistor = machine.ADC(28)  # Entrada analógica del termistor

    # Inicializar comunicación I2C para la pantalla LCD1602
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Crear un objeto LCD para controlar la pantalla LCD1602
    lcd = LCD(i2c)

    # Bucle principal para leer y mostrar la temperatura continuamente
    while True:
        # Leer el valor ADC en bruto del termistor
        temperature_value = thermistor.read_u16()

        # Convertir el valor ADC a un voltaje (rango 0-3.3V)
        Vr = 3.3 * float(temperature_value) / 65535  # Conversión de valor ADC a voltaje

        # Calcular la resistencia del termistor (usando un divisor de voltaje con una resistencia de 10kOhm)
        Rt = 10000 * Vr / (3.3 - Vr)  # Rt = resistencia del termistor

        # Usar la ecuación de Steinhart-Hart para calcular la temperatura en Kelvin
        # Los valores utilizados son específicos del termistor (3950 es el coeficiente beta)
        temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))  # Temperatura en Kelvin

        # Convertir la temperatura de Kelvin a Celsius
        Cel = temp - 273.15

        # Mostrar la temperatura en la pantalla LCD en grados Celsius
 string = " Temperature is \n    " + str('{:.2f}'.format(Cel)) + " C"  # Format string for the LCD
        lcd.message(string)  # Mostrar la cadena en la LCD

        utime.sleep(1)  # Esperar 1 segundo
        lcd.clear()  # Limpiar la LCD para la siguiente lectura

La pantalla LCD mostrará el valor de la temperatura en el ambiente actual después de que el programa se ejecute.

.. note:: 
    Si el código y las conexiones están correctas, pero la pantalla LCD aún no muestra contenido, ajusta el potenciómetro en la parte posterior para aumentar el contraste.
