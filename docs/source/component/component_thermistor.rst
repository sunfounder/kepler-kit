.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_thermistor:

Termistor
===============

|img_thermistor|

Un termistor es un tipo de resistencia cuya resistencia depende en gran medida de la temperatura, más que en los resistores estándar. La palabra es una combinación de "térmico" y "resistor". Los termistores se utilizan ampliamente como limitadores de corriente de arranque, sensores de temperatura (generalmente de tipo NTC, coeficiente de temperatura negativo), protectores de sobrecorriente autorreajustables y elementos calefactores autorreguladores (generalmente de tipo PTC, coeficiente de temperatura positivo).

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Aquí está el símbolo electrónico del termistor.

|img_thermistor_symbol|

Existen dos tipos fundamentales de termistores:

* Con los termistores NTC, la resistencia disminuye a medida que aumenta la temperatura, generalmente debido a un aumento en los electrones de conducción impulsados por la agitación térmica desde la banda de valencia. Un NTC se usa comúnmente como sensor de temperatura o en serie con un circuito como limitador de corriente de arranque.
* Con los termistores PTC, la resistencia aumenta a medida que sube la temperatura, generalmente debido al aumento de las agitaciones térmicas en la red, especialmente las de impurezas e imperfecciones. Los termistores PTC se instalan comúnmente en serie con un circuito y se utilizan para proteger contra condiciones de sobrecorriente, como fusibles autorreajustables.

En este kit usamos un NTC. Cada termistor tiene una resistencia normal, que aquí es de 10k ohmios, medida a 25 grados Celsius.

La relación entre la resistencia y la temperatura es la siguiente:

    RT = RN * expB(1/TK - 1/TN)   

* **RT** es la resistencia del termistor NTC cuando la temperatura es TK. 
* **RN** es la resistencia del termistor NTC bajo la temperatura nominal TN. Aquí, el valor de RN es 10k.
* **TK** es la temperatura en Kelvin y la unidad es K. Aquí, el valor de TK es 273.15 + grados Celsius.
* **TN** es la temperatura nominal en Kelvin; la unidad también es K. Aquí, el valor de TN es 273.15 + 25.
* **B (beta)**, la constante del material del termistor NTC, también se llama índice de sensibilidad térmica, con un valor numérico de 3950.      
* **exp** es la abreviatura de exponencial, y el número base e es un número natural que aproximadamente equivale a 2.7.  

Convierte esta fórmula TK=1/(ln(RT/RN)/B+1/TN) para obtener la temperatura en Kelvin que, menos 273.15, equivaldrá a grados Celsius.

Esta relación es una fórmula empírica. Es precisa solo cuando la temperatura y la resistencia están dentro del rango efectivo.

.. Example
.. -------------------

.. :ref:`Thermometer`

**Example**

* :ref:`py_temp` (Para usuarios de MicroPython)
* :ref:`py_room_temp` (Para usuarios de MicroPython)
* :ref:`ar_temp` (Para usuarios de Arduino)
