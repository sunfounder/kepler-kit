.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_reversing_aid:

7.10 Ayuda de Reversa
========================

Este proyecto utiliza un LED, un zumbador y un módulo ultrasónico para crear un sistema de asistencia de reversa.
Podemos colocarlo en un coche de control remoto para simular el proceso real de estacionamiento en reversa en un garaje.


**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Zumbador Activo :ref:`cpn_buzzer`
        - 1
        -
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Diagrama**

|sch_reversing_aid|


**Conexiones**

|wiring_reversing_aid| 

**Código**

.. note::

    * Abre el archivo ``7.10_reversing_aid.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.



.. code-block:: python

    import machine
    import time

    # Inicializar los pines para el zumbador y el LED
    buzzer = machine.Pin(15, machine.Pin.OUT)  # Zumbador en el pin 15
    led = machine.Pin(14, machine.Pin.OUT)  # LED en el pin 14

    # Inicializar los pines para el sensor ultrasónico (HC-SR04)
    TRIG = machine.Pin(17, machine.Pin.OUT)  # Pin de disparo para el sensor ultrasónico
    ECHO = machine.Pin(16, machine.Pin.IN)  # Pin de eco para el sensor ultrasónico

    dis = 100  # Variable global para almacenar la distancia

    # Función para medir la distancia usando el sensor ultrasónico
    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()

        timeout_start = time.ticks_us()  # Usar microsegundos para mayor precisión
        
        # Esperar a que el pin ECHO pase a alto (inicio del pulso de eco)
        while not ECHO.value():
            if time.ticks_diff(time.ticks_us(), timeout_start) > 30000:  # Tiempo de espera de 30ms
                return -1  # Tiempo de espera agotado, retornar -1 si no se detecta pulso
        
        time1 = time.ticks_us()  # Tiempo de inicio para el cálculo de ancho de pulso
        
        # Esperar a que el pin ECHO pase a bajo (fin del pulso de eco)
        while ECHO.value():
            if time.ticks_diff(time.ticks_us(), time1) > 30000:  # Tiempo de espera de 30ms
                return -1  # Tiempo de espera agotado, retornar -1 si el pulso es demasiado largo
        
        time2 = time.ticks_us()  # Tiempo de fin para el cálculo de ancho de pulso
        
        # Calcular la distancia basada en la duración del pulso de eco
        during = time.ticks_diff(time2, time1)
        distance_cm = during * 340 / 2 / 10000  # Convertir tiempo a distancia en cm
        return distance_cm

    # Función para hacer sonar el zumbador y encender el LED
    def beep():
        buzzer.value(1)  # Encender el zumbador
        led.value(1)  # Encender el LED
        time.sleep(0.1)  # Duración del pitido
        buzzer.value(0)  # Apagar el zumbador
        led.value(0)  # Apagar el LED
        time.sleep(0.1)  # Breve pausa entre pitidos

    # Inicializar variables para controlar los intervalos de pitido
    intervals = 2000  # Intervalo largo inicial por defecto
    previousMillis = time.ticks_ms()  # Almacenar el tiempo anterior para controlar los intervalos de pitido

    # Bucle principal para manejar los intervalos de pitido según la distancia
    while True:
        dis = distance()  # Medir la distancia directamente en el bucle principal

        # Ajustar los intervalos de pitido en función de la distancia
        if dis > 0:  # Asegurarse de que se mida una distancia válida
            if dis <= 10:
                intervals = 300  # Distancia cercana, pitidos más rápidos
            elif dis <= 20:
                intervals = 500  # Distancia media-cercana, pitidos moderados
            elif dis <= 50:
                intervals = 1000  # Distancia media, pitidos más lentos
            else:
                intervals = 2000  # Distancia lejana, pitidos mucho más lentos

            # Imprimir la distancia medida
            print(f'Distance: {dis:.2f} cm')
            
            # Verificar si es momento de pitido según el intervalo
            currentMillis = time.ticks_ms()  # Obtener el tiempo actual
            if time.ticks_diff(currentMillis, previousMillis) >= intervals:
                beep()  # Emitir el pitido y parpadear el LED
                previousMillis = currentMillis  # Actualizar el tiempo del último pitido
            
        time.sleep_ms(100)  # Pequeña pausa para evitar lecturas demasiado frecuentes


* Al ejecutar el programa, el sensor ultrasónico leerá continuamente la distancia al obstáculo frente a él, y podrás ver el valor exacto de la distancia en el shell.
* El LED y el zumbador cambiarán la frecuencia de parpadeo y pitido según el valor de la distancia, indicando así la cercanía del obstáculo.
* En el artículo :ref:`py_ultrasonic` se mencionó que cuando el sensor ultrasónico funciona, el programa se pausa.
* Para evitar interferir con el tiempo del LED o el zumbador, hemos creado un hilo separado para la medición de distancia en este ejemplo.
