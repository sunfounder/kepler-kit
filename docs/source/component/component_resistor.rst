.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_resistor:

Resistor
============

|img_res|

El resistor es un elemento electrónico que puede limitar la corriente en un circuito. 
Un resistor fijo es un tipo de resistor cuya resistencia no se puede cambiar, mientras que la de un potenciómetro o resistor variable sí se puede ajustar.

Existen dos símbolos de circuito generalmente usados para los resistores. Normalmente, la resistencia está indicada en el componente. Así que, si ves estos símbolos en un circuito, representan un resistor.

|img_res_symbol|

**Ω** es la unidad de resistencia y las unidades más grandes incluyen KΩ, MΩ, etc. 
Su relación se muestra de la siguiente manera: 1 MΩ=1000 KΩ, 1 KΩ = 1000 Ω. Normalmente, el valor de la resistencia está marcado en el componente.

Al usar un resistor, necesitamos conocer su resistencia primero. Aquí hay dos métodos: puedes observar las bandas de colores en el resistor o usar un multímetro para medir la resistencia. Se recomienda usar el primer método, ya que es más conveniente y rápido.

|img_res_card|

Como se muestra en la tarjeta, cada color representa un número.

.. list-table::

   * - Negro
     - Marrón
     - Rojo
     - Naranja
     - Amarillo
     - Verde
     - Azul
     - Violeta
     - Gris
     - Blanco
     - Oro
     - Plata
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0.1
     - 0.01

Los resistores de 4 y 5 bandas se utilizan con frecuencia, y tienen 4 o 5 bandas cromáticas.

Normalmente, cuando obtienes un resistor, puede ser difícil determinar de qué extremo comenzar a leer los colores.
El truco es que el espacio entre la 4ª y la 5ª banda será comparativamente mayor.

Por lo tanto, puedes observar el espacio entre dos bandas cromáticas en uno de los extremos del resistor; 
si es más grande que los demás espacios entre bandas, entonces puedes leer desde el lado opuesto.

Veamos cómo leer el valor de resistencia de un resistor de 5 bandas como se muestra a continuación.

|img_220ohm|

Para este resistor, el valor se debe leer de izquierda a derecha. 
El valor se presenta en este formato: 1ª Banda 2ª Banda 3ª Banda x 10^Multiplicador (Ω) y el error permisible es ± Tolerancia%. 
Por lo tanto, el valor de resistencia de este resistor es 2(rojo) 2(rojo) 0(negro) x 10^0(negro) Ω = 220 Ω, 
y el error permisible es ± 1% (marrón).

.. list-table:: Bandas de color comunes en resistores
    :header-rows: 1

    * - :ref:`cpn_resistor` 
      - Bandas de Color  
    * - 10Ω   
      - marrón negro negro plata marrón
    * - 100Ω   
      - marrón negro negro negro marrón
    * - 220Ω 
      - rojo rojo negro negro marrón
    * - 330Ω 
      - naranja naranja negro negro marrón
    * - 1kΩ 
      - marrón negro negro marrón marrón
    * - 2kΩ 
      - rojo negro negro marrón marrón
    * - 5.1kΩ 
      - verde marrón negro marrón marrón
    * - 10kΩ 
      - marrón negro negro rojo marrón 
    * - 100kΩ 
      - marrón negro negro naranja marrón 
    * - 1MΩ 
      - marrón negro negro verde marrón 

Puedes aprender más sobre los resistores en Wiki: `Resistor - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.
