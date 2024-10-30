.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete junto a otros entusiastas en el fascinante mundo de Raspberry Pi, Arduino y ESP32.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones Exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones en temporadas festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_music_player:

7.8 Reproductor de Música con RFID
======================================

En nuestro proyecto anterior, :ref:`py_rfid`, aprendimos que el módulo MFRC522 nos permite escribir hasta 48 letras de información en la tarjeta (o llave), incluyendo la clave de acceso, datos de identidad e incluso una partitura musical.

Como ejemplo, si escribes ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC``, el zumbador reproducirá la melodía cuando la tarjeta (o llave) se vuelva a leer. Además, puedes agregar un WS2812 para mostrar efectos visuales increíbles.

Puedes encontrar más partituras en Internet, escribir tu propia música, almacenarla en la tarjeta (o llave) y compartirla con tus amigos.

|rfid_player|

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Zumbador Pasivo :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Diagrama**

|sch_music_player|


**Conexiones**

|wiring_rfid_music_player| 

**Código**

#. Abre el archivo ``6.5_rfid_write.py`` en la ruta de ``kepler-kit-main/micropython``, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

   .. note::

    Aquí necesitas utilizar las bibliotecas en la carpeta ``mfrc522``; asegúrate de que están cargadas en el Pico. Consulta :ref:`add_libraries_py` para un tutorial detallado.

#. Después de ejecutar, escribe ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` en el shell, luego acerca la tarjeta (o llave) al módulo MFRC522 para almacenar una partitura de "Oda a la Alegría".

#. Abre el archivo ``7.8_rfid_music_player.py`` en la ruta de ``kepler-kit-main/micropython`` o copia este código en Thonny, luego haz clic en "Run Current Script" o simplemente presiona F5 para ejecutarlo.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # Configuración del LED WS2812
        ws = WS2812(machine.Pin(0), 8)

        # Configuración del lector RFID MFRC522
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # Frecuencias de notas del zumbador (en Hertz)
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # Inicializar PWM para el zumbador en el pin 15
        buzzer = machine.PWM(machine.Pin(15))

        # Lista de frecuencias de notas correspondientes a notas musicales
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # Función para tocar una nota en el zumbador con frecuencia y duración específicas
        def tone(pin, frequency, duration):
            pin.freq(frequency)
            pin.duty_u16(30000)
            time.sleep_ms(duration)
            pin.duty_u16(0)

        # Función para encender un LED WS2812 en un índice específico con un color aleatorio
        def lumi(index):
            for i in range(8):
                ws[i] = 0x000000
            ws[index] = int(urandom.uniform(0, 0xFFFFFF))
            ws.write()

        # Codificar texto de notas musicales en índices y tocar las notas correspondientes
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]
        def take_text(text):
            string = text.replace(' ', '').upper()
            while len(string) > 0:
                index = words.index(string[0])
                tone(buzzer, note[index], 250)
                lumi(index)
                string = string[1:]

        # Función para leer desde la tarjeta RFID y reproducir la partitura almacenada
        def read():
            print("Reading...Please place the card...")
            id, text = reader.read()
            print("ID: %s\nTexto: %s" % (id, text))
            take_text(text)
            
        # Comienza a leer desde la tarjeta RFID y reproduce la partitura correspondiente
        read()



#. Al acercar la tarjeta (o llave) al módulo MFRC522 nuevamente, el zumbador reproducirá la música almacenada en la tarjeta (o llave), y la tira RGB se iluminará en un color aleatorio.

