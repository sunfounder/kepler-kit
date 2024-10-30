.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_button:

2.5 - Lectura del Valor de un Botón
==============================================

Como su nombre indica, GPIO (entrada/salida de propósito general) es capaz de funcionar como pin de entrada y salida. 
En las lecciones anteriores usamos su función de salida; en este capítulo exploraremos su función de entrada para leer el valor de un botón.

* :ref:`cpn_button`

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Esquema**

|sch_button|

Un pin del botón está conectado a 3.3V, y el otro pin está conectado a GP14. De esta forma, cuando se presiona el botón, GP14 recibirá un nivel alto. Sin embargo, cuando el botón no se presiona, GP14 queda en un estado flotante y podría tener un nivel alto o bajo. Para obtener un nivel bajo estable cuando el botón no está presionado, GP14 debe estar conectado a GND a través de una resistencia pull-down de 10K.

**Conexión**

|wiring_button|

.. note::
    Podemos imaginar el botón de cuatro patas como un botón en forma de "H". Sus dos patas del lado izquierdo (o derecho) están conectadas entre sí, lo que significa que al cruzar la línea divisoria central, conecta ambas mitades de la misma fila (por ejemplo, en mi circuito, E23 y F23 están conectados, al igual que E25 y F25).

    Antes de presionar el botón, los lados izquierdo y derecho están aislados, y la corriente no puede fluir de un lado al otro.


**Código**

.. note::

    * Puedes abrir el archivo ``2.5_reading_button_value.ino`` en la ruta ``kepler-kit-main/arduino/2.5_reading_button_value``.
    * O copia este código en el **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6fcb7cac-e866-4a2d-8162-8e0c6fd17660/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el código, haz clic en el ícono de la lupa en la esquina superior derecha del IDE de Arduino (Monitor Serial).

.. image:: img/open_serial_monitor.png

Ahora, cuando presiones el botón, el Monitor Serial imprimirá "¡Has presionado el botón!".


**¿Cómo funciona?**

Para habilitar el Monitor Serial, es necesario iniciar la comunicación serial en ``setup()`` y configurar la tasa de datos a 9600.

.. code-block:: arduino

    Serial.begin(115200);

    
* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_


Para el botón, debemos configurar su modo en ``INPUT`` para poder leer sus valores.

.. code-block:: arduino

    pinMode(buttonPin, INPUT);

Lee el estado de ``buttonPin`` en ``loop()`` y asígnalo a la variable ``buttonState``.

.. code-block:: arduino

    buttonState = digitalRead(buttonPin);
    
* `digitalRead() <https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/>`_


Si ``buttonState`` es HIGH, el LED parpadeará e imprimirá "¡Has presionado el botón!" en el Monitor Serial.

.. code-block:: arduino

    if (buttonState == HIGH) {
        Serial.println("You pressed the button!");
    }


**Modo de Funcionamiento Pull-up**

A continuación, mostramos el cableado y código para el botón en modo pull-up. Prueba este modo también.

|wiring_button_pullup|

.. 1. Conecta el pin 3V3 de la Pico W al bus positivo de la protoboard.
.. #. Inserta el botón en la protoboard, cruzando la línea divisoria central.
.. #. Conecta uno de los pines del botón al bus **negativo** (en mi caso, es el pin en la esquina superior derecha).
.. #. Conecta el otro pin (esquina superior izquierda o inferior izquierda) a GP14 con un cable de puente.
.. #. Usa una resistencia de 10K para conectar el pin en la esquina superior izquierda del botón al bus **positivo**.
.. #. Conecta el bus negativo de la protoboard al GND de la Pico.

La única diferencia con el modo pull-down es que la resistencia de 10K se conecta a 3.3V y el botón a GND, de modo que al presionar el botón, GP14 recibirá un nivel bajo, siendo opuesto al valor obtenido en el modo pull-down.
Por lo tanto, solo cambia este código a ``if (buttonState == LOW)``.

