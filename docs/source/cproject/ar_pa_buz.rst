.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora a fondo Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_pa_buz:


3.2 - Tono personalizado
==========================================


En el proyecto anterior usamos un zumbador activo; esta vez utilizaremos un zumbador pasivo.

Al igual que el zumbador activo, el zumbador pasivo también utiliza el fenómeno de la inducción electromagnética para funcionar. La diferencia es que un zumbador pasivo no tiene una fuente de oscilación, por lo que no emitirá sonido si se utiliza una señal de corriente continua (DC). Sin embargo, esto permite que el zumbador pasivo ajuste su propia frecuencia de oscilación y emita diferentes notas como “do, re, mi, fa, sol, la, si”.

¡Hagamos que el zumbador pasivo emita una melodía!

* :ref:`Buzzer`

**Componentes necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ITEMS EN ESTE KIT
        - LINK DE COMPRA
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCCIÓN DEL COMPONENTE	
        - CANTIDAD
        - LINK DE COMPRA

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
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Zumbador pasivo :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Esquema**

|sch_buzzer|

Cuando la salida de GP15 está en alto, después de pasar por el resistor limitador de corriente de 1K (para proteger el transistor), el S8050 (transistor NPN) conducirá, haciendo que el zumbador emita sonido.

El transistor S8050 (NPN) tiene el rol de amplificar la corriente para hacer que el zumbador suene más fuerte. En realidad, puedes conectar el zumbador directamente al pin GP15, pero notarás que el sonido es más bajo.

**Conexión**

|img_buzzer|

En el kit se incluyen dos zumbadores; aquí usaremos el zumbador pasivo (el que tiene una PCB expuesta en la parte trasera).

El zumbador necesita un transistor para funcionar; aquí utilizamos el S8050.

|wiring_buzzer|

**Código**

.. note::

    * Puedes abrir el archivo ``3.2_custom_tone.ino`` en la ruta ``kepler-kit-main/arduino/3.2_custom_tone``.
    * O copiar este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/69c55e56-9eeb-46bb-b3a8-b354c500cc17/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**¿Cómo funciona?**

Si se proporciona una señal digital al zumbador pasivo, solo moverá la membrana sin producir sonido.

Por lo tanto, usamos la función ``tone()`` para generar la señal PWM que hace sonar el zumbador pasivo.

Esta función tiene tres parámetros:

  * **pin**, el pin GPIO que controla el zumbador.
  * **frecuencia**, determina el tono del zumbador; a mayor frecuencia, mayor tono.
  * **duración**, el tiempo durante el cual se emite el tono.

* `tone <https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/>`_

**Aprende más**

Podemos simular tonos específicos según la frecuencia fundamental del piano, y así reproducir una pieza completa.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_

.. note::

    * Puedes abrir el archivo ``3.2_custom_tone_2.ino`` en la ruta ``kepler-kit-main/arduino/3.2_custom_tone_2``.
    * O copiar este código en el **Arduino IDE**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f934c785-7204-4972-aae5-01edde3c79cc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>