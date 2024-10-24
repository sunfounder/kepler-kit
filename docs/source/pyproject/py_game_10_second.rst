.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_10_second:

7.5 JEU - 10 Secondes
============================


Pour mettre votre concentration à l'épreuve, suivez-moi pour créer un appareil de jeu.
Fabriquez une baguette magique en connectant l'interrupteur à bascule à un bâton. Lorsque vous secouez la baguette, l'afficheur 4 chiffres commencera à compter, et quand vous la secouerez à nouveau, le compteur s'arrêtera. Pour gagner, vous devez réussir à maintenir le décompte affiché à **10.00**. Vous pouvez jouer avec vos amis pour voir qui est le véritable maître du temps.

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ÉLÉMENTS DANS CE KIT
        - LIEN
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.


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
        - :ref:`cpn_resistor`
        - 5(4-220Ω, 1-10KΩ)
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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schéma**


|sch_10_second|


* Ce circuit est basé sur :ref:`py_74hc_4dig` avec l'ajout d'un interrupteur à bascule.
* GP16 est à l'état haut lorsque l'interrupteur à bascule est en position verticale ; bas lorsqu'il est incliné.

**Câblage**

|wiring_game_10_second| 


**Code**


.. note::

    * Ouvrez le fichier ``7.5_game_10_second.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    # Codes pour afficher les chiffres 0-9 sur un afficheur 7 segments, en utilisant l'hexadécimal pour représenter les segments LED
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    # Définir les broches pour la communication avec le registre à décalage (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Entrée de données série
    rclk = machine.Pin(19, machine.Pin.OUT)  # Horloge de registre (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Horloge du registre à décalage

    # Initialiser la liste pour stocker les broches de contrôle des 4 chiffres
    placePin = []

    # Définir les broches de contrôle pour chaque chiffre (anodes communes)
    pin = [10,13,12,11]  # Numéros de broches pour l'afficheur 4 chiffres
    for i in range(4):
        placePin.append(None)  # Réserver de la place dans la liste
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialiser les broches en sortie

    # Fonction pour sélectionner quel chiffre (0-3) afficher en contrôlant les broches d'anode commune
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Éteindre tous les chiffres
        placePin[digit].value(0)  # Allumer le chiffre sélectionné

    # Fonction pour effacer l'affichage en envoyant '0x00' au registre à décalage
    def clearDisplay():
        hc595_shift(0x00)

    # Fonction pour envoyer des données au registre à décalage (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Tirer le verrou à bas pour préparer le décalage des données
        time.sleep_us(200)  # Petit délai pour la stabilité du timing
        for bit in range(7, -1, -1):  # Parcourir chaque bit (MSB en premier)
            srclk.low()  # Préparer à envoyer le prochain bit
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extraire le bit actuel des données
            sdi.value(value)  # Régler la ligne de données sur la valeur du bit actuel
            time.sleep_us(200)
            srclk.high()  # Pulsation de l'horloge de décalage pour stocker le bit dans le registre
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulsation de l'horloge de registre pour déplacer les données vers la sortie

    # Fonction pour afficher un nombre sur l'afficheur 7 segments
    # Cette fonction divise le nombre en ses chiffres individuels et les affiche un par un
    def display(num):
        pickDigit(0)  # Sélectionner les unités
        hc595_shift(SEGCODE[num % 10])  # Afficher les unités

        pickDigit(1)  # Sélectionner les dizaines
        hc595_shift(SEGCODE[num % 100 // 10])  # Afficher les dizaines

        pickDigit(2)  # Sélectionner les centaines
        hc595_shift(SEGCODE[num % 1000 // 100] + 0x80)  # Afficher les centaines (avec point décimal)

        pickDigit(3)  # Sélectionner les milliers
        hc595_shift(SEGCODE[num % 10000 // 1000])  # Afficher les milliers

    # Initialiser le capteur à bascule sur la broche 16
    tilt_switch = machine.Pin(16, machine.Pin.IN)

    # Indicateur booléen pour contrôler si le comptage doit continuer
    count_flag = False

    # Gestionnaire d'interruptions pour l'interrupteur à bascule, bascule l'état de comptage à chaque déclenchement
    def shake(pin):
        global timeStart, count_flag
        count_flag = not count_flag  # Basculer l'état de comptage
        if count_flag == True:
            timeStart = time.ticks_ms()  # Enregistrer le moment où le comptage commence

    # Configurer une interruption sur l'interrupteur à bascule pour détecter les secousses et appeler la fonction shake()
    tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)

    # Initialiser la variable de comptage à zéro
    count = 0

    # Boucle principale pour mettre continuellement à jour l'affichage en fonction du temps écoulé depuis le déclenchement de l'interrupteur à bascule
    while True:
        if count_flag == True:
            count = int((time.ticks_ms() - timeStart) / 10)  # Calculer le comptage en dixièmes de seconde
        display(count)  # Mettre à jour l'affichage avec le comptage actuel


L'afficheur 4 chiffres commencera à compter lorsque vous secouerez la baguette, et s'arrêtera lorsque vous la secouerez à nouveau.
Vous gagnez si vous parvenez à maintenir le décompte affiché à 10.00. Le jeu reprendra après une nouvelle secousse.
