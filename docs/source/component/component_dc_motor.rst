.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_motor:

Motor DC
===================

|img_dc_motor|

Este es un motor de corriente continua (DC) de 3V. Cuando se aplica un nivel alto y un nivel bajo a cada uno de los dos terminales, el motor comenzará a girar.

* **Tamaño**: 25*20*15MM
* **Voltaje de Operación**: 1-6V
* **Corriente sin Carga** (3V): 70mA
* **Velocidad sin Carga** (3V): 13000RPM
* **Corriente de Bloqueo** (3V): 800mA
* **Diámetro del Eje**: 2mm

El motor de corriente continua (DC) es un actuador que convierte energía eléctrica en energía mecánica de manera continua. Los motores DC hacen que bombas rotativas, ventiladores, compresores, impulsores y otros dispositivos funcionen produciendo una rotación angular continua.

Un motor DC se compone de dos partes: la parte fija del motor llamada **estator** y la parte interna del motor llamada **rotor** (o **armadura** de un motor DC) que gira para producir movimiento.
La clave para generar movimiento es posicionar la armadura dentro del campo magnético del imán permanente (cuyo campo se extiende del polo norte al polo sur). La interacción entre el campo magnético y las partículas cargadas en movimiento (el cable que transporta la corriente genera el campo magnético) produce el par que hace girar la armadura.

|img_dc_motor_sche|

La corriente fluye desde el terminal positivo de la batería a través del circuito, pasando por las escobillas de cobre hacia el conmutador, y luego a la armadura.
Pero debido a las dos interrupciones en el conmutador, este flujo se invierte a la mitad de cada rotación completa.
Esta inversión continua esencialmente convierte la corriente continua (DC) de la batería en corriente alterna (AC), permitiendo que la armadura experimente el par en la dirección correcta y en el momento adecuado para mantener la rotación.

* `DC Motor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Fleming's left-hand rule for motors - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_



**Ejemplos**

* :ref:`py_motor` (Para usuarios de MicroPython)
* :ref:`ar_motor` (Para usuarios de Arduino)
* :ref:`per_smart_fan` (Para usuarios de Piper Make)
