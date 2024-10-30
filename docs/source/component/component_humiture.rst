.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_dht11:

Sensor de Humedad y Temperatura DHT11
=============================================

El sensor digital de temperatura y humedad DHT11 es un sensor compuesto que contiene una salida de señal digital calibrada para temperatura y humedad. 
Se aplican tecnologías de módulos digitales dedicados y de detección de temperatura y humedad para garantizar que el producto tenga alta fiabilidad y excelente estabilidad a largo plazo.

El sensor incluye un componente resistivo para la medición de humedad y un dispositivo NTC para la medición de temperatura, y está conectado a un microcontrolador de alto rendimiento de 8 bits.

.. El diagrama esquemático del Módulo de Sensor de Humedad y Temperatura se muestra a continuación: |img_Hum-sch|

Solo tres pines están disponibles para su uso: VCC, GND y DATA. 
El proceso de comunicación comienza con la línea DATA enviando señales de inicio al DHT11, que recibe las señales y devuelve una señal de respuesta. 
Luego, el host recibe esta señal de respuesta y empieza a recibir los datos de 40 bits sobre humedad y temperatura (8 bits de humedad entera + 8 bits de humedad decimal + 8 bits de temperatura entera + 8 bits de temperatura decimal + 8 bits de suma de verificación).

|img_Dht11|

**Características**

    #. Rango de medición de humedad: 20 - 90%RH
    #. Rango de medición de temperatura: 0 - 60℃
    #. Señales digitales de salida que indican temperatura y humedad
    #. Voltaje de funcionamiento: DC 5V; Tamaño del PCB: 2.0 x 2.0 cm
    #. Precisión de medición de humedad: ±5%RH
    #. Precisión de medición de temperatura: ±2℃

* `DHT11 Datasheet <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Ejemplos**

* :ref:`py_dht11` (Para usuarios de MicroPython)
* :ref:`ar_dht11` (Para usuarios de Arduino)
