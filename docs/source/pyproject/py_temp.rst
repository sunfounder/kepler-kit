.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el apasionante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_temp:

2.13 Termómetro
===================

Un termómetro es un dispositivo que mide la temperatura o un gradiente de 
temperatura (el nivel de calor o frío de un objeto). Un termómetro tiene 
dos elementos importantes: (1) un sensor de temperatura (por ejemplo, el 
bulbo de un termómetro de mercurio en vidrio o el sensor pirométrico en un 
termómetro infrarrojo), en el que ocurre algún cambio con una variación en 
la temperatura; y (2) un medio para convertir ese cambio en un valor numérico 
(por ejemplo, la escala visible en un termómetro de mercurio en vidrio o la 
lectura digital en un modelo infrarrojo). Los termómetros se utilizan 
ampliamente en tecnología e industria para monitorear procesos, en meteorología, 
en medicina y en investigaciones científicas.

Un termistor es un tipo de sensor de temperatura cuya resistencia depende 
fuertemente de la temperatura. Existen dos tipos de termistores: de Coeficiente 
de Temperatura Negativo (NTC) y de Coeficiente de Temperatura Positivo (PTC). 
La resistencia del termistor PTC aumenta con la temperatura, mientras que la 
del NTC disminuye a medida que la temperatura aumenta.

En este experimento, usaremos un **termistor NTC** para crear un termómetro.

* :ref:`cpn_thermistor`

**Componentes Necesarios**

Para este proyecto, necesitaremos los siguientes componentes.

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Esquemático**

|sch_temp|

En este circuito, el resistor de 10K y el termistor están conectados en serie, y la corriente que pasa a través de ellos es la misma. El resistor de 10K actúa como protección, y el pin GP28 lee el valor después de la conversión de voltaje del termistor.

Cuando la temperatura aumenta, el valor de resistencia del termistor NTC disminuye, lo que provoca una disminución en su voltaje, por lo que el valor de GP28 disminuirá. Si la temperatura es lo suficientemente alta, la resistencia del termistor se acercará a 0, y el valor de GP28 estará cerca de 0. En este caso, el resistor de 10K desempeña un papel protector, evitando que 3.3V y GND se conecten directamente, lo que resultaría en un cortocircuito.

Cuando la temperatura baja, el valor de GP28 aumentará. Cuando la temperatura es lo suficientemente baja, la resistencia del termistor será infinita, y su voltaje estará cerca de 3.3V (el resistor de 10K es insignificante), y el valor de GP28 se acercará al valor máximo de 65535.

La fórmula de cálculo es la siguiente:

    (Vp/3.3V) x 65535 = Ap

**Conexiones**

|wiring_temp|
 
.. #. Conecta los pines 3V3 y GND del Pico W al bus de alimentación de la breadboard.
.. #. Conecta un terminal del termistor al pin GP28, luego conecta el mismo terminal al bus positivo de alimentación con un resistor de 10K ohmios.
.. #. Conecta el otro terminal del termistor al bus negativo de alimentación.

.. note::
    * El termistor es negro y está marcado con 103.
    * El código de colores del resistor de 10K ohmios es rojo, negro, negro, rojo y marrón.

**Código**

.. note::

    * Abre el archivo ``2.13_thermometer.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.
    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.

    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    import math

    thermistor = machine.ADC(28)  

    while True:
        temperature_value = thermistor.read_u16()
        Vr = 3.3 * float(temperature_value) / 65535
        Rt = 10000 * Vr / (3.3 - Vr)
        temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        Cel = temp - 273.15
        Fah = Cel * 1.8 + 32
        print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
        utime.sleep_ms(200)

Al ejecutar el programa, la consola imprimirá las temperaturas en Celsius y Fahrenheit.

**¿Cómo funciona?**

Cada termistor tiene una resistencia normal. Aquí es de 10k ohmios, medida a 25 grados Celsius.

Cuando la temperatura aumenta, la resistencia del termistor disminuye. Luego, los datos de voltaje se convierten en cantidades digitales mediante el adaptador A/D.

La temperatura en grados Celsius o Fahrenheit se obtiene mediante programación.

.. code-block:: python

    import math 

Existe una biblioteca de funciones matemáticas que declara un conjunto de funciones para realizar operaciones y transformaciones matemáticas comunes.

* `math <https://docs.micropython.org/en/latest/library/math.html>`_

.. code-block:: python

    temperature_value = thermistor.read_u16()

Esta función se utiliza para leer el valor del termistor.

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah))
    utime.sleep_ms(200)

Estos cálculos convierten los valores del termistor en grados Celsius y Fahrenheit.

.. code-block:: python

    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)

En las dos líneas de código anteriores, se calcula primero el voltaje utilizando el valor analógico leído, y luego se obtiene Rt (la resistencia del termistor).

.. code-block:: python

    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25))) 

.. note::
    Aquí está la relación entre la resistencia y la temperatura:

    **RT = RN expB(1/TK – 1/TN)** 

    * RT es la resistencia del termistor NTC a la temperatura TK. 
    * RN es la resistencia del termistor NTC bajo la temperatura nominal TN, aquí con un valor de 10k. 
    * TK es la temperatura en Kelvin, y su unidad es K (273.15 + grados Celsius).
    * TN es la temperatura nominal en Kelvin, también en K. Aquí TN es 273.15 + 25.
    * B (beta), la constante del material del termistor NTC, también se llama índice de sensibilidad térmica y tiene un valor de 3950.
    * exp es la abreviatura de exponencial, y el número base e es un número natural aproximadamente igual a 2.7.

    Convierte esta fórmula TK=1/(ln(RT/RN)/B+1/TN) para obtener la temperatura en Kelvin, y resta 273.15 para obtener los grados Celsius.

Esta relación es una fórmula empírica, precisa solo cuando la temperatura y resistencia están dentro del rango efectivo.

Este código se refiere a insertar Rt en la fórmula TK=1/(ln(RT/RN)/B+1/TN) para obtener la temperatura en Kelvin.

.. code-block:: python

    temp = temp - 273.15 

Convierte la temperatura de Kelvin a grados Celsius.

.. code-block:: python

    Fah = Cel * 1.8 + 32 

Convierte los grados Celsius a grados Fahrenheit.

.. code-block:: python

    print ('Celsius: %.2f °C Fahrenheit: %.2f ℉' % (Cel, Fah)) 

Imprime los grados Celsius y Fahrenheit con sus respectivas unidades en la consola.

