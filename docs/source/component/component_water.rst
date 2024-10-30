.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_water_level:

Módulo Sensor de Nivel de Agua
=================================

|img_water_sensor|

El sensor de nivel de agua transmite la señal del nivel detectado al controlador, y el ordenador en el controlador compara la señal medida con la señal establecida para determinar la desviación, emitiendo comandos de "encendido" y "apagado" a la válvula eléctrica de suministro de agua según la naturaleza de la desviación, para asegurar que el recipiente alcance el nivel de agua establecido.

El sensor de nivel de agua tiene diez trazas de cobre expuestas, cinco para las trazas de potencia y cinco para las trazas del sensor, que se cruzan y conectan por el agua cuando el sensor está sumergido.
La placa de circuito tiene un LED de alimentación que se enciende cuando la placa está energizada.

La combinación de estas trazas actúa como una resistencia variable, cambiando el valor de la resistencia de acuerdo con el nivel de agua.
Para ser más precisos, cuanto más agua esté inmerso el sensor, mejor será la conductividad y menor la resistencia. Por el contrario, cuanto menos conductividad tenga, mayor será la resistencia.
Luego, el sensor procesará el voltaje de la señal de salida, que se enviará al microcontrolador, ayudándonos así a determinar el nivel de agua.

.. warning:: 
    El sensor no debe sumergirse completamente en el agua, por favor, solo deje la parte donde se encuentran las diez trazas en contacto con el agua. Además, energizar el sensor en un entorno húmedo acelerará la corrosión de la sonda y reducirá la vida útil del sensor, por lo que recomendamos suministrar energía solo cuando se estén tomando lecturas.


**Example**

* :ref:`py_water` (Para usuarios de MicroPython)
* :ref:`ar_water` (Para usuarios de Arduino)
* :ref:`per_water_tank` (Para usuarios de Piper Make)
