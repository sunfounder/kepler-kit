.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_water:

2.14 - Detectar el Nivel de Agua
=====================================

|img_water_sensor|

El sensor de agua está diseñado para la detección de agua y se puede utilizar ampliamente para detectar lluvia, nivel de agua e incluso fugas de líquidos.

Este sensor mide el nivel de agua utilizando una serie de trazas de cables paralelos expuestos para medir el tamaño de las gotas o el volumen de agua. El volumen de agua se convierte fácilmente en una señal analógica, y el valor de salida analógica puede ser leído directamente por la placa de control para activar una alarma de nivel de agua.

.. warning:: 

    El sensor no debe sumergirse completamente en agua; solo se debe dejar la parte donde se encuentran las diez trazas en contacto con el agua. Además, alimentar el sensor en un entorno húmedo acelerará la corrosión de la sonda y reducirá su vida útil, por lo que se recomienda alimentarlo únicamente al tomar lecturas.

* :ref:`cpn_water_level`

**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

Es muy conveniente adquirir un kit completo; aquí está el enlace:

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Esquema**

|sch_water|

**Cableado**

|wiring_water|

**Código**

.. note::

    * Puedes abrir el archivo ``2.14_feel_the_water_level.ino`` en la ruta ``kepler-kit-main/arduino/2.14_feel_the_water_level``.
    * O copia este código en **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/32ee87a1-08eb-482f-bf4c-b12b24ef05c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Después de ejecutar el programa, sumerge lentamente el módulo del sensor de agua en el agua. A medida que aumenta la profundidad, la consola imprimirá un valor más alto.

**Aprende Más**

Hay una forma de usar el módulo de entrada analógica como un módulo digital.

Primero, toma una lectura del sensor de agua en un ambiente seco, regístrala y utilízala como valor umbral. Luego, completa la programación y vuelve a leer el sensor de agua. Cuando la lectura del sensor de agua se desvía significativamente de la lectura en un ambiente seco, se puede inferir la presencia de líquido. Esto significa que al colocar este dispositivo cerca de una tubería de agua, puede detectar si hay una fuga en la tubería.


.. note::

    * Puedes abrir el archivo ``2.14_water_level_threshold.ino`` en la ruta ``kepler-kit-main/arduino/2.14_water_level_threshold``.
    * O copia este código en **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. :raw-code:
