.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_alarm_lamp:

7.3 Lámpara de Alarma
===========================

Las luces policiales son comunes en la vida real (o en películas). Usualmente se emplean para mantener el tráfico, como dispositivos de advertencia y como elemento de seguridad esencial en vehículos oficiales, de emergencia, bomberos y de ingeniería. Cuando ves sus luces o escuchas su sonido, debes estar alerta, ya que significa que podrías estar en una situación peligrosa.

En este proyecto, utilizamos un LED y un zumbador para crear una pequeña luz de advertencia, activada mediante un interruptor deslizante.

|sirem_alarm|


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
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Esquema**

|sch_alarm_siren_lamp|

* GP17 está conectado al pin central del interruptor deslizable, junto con una resistencia de 10K y un capacitor (filtro) en paralelo a GND, lo que permite que el interruptor proporcione un nivel alto o bajo estable al moverse a la izquierda o derecha.
* Cuando GP15 está en alto, el transistor NPN se activa, haciendo que el zumbador pasivo emita sonido. Este zumbador se programa para aumentar gradualmente en frecuencia y simular un sonido de sirena.
* Un LED está conectado a GP16 y se programa para cambiar periódicamente su brillo y simular una luz de sirena.

**Conexión**

|wiring_alarm_siren_lamp|

**Código**

.. note::

    * Abre el archivo ``7.3_alarm_siren_lamp.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    # Inicializa el PWM para el zumbador (en el pin 15) y el LED (en el pin 16)
    buzzer = machine.PWM(machine.Pin(15))  # PWM para el zumbador
    led = machine.PWM(machine.Pin(16))  # PWM para el LED
    led.freq(1000)  # Establece la frecuencia del PWM del LED en 1kHz

    # Inicializa el interruptor (en el pin 17) como pin de entrada
    switch = machine.Pin(17, machine.Pin.IN)

    # Función para detener el zumbador estableciendo el ciclo de trabajo en 0%
    def noTone(pin):
        pin.duty_u16(0)  # Configura el ciclo de trabajo del PWM a 0, deteniendo el sonido

    # Función para reproducir un tono en el zumbador con una frecuencia específica
    def tone(pin, frequency):
        pin.freq(frequency)  # Establece la frecuencia del zumbador
        pin.duty_u16(30000)  # Ciclo de trabajo al 50% (30000 de 65535)

    # Función para mapear un valor de un rango a otro
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Función de interrupción para alternar el bell_flag cuando se pulsa el interruptor
    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag  # Alterna el valor de bell_flag
        print(bell_flag)  # Imprime el estado actual de bell_flag para depuración
        
        # Cambia la interrupción del interruptor según el estado de bell_flag
        if bell_flag:
            # Si bell_flag es True, detecta el borde descendente (cuando se suelta el interruptor)
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            # Si bell_flag es False, detecta el borde ascendente (cuando se pulsa el interruptor)
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Inicializa bell_flag en False (zumbador y LED apagados por defecto)
    bell_flag = False

    # Configura una interrupción para detectar cuando se pulsa el interruptor (borde ascendente)
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Bucle principal para controlar el zumbador y el LED basado en bell_flag
    while True:
        if bell_flag == True:
            # Si bell_flag es True, incrementa gradualmente el brillo del LED
            # y cambia la frecuencia del zumbador para simular el efecto de una campana
            for i in range(0, 100, 2):  # Bucle de 0 a 100 en pasos de 2
                led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))  # Mapea i a brillo del LED
                tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))  # Mapea i a frecuencia del zumbador
                time.sleep_ms(10)  # Pequeña pausa para crear un aumento suave
        else:
            # Si bell_flag es False, detiene el zumbador y apaga el LED
            noTone(buzzer)  # Detiene el zumbador
            led.duty_u16(0)  # Apaga el LED (ciclo de trabajo a 0)

Al ejecutar el programa, desliza el interruptor hacia la izquierda (o hacia la derecha, según tu configuración) y el zumbador emitirá un tono progresivo de advertencia mientras el LED cambia su brillo; mueve el interruptor a la posición opuesta y el zumbador y el LED se detendrán.
