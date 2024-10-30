.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_reed:

2.9 - Detecta el Magnetismo
===============================

El tipo más común de interruptor reed contiene un par de láminas metálicas flexibles magnetizables, cuyas puntas están separadas por un pequeño espacio cuando el interruptor está abierto.

Un campo magnético, ya sea de un electroimán o un imán permanente, hará que las láminas se atraigan entre sí, completando así el circuito eléctrico.
Cuando el campo magnético desaparece, la fuerza de resorte de las láminas las separa y abre el circuito.

Un ejemplo común de aplicación de un interruptor reed es detectar la apertura de puertas o ventanas para un sistema de alarma de seguridad.

* :ref:`cpn_reed`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Esquema**

|sch_reed|

Por defecto, el pin GP14 está en bajo; cuando el imán está cerca del interruptor reed, pasará a estado alto.

La función de la resistencia de 10K es mantener el GP14 en un nivel bajo constante cuando no hay un imán cerca.

**Conexión**

|wiring_reed|

**Código**

.. note::

    * Puedes abrir el archivo ``2.9_feel_the_magnetism.ino`` en la ruta ``kepler-kit-main/arduino/2.9_feel_the_magnetism``.
    * O copiar este código en el **Arduino IDE**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bba18c-7921-4df9-806f-deffce17de9a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Cuando un imán se acerca, el circuito se cerrará, de forma similar al botón en el capítulo :ref:`ar_button`.

.. **Learn More**

.. This time, we tried a flexible way of using switches: interrupt requests, or IRQs.:  interrupt requests, or IRQs.

.. For example, you are reading a book page by page, as if a program is executing a thread. At this time, someone came to you to ask a question and interrupted your reading. Then the person is executing the interrupt request: asking you to stop what you are doing, answer his questions, and then let you return to reading the book after the end.

.. The interrupt request also works in the same way, it allows certain operations to interrupt the main program. 

.. .. :raw-code:

.. .. note::

..    * You can open the file ``2.9_feel_the_magnetism_irq.ino`` under the path of ``kepler-kit-main/arduino/2.9_feel_the_magnetism_irq``. 
..    * Or copy this code into **Arduino IDE**.

.. 
..     * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.




.. A callback function ``detected()`` is defined here, called the interrupt handler. It will be executed when an interrupt request is triggered.
.. Then, an interrupt request is set up in ``setup``, which contains two parts: ``mode`` and ``ISR``.

.. In this program, ``mode`` is ``RISING``, which indicates that the value of the pin is raised from low to high (i.e, button pressed).

.. ``ISR`` is ``detected`` , the callback function we defined.

.. * `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_