.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_rgb:


2.4 - Luz Colorida
=============================

Como sabemos, la luz se puede superponer. Por ejemplo, la mezcla de luz azul y verde da luz cian, mientras que la luz roja y verde da luz amarilla. A este fenómeno se le llama "método aditivo de mezcla de colores".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Basándonos en este método, podemos usar los tres colores primarios para mezclar la luz visible de cualquier color según diferentes proporciones. Por ejemplo, el naranja se produce con más rojo y menos verde.

En este capítulo, exploraremos el misterio de la mezcla aditiva de colores utilizando un LED RGB.

Un LED RGB es equivalente a encapsular un LED rojo, uno verde y uno azul bajo una misma tapa, y los tres LEDs comparten un pin de cátodo común. Al proporcionar una señal eléctrica para cada pin del ánodo, el LED RGB puede mostrar un color específico. Al cambiar la intensidad de la señal eléctrica de cada ánodo, se pueden producir diversos colores.

* :ref:`cpn_rgb`

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
        - 3 (1 de 330Ω, 2 de 220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Diagrama Esquemático**

|sch_rgb|

Los pines PWM GP13, GP14 y GP15 controlan los pines Rojo, Verde y Azul del LED RGB, respectivamente, y conectan el pin de cátodo común a GND. Esto permite que el LED RGB muestre un color específico al superponer la luz en estos pines con diferentes valores PWM.

**Conexión**

|img_rgb_pin|

Un LED RGB tiene 4 pines: el pin más largo es el cátodo común, que usualmente se conecta a GND, el pin a la izquierda junto al más largo es Rojo, y los 2 pines a la derecha son Verde y Azul.

|wiring_rgb|


**Código**

Aquí, podemos elegir nuestro color favorito en un software de dibujo (como Paint) y mostrarlo en el LED RGB.

.. note::

    * Puedes abrir el archivo ``2.4_colorful_light.ino`` en la ruta ``kepler-kit-main/arduino/2.4_colorful_light``. 
    * O copia este código en el  **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/c869191c-026c-4aac-8396-09eaf6ee2204/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

|img_take_color|

Escribe el valor RGB en ``color_set()``, y podrás ver cómo el LED RGB ilumina los colores deseados.


**¿Cómo funciona?**

En este ejemplo, la función utilizada para asignar valores a los tres pines del RGB está empaquetada en una subfunción independiente ``color()``.

.. code-block:: C

    void color (unsigned char red, unsigned char green, unsigned char blue)
    {
        analogWrite(redPin, red);
        analogWrite(greenPin, green);
        analogWrite(bluePin, blue);
    }

En ``loop()``, el valor RGB funciona como un argumento de entrada para llamar a la función ``color()``, permitiendo que el LED RGB emita diferentes colores.

.. code-block:: C

    void loop() 
    {    
        color(255, 0, 0); // rojo 
        delay(1000); 
        color(0,255, 0); // verde  
        delay(1000);  
        color(0, 0, 255); // azul  
        delay(1000);
    }
