.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_lipo_charger:

Módulo Cargador Li-po
=================================================

|lipo_module|

Este es un módulo cargador de baterías Li-po diseñado para Raspberry Pi Pico/Pico H/Pico W. Simplemente conéctalo junto con el Pico al protoboard como se muestra a continuación, luego conecta la batería en el otro extremo y estará listo para usar.

Cuando conectas el Pico W a un cable USB conectado a una computadora o toma de corriente, la luz indicadora del módulo cargador Li-po se encenderá, lo que significa que la batería se cargará al mismo tiempo. Al desconectar el cable USB, el Pico W será alimentado por la batería, permitiendo que tu proyecto continúe funcionando.

.. note::
    Para algunos ordenadores con bajo rendimiento, puede suceder que si conectas tu Pico W a la computadora con este módulo de carga conectado, el ordenador no reconozca tu Pico W.

    La razón es que, al conectar el cargador, mientras se carga la batería, el voltaje del puerto USB disminuye, resultando en un suministro insuficiente de energía para que el Pico W sea reconocido por la computadora.
    
    En este caso, necesitas desconectar el módulo de carga Li-po y luego volver a conectar el Pico W.

|lipo_wire|

**Características**

* Voltaje de entrada: 5V
* Voltaje de salida: 3.3V
* Tamaño: 20mmx7mm
* Modelo de interfaz: PH2.0
* Hay un soporte de batería de 1A compatible y una batería 18650 de 800mAh para usar en conjunto.

**Esquema**

|sch_lipo_charger|
