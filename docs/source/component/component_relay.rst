.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_relay:

Relé
==========================================

|img_relay|

Como sabemos, un relé es un dispositivo que se utiliza para establecer 
una conexión entre dos o más puntos o dispositivos en respuesta a la 
señal de entrada aplicada. En otras palabras, los relés proporcionan 
aislamiento entre el controlador y el dispositivo, ya que estos pueden 
funcionar tanto en corriente alterna (AC) como en corriente continua (DC). 
Sin embargo, reciben señales de un microcontrolador que opera en DC, por 
lo que se requiere un relé para cerrar la brecha. El relé es extremadamente 
útil cuando se necesita controlar una gran cantidad de corriente o voltaje 
con una pequeña señal eléctrica.

Hay 5 partes en cada relé:

**Electroimán** - Consiste en un núcleo de hierro envuelto en una bobina de 
cables. Cuando pasa electricidad a través de ella, se vuelve magnético. Por 
eso se le llama electroimán.

**Armadura** - La tira magnética móvil se conoce como armadura. Cuando la 
corriente fluye a través de ella, la bobina se energiza produciendo un campo 
magnético que se utiliza para abrir o cerrar los puntos normalmente abiertos 
(N/O) o normalmente cerrados (N/C). La armadura puede moverse tanto con 
corriente continua (DC) como con corriente alterna (AC).

**Resorte** - Cuando no hay corriente circulando por la bobina del electroimán, 
el resorte aleja la armadura para que el circuito no se complete.

Conjunto de **contactos eléctricos** - Hay dos puntos de contacto:

-  Normalmente abierto (N/O) - conectado cuando el relé está activado y desconectado cuando está inactivo.

-  Normalmente cerrado (N/C) - desconectado cuando el relé está activado y conectado cuando está inactivo.

**Marco moldeado** - Los relés están cubiertos con plástico para protección.

El principio de funcionamiento del relé es sencillo. Cuando se suministra 
energía al relé, la corriente comienza a fluir a través de la bobina de 
control; como resultado, el electroimán se energiza. Luego, la armadura 
es atraída hacia la bobina, bajando el contacto móvil y conectándolo con 
los contactos normalmente abiertos. Así, el circuito con la carga se energiza. 
Al romper el circuito ocurre un caso similar, ya que el contacto móvil será 
llevado hacia los contactos normalmente cerrados por la fuerza del resorte. 
De esta manera, el encendido y apagado del relé puede controlar el estado de 
un circuito de carga.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Ejemplos**


* :ref:`py_relay` (Para usuarios de MicroPython)
* :ref:`ar_relay` (Para usuarios de Arduino)
