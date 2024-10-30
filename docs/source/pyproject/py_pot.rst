.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_pot:

2.11 Gira la Perilla
===========================

En los proyectos anteriores, hemos usado la entrada digital en el Pico W.
Por ejemplo, un botón puede cambiar el pin de nivel bajo (apagado) a nivel alto (encendido). Esto es un estado binario de funcionamiento.

Sin embargo, el Pico W puede recibir otro tipo de señal de entrada: entrada analógica.
Esta puede estar en cualquier estado desde completamente cerrado hasta completamente abierto, y tiene un rango de valores posibles.
La entrada analógica permite al microcontrolador captar la intensidad de la luz, el sonido, la temperatura, la humedad, entre otros aspectos del mundo físico.

Normalmente, un microcontrolador necesita hardware adicional para implementar la entrada analógica: el convertidor de analógico a digital (ADC).
Pero el Pico W tiene un ADC incorporado que podemos usar directamente.

|pin_adc|

Pico W tiene tres pines GPIO que pueden usar entrada analógica: GP26, GP27 y GP28. Es decir, los canales analógicos 0, 1 y 2.
Además, hay un cuarto canal analógico, que está conectado al sensor de temperatura incorporado y que no se abordará aquí.

En este proyecto, intentaremos leer el valor analógico de un potenciómetro.

* :ref:`cpn_potentiometer`

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Esquema**

|sch_pot|

El potenciómetro es un dispositivo analógico y cuando lo giras en dos direcciones diferentes.

Conecta el pin central del potenciómetro al pin analógico GP28. La Raspberry Pi Pico W contiene un convertidor de analógico a digital multicanal de 16 bits. Esto significa que mapea el voltaje de entrada entre 0 y el voltaje de operación (3.3V) a un valor entero entre 0 y 65535, de modo que el valor de GP28 varía de 0 a 65535.

La fórmula de cálculo se muestra a continuación.

    (Vp/3.3V) x 65535 = Ap

Luego, programa el valor de GP28 (potenciómetro) como el valor PWM de GP15 (LED).
De esta forma, verás que al girar el potenciómetro, el brillo del LED cambiará al mismo tiempo.

**Conexiones**

|wiring_pot|

**Código**

.. note::

    * Abre el archivo ``2.11_turn_the_knob.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value=potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

Cuando el programa esté en ejecución, podremos ver el valor analógico que actualmente lee el pin GP28 en la Shell. 
Gira la perilla y el valor cambiará de 0 a 65535.
Al mismo tiempo, el brillo del LED aumentará a medida que aumente el valor analógico.

**¿Cómo funciona?**

.. code-block:: python

    potentiometer = machine.ADC(28)

Accede al ADC asociado con una fuente identificada por id. En este ejemplo es GP28.

.. code-block:: python

    potentiometer.read_u16()

Toma una lectura analógica y devuelve un número entero en el rango de 0-65535. El valor de retorno representa la lectura cruda tomada por el ADC, escalada de tal forma que el valor mínimo es 0 y el máximo es 65535.

* `machine.ADC - MicroPython Docs <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_