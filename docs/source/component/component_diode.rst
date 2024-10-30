.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_diode:

Diodo
=================

|img_diode|

Un diodo es un componente electrónico con dos electrodos que permite que la corriente fluya en una sola dirección, lo que comúnmente se denomina función de "rectificación".
Por lo tanto, se puede pensar en un diodo como la versión electrónica de una válvula de retención.

Los dos terminales de un diodo están polarizados, con el extremo positivo llamado ánodo y el extremo negativo llamado cátodo.
El cátodo suele estar hecho de plata o tener una banda de color.
Controlar la dirección del flujo de corriente es una de las características clave de los diodos: la corriente en un diodo fluye del ánodo al cátodo. El comportamiento de un diodo es similar al de una válvula de retención. Una de las características más importantes de un diodo es su no linealidad en la relación corriente-voltaje. Si se conecta un voltaje más alto al ánodo, la corriente fluye del ánodo al cátodo, y a este proceso se le llama polarización directa. Sin embargo, si el voltaje más alto se conecta al cátodo, el diodo no conduce electricidad, y este proceso se llama polarización inversa.

Debido a su conductividad unidireccional, el diodo se utiliza en casi todos los circuitos electrónicos de cierta complejidad. Fue uno de los primeros dispositivos semiconductores creados y tiene aplicaciones muy extendidas.

Sin embargo, en la práctica, los diodos no muestran una direccionalidad tan perfecta de encendido y apagado, sino que exhiben características electrónicas no lineales más complejas, que dependen del tipo específico de tecnología del diodo.

Un diodo es una unión p-n formada por un semiconductor tipo p y un semiconductor tipo n, con una capa de carga espacial en ambos lados de su interfaz y un campo eléctrico autoinducido, que se encuentra en equilibrio eléctrico cuando no hay voltaje aplicado, ya que la corriente de difusión debida a la diferencia de concentración de portadores entre ambos lados de la unión p-n y la corriente de deriva causada por el campo eléctrico autoinducido son iguales. Cuando se genera una polarización directa, la supresión mutua del campo eléctrico externo y el campo autoinducido aumenta la corriente de difusión de los portadores, lo que causa la corriente directa (que es la razón de la conductividad). Cuando se genera una polarización inversa, el campo eléctrico externo y el autoinducido se fortalecen, formando una corriente de saturación inversa I0 en un rango de voltaje inverso que es independiente del valor del voltaje de polarización inversa (lo que explica la no conductividad).
Cuando el voltaje inverso aplicado es suficientemente alto, la intensidad del campo eléctrico en la capa de carga espacial de la unión p-n alcanza un valor crítico que provoca un proceso de multiplicación de portadores, generando una gran cantidad de pares de electrones-huecos, resultando en un valor elevado de corriente de ruptura inversa, conocido como el fenómeno de ruptura del diodo.

**1. Característica Directa**

Cuando se aplica un voltaje directo externo, al inicio de la característica directa, el voltaje es muy pequeño y no suficiente para superar el efecto de bloqueo del campo eléctrico en la unión p-n, por lo que la corriente directa es casi nula, a esta parte se le llama zona muerta.
Este voltaje directo que no permite la conducción del diodo se conoce como voltaje de umbral. Cuando el voltaje directo es mayor que el voltaje de umbral, se supera el campo eléctrico de la unión p-n, permitiendo la conducción directa del diodo, y la corriente aumenta rápidamente con el voltaje.
Dentro del rango de corriente de uso normal, el voltaje terminal del diodo durante la conducción permanece casi constante, conocido como voltaje directo del diodo.

**2. Característica Inversa**

Cuando se aplica un voltaje inverso que no excede cierto rango, la corriente que pasa por el diodo es una corriente de deriva formada por unos pocos portadores en movimiento inverso.
Como esta corriente inversa es muy pequeña, el diodo está en estado de corte. Esta corriente inversa también se conoce como corriente de saturación inversa o corriente de fuga, y está muy influenciada por la temperatura.

**3. Ruptura**

Cuando el voltaje inverso aplicado excede un valor determinado, la corriente inversa aumentará repentinamente, fenómeno conocido como ruptura eléctrica.
El voltaje crítico que provoca la ruptura eléctrica se llama voltaje de ruptura inverso, y el diodo pierde su conductividad unidireccional en el momento de la ruptura.
Por lo tanto, se debe evitar el uso del diodo cuando el voltaje inverso aplicado es demasiado alto.

Los primeros diodos consistían en cristales de "Bigote de Gato" y tubos de vacío (también llamados "válvulas termiónicas"). La mayoría de los diodos actuales utilizan materiales semiconductores como el silicio o el germanio.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_
 
* `Diode - Wikipedia <https://en.wikipedia.org/wiki/Diode>`_


