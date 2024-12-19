.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_traffic_light:


7.6 Feu de circulation
=================================


Le `Traffic Light <https://en.wikipedia.org/wiki/Traffic_light>`_ est un dispositif de signalisation installé aux intersections, passages pour piétons et autres endroits pour réguler la circulation.

Les signaux de circulation sont normalisés par la `Convention de Vienne sur la signalisation routière <https://fr.wikipedia.org/wiki/Convention_de_Vienne_sur_la_signalisation_routi%C3%A8re>`_. Ils accordent la priorité aux usagers en alternant des LEDs de trois couleurs standardisées.

* **Feu rouge** : La circulation doit s'arrêter devant un feu rouge clignotant, équivalent à un panneau stop.
* **Feu jaune** : Un signal d'avertissement indique un passage imminent au rouge. Les feux jaunes sont interprétés différemment selon les pays (régions).
* **Feu vert** : Autorise la circulation dans la direction indiquée.

Dans ce projet, nous allons utiliser trois LEDs de différentes couleurs pour simuler les changements de feux de circulation et un afficheur 7 segments à 4 chiffres pour afficher la durée de chaque état du feu.

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants.

Il est bien sûr plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
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
        - :ref:`cpn_resistor`
        - 7 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_led`
        - 3
        - |link_led_buy|


**Schéma**


|sch_traffic_light|


* Ce circuit est basé sur le :ref:`py_74hc_4dig` avec l'ajout de 3 LEDs.
* Les 3 LEDs rouges, jaunes et vertes sont connectées respectivement aux GP7~GP9.

**Câblage**


|wiring_traffic_light| 


**Code**

.. note::

    * Ouvrez le fichier ``7.6_traffic_light.py`` situé sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time
    from machine import Timer

    # Définir la durée pour chaque couleur de feu en secondes [Vert, Jaune, Rouge]
    lightTime = [30, 5, 30]

    # Codes de l'afficheur 7 segments pour les chiffres 0-9, utilisant des valeurs hexadécimales pour représenter les segments LED
    SEGCODE = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]

    # Initialiser les broches pour la communication avec le registre à décalage (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Entrée de données série
    rclk = machine.Pin(19, machine.Pin.OUT)  # Horloge de registre (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Horloge de registre à décalage

    # Initialiser la liste pour stocker les broches de contrôle des 4 chiffres de l'afficheur 7 segments
    placePin = []
    pin = [10, 13, 12, 11]  # Numéros de broches pour l'afficheur 4 chiffres
    for i in range(4):
        placePin.append(None)  # Réserver un espace dans la liste
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialiser les broches en sortie

    # Fonction pour sélectionner quel chiffre (0-3) afficher en contrôlant les broches d'anode commune
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Éteindre tous les chiffres
        placePin[digit].value(0)  # Allumer le chiffre sélectionné

    # Fonction pour effacer l'afficheur en envoyant '0x00' au registre à décalage
    def clearDisplay():
        hc595_shift(0x00)

    # Fonction pour envoyer des données au registre à décalage (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Abaisser la latch pour préparer le décalage de données
        time.sleep_us(200)  # Petit délai pour la stabilité du timing
        for bit in range(7, -1, -1):  # Parcourir chaque bit (MSB d'abord)
            srclk.low()  # Préparer pour envoyer le bit suivant
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extraire le bit actuel des données
            sdi.value(value)  # Régler la ligne de données sur la valeur du bit actuel
            time.sleep_us(200)
            srclk.high()  # Pulse l'horloge de décalage pour enregistrer le bit
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulse l'horloge de registre pour déplacer les données vers la sortie

    # Fonction pour afficher un nombre sur l'afficheur 7 segments
    # Cette fonction décompose le nombre en ses chiffres individuels et les affiche
    def display(num):
        pickDigit(0)  # Sélectionner l'unité
        hc595_shift(SEGCODE[num % 10])  # Afficher l'unité

        pickDigit(1)  # Sélectionner la dizaine
        hc595_shift(SEGCODE[num % 100 // 10])  # Afficher la dizaine

        pickDigit(2)  # Sélectionner la centaine
        hc595_shift(SEGCODE[num % 1000 // 100])  # Afficher la centaine

        pickDigit(3)  # Sélectionner le millier
        hc595_shift(SEGCODE[num % 10000 // 1000])  # Afficher le millier

    # Configuration des LEDs du feu de circulation (Rouge, Jaune, Vert)
    # Les LEDs sont connectées aux broches 9 (Vert), 8 (Jaune) et 7 (Rouge)
    pin = [7, 8, 9]  # Numéros de broches pour les LEDs
    led = []
    for i in range(3):
        led.append(None)  # Réserver un espace dans la liste
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialiser chaque broche en sortie pour les LEDs

    # Fonction pour allumer la LED correcte en fonction de l'état actuel
    # 0 = Vert, 1 = Jaune, 2 = Rouge
    def lightup(state):
        for i in range(3):
            led[i].value(0)  # Éteindre toutes les LEDs
        led[state].value(1)  # Allumer la LED sélectionnée (Vert, Jaune ou Rouge)

    # Variables liées au timer
    counter = 0  # Compteur pour le temps restant
    color_state = 0  # État actuel du feu de circulation (0 = Vert, 1 = Jaune, 2 = Rouge)

    # Fonction de rappel d'interruption du timer pour mettre à jour l'état du feu de circulation et le compteur
    def time_count(ev):
        global counter, color_state
        counter -= 1  # Réduire le compteur de 1 seconde
        if counter <= 0:  # Si le compteur atteint zéro, passer à la couleur suivante
            color_state = (color_state + 1) % 3  # Cycle entre Vert, Jaune et Rouge
            counter = lightTime[color_state]  # Réinitialiser le compteur en fonction de la durée de la nouvelle couleur

    # Initialiser un timer pour appeler la fonction time_count toutes les 1 seconde (1000ms)
    tim = Timer(period=1000, mode=Timer.PERIODIC, callback=time_count)

    # Boucle principale pour mettre à jour l'afficheur 7 segments et les LEDs du feu de circulation
    while True:
        display(counter)  # Mettre à jour l'afficheur avec le temps restant
        lightup(color_state)  # Mettre à jour les LEDs du feu de circulation en fonction de la couleur actuelle


Lorsque le code est exécuté, la LED verte reste allumée pendant 30 secondes, la LED jaune reste allumée pendant 5 secondes, et la LED rouge reste allumée pendant 30 secondes.
