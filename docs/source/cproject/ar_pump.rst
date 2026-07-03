.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_pump:

3.6 - Bombeo de Agua
=======================

Las bombas centrífugas pequeñas son ideales para proyectos de riego automático 
de plantas. También se pueden utilizar para crear pequeñas fuentes de agua inteligentes.

Su componente de potencia es un motor eléctrico, que se controla de la misma forma que un 
motor convencional.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Conecta el tubo a la salida de la bomba, sumerge la bomba en agua y enciéndela.
    #. Debes asegurarte de que el nivel del agua esté siempre por encima del motor. Si el motor funciona en vacío, puede dañarse por generación de calor y producir ruido.
    #. Si estás regando plantas, evita que el suelo entre en la bomba, ya que puede obstruirla.
    #. Si no sale agua del tubo, puede haber agua residual bloqueando el flujo de aire; debes vaciar el tubo primero.

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Power Pack
        - 1
        -  
    *   - 8
        - Soporte para batería
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Esquema**

|sch_pump|

**Conexión**

.. note::

    * Dado que la bomba requiere una corriente alta, usamos un módulo de carga Li-po para alimentar el motor por razones de seguridad.
    * Asegúrate de que tu módulo de carga Li-po esté conectado tal como se muestra en el diagrama. De lo contrario, un cortocircuito podría dañar tu batería y el circuito.

|wiring_pump|

**Código**

.. note::

    * Puedes abrir el archivo ``3.6_pumping.ino`` en la ruta ``kepler-kit-main/arduino/3.6_pumping``.
    * O copiar este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/4194feb8-92d4-4ab4-b51c-286d014af0a6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



Una vez que el código se ejecute, la bomba comenzará a funcionar y verás que el agua fluye por el tubo.

.. note::

    * Si no puedes subir el código nuevamente, esta vez debes conectar el pin **RUN** en el Pico W a GND con un cable para reiniciarlo y, luego, desconectar el cable para ejecutar el código otra vez.
    * Esto se debe a que el motor está operando con demasiada corriente, lo cual puede hacer que el Pico W se desconecte de la computadora.

    |wiring_run_reset|
