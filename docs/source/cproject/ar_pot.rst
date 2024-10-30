.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_pot:

2.11 - Gira el Potenciómetro
=================================

En proyectos anteriores, hemos usado la entrada digital en el Pico W. Por 
ejemplo, un botón puede cambiar el pin de nivel bajo (apagado) a nivel alto 
(encendido), lo que representa un estado de funcionamiento binario.

Sin embargo, Pico W también puede recibir otro tipo de señal de entrada: la 
entrada analógica. Esta puede estar en cualquier estado, desde completamente 
cerrado hasta completamente abierto, y tiene un rango de valores posibles. La 
entrada analógica permite que el microcontrolador detecte la intensidad de luz, 
intensidad de sonido, temperatura, humedad, etc., del mundo físico.

Normalmente, un microcontrolador necesita hardware adicional para implementar 
la entrada analógica: un convertidor analógico a digital (ADC). Pero Pico W ya 
incluye un ADC incorporado que podemos usar directamente.

|pin_adc|

Pico W cuenta con tres pines GPIO que pueden usar entrada analógica: GP26, GP27, 
GP28, es decir, los canales analógicos 0, 1 y 2. Además, existe un cuarto canal 
analógico, que está conectado al sensor de temperatura interno y no se introducirá aquí.

En este proyecto, intentaremos leer el valor analógico de un potenciómetro.

* :ref:`cpn_potentiometer`

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

El potenciómetro es un dispositivo analógico y su comportamiento cambia al girarlo en dos direcciones diferentes.

Conecta el pin central del potenciómetro al pin analógico GP28. La Raspberry Pi Pico W tiene un convertidor analógico a digital de múltiples canales y 16 bits, lo que significa que asigna el voltaje de entrada entre 0 y el voltaje de operación (3.3V) a un valor entero entre 0 y 65535. Así, el valor de GP28 oscilará entre 0 y 65535.

La fórmula de cálculo es la siguiente:

    (Vp/3.3V) x 65535 = Ap

Luego, programa el valor de GP28 (potenciómetro) como el valor PWM de GP15 (LED). 
De esta forma, verás que al girar el potenciómetro, la intensidad del LED cambia al mismo tiempo.

**Conexión**

|wiring_pot|

**Código**

.. note::

    * Puedes abrir el archivo ``2.11_turn_the_knob.ino`` en la ruta ``kepler-kit-main/arduino/2.11_turn_the_knob``.
    * O copiar este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.


Cuando el programa esté funcionando, podrás ver el valor analógico actualmente leído por el pin 
GP28 en el Monitor Serial. Gira la perilla, y el valor cambiará de 0 a 1023. Al mismo tiempo, la 
intensidad del LED aumentará conforme el valor analógico sube.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3e3927a-bd1a-4756-83f2-141d47f99b1c/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**¿Cómo funciona?**

Para habilitar el Monitor Serial, es necesario iniciar la comunicación serial en ``setup()`` y establecer la velocidad de datos en 9600.

.. code-block:: arduino
    :emphasize-lines: 3

    void setup() {
        pinMode(ledPin, OUTPUT);
        Serial.begin(9600);
    }


* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

En la función loop, el valor del potenciómetro se lee y luego se mapea de 0-1023 a 0-255. Finalmente, el valor después del mapeo se utiliza para controlar la intensidad del LED.

.. code-block:: arduino

    void loop() {
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
        int brightness = map(sensorValue, 0, 1023, 0, 255);
        analogWrite(ledPin, brightness);
    }

* `analogRead() <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ se usa para leer el valor de ``sensorPin`` (potenciómetro) y lo asigna a la variable ``sensorValue``.

.. code-block:: arduino

    int sensorValue = analogRead(sensorPin);

* Imprime el valor de SensorValue en el Monitor Serial.

.. code-block:: arduino

    Serial.println(sensorValue);

* Aquí, la función `map(value, fromLow, fromHigh, toLow, toHigh) <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ es necesaria, ya que el valor del potenciómetro está en el rango de 0-1023, mientras que el valor de un pin PWM está en el rango de 0-255. Re-mapea un número de un rango a otro, es decir, un valor de fromLow se mapearía a toLow, y un valor de fromHigh a toHigh.

.. code-block:: arduino

    int brightness = map(sensorValue, 0, 1023, 0, 255);

* Ahora podemos usar este valor para controlar la intensidad del LED.

.. code-block:: arduino

    analogWrite(ledPin,brightness);
