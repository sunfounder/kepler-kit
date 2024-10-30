.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_ir_receiver:

Receptor Infrarrojo
=================================

Receptor IR
----------------------------

|img_irrecv|

* S: Salida de señal
* +: VCC
* -: GND

Un receptor infrarrojo es un componente que recibe señales infrarrojas y puede recibir de forma independiente rayos infrarrojos, emitiendo señales compatibles con el nivel TTL. Es similar en tamaño a un transistor normal empaquetado en plástico y es adecuado para todo tipo de control remoto por infrarrojos y transmisión de señales infrarrojas.

La comunicación por infrarrojos, o IR, es una tecnología inalámbrica popular, de bajo costo y fácil de usar. La luz infrarroja tiene una longitud de onda ligeramente más larga que la luz visible, por lo que es imperceptible al ojo humano, lo que la hace ideal para la comunicación inalámbrica. Un esquema común de modulación para la comunicación infrarroja es la modulación a 38KHz.

* Adopta el sensor receptor IR HX1838, alta sensibilidad
* Puede utilizarse para control remoto
* Fuente de alimentación: 3.3~5V
* Interfaz: Digital
* Frecuencia de modulación: 38KHz

Control Remoto
-------------------------

|img_controller|

Este es un control remoto inalámbrico por infrarrojos, delgado y mini, con 21 botones de función y una distancia de transmisión de hasta 8 metros, adecuado para operar una amplia gama de dispositivos en la habitación de un niño.

* Tamaño: 85x39x6mm
* Rango de control remoto: 8-10m
* Batería: Tipo botón de litio-manganeso de 3V
* Frecuencia portadora de infrarrojos: 38KHz
* Material de la superficie: 0.125mm PET
* Vida útil efectiva: más de 20,000 usos

**Ejemplos**

* :ref:`py_irremote` (Para usuarios de MicroPython)
* :ref:`ar_irremote` (Para usuarios de Arduino)
