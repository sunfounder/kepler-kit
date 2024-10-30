.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_relay:

2.16 - Controlar Otro Circuito
=================================

En nuestra vida diaria, podemos presionar un interruptor para encender o 
apagar una lámpara. Pero, ¿qué sucede si quieres controlar la lámpara con 
el Pico W para que se apague automáticamente después de diez minutos?

Un relé puede ayudarte a lograrlo.

Un relé es en realidad un tipo especial de interruptor controlado por un lado del circuito (generalmente de bajo voltaje) y que se usa para controlar el otro lado del circuito (usualmente de alto voltaje). Esto facilita la modificación de nuestros electrodomésticos para ser controlados por un programa, convertirlos en dispositivos inteligentes o incluso acceder a Internet.

.. warning::
    La modificación de electrodomésticos conlleva grandes peligros; no lo intentes a la ligera. Hazlo bajo la supervisión de un profesional.

* :ref:`cpn_relay`

Aquí usaremos un circuito simple alimentado por un módulo de alimentación de protoboard como ejemplo de cómo controlarlo mediante un relé.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Conexión**

Primero, construye un circuito de bajo voltaje para controlar un relé. Conducir 
el relé requiere una alta corriente, por lo que es necesario un transistor, y aquí utilizamos el S8050.

|sch_relay_1|

|wiring_relay_1|

Se utiliza un diodo de protección aquí para proteger el circuito. El cátodo es el extremo con la banda plateada conectada a la fuente de alimentación, y el ánodo está conectado al transistor.

Cuando la entrada de voltaje cambia de Alto (5V) a Bajo (0V), el transistor cambia de saturación (amplificación, saturación y corte) a corte, y de repente no hay forma de que la corriente pase por la bobina.

En este punto, si no existiera este diodo de rueda libre, la bobina generaría un potencial eléctrico autoinducido en ambos extremos que es varias veces mayor que el voltaje de alimentación. Este voltaje, sumado al del transistor, es suficiente para dañarlo.

Al añadir el diodo, la bobina y el diodo forman instantáneamente un nuevo circuito alimentado por la energía almacenada en la bobina, evitando así que el voltaje excesivo dañe dispositivos como transistores en el circuito.

* :ref:`cpn_diode`
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

El programa está listo para ejecutarse, y después de iniciarlo escucharás un sonido de "tik tok", que es el sonido del contacto interno de la bobina del relé activándose y desactivándose.

Luego conectamos los dos extremos del circuito de carga a los pines 3 y 6 del relé, respectivamente.

..(Tomamos como ejemplo el circuito simple alimentado por el módulo de alimentación de protoboard descrito en el artículo anterior).

|sch_relay_2|

|wiring_relay_2|

En este punto, el relé podrá controlar el encendido y apagado del circuito de carga.

**Código**

.. note::

    * Puedes abrir el archivo ``2.16_relay.ino`` en la ruta de ``kepler-kit-main/arduino/2.16_relay``.
    * O copiar este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/3be98f10-8223-49f2-8238-2acc53ebbf80/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Al ejecutar el código, el relé cambiará el estado de operación del circuito controlado cada dos segundos. 
Puedes comentar manualmente una de las líneas para ver más claramente la correspondencia entre el circuito del relé y el circuito de carga.


**Más Información**

El pin 3 del relé está normalmente abierto y solo se activa cuando la bobina del contactor está en operación; el pin 4 está normalmente cerrado y se activa cuando la bobina del contactor está energizada. 

El pin 1 está conectado al pin 6 y es el terminal común del circuito de carga. 

Al cambiar un extremo del circuito de carga del pin 3 al pin 4, podrás obtener exactamente el estado de operación opuesto.
