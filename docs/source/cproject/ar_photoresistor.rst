.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Explora a fondo Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_photoresistor:


2.12 - Siente la Luz
=================================

El fotorresistor es un dispositivo típico para entradas analógicas, y su uso es muy similar al de un potenciómetro. Su valor de resistencia depende de la intensidad de la luz: a mayor intensidad de luz, menor resistencia, y viceversa.


* :ref:`cpn_photoresistor`

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Esquema**

|sch_photoresistor|

En este circuito, el resistor de 10K y el fotorresistor están conectados en serie, y la corriente que pasa por ellos es la misma. El resistor de 10K actúa como protección, y el pin GP28 lee el valor después de la conversión de voltaje del fotorresistor.

Cuando la luz se intensifica, la resistencia del fotorresistor disminuye, entonces su voltaje también disminuye, y el valor de GP28 también disminuirá. Si la luz es lo suficientemente fuerte, la resistencia del fotorresistor se acercará a 0, y el valor de GP28 será cercano a 0. En este punto, el resistor de 10K desempeña un rol protector para evitar un cortocircuito al impedir que se unan 3.3V y GND.

Si colocas el fotorresistor en la oscuridad, el valor de GP28 aumentará. En una situación lo suficientemente oscura, la resistencia del fotorresistor será infinita, y su voltaje se aproximará a 3.3V (el resistor de 10K es despreciable), y el valor de GP28 será cercano al valor máximo de 65535.

La fórmula de cálculo se muestra a continuación.

    (Vp/3.3V) x 65535 = Ap

**Conexión**

|wiring_photoresistor|

**Código**

.. note::

    * Puedes abrir el archivo ``2.12_feel_the_light.ino`` en la ruta ``kepler-kit-main/arduino/2.12_feel_the_light``.
    * O copiar este código en el **IDE de Arduino**.
    * No olvides seleccionar la placa Raspberry Pi Pico y el puerto correcto antes de hacer clic en el botón **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/44074b9e-3e4e-475b-af37-689254f87ab2/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el programa, el Monitor Serial mostrará los valores del fotorresistor. Puedes iluminarlo con una linterna o cubrirlo con la mano para observar cómo cambia el valor.
