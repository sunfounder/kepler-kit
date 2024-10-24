.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_fruit_piano:

7.9 Piano de fruits
============================


La conductivité électrique se trouve dans de nombreux objets métalliques, ainsi que dans le corps humain et les fruits.
Cette propriété permet de créer un projet amusant : un piano de fruits.
En d'autres termes, nous transformons des fruits en claviers qui peuvent jouer de la musique simplement en les touchant.

|fruit_piano|

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - Buzzer passif :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schéma**

|sch_fruit_piano| 

Pour transformer le fruit en touche de piano, vous devez connecter les électrodes du MPR121 au fruit (par exemple, dans la queue de la banane).

Au départ, le MPR121 va s'initialiser et chaque électrode obtiendra une valeur basée sur la charge actuelle ; lorsqu'un conducteur (tel qu'un corps humain) touche une électrode, la charge se modifie et se rééquilibre.
Par conséquent, la valeur de l'électrode diffère de sa valeur initiale, indiquant au microcontrôleur qu'elle a été touchée.
Pendant ce processus, assurez-vous que le câblage de chaque électrode est stable afin que sa charge soit équilibrée lors de l'initialisation.


**Câblage**


|wiring_fruit_piano| 


**Code**


.. note::

    * Ouvrez le fichier ``7.9_fruit_piano.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`. 
    
    * Vous devrez utiliser la bibliothèque appelée ``mpr121.py``, vérifiez qu'elle a été téléchargée sur Pico W, pour un tutoriel détaillé, reportez-vous à :ref:`add_libraries_py`.


.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time
    import urandom

    # Initialiser la connexion I2C pour le capteur tactile capacitif MPR121
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))  # Configurer le bus I2C avec SDA sur la broche 6 et SCL sur la broche 7
    mpr = MPR121(i2c)  # Créer une instance du capteur tactile MPR121

    # Fréquences des notes pour le buzzer (en Hertz) pour différentes notes musicales
    NOTE_A3 = 220
    NOTE_B3 = 247
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523
    NOTE_D5 = 587
    NOTE_E5 = 659

    # Initialiser le PWM pour le buzzer sur la broche 15
    buzzer = machine.PWM(machine.Pin(15))

    # Liste des fréquences des notes à jouer par le buzzer
    note = [NOTE_A3, NOTE_B3, NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5, NOTE_D5, NOTE_E5]

    # Fonction pour jouer une tonalité sur le buzzer à une fréquence spécifique
    def tone(pin, frequency):
        pin.freq(frequency)  # Régler la fréquence du buzzer
        pin.duty_u16(30000)  # Régler le cycle de travail à 50% (approx.)

    # Fonction pour arrêter la tonalité (couper le buzzer)
    def noTone(pin):
        pin.duty_u16(0)  # Régler le cycle de travail à 0% (silence)

    # Initialisation de la LED RGB via PWM sur les broches 13, 12 et 11 (pour rouge, vert, bleu)
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(12))
    blue = machine.PWM(machine.Pin(11))

    # Régler la fréquence PWM pour chaque couleur (1kHz)
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # Fonction pour mapper une valeur `x` d'une plage à une autre
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Fonction pour allumer aléatoirement la LED RGB avec des valeurs de couleur aléatoires
    def lightup():
        red.duty_u16(int(urandom.uniform(0, 65535)))  # Régler l'intensité aléatoire pour le rouge
        green.duty_u16(int(urandom.uniform(0, 65535)))  # Régler l'intensité aléatoire pour le vert
        blue.duty_u16(int(urandom.uniform(0, 65535)))  # Régler l'intensité aléatoire pour le bleu

    # Fonction pour éteindre toutes les couleurs de la LED RGB (tout mettre à 0)
    def dark():
        red.duty_u16(0)  # Éteindre la LED rouge
        green.duty_u16(0)  # Éteindre la LED verte
        blue.duty_u16(0)  # Éteindre la LED bleue

    # Boucle principale du projet
    lastState = mpr.get_all_states()  # Obtenir l'état initial de toutes les entrées tactiles
    touchMills = time.ticks_ms()  # Enregistrer le moment du dernier événement tactile
    beat = 500  # Définir la durée de l'effet sonore et lumineux (500ms)

    # Boucle principale pour gérer la détection tactile et les effets
    while True:
        currentState = mpr.get_all_states()  # Obtenir l'état actuel de toutes les entrées tactiles
        
        # Vérifier s'il y a un changement dans l'état des entrées tactiles (début ou fin de contact)
        if currentState != lastState:
            for i in range(12):  # Itérer sur les 12 entrées tactiles possibles
                # Vérifier si un contact a commencé (touché dans l'état actuel mais pas dans le dernier état)
                if i in list(currentState) and not i in list(lastState):
                    tone(buzzer, note[i])  # Jouer la note correspondante pour l'entrée touchée
                    lightup()  # Allumer la LED RGB avec des couleurs aléatoires
                    touchMills = time.ticks_ms()  # Enregistrer le moment de l'événement tactile
        
        # Vérifier si la durée du beat est écoulée ou si aucune entrée tactile n'est active
        if time.ticks_diff(time.ticks_ms(), touchMills) >= beat or len(currentState) == 0:
            noTone(buzzer)  # Arrêter le buzzer
            dark()  # Éteindre la LED RGB
        
        # Mettre à jour le dernier état avec l'état actuel pour la prochaine itération
        lastState = currentState


Veuillez ne pas toucher le fruit avant que le programme ne démarre pour éviter de fausser la référence initiale lors de l'initialisation.
Après le démarrage du programme, touchez doucement le fruit, le buzzer émettra la tonalité correspondante et la lumière RGB clignotera une fois de manière aléatoire.
