.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans le Raspberry Pi, l'Arduino et l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux démonstrations exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_passage_counter:


7.4 Compteur de Passagers
==============================

Dans les grands centres commerciaux, aéroports, gares, musées et autres lieux publics comme les salles d'exposition, le flux de passagers est une donnée indispensable.

Par exemple, dans les aéroports et les gares, le nombre de personnes doit être strictement contrôlé pour garantir la sécurité et fluidifier les déplacements. 
Il est également possible de savoir quand il y a plus de visiteurs dans les centres commerciaux et les magasins, combien de commandes chaque utilisateur peut générer, etc. 
Ainsi, nous pouvons analyser les habitudes de consommation des gens et augmenter le chiffre d'affaires.

Les compteurs de passagers aident à comprendre le fonctionnement de ces lieux publics et à organiser leurs opérations de manière efficace.

Un simple compteur de passagers peut être créé à l'aide d'un capteur PIR et d'un affichage 7 segments à 4 chiffres.


**Composants Requis**

Dans ce projet, nous aurons besoin des composants suivants.

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
        - 4 (220Ω)
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Schéma**

|sch_passager_counter| 

* Ce circuit est basé sur le :ref:`py_74hc_4dig` avec l'ajout d'un module PIR.
* Le PIR envoie un signal haut d'environ 2,8 secondes lorsqu'une personne passe devant lui.
* Le module PIR possède deux potentiomètres : l'un ajuste la sensibilité, l'autre ajuste la distance de détection. Pour un meilleur fonctionnement du module PIR, il faut tourner les deux potentiomètres à fond dans le sens antihoraire.

    |img_PIR_TTE|


**Câblage**

|wiring_passager_counter|

**Code**

.. note::

    * Ouvrez le fichier ``7.4_passenger_counter.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    # Initialiser le capteur PIR sur la broche 16, configuré en entrée
    pir_sensor = machine.Pin(16, machine.Pin.IN)

    # Codes d'affichage 7 segments pour les chiffres 0-9, en utilisant l'hexadécimal pour représenter les segments LED
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    # Définir les broches pour la communication avec le registre de décalage (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Entrée de données série
    rclk = machine.Pin(19, machine.Pin.OUT)  # Horloge de registre (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Horloge du registre de décalage

    # Initialiser la liste pour stocker les broches de contrôle des 4 chiffres
    placePin = []

    # Définir les broches de contrôle pour chaque chiffre (anodes communes)
    pin = [10,13,12,11] # Numéros de broche pour l'affichage 4 chiffres
    for i in range(4):
        placePin.append(None)  # Réserver de la place dans la liste
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialiser la broche en sortie

    # Initialiser le compteur pour suivre les événements de mouvement détectés
    count = 0

    # Fonction pour sélectionner quel chiffre (0-3) afficher en contrôlant les broches d'anodes communes
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Éteindre tous les chiffres
        placePin[digit].value(0)  # Allumer le chiffre sélectionné

    # Fonction pour effacer l'affichage en envoyant '0x00' au registre de décalage
    def clearDisplay():
        hc595_shift(0x00)

    # Fonction pour envoyer des données au registre de décalage (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Tirer la latch en bas pour préparer le décalage des données
        time.sleep_us(200)  # Petite pause pour la stabilité du timing
        for bit in range(7, -1, -1):  # Boucler à travers chaque bit (MSB en premier)
            srclk.low()  # Préparer pour envoyer le bit suivant
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extraire le bit courant des données
            sdi.value(value)  # Régler la ligne de données sur la valeur du bit courant
            time.sleep_us(200)
            srclk.high()  # Pulser l'horloge de décalage pour stocker le bit dans le registre
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulser l'horloge de registre pour déplacer les données vers la sortie

    # Gestionnaire d'interruption pour le capteur PIR, déclenché à la détection de mouvement (front montant)
    # Incrémente le compteur de mouvements chaque fois que le capteur est déclenché
    def motion_detected(pin):
        global count
        count = count + 1  # Incrémenter le compteur à la détection de mouvement

    # Configurer une interruption pour détecter les mouvements à l'aide du capteur PIR
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # Boucle principale pour mettre à jour en continu l'affichage 7 segments avec le compteur courant
    while True:
        # Mettre à jour le premier chiffre (unités)
        pickDigit(0)
        hc595_shift(SEGCODE[count % 10])

        # Mettre à jour le deuxième chiffre (dizaines)
        pickDigit(1)
        hc595_shift(SEGCODE[count % 100 // 10])

        # Mettre à jour le troisième chiffre (centaines)
        pickDigit(2)
        hc595_shift(SEGCODE[count % 1000 // 100])

        # Mettre à jour le quatrième chiffre (milliers)
        pickDigit(3)
        hc595_shift(SEGCODE[count % 10000 // 1000])


Lorsque le code est exécuté, le nombre sur l'affichage 7 segments à 4 chiffres sera incrémenté de un chaque fois qu'une personne passe devant le module PIR.
