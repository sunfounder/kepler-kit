.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_74hc_4dig:

5.3 Contador de Tiempo
================================

El display de 7 segmentos de 4 dígitos está compuesto por cuatro displays de 7 
segmentos que trabajan juntos.

Cada dígito funciona de manera independiente, utilizando el principio de 
persistencia visual para mostrar rápidamente los caracteres de cada segmento 
de forma secuencial, formando así una cadena continua.

Por ejemplo, cuando en el display se muestra "1234", se visualiza primero "1" 
en el primer dígito, mientras que "234" no aparece. Después de un breve intervalo, 
el segundo dígito muestra "2" mientras que el 1°, 3° y 4° permanecen apagados. 
Así, los cuatro dígitos se muestran en secuencia. Este proceso es muy corto 
(normalmente 5 ms), y gracias al efecto de postimagen y a la persistencia de 
la visión, podemos ver los cuatro caracteres al mismo tiempo.

**Componentes Requeridos**

En este proyecto, necesitaremos los siguientes componentes.

Comprar un kit completo es muy conveniente; aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ÍTEMS EN ESTE KIT
        - ENLACE
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes adquirirlos por separado desde los enlaces a continuación.

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
        - :ref:`cpn_resistor`
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Esquema**

|sch_4dig|

Aquí el principio de cableado es básicamente el mismo que en :ref:`py_74hc_led`, la única diferencia es que Q0-Q7 están conectados a los pines a ~ g del display de 7 segmentos de 4 dígitos.

Luego, G10 ~ G13 seleccionarán qué dígito del display de 7 segmentos estará activo.

**Cableado**

|wiring_4dig|

**Código**

.. note::

    * Abre el archivo ``5.3_time_counter.py`` en la ruta ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()
        time.sleep_us(200)

    while True:
        count = timer1()
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])     

Después de ejecutar el programa, verás el display de 7 segmentos de 4 dígitos funcionando como un contador que aumenta en 1 cada segundo.

**¿Cómo funciona?**

La escritura de señales en cada dígito del display de 7 segmentos se realiza de la misma manera que en :ref:`py_74hc_7seg`, utilizando la función ``hc595_shift()``.
El punto clave del display de 7 segmentos de 4 dígitos es activar selectivamente cada dígito. El código relacionado con esto es el siguiente.

.. code-block:: python

    placePin = []
    pin = [13,12,11,10]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    while True:
        
        hc595_shift(SEGCODE[count%10])
        pickDigit(0)

        hc595_shift(SEGCODE[count%100//10])
        pickDigit(1)
        
        hc595_shift(SEGCODE[count%1000//100])
        pickDigit(2)    
        
        hc595_shift(SEGCODE[count%10000//1000])
        pickDigit(3)   

Aquí, se utilizan cuatro pines (GP10, GP11, GP12, GP13) para controlar cada dígito del display de 7 segmentos de manera individual.
Cuando el estado de estos pines es ``0``, el dígito correspondiente está activo; cuando el estado es ``1``, está inactivo.

La función ``pickDigit(digit)`` se utiliza para desactivar los cuatro dígitos y luego activar un dígito específico.
Después, se usa ``hc595_shift()`` para escribir el código de 8 bits correspondiente al dígito seleccionado del display de 7 segmentos.

El display de 7 segmentos de 4 dígitos necesita activarse continuamente en turnos para que podamos ver los cuatro dígitos. Esto significa que el programa principal no puede agregar fácilmente código que altere el tiempo de activación.
Sin embargo, necesitamos agregar una función de temporización a este ejemplo, y si añadimos un ``sleep(1)``, veríamos que tiene cuatro dígitos.
Veríamos entonces que, en realidad, solo un dígito se ilumina a la vez.
La función ``time.ticks_ms()`` en la biblioteca ``time`` es una excelente manera de lograr esto.

.. code-block:: python

    import time

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    while True:
        count = timer1()


La función ``time.ticks_ms()`` obtiene un tiempo (no explícito), y registramos el primer valor como ``timerStart``.
Después, cuando se necesita el tiempo, se llama nuevamente a ``time.ticks_ms()``, y el valor se resta de ``timerStart`` para obtener el tiempo que el programa lleva en ejecución (en milisegundos).

Finalmente, convierte y muestra este valor de tiempo en el display de 7 segmentos de 4 dígitos, y listo.

* `Time - MicroPython Docs <https://docs.micropython.org/en/latest/library/time.html>`_