.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones durante festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_pa_buz:

3.2 Tono Personalizado
==========================================

En el proyecto anterior usamos un zumbador activo; esta vez utilizaremos un zumbador pasivo.


Al igual que el zumbador activo, el zumbador pasivo también funciona por inducción electromagnética. 
La diferencia es que el zumbador pasivo no tiene una fuente de oscilación interna, por lo que no emitirá 
sonidos si se usan señales de corriente continua. Sin embargo, esta característica permite que el zumbador 
pasivo ajuste su propia frecuencia de oscilación y pueda emitir diferentes notas como "do, re, mi, fa, sol, la, si".

¡Vamos a hacer que el zumbador pasivo emita una melodía!

* :ref:`cpn_buzzer`

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
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Zumbador Pasivo :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Esquema**

|sch_buzzer|

Cuando el pin GP15 emite un nivel alto, la corriente pasa a través de la resistencia limitadora de 1K (para proteger el transistor), el transistor S8050 (NPN) conduce, y el zumbador emite sonido.

El rol del transistor S8050 (NPN) es amplificar la corriente y hacer que el zumbador suene más fuerte. De hecho, también se podría conectar el zumbador directamente a GP15, pero notarás que el sonido es más bajo.

**Conexiones**

|img_buzzer|

En el kit se incluyen dos zumbadores; aquí usaremos el zumbador pasivo (el que tiene una PCB expuesta en la parte posterior).

El zumbador necesita un transistor para funcionar; aquí usamos el S8050.

|wiring_buzzer|

.. 1. Conecta 3V3 y GND de la Pico W a la barra de energía de la protoboard.
.. #. Conecta el pin positivo del zumbador a la barra positiva de la protoboard.
.. #. Conecta el pin negativo del zumbador al pin **colector** del transistor.
.. #. Conecta el pin **base** del transistor al pin GP15 a través de una resistencia de 1kΩ.
.. #. Conecta el pin **emisor** del transistor a la barra negativa de energía.

**Código**

.. note::

    * Abre el archivo ``3.2_custom_tone.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    tone(buzzer,440,250)
    utime.sleep_ms(500)
    tone(buzzer,494,250)
    utime.sleep_ms(500)
    tone(buzzer,523,250)


**¿Cómo funciona?**

Si el zumbador pasivo recibe una señal digital, solo moverá el diafragma sin producir sonido.

Por lo tanto, usamos la función ``tone()`` para generar la señal PWM y hacer que el zumbador pasivo suene.

Esta función tiene tres parámetros:

* **pin**, el pin GPIO que controla el zumbador.
* **frequency**, la frecuencia que determina el tono del zumbador; cuanto mayor es la frecuencia, más alto es el tono.
* **duration**, la duración de la nota.

Usamos la función ``duty_u16()`` para establecer el ciclo de trabajo en 30000 (aproximadamente 50%). Este valor puede ser diferente; solo necesita generar una señal eléctrica discontinua para provocar la oscilación.


**Aprende Más**

Podemos simular tonos específicos según la frecuencia fundamental del piano, para así reproducir una melodía completa.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_



.. note::

    * Abre el archivo ``3.2_custom_tone_2.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    NOTE_C4 = 262
    NOTE_G3 = 196
    NOTE_A3 = 220
    NOTE_B3 = 247

    melody =[NOTE_C4,NOTE_G3,NOTE_G3,NOTE_A3,NOTE_G3,NOTE_B3,NOTE_C4]

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    for note in melody:
        tone(buzzer,note,250)
        utime.sleep_ms(150)
