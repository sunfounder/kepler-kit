.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en temas avanzados sobre Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_light_theremin:

7.1 Theremin de Luz
=========================

El theremin es un instrumento musical electrónico que no requiere contacto físico. Según la posición de la mano del jugador, produce diferentes tonos.

La sección de control suele estar compuesta por dos antenas metálicas que detectan la posición de las manos del thereminista, controlando un oscilador con una mano y el volumen con la otra. Las señales eléctricas del theremin se amplifican y se envían a un altavoz.

No podemos reproducir el mismo instrumento con el Pico W, pero podemos usar una fotorresistencia y un zumbador pasivo para lograr un efecto de juego similar.

* `Theremin - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Zumbador Pasivo :ref:`cpn_buzzer`
        - 1
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Esquema**

|sch_light_theremin|

Antes de comenzar el proyecto, mueve tu mano arriba y abajo sobre la fotorresistencia para calibrar el rango de intensidad de luz. El LED conectado en GP16 indica el tiempo de calibración: se encenderá al inicio y se apagará al finalizar.

Cuando GP15 emite un nivel alto, el S8050 (transistor NPN) conduce y el zumbador pasivo comienza a sonar.

Cuando la luz es más intensa, el valor de GP28 es menor; y viceversa, cuando la luz es más tenue, el valor es mayor.
Mediante programación, el valor de la fotorresistencia afecta la frecuencia del zumbador pasivo, creando un dispositivo fotosensible.


**Conexiones**

|wiring_light_theremin|


**Código**

.. note::

    * Abre el archivo ``7.1_light_theremin.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # Inicializar LED, fotorresistencia y zumbador
    led = machine.Pin(16, machine.Pin.OUT)  # LED en pin 16
    photoresistor = machine.ADC(28)  # Fotorresistencia en pin ADC 28
    buzzer = machine.PWM(machine.Pin(15))  # Zumbador en pin 15 con PWM

    # Variables para almacenar las lecturas de luz más altas y más bajas para calibración
    light_low = 65535 
    light_high = 0 

    # Función para mapear un rango de valores a otro
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Función para reproducir un tono en el zumbador a una frecuencia y duración específicas
    def tone(pin, frequency, duration):
        pin.freq(frequency)  # Establecer frecuencia del zumbador
        pin.duty_u16(30000)  # Fijar ciclo de trabajo al 50%
        utime.sleep_ms(duration)  # Reproducir el tono durante la duración especificada
        pin.duty_u16(0)  # Apagar el tono estableciendo el ciclo de trabajo a 0

    # Calibrar la fotorresistencia encontrando los valores de luz más altos y más bajos durante 5 segundos
    timer_init_start = utime.ticks_ms()  # Obtener el tiempo actual (inicio)
    led.value(1)  # Encender el LED para indicar que la calibración está en progreso
    while utime.ticks_diff(utime.ticks_ms(), timer_init_start) < 5000:  # Ejecutar calibración por 5 segundos
        light_value = photoresistor.read_u16()  # Leer el valor de luz de la fotorresistencia
        if light_value > light_high:  # Registrar el valor máximo de luz
            light_high = light_value
        if light_value < light_low:  # Registrar el valor mínimo de luz
            light_low = light_value
    led.value(0)  # Apagar el LED después de la calibración

    # Bucle principal para leer los niveles de luz y reproducir los tonos correspondientes
    while True:
        light_value = photoresistor.read_u16()  # Leer el valor actual de luz de la fotorresistencia
        pitch = int(interval_mapping(light_value, light_low, light_high, 50, 6000))  # Mapear el valor de luz a un rango de tonos
        if pitch > 50:  # Reproducir tonos solo si el tono está por encima de un umbral mínimo
            tone(buzzer, pitch, 20)  # Reproducir el tono correspondiente por 20ms
        utime.sleep_ms(10)  # Pequeña pausa entre lecturas

Tan pronto como el programa se ejecute, el LED se encenderá, y tendremos cinco segundos para calibrar el rango de detección de la fotorresistencia.

Esto se debe a que los entornos de luz pueden variar (por ejemplo, la intensidad de luz al mediodía y al anochecer), así como la altura de la mano sobre la fotorresistencia. Necesitas establecer la altura máxima y mínima de tu mano desde la fotorresistencia, que también es la altura a la que “tocas” el instrumento.

Después de cinco segundos, el LED se apagará, y podremos mover la mano sobre la fotorresistencia y tocar.
