.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_led:

2.1 - ¡Hola, LED!
=======================================

Así como imprimir “Hola, mundo” es el primer paso para aprender a programar, controlar un LED a través de un programa es la introducción tradicional a la programación física.

* :ref:`cpn_led`

**Componentes Necesarios**

Para este proyecto, necesitamos los siguientes componentes.

Es muy conveniente adquirir un kit completo, aquí tienes el enlace:

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
        - :ref:`cpn_resistor`
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Esquema**

|sch_led|

El principio de este circuito es simple y la dirección de la corriente se muestra en la figura. Cuando GP15 emite un nivel alto (3.3v), el LED se ilumina después de pasar por la resistencia limitadora de corriente de 220Ω. Cuando GP15 emite un nivel bajo (0v), el LED se apaga.

**Conexión**

|wiring_led|

¡Sigamos la dirección de la corriente para construir el circuito!

1. Aquí usamos la señal eléctrica del pin GP15 de la placa Pico W para hacer que funcione el LED, y el circuito comienza desde aquí.
2. La corriente necesita pasar a través de una resistencia de 220Ω (utilizada para proteger el LED). Inserta un extremo (cualquiera de los dos) de la resistencia en la misma fila que el pin GP15 de Pico W (fila 20 en mi circuito), y el otro extremo en una fila libre del protoboard (fila 24 en mi circuito).
3. Toma el LED; verás que una de sus patas es más larga que la otra. Inserta la pata más larga en la misma fila que el extremo de la resistencia, y conecta la pata más corta al otro lado del protoboard en la misma fila.
4. Inserta un cable macho-macho (M2M) en la misma fila que la pata corta del LED y conéctalo a la barra de tierra del protoboard.
5. Usa un cable para conectar la barra de tierra al pin GND de Pico W.


**Código**

.. note::

    * Puedes abrir el archivo ``2.1_hello_led.ino`` en la ruta ``kepler-kit-main/arduino/2.1_hello_led``.
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/898b8ba7-9bdf-468d-9181-ca8535e8dca6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Después de ejecutar el código, verás que el LED parpadea.

**¿Cómo funciona?**

Aquí conectamos el LED al pin digital 15, por lo que necesitamos declarar una variable entera llamada ``ledPin`` al inicio del programa y asignarle el valor de 15.

.. code-block:: C

    const int ledPin = 15;

Ahora, inicializa el pin en la función ``setup()``, donde debes configurarlo en modo ``OUTPUT``.

.. code-block:: C

    void setup() {
        pinMode(ledPin, OUTPUT);
    }

En ``loop()``, ``digitalWrite()`` se utiliza para proporcionar una señal de nivel alto de 3.3V a ``ledPin``, lo que generará una diferencia de voltaje en los pines del LED y lo encenderá.

.. code-block:: C

    digitalWrite(ledPin, HIGH);

Si el nivel de señal se cambia a LOW, la señal de ``ledPin`` volverá a 0V, apagando el LED.

.. code-block:: C

    digitalWrite(ledPin, LOW);

Se requiere un intervalo entre el encendido y apagado para que sea visible el cambio, 
por lo que usamos ``delay(1000)`` para que el controlador se detenga por 1000 ms.

.. code-block:: C

    delay(1000);   
