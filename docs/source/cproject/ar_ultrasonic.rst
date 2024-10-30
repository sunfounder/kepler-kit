.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _ar_ultrasonic:

6.1 - Medición de Distancia
======================================

El módulo sensor ultrasónico funciona bajo el principio de sonar y radar para determinar la distancia a un objeto.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Esquema**

|sch_ultrasonic|

**Cableado**

|wiring_ultrasonic|

**Código**

.. note::

    * Puedes abrir el archivo ``6.1_ultrasonic.ino`` en la ruta ``kepler-kit-main/arduino/6.1_ultrasonic``.
    * O copia este código en **Arduino IDE**.
    * No olvides seleccionar la placa (Raspberry Pi Pico) y el puerto correcto antes de hacer clic en el botón **Subir**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Una vez que el programa esté en funcionamiento, el Monitor Serial imprimirá la distancia entre el sensor ultrasónico y el obstáculo delante de él.


**¿Cómo funciona?**

Para la aplicación del sensor ultrasónico, podemos consultar directamente la subfunción.

.. code-block:: arduino

    float readSensorData(){// ...}

``PING`` se activa mediante un pulso HIGH de 2 microsegundos o más. (Antes de esto, envía un pulso corto LOW para asegurar un pulso limpio de HIGH).

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

El pin echo se usa para leer la señal de PING, un pulso HIGH cuya duración es 
el tiempo (en microsegundos) desde el envío del ping hasta la recepción del eco 
reflejado por el objeto.

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

La velocidad del sonido es de 340 m/s o 29 microsegundos por centímetro.

Esto da la distancia recorrida por el ping (ida y vuelta), así que dividimos 
por 2 para obtener la distancia al obstáculo.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  

Ten en cuenta que el sensor ultrasónico pausará el programa mientras esté 
funcionando, lo que puede causar cierto retraso al escribir proyectos más complejos.
