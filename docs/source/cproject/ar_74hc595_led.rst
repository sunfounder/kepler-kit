.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_74hc_led:

5.1 - Microchip - 74HC595
===========================

El circuito integrado (o "IC" por sus siglas en inglés) es un dispositivo o componente electrónico en miniatura que se representa en los circuitos mediante el símbolo "IC".

Mediante un proceso específico, se interconectan transistores, resistencias, condensadores, inductores y otros componentes y cables necesarios en un circuito, todo fabricado en una o varias pequeñas obleas de semiconductor o sustratos dieléctricos y luego encapsulados en una carcasa. Esto crea una estructura en miniatura con las funciones de circuito requeridas, donde todos los componentes están estructurados en una sola unidad, logrando un gran avance hacia la micro-miniaturización, bajo consumo energético, inteligencia y alta fiabilidad en los componentes electrónicos.

Los inventores de los circuitos integrados son Jack Kilby (circuitos integrados basados en germanio (Ge)) y Robert Norton Noyce (circuitos integrados basados en silicio (Si)).

Este kit incluye un IC, el 74HC595, que permite reducir considerablemente el uso de pines GPIO. En concreto, puede reemplazar 8 pines de salida de señales digitales escribiendo un número binario de 8 bits.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

* :ref:`74HC595`

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
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Esquema**

|sch_74hc_led|

* Cuando MR (pin 10) está en nivel alto y OE (pin 13) en nivel bajo, los datos se ingresan en el flanco ascendente de SHcp y pasan al registro de memoria mediante el flanco ascendente de SHcp.
* Si ambos relojes están conectados, el registro de desplazamiento siempre tiene un pulso de anticipación sobre el registro de memoria.
* El registro de memoria cuenta con un pin de entrada en serie (Ds), un pin de salida en serie (Q) y un botón de reinicio asíncrono (nivel bajo).
* El registro de memoria produce un bus con salida paralela de 8 bits y en tres estados.
* Cuando OE está habilitado (nivel bajo), los datos en el registro de memoria se emiten al bus (Q0 ~ Q7).

**Conexión**

|wiring_74hc_led|

**Código**

.. note::

    * Puedes abrir el archivo ``5.1_microchip_74hc595.ino`` en la ruta ``kepler-kit-main/arduino/5.1_microchip_74hc595``.
    * O copia este código en el **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/71854882-0c1b-4d09-b3e7-5ef7272f7293/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Cuando el programa esté en ejecución, podrás ver cómo los LEDs se encienden uno tras otro.

**¿Cómo funciona?**

Declara un array donde se almacenan varios números binarios de 8 bits que se utilizan para cambiar el estado de los ocho LEDs controlados por el 74HC595.

.. code-block:: arduino

    int datArray[] = {0b00000000, 0b00000001, 0b00000011, 0b00000111, 0b00001111, 0b00011111, 0b00111111, 0b01111111, 0b11111111};

Configura ``STcp`` a nivel bajo primero y luego a nivel alto. Esto generará un pulso ascendente en ``STcp``.

.. code-block:: arduino

    digitalWrite(STcp,LOW); 

La función ``shiftOut()`` desplaza un byte de datos un bit a la vez, lo que significa que desplaza un byte de datos en datArray[num] al registro de desplazamiento con el pin DS. MSBFIRST indica que se mueve desde los bits más altos.

.. code-block:: arduino

    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);

Después de ejecutar ``digitalWrite(STcp,HIGH)``, STcp estará en el flanco ascendente. En ese momento, los datos en el registro de desplazamiento se moverán al registro de memoria.

.. code-block:: arduino

    digitalWrite(STcp,HIGH);

Un byte de datos se transferirá al registro de memoria después de 8 veces. Luego, los datos del registro de memoria se envían al bus (Q0-Q7). Por ejemplo, desplazando ``B00000001`` se encenderá el LED controlado por Q0 y apagará los LEDs controlados por Q1~Q7.
