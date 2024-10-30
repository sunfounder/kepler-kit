.. note::

    ¡Hola! ¡Bienvenidos a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previews Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_mfrc522:

Módulo MFRC522
====================

|img_mfrc522|

El MFRC522 es un tipo de chip integrado para lectura y escritura de tarjetas, 
comúnmente utilizado en la radiofrecuencia de 13.56MHz. Lanzado por la compañía 
NXP, es un chip de tarjeta sin contacto de bajo voltaje, bajo costo y tamaño 
reducido, siendo una excelente opción para instrumentos inteligentes y 
dispositivos portátiles de mano.

El MFRC522 utiliza un concepto avanzado de modulación y demodulación que se 
presenta completamente en todos los tipos de métodos y protocolos de comunicación 
pasiva sin contacto a 13.56MHz. Además, soporta un algoritmo de encriptación 
rápida CRYPTO1 para verificar productos MIFARE. El MFRC522 también es compatible 
con la serie MIFARE para comunicación sin contacto de alta velocidad, con una 
tasa de transmisión de datos bidireccional de hasta 424kbit/s. Como nuevo 
miembro de la serie de lectores integrados a 13.56MHz, el MFRC522 es muy similar 
a los modelos existentes MF RC500 y MF RC530, aunque presenta algunas diferencias 
significativas. Se comunica con la máquina anfitriona a través de un modo serial, 
lo que requiere menos cableado. Puedes elegir entre los modos SPI, I2C y UART 
serial (similar a RS232), lo que ayuda a reducir las conexiones, ahorrar espacio 
en la placa PCB (tamaño más pequeño) y reducir costos.

* `MFRC522 Data sheet <https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf>`_


**Ejemplos**


* :ref:`py_rfid` (Para usuarios de MicroPython)
* :ref:`py_music_player` (Para usuarios de MicroPython)
* :ref:`ar_rfid` (Para usuarios de Arduino)
