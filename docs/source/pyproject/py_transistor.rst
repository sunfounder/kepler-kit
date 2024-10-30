.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_transistor:

2.15 Dos Tipos de Transistores
=====================================

Este kit incluye dos tipos de transistores, el S8550 y el S8050; el primero es PNP y el segundo es NPN. Son muy similares en apariencia, por lo que es necesario verificar cuidadosamente sus etiquetas. Cuando un transistor NPN recibe una señal de alto nivel, se activa, mientras que un transistor PNP necesita una señal de bajo nivel para funcionar. Ambos tipos se utilizan frecuentemente en interruptores sin contacto, como en este experimento.

|img_NPN&PNP|

Vamos a usar un LED y un botón para entender cómo funciona el transistor.

:ref:`cpn_transistor`

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
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|

**Cómo conectar el transistor NPN (S8050)**

|sch_s8050|

En este circuito, al presionar el botón, GP14 se activa en alto.

Al programar GP15 para que emita una señal alta y tras un resistor limitador de corriente de 1k (para proteger el transistor), se permite que el S8050 (transistor NPN) conduzca, encendiendo así el LED.

|wiring_s8050|

**Cómo conectar el transistor PNP (S8550)**

|sch_s8550|

En este circuito, GP14 está en bajo por defecto y cambiará a alto cuando se presione el botón.

Al programar GP15 para que emita una señal **baja** y a través de un resistor limitador de corriente de 1k (para proteger el transistor), se permite que el S8550 (transistor PNP) conduzca, encendiendo así el LED.

La única diferencia que notarás entre este circuito y el anterior es que, en el circuito anterior, el cátodo del LED está conectado al **colector** del **S8050 (transistor NPN)**, mientras que en este caso está conectado al **emisor** del **S8550 (transistor PNP)**.

|wiring_s8550|

**Código**

.. note::

    * Abre el archivo ``2.15_transistor.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.
    * No olvides seleccionar el intérprete "MicroPython (Raspberry Pi Pico)" en la esquina inferior derecha.
    * Para tutoriales detallados, consulta :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)    

    while True:
        button_status = button.value()
        if button_status== 1:
            signal.value(1)
        elif button_status == 0:
            signal.value(0)



Ambos tipos de transistores pueden ser controlados con el mismo código. Cuando presionamos el botón, Pico W enviará una señal de alto nivel al transistor; al soltarlo, enviará una señal de bajo nivel.
Podemos observar fenómenos diametralmente opuestos en los dos circuitos:

* El circuito que utiliza el S8050 (transistor NPN) encenderá el LED cuando se presiona el botón, indicando un circuito de conducción de alto nivel.
* El circuito que utiliza el S8550 (transistor PNP) encenderá el LED cuando se suelta el botón, indicando un circuito de conducción de bajo nivel.
