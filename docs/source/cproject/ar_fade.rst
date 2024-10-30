.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_fade:

2.3 - Atenuación de un LED
==================================

Hasta ahora, solo hemos utilizado dos señales de salida: nivel alto y nivel bajo (también llamados 1 y 0, ENCENDIDO y APAGADO), lo que se denomina salida digital.
Sin embargo, en la práctica, muchos dispositivos no solo funcionan con ENCENDIDO/APAGADO; por ejemplo, al ajustar la velocidad de un motor o la intensidad de una lámpara de escritorio.
Antes se utilizaba un deslizador que ajustaba la resistencia para lograr esto, pero este método es poco confiable e ineficiente.
Por ello, la Modulación por Ancho de Pulso (PWM) ha surgido como una solución práctica para problemas más complejos.

Un pulso de salida digital compuesto por niveles alto y bajo se denomina pulso, y el ancho de este pulso se puede ajustar variando la velocidad de ENCENDIDO/APAGADO.

Simplificando, cuando estamos en un período corto (como 20 ms, el tiempo de persistencia visual de la mayoría de las personas),
si el LED se enciende, se apaga y se enciende de nuevo, no parecerá que se apaga, pero la intensidad de la luz será levemente menor.
En este período, cuanto más tiempo permanezca encendido el LED, mayor será su brillo.
En otras palabras, en el ciclo, cuanto más amplio sea el pulso, mayor será la "intensidad de señal eléctrica" que el microcontrolador entrega.
Así es como el PWM controla la intensidad de un LED (o la velocidad de un motor).

* `Pulse-width modulation - Wikipedia <https://en.wikipedia.org/wiki/Pulse-width_modulation>`_

Existen algunos aspectos a tener en cuenta cuando se usa PWM en Pico W. Observa la siguiente imagen.

|pin_pwm|

Cada pin GPIO del Pico W soporta PWM, pero en realidad tiene un total de 16 salidas PWM independientes (en lugar de 30), distribuidas entre GP0 a GP15 en el lado izquierdo, y el PWM de los GPIO del lado derecho es equivalente a una copia de los del izquierdo.

Es importante evitar asignar el mismo canal PWM para diferentes funciones en el programa (por ejemplo, GP0 y GP16 comparten PWM_0A).

Con estos conceptos claros, intentemos lograr el efecto de atenuación en el LED.

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

Este proyecto utiliza el mismo circuito que el primer proyecto :ref:`ar_led`, pero el tipo de señal es diferente. En el primer proyecto se enviaban directamente niveles digitales alto y bajo (0 y 1) desde GP15 para encender y apagar el LED. En este proyecto, se envía una señal PWM desde GP15 para controlar la intensidad del LED.

**Conexión**

|wiring_led|

**Código**

.. note::

    * Puedes abrir el archivo ``2.3_fading_led.ino`` en la ruta ``kepler-kit-main/arduino/2.3_fading_led``.
    * O copia este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/86807da4-4714-4d3c-b6af-0f1b9a62223b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


El LED aumentará gradualmente su brillo a medida que el programa se ejecute.

**¿Cómo funciona?**

Declara el pin 15 como ledPin.

.. code-block:: C

    const int ledPin = 15;

En el ``loop()``, ``analogWrite()`` asigna al ledPin un valor analógico (onda PWM) entre 0 y 255 para modificar la intensidad del LED.

.. code-block:: C

    analogWrite(ledPin, value);

Usando un bucle for, el valor de ``analogWrite()`` puede ajustarse paso a paso entre el valor mínimo (0) y el máximo (255).

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
    }

Para visualizar claramente el efecto, es necesario agregar un ``delay(30)`` dentro del ciclo for para controlar el tiempo de cambio de intensidad.

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
        delay(30);
    }
