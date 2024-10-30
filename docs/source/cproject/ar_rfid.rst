.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ar_rfid:

6.5 - Identificación por Radiofrecuencia
==============================================

La Identificación por Radiofrecuencia (RFID) se refiere a tecnologías que utilizan comunicación inalámbrica entre un objeto (o etiqueta) y un dispositivo interrogador (o lector) para rastrear e identificar automáticamente dichos objetos. El alcance de transmisión de la etiqueta está limitado a unos pocos metros desde el lector. No es necesario que haya una línea de visión clara entre el lector y la etiqueta.

La mayoría de las etiquetas contienen al menos un circuito integrado (IC) y una antena. 
El microchip almacena información y es responsable de gestionar la comunicación por radiofrecuencia (RF) con el lector. Las etiquetas pasivas no tienen una fuente de energía independiente y dependen de una señal electromagnética externa, proporcionada por el lector, para activar su funcionamiento. 
Las etiquetas activas contienen una fuente de energía independiente, como una batería, lo que les proporciona mayor capacidad de procesamiento, transmisión y alcance.

* :ref:`cpn_mfrc522`

**Componentes Necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es muy conveniente comprar un kit completo; aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
        - LINK DE COMPRA
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCCIÓN DEL COMPONENTE
        - CANTIDAD
        - LINK DE COMPRA

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cable Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Varios
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Diagrama Esquemático**

|sch_rfid|

**Conexión**

|wiring_rfid|

**Código**

.. note::

   * Se utiliza la biblioteca ``MFRC522`` aquí; puedes instalarla desde el **Administrador de Bibliotecas**.

      .. image:: img/lib_mfrc522.png

La función principal se divide en dos:

* ``6.5_rfid_write`` para escribir información en la tarjeta (o llave).

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  Después de ejecutarlo, podrás ingresar un mensaje en el monitor serial, finalizando con ``#``, y luego escribir el mensaje en la tarjeta acercándola al módulo MFRC522.

* ``6.5_rfid_read`` para leer la información de la tarjeta (o llave).

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  Después de ejecutarlo, podrás leer el mensaje almacenado en la tarjeta (o llave).

**¿Cómo funciona?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         9
    #define SS_PIN          17

    MFRC522 mfrc522(SS_PIN, RST_PIN);

Primero, instancia la clase ``MFRC522()``.

Para facilitar su uso, la biblioteca ``MFRC522`` está encapsulada con las siguientes funciones.

* ``void simple_mfrc522_init()`` : Inicia la comunicación SPI e inicializa el módulo mfrc522.
* ``void simple_mfrc522_get_card()`` : Suspende el programa hasta que se detecta la tarjeta (o llave), imprime el UID de la tarjeta y el tipo de PICC.
* ``void simple_mfrc522_write(String text)`` : Escribe una cadena de texto en la tarjeta (o llave).
* ``void simple_mfrc522_write(byte* buffer)`` : Escribe información en la tarjeta (o llave), generalmente proveniente del puerto serial.
* ``void simple_mfrc522_write(byte section, String text)`` : Escribe una cadena en un sector específico. ``section`` se establece en 0 para escribir en los sectores 1-2; ``section`` se establece en 1 para escribir en los sectores 3-4.
* ``void simple_mfrc522_write(byte section, byte* buffer)`` : Escribe información en un sector específico, generalmente desde el puerto serial. ``section`` establecido en 0, escribe en sectores 1-2; ``section`` establecido en 1, escribe en sectores 3-4.
* ``String simple_mfrc522_read()`` : Lee la información de la tarjeta (o llave) y devuelve una cadena.
* ``String simple_mfrc522_read(byte section)`` : Lee la información en un sector específico y devuelve una cadena. ``section`` se establece en 0, lee sectores 1-2; ``section`` se establece en 1, lee sectores 3-4.

En el ejemplo ``6.5_rfid_write.ino``, se utiliza la función ``Serial.readBytesUntil()``, que es un método común de entrada serial.

* `Serial.readBytesUntil <https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytesuntil/>`_