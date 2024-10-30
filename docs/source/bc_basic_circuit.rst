.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Únete a otros entusiastas y explora en profundidad el mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Acceso Exclusivo**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Circuito Electrónico
========================

Muchos de los objetos que usas a diario funcionan con electricidad, como las luces de tu hogar y la computadora desde la que lees esto.

Para utilizar la electricidad, debes crear un circuito eléctrico. Un circuito eléctrico está compuesto de cables metálicos y componentes eléctricos y electrónicos.

Los circuitos requieren una fuente de alimentación. En tu hogar, la mayoría de los electrodomésticos (como televisores y luces) funcionan gracias a los enchufes de pared. Sin embargo, muchos circuitos más pequeños y portátiles (como juguetes electrónicos y teléfonos móviles) funcionan con baterías. Una batería tiene dos terminales: el positivo, marcado con un signo más (+), y el negativo, que suele simbolizarse con un signo menos (-), aunque no siempre aparece en las baterías.

Para que fluya la corriente, debe existir un camino conductor que conecte el terminal positivo con el negativo, a lo que se le llama un circuito cerrado (si está desconectado, se le llama un circuito abierto). La corriente eléctrica pasa a través de dispositivos como lámparas para que funcionen (por ejemplo, para que se enciendan).

|bc1|

Una Pico W tiene pines de salida de potencia (positivo) y pines de tierra (negativo).
Puedes utilizar estos pines como las partes positiva y negativa de la fuente de alimentación al conectar la Pico W a una fuente de energía.

|bc2| 

Con electricidad, puedes crear trabajos con luz, sonido y movimiento.
Puedes encender un LED conectando su patilla larga al terminal positivo y la patilla corta al terminal negativo.
El LED se quemará rápidamente si haces esto sin añadir una resistencia de 220Ω en el circuito para protegerlo.

El circuito que forman se muestra a continuación.

|bc2.5| 

Podrías preguntarte: ¿cómo construyo este circuito? ¿Sostengo los cables con la mano o los pego con cinta?

En esta situación, las protoboards sin soldadura serán tus mejores aliadas.

.. _bc_bb:

¡Hola, Protoboard!
------------------------------

Una protoboard es una placa de plástico rectangular con numerosos agujeros. 
Estos agujeros nos permiten insertar fácilmente componentes electrónicos y construir circuitos electrónicos.
Las protoboards no fijan permanentemente los componentes, por lo que podemos reparar un circuito y empezar de nuevo fácilmente si algo sale mal.

.. note::
    No se necesitan herramientas especiales para usar protoboards. Sin embargo, muchos componentes electrónicos son muy pequeños, por lo que un par de pinzas puede ayudarnos a manipular las piezas mejor.

En Internet, podemos encontrar mucha información sobre las protoboards.

* `How to Use a Breadboard - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `What is a BREADBOARD? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_


Aquí hay algunos puntos que debes conocer sobre las protoboards.

#. Cada grupo de media fila (como la columna A-E en la fila 1 o la columna F-J en la fila 3) está conectado. Por lo tanto, si una señal eléctrica ingresa por A1, puede salir por B1, C1, D1, E1, pero no por F1 ni A2.

#. En la mayoría de los casos, ambos lados de la protoboard se usan como buses de alimentación, y los agujeros en cada columna (aproximadamente 50 agujeros) están conectados entre sí. Por lo general, los suministros positivos se conectan a los agujeros cercanos al cable rojo, y los negativos a los del cable azul.

#. En un circuito, la corriente fluye del polo positivo al polo negativo después de pasar por la carga. En este caso, puede ocurrir un cortocircuito.

|bc3|

¡Sigamos la dirección de la corriente para construir el circuito!

1. En este circuito, usamos el pin 3V3 de la Pico W para alimentar el LED. Conecta un cable macho a macho (M2M) al bus de energía rojo.
#. Para proteger el LED, la corriente debe pasar por una resistencia de 220 ohmios. Conecta un extremo de la resistencia al bus de energía rojo y el otro extremo a una fila libre en la protoboard (en mi circuito, la fila 24).

    .. note::
        El código de colores de la resistencia de 220 ohmios es rojo, rojo, negro, negro y marrón.

#. Si observas el LED, verás que uno de sus terminales es más largo. Conecta el terminal más largo a la misma fila que la resistencia, y el terminal más corto a la fila opuesta a través de la división central en la protoboard.

    .. note::
        El terminal largo es el ánodo, que representa el lado positivo del circuito; el corto es el cátodo, que representa el lado negativo. 

        El ánodo debe conectarse al pin GPIO a través de una resistencia; el cátodo al pin GND.

#. Con un cable M2M, conecta el terminal corto del LED al bus de energía negativo de la protoboard.
#. Conecta el pin GND de la Pico W al bus de energía negativo usando un cable de salto.

Precaución con los cortocircuitos
---------------------------------------

Los cortocircuitos ocurren cuando dos componentes que no deberían estar conectados lo están accidentalmente. 
Este kit incluye resistencias, transistores, condensadores, LEDs, etc., que tienen terminales largos que pueden tocarse y causar un cortocircuito. Algunos cortos simplemente impiden el funcionamiento del circuito, mientras que otros pueden dañar los componentes, especialmente si ocurren entre la fuente de energía y el bus de tierra, calentando mucho el circuito y derritiendo el plástico de la protoboard o incluso quemando componentes.

Por lo tanto, siempre asegúrate de que las patillas de todos los componentes en la protoboard no se toquen entre sí.

Dirección del circuito
-------------------------------

Los circuitos tienen orientación, y esta es importante en ciertos componentes. Algunos dispositivos tienen polaridad, lo que significa que deben conectarse correctamente según sus polos positivo y negativo. Los circuitos montados en la dirección incorrecta no funcionarán.

|bc3|

Si inviertes el LED en este circuito simple que construimos antes, verás que deja de funcionar.

En contraste, algunos dispositivos, como las resistencias en este circuito, no tienen dirección, por lo que puedes probar invirtiéndolas sin afectar el funcionamiento normal del LED.

La mayoría de los componentes y módulos con etiquetas como "+", "-", "GND", "VCC" o con terminales de distintas longitudes deben conectarse en una orientación específica.

Protección del circuito
-------------------------------------

La corriente es la velocidad a la que los electrones pasan por un punto en un circuito eléctrico completo. Básicamente, corriente = flujo. El amperio es la unidad internacional de medida de la corriente, y expresa la cantidad de electrones (a veces llamada "carga eléctrica") que pasan por un punto en un circuito en un tiempo dado.

La fuerza que impulsa el flujo de corriente se llama voltaje y se mide en voltios (V).

La resistencia (R) es la propiedad del material que restringe el flujo de corriente y se mide en ohmios (Ω).

Según la ley de Ohm (siempre que la temperatura se mantenga constante), la corriente, el voltaje y la resistencia son proporcionales.
La corriente en un circuito es proporcional a su voltaje e inversamente proporcional a su resistencia.

Por lo tanto, corriente (I) = voltaje (V) / resistencia (R).

* `Ohm's law - Wikipedia <https://en.wikipedia.org/wiki/Ohm%27s_law>`_

Podemos hacer un simple experimento sobre la ley de Ohm.

|bc3|

Al cambiar el cable de conexión de 3V3 a 5V (es decir, VBUS, el pin 40 de la Pico W), el LED se iluminará más.
Si cambias la resistencia de 220 ohmios a 1000 ohmios (anillo de color: marrón, negro, negro, marrón y marrón), notarás que el LED se vuelve más tenue. Cuanto mayor sea la resistencia, menos brillo tendrá el LED.

.. note::
    Para una introducción a las resistencias y cómo calcular valores de resistencia, consulta :ref:`cpn_resistor`.

La mayoría de los módulos empaquetados solo necesitan acceso a un voltaje adecuado (normalmente 3.3V o 5V), como el módulo ultrasónico.

Sin embargo, en tus circuitos personalizados, debes ser consciente del voltaje de alimentación y del uso de resistencias para los dispositivos eléctricos.

Por ejemplo, los LEDs suelen consumir 20mA de corriente, y su caída de voltaje es de aproximadamente 1.8V. Según la ley de Ohm, si usamos una fuente de alimentación de 5V, necesitamos conectar una resistencia de al menos 160 ohmios ((5-1.8)/20mA) para evitar que el LED se queme.

