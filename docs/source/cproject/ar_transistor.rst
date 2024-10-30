.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_transistor:

2.15 - Dos Tipos de Transistores
==========================================

Este kit incluye dos tipos de transistores, S8550 y S8050, siendo el primero un transistor PNP y el segundo un transistor NPN. Ambos tienen un aspecto muy similar, por lo que es necesario verificar cuidadosamente sus etiquetas.
Cuando una señal de nivel alto pasa por un transistor NPN, este se energiza. Sin embargo, un transistor PNP requiere una señal de nivel bajo para funcionar. Ambos tipos de transistores se utilizan con frecuencia en interruptores sin contacto, como en este experimento.

|img_NPN&PNP|

¡Vamos a usar un LED y un botón para comprender cómo se utiliza un transistor!

:ref:`cpn_transistor`

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

**Conexión para transistor NPN (S8050)**

|sch_s8050|

En este circuito, cuando se presiona el botón, GP14 está en alto.

Programando GP15 para que emita un nivel alto, después de una resistencia limitadora de corriente de 1k (para proteger el transistor), el S8050 (transistor NPN) permite la conducción, permitiendo así que el LED se encienda.

|wiring_s8050|

.. 1. Conecta 3V3 y GND de Pico W a la barra de alimentación de la protoboard.
.. #. Conecta el ánodo del LED a la barra de alimentación positiva mediante una resistencia de 220Ω.
.. #. Conecta el cátodo del LED al **colector** del transistor.
.. #. Conecta la base del transistor al pin GP15 a través de una resistencia de 1kΩ.
.. #. Conecta el **emisor** del transistor a la barra de alimentación negativa.
.. #. Conecta un lado del botón al pin GP14, y utiliza una resistencia de 10kΩ para conectar el mismo lado a la barra de alimentación negativa. El otro lado se conecta a la barra de alimentación positiva.

.. .. note::
..     * Los colores de la resistencia de 220Ω son rojo, rojo, negro, negro y marrón.
..     * Los colores de la resistencia de 1kΩ son marrón, negro, negro, marrón y marrón.
..     * Los colores de la resistencia de 10kΩ son marrón, negro, negro, rojo y marrón.

**Conexión para transistor PNP (S8550)**

|sch_s8550|

En este circuito, GP14 está en bajo por defecto y cambiará a alto cuando se presione el botón.

Programando GP15 para que emita **bajo**, después de una resistencia limitadora de corriente de 1k (para proteger el transistor), el S8550 (transistor PNP) permite la conducción, permitiendo que el LED se encienda.

La única diferencia que notarás entre este circuito y el anterior es que en el circuito anterior el cátodo del LED está conectado al **colector** del **S8050 (transistor NPN)**, mientras que en este está conectado al **emisor** del **S8550 (transistor PNP)**.

|wiring_s8550|

.. 1. Conecta 3V3 y GND de Pico W a la barra de alimentación de la protoboard.
.. #. Conecta el ánodo del LED a la barra de alimentación positiva mediante una resistencia de 220Ω.
.. #. Conecta el cátodo del LED al **emisor** del transistor.
.. #. Conecta la base del transistor al pin GP15 a través de una resistencia de 1kΩ.
.. #. Conecta el **colector** del transistor a la barra de alimentación negativa.
.. #. Conecta

**Código**

.. note::

    * Puedes abrir el archivo ``2.15_transistor.ino`` en la ruta ``kepler-kit-main/arduino/2.15_transistor``.
    * O copia este código en **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/77c437de-028f-47c1-9d79-177e90eb0599/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Los dos tipos de transistores se pueden controlar con el mismo código. Cuando presionamos el botón, el Pico W enviará una señal de nivel alto al transistor; al soltarlo, enviará una señal de nivel bajo.
Podemos ver que han ocurrido fenómenos opuestos en los dos circuitos.

* El circuito que utiliza el S8050 (transistor NPN) se encenderá cuando se presione el botón, lo que significa que está recibiendo un circuito de conducción de nivel alto;
* El circuito que utiliza el S8550 (transistor PNP) se encenderá cuando se suelte el botón, lo que significa que está recibiendo un circuito de conducción de nivel bajo.
