.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_traffic_light:

7.6 Semáforo
=================

Un `Traffic Light <https://en.wikipedia.org/wiki/Traffic_light>`_ es un dispositivo de señalización ubicado en intersecciones, pasos peatonales y otros lugares, cuyo objetivo es regular el flujo de tráfico.

Las señales de tráfico están estandarizadas según la `Vienna Convention on Road Signs and Signals <https://en.wikipedia.org/wiki/Vienna_Convention_on_Road_Signs_and_Signals>`_. Estas señales alternan entre tres colores LED para indicar el paso.

* **Luz roja**: Indica a los conductores que deben detenerse, similar a una señal de alto.
* **Luz amarilla**: Una señal de advertencia de que la luz cambiará a roja. Este color tiene diferentes interpretaciones según el país o región.
* **Luz verde**: Permite el paso en la dirección indicada.

En este proyecto, utilizaremos tres LEDs de colores para simular el cambio de luces en un semáforo y un display de 7 segmentos de 4 dígitos para mostrar el tiempo de cada estado de tráfico.

**Componentes Necesarios**

Para este proyecto, necesitaremos los siguientes componentes. 

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
        - 7(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_led`
        - 3
        - |link_led_buy|

**Esquemático**

|sch_traffic_light|

* Este circuito se basa en el :ref:`py_74hc_4dig` y añade 3 LEDs.
* Los 3 LEDs de color rojo, amarillo y verde están conectados respectivamente a los pines GP7~GP9.

**Conexiones**

|wiring_traffic_light|

**Código**

.. note::

    * Abre el archivo ``7.6_traffic_light.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.
    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.
    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time
    from machine import Timer

    # Duración de cada color del semáforo en segundos [Verde, Amarillo, Rojo]
    lightTime = [30, 5, 30]

    # Códigos de 7 segmentos para los dígitos 0-9, en hexadecimal para representar segmentos LED
    SEGCODE = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]

    # Inicializar pines para la comunicación con el registro de desplazamiento (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Entrada de datos serie
    rclk = machine.Pin(19, machine.Pin.OUT)  # Reloj del registro (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Reloj del registro de desplazamiento

    # Inicializar lista para almacenar pines de control de 4 dígitos para el display de 7 segmentos
    placePin = []
    pin = [10, 13, 12, 11]  # Números de pines para el display de 4 dígitos
    for i in range(4):
        placePin.append(None)  # Reservar espacio en la lista
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Inicializar pines como salida

    # Función para seleccionar el dígito (0-3) que se mostrará, controlando los pines de ánodo común
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Apagar todos los dígitos
        placePin[digit].value(0)  # Encender el dígito seleccionado

    # Función para limpiar el display enviando '0x00' al registro de desplazamiento
    def clearDisplay():
        hc595_shift(0x00)

    # Función para enviar datos al registro de desplazamiento (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Bajar el latch para preparar el desplazamiento de datos
        time.sleep_us(200)  # Pequeño retraso para estabilidad de temporización
        for bit in range(7, -1, -1):  # Recorrer cada bit (MSB primero)
            srclk.low()  # Prepararse para enviar el siguiente bit
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extraer el bit actual de los datos
            sdi.value(value)  # Establecer el valor de la línea de datos en el bit actual
            time.sleep_us(200)
            srclk.high()  # Pulso del reloj de desplazamiento para almacenar el bit en el registro
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulso del reloj de registro para mover los datos a la salida

    # Función para mostrar un número en el display de 7 segmentos
    # Esta función descompone el número en sus dígitos individuales y los muestra
    def display(num):
        pickDigit(0)  # Seleccionar las unidades
        hc595_shift(SEGCODE[num % 10])  # Mostrar unidades

        pickDigit(1)  # Seleccionar las decenas
        hc595_shift(SEGCODE[num % 100 // 10])  # Mostrar decenas

        pickDigit(2)  # Seleccionar las centenas
        hc595_shift(SEGCODE[num % 1000 // 100])  # Mostrar centenas

        pickDigit(3)  # Seleccionar los millares
        hc595_shift(SEGCODE[num % 10000 // 1000])  # Mostrar millares

    # Configuración para LEDs del semáforo (Rojo, Amarillo, Verde)
    # LEDs conectados a pines 9 (Verde), 8 (Amarillo) y 7 (Rojo)
    pin = [7, 8, 9]  # Números de pines para LEDs
    led = []
    for i in range(3):
        led.append(None)  # Reservar espacio en la lista
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Inicializar cada pin como salida para LEDs

    # Función para encender el LED correcto según el estado actual
    # 0 = Verde, 1 = Amarillo, 2 = Rojo
    def lightup(state):
        for i in range(3):
            led[i].value(0)  # Apagar todos los LEDs
        led[state].value(1)  # Encender el LED seleccionado (Verde, Amarillo o Rojo)

    # Variables relacionadas con el temporizador
    counter = 0  # Contador para el tiempo restante
    color_state = 0  # Estado actual del semáforo (0 = Verde, 1 = Amarillo, 2 = Rojo)

    # Callback del temporizador para actualizar el estado del semáforo y el contador
    def time_count(ev):
        global counter, color_state
        counter -= 1  # Reducir el contador en 1 segundo
        if counter <= 0:  # Si el contador llega a cero, cambiar al siguiente color
            color_state = (color_state + 1) % 3  # Ciclar entre Verde, Amarillo y Rojo
            counter = lightTime[color_state]  # Reiniciar el contador según la duración del nuevo color

    # Inicializar un temporizador para llamar a la función time_count cada 1 segundo (1000ms)
    tim = Timer(period=1000, mode=Timer.PERIODIC, callback=time_count)

    # Bucle principal para actualizar el display de 7 segmentos y LEDs del semáforo
    while True:
        display(counter)  # Actualizar el display con el tiempo restante
        lightup(color_state)  # Actualizar los LEDs del semáforo según el color actual


Cuando el código se ejecute, el LED verde permanecerá encendido durante 30 segundos, el LED amarillo durante 5 segundos y el LED rojo durante 30 segundos.
