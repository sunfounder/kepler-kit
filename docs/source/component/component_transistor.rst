.. note::

    ¡Hola! Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_transistor:

Transistor
==============

|img_NPN&PNP|

El transistor es un dispositivo semiconductor que controla la corriente mediante otra corriente. Su función principal es amplificar señales débiles a señales de mayor amplitud y también se utiliza como interruptor sin contacto.

Un transistor tiene una estructura de tres capas compuesta por semiconductores tipo P y N. Estas capas forman tres regiones internas. La más delgada en el medio es la región base; las otras dos son de tipo N o P: la región más pequeña con la mayoría de portadores es la región emisor, mientras que la otra es la región colector. Esta composición permite que el transistor actúe como amplificador. 
De estas tres regiones se generan tres terminales: base (b), emisor (e) y colector (c). Forman dos uniones P-N, conocidas como la unión emisor y la unión colector. La dirección de la flecha en el símbolo del circuito del transistor indica la polaridad de la unión emisor.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

Según el tipo de semiconductor, los transistores se dividen en dos grupos: NPN y PNP. A partir de la abreviatura, podemos deducir que el primero está compuesto por dos semiconductores tipo N y uno tipo P, mientras que el segundo es lo opuesto. Ver la imagen a continuación.

.. note::
    s8550 es un transistor PNP y s8050 es uno NPN. Se ven muy similares, por lo que es necesario revisar cuidadosamente sus etiquetas.

|img_transistor_symbol|

Cuando una señal de alto nivel atraviesa un transistor NPN, se energiza. Sin embargo, un transistor PNP necesita una señal de bajo nivel para funcionar. Ambos tipos de transistores se utilizan frecuentemente como interruptores sin contacto, tal como en este experimento.

* `S8050 Transistor Datasheet <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

Coloca la etiqueta hacia ti y los pines hacia abajo. Los pines de izquierda a derecha son: emisor (e), base (b) y colector (c).

|img_ebc|

.. note::
    * La base es el dispositivo que controla la puerta para el suministro eléctrico mayor.
    * En el transistor NPN, el colector es el suministro eléctrico mayor y el emisor es la salida de ese suministro. En el transistor PNP, es exactamente al revés.


.. Example
.. -------------------

.. :ref:`Two Kinds of Transistors`


**Example**

* :ref:`py_transistor` (Para usuarios de MicroPython)
* :ref:`py_relay` (Para usuarios de MicroPython)
* :ref:`py_ac_buz` (Para usuarios de MicroPython)
* :ref:`py_pa_buz` (Para usuarios de MicroPython)
* :ref:`py_light_theremin` (Para usuarios de MicroPython)
* :ref:`py_alarm_lamp` (Para usuarios de MicroPython)
* :ref:`py_music_player` (Para usuarios de MicroPython)
* :ref:`py_fruit_piano` (Para usuarios de MicroPython)
* :ref:`py_reversing_aid` (Para usuarios de MicroPython)
* :ref:`ar_ac_buz` (Para usuarios de Arduino)
* :ref:`ar_pa_buz` (Para usuarios de Arduino)
* :ref:`ar_transistor` (Para usuarios de Arduino)
* :ref:`ar_relay` (Para usuarios de Arduino)
* :ref:`per_service_bell` (Para usuarios de Piper Make)
* :ref:`per_reversing_system` (Para usuarios de Piper Make)
* :ref:`per_reaction_game` (Para usuarios de Piper Make)
