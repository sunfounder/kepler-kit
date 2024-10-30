.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_temp:

2.13 - Termómetro
===========================

Un termómetro es un dispositivo que mide la temperatura o un gradiente de temperatura (el nivel de calor o frío de un objeto). 
Un termómetro tiene dos elementos importantes: (1) un sensor de temperatura (p. ej., el bulbo de un termómetro de mercurio o el sensor pirométrico en un termómetro infrarrojo) en el cual ocurre algún cambio con la temperatura; 
y (2) un medio para convertir este cambio en un valor numérico (p. ej., la escala visible en un termómetro de mercurio o la lectura digital en un modelo infrarrojo). 
Los termómetros se utilizan ampliamente en tecnología e industria para monitorear procesos, en meteorología, en medicina y en investigación científica.

Un termistor es un tipo de sensor de temperatura cuya resistencia depende significativamente de la temperatura, y existen dos tipos:
Coeficiente de Temperatura Negativo (NTC) y Coeficiente de Temperatura Positivo (PTC).
La resistencia de un termistor PTC aumenta con la temperatura, mientras que el NTC muestra el comportamiento contrario.

En este experimento usaremos un **termistor NTC** para construir un termómetro.

* :ref:`cpn_thermistor`


**Componentes Necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Esquema**

|sch_temp|

En este circuito, la resistencia de 10K y el termistor están conectados en serie, y la corriente que los atraviesa es la misma. La resistencia de 10K actúa como protección, y el pin GP28 lee el valor tras la conversión de voltaje del termistor.

Cuando aumenta la temperatura, el valor de resistencia del termistor NTC disminuye, y su voltaje baja, por lo que el valor de GP28 también disminuye. Si la temperatura es lo suficientemente alta, la resistencia del termistor se aproximará a 0 y el valor de GP28 será cercano a 0. En este momento, la resistencia de 10K juega un papel protector, evitando que se conecten los 3.3V y GND, lo cual provocaría un cortocircuito.

Cuando la temperatura desciende, el valor de GP28 aumentará. En condiciones de frío extremo, la resistencia del termistor será infinita y su voltaje se acercará a 3.3V (la resistencia de 10K es despreciable), por lo que el valor de GP28 estará cerca del valor máximo de 65535.

La fórmula de cálculo se muestra a continuación:

    (Vp/3.3V) x 65535 = Ap

**Conexión**

|wiring_temp|

.. #. Conecta 3V3 y GND de la Pico W al bus de alimentación de la breadboard.
.. #. Conecta un terminal del termistor al pin GP28 y al mismo terminal, conecta una resistencia de 10K ohmios al bus positivo de alimentación.
.. #. Conecta el otro terminal del termistor al bus negativo de alimentación.

.. note::
    * El termistor es negro y está marcado como 103.
    * El anillo de colores de la resistencia de 10K ohmios es rojo, negro, negro, rojo y marrón.

**Código**

.. note::

    * Puedes abrir el archivo ``2.13_thermometer.ino`` en la ruta ``kepler-kit-main/arduino/2.13_thermometer``. 
    * O copia este código en **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/1ae1a028-2647-4e4c-b647-0d4759f6fd03/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Cuando el programa se ejecuta, el Monitor Serial imprimirá las temperaturas en grados Celsius y Fahrenheit.

**¿Cómo funciona?**

Cada termistor tiene una resistencia nominal. Aquí es de 10K ohmios, medida a 25 grados Celsius.

Cuando la temperatura aumenta, la resistencia del termistor disminuye.
Luego, los datos de voltaje se convierten en valores digitales mediante el adaptador A/D.

La temperatura en grados Celsius o Fahrenheit se muestra mediante programación.

.. code-block:: arduino

    long a = analogRead(analogPin);

Esta línea se usa para leer el valor del termistor.

.. code-block:: arduino

    float tempC = beta / (log((1025.0 * 10 / a - 10) / 10) + beta / 298.0) - 273.0;
    float tempF = 1.8 * tempC + 32.0;

Estos cálculos convierten los valores del termistor en grados centígrados y grados Fahrenheit.

.. note::
    Aquí está la relación entre la resistencia y la temperatura:

    **RT = RN expB(1/TK – 1/TN)** 

    * RT es la resistencia del termistor NTC cuando la temperatura es TK.
    * RN es la resistencia del termistor NTC a la temperatura nominal TN. Aquí, el valor de RN es 10k.
    * TK es la temperatura en Kelvin y su unidad es K. Aquí, el valor de TK es 273.15 + grados Celsius.
    * TN es la temperatura nominal en Kelvin; la unidad también es K. Aquí, el valor de TN es 273.15+25.
    * B (beta), la constante material del termistor NTC, también se llama índice de sensibilidad térmica, con un valor numérico de 3950.
    * exp es la abreviatura de exponencial, y el número base e es un número natural, aproximadamente igual a 2.7.

    Convierte esta fórmula TK=1/(ln(RT/RN)/B+1/TN) para obtener la temperatura en Kelvin, la cual menos 273.15 dará la temperatura en grados Celsius.

    Esta relación es una fórmula empírica. Es precisa solo cuando la temperatura y la resistencia están dentro del rango efectivo.

Este código se refiere a ingresar Rt en la fórmula TK=1/(ln(RT/RN)/B+1/TN) para obtener la temperatura en Kelvin.
