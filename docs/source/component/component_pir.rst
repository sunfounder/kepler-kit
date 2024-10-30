.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_pir:

Módulo Sensor de Movimiento PIR
==================================

|img_pir|

El sensor PIR detecta la radiación de calor infrarrojo que puede ser utilizada para identificar la presencia de organismos que emiten este tipo de radiación.

El sensor PIR está dividido en dos ranuras conectadas a un amplificador diferencial. Cuando un objeto estacionario se encuentra frente al sensor, ambas ranuras reciben la misma cantidad de radiación y la salida es cero. Si un objeto en movimiento se coloca frente al sensor, una de las ranuras recibe más radiación que la otra, lo que hace que la salida fluctúe de alto a bajo. Este cambio en el voltaje de salida indica la detección de movimiento.

|img_PIR_working_principle|

Después de cablear el módulo sensor, se inicia una fase de inicialización de un minuto. Durante esta fase, el módulo puede emitir señales de 0 a 3 veces en intervalos. Luego, el módulo entrará en modo de espera. Por favor, mantén la superficie del módulo libre de interferencias de fuentes de luz y otras posibles interferencias para evitar errores de operación. Es mejor usar el módulo en ausencia de corrientes de aire fuertes, ya que el viento también puede interferir con el sensor.

|img_pir_back|

**Ajuste de Distancia**

Girando la perilla del potenciómetro de ajuste de distancia en el sentido de las agujas del reloj, el rango de distancia de detección aumentará, alcanzando un máximo de aproximadamente 0-7 metros. Si se gira en sentido contrario, el rango de distancia de detección disminuirá, con un mínimo de aproximadamente 0-3 metros.

**Ajuste de Retardo**

Al girar la perilla del potenciómetro de ajuste de retardo en el sentido de las agujas del reloj, se incrementa el tiempo de retardo de la detección. El máximo de retardo puede llegar hasta 300s. Por el contrario, si se gira en sentido contrario, se reduce el retardo con un mínimo de 5s.

**Dos Modos de Disparo**

Selecciona diferentes modos usando el capuchón de puente.

* **H**: Modo de disparo repetitivo. Después de detectar la presencia de una persona, el módulo emite una señal de nivel alto. Durante el periodo de retardo, si alguien entra en el rango de detección, la salida se mantendrá en nivel alto.
* **L**: Modo de disparo no repetitivo. Emite un nivel alto cuando detecta la presencia de una persona. Después del retardo, la salida cambiará automáticamente de nivel alto a nivel bajo.

.. Ejemplo 
.. -------------------

.. :ref:`Intruder Alarm`


**Ejemplos**

* :ref:`py_pir` (Para usuarios de MicroPython)
* :ref:`py_passage_counter` (Para usuarios de MicroPython)
* :ref:`ar_pir` (Para usuarios de Arduino)
* :ref:`per_lucky_cat` (Para usuarios de Piper Make)
