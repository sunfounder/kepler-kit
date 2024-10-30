.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el apasionante mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_rfid:

6.5 Identificación por Radiofrecuencia
==========================================

La Identificación por Radiofrecuencia (RFID) es una tecnología que utiliza 
comunicación inalámbrica entre un objeto (o etiqueta) y un dispositivo lector 
para rastrear e identificar el objeto. El rango de transmisión de la etiqueta 
es limitado a varios metros y no requiere necesariamente estar en la línea de 
visión del lector.

La mayoría de las etiquetas contienen un circuito integrado (IC) y una antena. 
Además de almacenar información, el microchip gestiona la comunicación con el 
lector mediante frecuencia de radio (RF). Las etiquetas pasivas no tienen fuente 
de energía independiente y dependen de una señal electromagnética externa del 
lector para funcionar. En cambio, una etiqueta activa cuenta con una fuente de 
energía independiente, como una batería, lo cual puede mejorar su capacidad de 
procesamiento, transmisión y alcance.

* :ref:`cpn_mfrc522`

**Componentes Necesarios**

En este proyecto, necesitaremos los siguientes componentes.

Es muy conveniente adquirir un kit completo; aquí tienes el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE	
        - CANTIDAD
        - ENLACE

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

**Esquemático**

|sch_rfid|

**Conexiones**

|wiring_rfid|

**Código**

Aquí necesitas utilizar las bibliotecas en la carpeta ``mfrc522``; asegúrate de que están cargadas en el Pico W. Consulta :ref:`add_libraries_py` para un tutorial detallado.

La función principal se divide en dos partes:

* ``6.5_rfid_write.py``: Utilizado para escribir información en la tarjeta (o llave).
* ``6.5_rfid_read.py``: Utilizado para leer la información en la tarjeta (o llave).


Abre el archivo ``6.5_rfid_write.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

Después de ejecutar, podrás escribir un mensaje en el shell y luego acercar la tarjeta (o llave) al módulo MFRC522 para escribir el mensaje.

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

    def write():
        to_write = input("Please enter the message: ")
        print("Writing...Please place the card...")
        id, text = reader.write(to_write)
        print("ID: %s\nText: %s" % (id,text))

    write()

Abre el archivo ``6.5_rfid_read.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

Después de ejecutar, podrás leer el mensaje almacenado en la tarjeta (o llave).

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

    def read():
        print("Reading...Please place the card...")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

    read()

**¿Cómo funciona?**

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

Instancia de la clase ``SimpleMFRC522()``.

.. code-block:: python

    id, text = reader.read()

Esta función se utiliza para leer los datos de la tarjeta. Si la lectura es exitosa, se devuelven id y text.

.. code-block:: python

    id, text = reader.write("text")

Esta función se utiliza para escribir información en la tarjeta; 
presiona la tecla **Enter** para finalizar la escritura. ``texto`` es la información que se va a escribir en la tarjeta.
