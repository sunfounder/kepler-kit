.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_fruit_piano:

7.9 Piano de Frutas
==========================

La conductividad eléctrica se encuentra en muchos objetos metálicos, así como en el cuerpo humano y en las frutas.
Podemos aprovechar esta propiedad para crear un proyecto divertido: un piano de frutas.
Es decir, convertimos frutas en teclas de un teclado que pueden tocar música simplemente al tocarlas.

|fruit_piano|

**Componentes Requeridos**

En este proyecto, necesitamos los siguientes componentes. 

Es conveniente adquirir un kit completo; aquí tienes el enlace:

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

    *   - N.º
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
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - Buzzer :ref:`cpn_buzzer` Pasivo
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**Esquema**

|sch_fruit_piano|

Para convertir la fruta en una tecla de piano, necesitas conectar los electrodos del MPR121 a la fruta (por ejemplo, a la cáscara de un plátano).

Al inicio, el MPR121 se inicializa y cada electrodo recibe un valor basado en la carga actual. Cuando un conductor (como el cuerpo humano) toca un electrodo, la carga cambia y se reequilibra.
Como resultado, el valor del electrodo se diferencia de su valor inicial, indicando a la placa de control que ha sido tocado.
Durante este proceso, asegúrate de que el cableado de cada electrodo esté estable para mantener la carga equilibrada al iniciar.

**Conexión**

|wiring_fruit_piano| 

**Código**

.. note::

    * Abre el archivo ``7.9_fruit_piano.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`. 

    * Necesitarás la librería ``mpr121.py``; verifica si se ha subido a Pico W. Para más detalles, consulta :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time
    import urandom

    # Inicializar conexión I2C para el sensor táctil capacitivo MPR121
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # Frecuencias de las notas para el buzzer (en Hz)
    NOTE_A3 = 220
    NOTE_B3 = 247
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523
    NOTE_D5 = 587
    NOTE_E5 = 659

    # Inicializar PWM para el buzzer en el pin 15
    buzzer = machine.PWM(machine.Pin(15))

    # Lista de frecuencias de notas para el buzzer
    note = [NOTE_A3, NOTE_B3, NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5, NOTE_D5, NOTE_E5]

    # Función para reproducir un tono en el buzzer con una frecuencia específica
    def tone(pin, frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    # Función para silenciar el tono (detener el buzzer)
    def noTone(pin):
        pin.duty_u16(0)

    # Inicialización del LED RGB usando PWM en los pines 13, 12 y 11
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(12))
    blue = machine.PWM(machine.Pin(11))

    # Configurar la frecuencia PWM para cada color (1kHz)
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # Función para mapear un valor `x` de un rango a otro
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Función para iluminar aleatoriamente el LED RGB con valores de color aleatorios
    def lightup():
        red.duty_u16(int(urandom.uniform(0, 65535)))
        green.duty_u16(int(urandom.uniform(0, 65535)))
        blue.duty_u16(int(urandom.uniform(0, 65535)))

    # Función para apagar todos los colores del LED RGB (todos en 0)
    def dark():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # Bucle principal del proyecto
    lastState = mpr.get_all_states()
    touchMills = time.ticks_ms()
    beat = 500

    # Bucle principal para detectar toques y ejecutar efectos
    while True:
        currentState = mpr.get_all_states()
        
        # Check if there's a change in the touch input state (touch started or ended)
        if currentState != lastState:
            for i in range(12):
                if i in list(currentState) and not i in list(lastState):
                    tone(buzzer, note[i])
                    lightup()
                    touchMills = time.ticks_ms()
        
        if time.ticks_diff(time.ticks_ms(), touchMills) >= beat or len(currentState) == 0:
            noTone(buzzer)
            dark()
        
        lastState = currentState


No toques la fruta antes de que el programa se ejecute para evitar obtener una referencia incorrecta durante la inicialización.
Una vez que el programa esté en ejecución, toca la fruta suavemente, el buzzer emitirá el tono correspondiente y el LED RGB parpadeará aleatoriamente.
