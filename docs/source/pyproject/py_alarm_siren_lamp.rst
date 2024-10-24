.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_alarm_lamp:

7.3 Lampe d'Alarme avec Sirène
=====================================

Les gyrophares sont souvent visibles dans la vie réelle (ou dans les films). Ils sont généralement utilisés pour réguler le trafic, servir de dispositif d'avertissement et comme accessoire de sécurité essentiel pour les officiers, véhicules d'urgence, camions de pompiers et véhicules d'intervention. Quand vous voyez leurs lumières ou entendez leur son, soyez prudent, cela signifie que vous (ou votre entourage) pourriez être en danger.

Ici, une LED et un buzzer sont utilisés pour créer un petit feu d'avertissement, activé par un interrupteur à glissière.

|sirem_alarm|


**Composants Requis**

Pour ce projet, nous avons besoin des composants suivants : 

Il est plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous :

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPOSANT	
        - QUANTITÉ
        - LIEN

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Câble Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Plusieurs
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Buzzer Passif :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schéma**

|sch_alarm_siren_lamp|

* Le GP17 est connecté à la broche centrale de l'interrupteur à glissière, avec une résistance de 10K et un condensateur (filtre) en parallèle vers la masse, ce qui permet à l'interrupteur de sortir un niveau haut ou bas stable lorsqu'il est basculé à gauche ou à droite.
* Dès que le GP15 est à un niveau haut, le transistor NPN conduit, activant le buzzer passif qui commence à émettre un son. Ce buzzer passif est programmé pour augmenter progressivement en fréquence afin de produire un son de sirène.
* Une LED est connectée au GP16 et est programmée pour varier périodiquement en intensité, simulant ainsi un gyrophare.


**Câblage**

|wiring_alarm_siren_lamp|

**Code**

.. note::

    * Ouvrez le fichier ``7.3_alarm_siren_lamp.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    # Initialiser le PWM pour le buzzer (sur la broche 15) et la LED (sur la broche 16)
    buzzer = machine.PWM(machine.Pin(15))  # PWM pour le buzzer
    led = machine.PWM(machine.Pin(16))  # PWM pour la LED
    led.freq(1000)  # Régler la fréquence du PWM de la LED à 1kHz

    # Initialiser l'interrupteur (sur la broche 17) en tant que broche d'entrée
    switch = machine.Pin(17, machine.Pin.IN)

    # Fonction pour arrêter le buzzer en réglant le cycle de service à 0%
    def noTone(pin):
        pin.duty_u16(0)  # Régler le cycle de service PWM à 0, arrêtant ainsi le son

    # Fonction pour jouer un son sur le buzzer avec une fréquence spécifiée
    def tone(pin, frequency):
        pin.freq(frequency)  # Régler la fréquence pour le buzzer
        pin.duty_u16(30000)  # Régler le cycle de service à environ 50% (30000 sur 65535)

    # Fonction pour mapper une valeur d'une plage à une autre
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Gestionnaire d'interruptions pour basculer le bell_flag lorsque l'interrupteur est pressé
    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag  # Basculer la valeur de bell_flag
        print(bell_flag)  # Afficher l'état actuel de bell_flag pour le débogage
        
        # Changer l'interruption de l'interrupteur en fonction de l'état de bell_flag
        if bell_flag:
            # Si bell_flag est True, écouter un front descendant (quand l'interrupteur est relâché)
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            # Si bell_flag est False, écouter un front montant (quand l'interrupteur est pressé)
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Initialiser bell_flag à False (buzzer et LED éteints par défaut)
    bell_flag = False

    # Configurer une interruption pour détecter quand l'interrupteur est pressé (front montant)
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Boucle principale pour contrôler le buzzer et la LED en fonction de bell_flag
    while True:
        if bell_flag == True:
            # Si bell_flag est True, augmenter progressivement la luminosité de la LED
            # et changer la fréquence du buzzer pour simuler un effet de sirène
            for i in range(0, 100, 2):  # Boucler de 0 à 100 par pas de 2
                led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))  # Mapper i à la luminosité de la LED
                tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))  # Mapper i à la fréquence du buzzer
                time.sleep_ms(10)  # Courte pause pour créer une montée en douceur
        else:
            # Si bell_flag est False, arrêter le buzzer et éteindre la LED
            noTone(buzzer)  # Arrêter le buzzer
            led.duty_u16(0)  # Éteindre la LED (cycle de service à 0)

Après l'exécution du programme, basculez l'interrupteur à glissière vers la gauche (ou vers la droite, selon le câblage de votre interrupteur), et le buzzer émettra un son d'alarme progressif tandis que la LED changera de luminosité en conséquence. Basculez l'interrupteur dans l'autre sens pour arrêter le buzzer et la LED.
