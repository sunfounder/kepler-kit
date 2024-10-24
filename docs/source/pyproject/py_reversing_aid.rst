.. note::

    Bonjour, bienvenue dans la communauté des passionnés SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez plus en profondeur le Raspberry Pi, l'Arduino et l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_reversing_aid:

7.10 Assistance au Recul
============================

Ce projet utilise une LED, un buzzer et un module ultrasonique pour créer un système d'assistance au recul.
Nous pouvons l'installer sur une voiture télécommandée pour simuler le processus réel de recul d'une voiture dans un garage.


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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2 (1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Buzzer Actif :ref:`cpn_buzzer`
        - 1
        -
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schéma**

|sch_reversing_aid|

**Câblage**

|wiring_reversing_aid| 

**Code**

.. note::

    * Ouvrez le fichier ``7.10_reversing_aid.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    # Initialiser les broches pour le buzzer et la LED
    buzzer = machine.Pin(15, machine.Pin.OUT)  # Buzzer sur la broche 15
    led = machine.Pin(14, machine.Pin.OUT)  # LED sur la broche 14

    # Initialiser les broches pour le capteur ultrasonique (HC-SR04)
    TRIG = machine.Pin(17, machine.Pin.OUT)  # Broche Trigger pour le capteur ultrasonique
    ECHO = machine.Pin(16, machine.Pin.IN)  # Broche Echo pour le capteur ultrasonique

    dis = 100  # Variable globale pour stocker la distance

    # Fonction pour mesurer la distance avec le capteur ultrasonique
    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()

        timeout_start = time.ticks_us()  # Utiliser les microsecondes pour plus de précision
        
        # Attendre que la broche ECHO passe à haut (début de l'impulsion echo)
        while not ECHO.value():
            if time.ticks_diff(time.ticks_us(), timeout_start) > 30000:  # Timeout 30ms
                return -1  # Timeout, retourner -1 si aucune impulsion n'est détectée
        
        time1 = time.ticks_us()  # Temps de départ pour le calcul de la largeur de l'impulsion
        
        # Attendre que la broche ECHO passe à bas (fin de l'impulsion echo)
        while ECHO.value():
            if time.ticks_diff(time.ticks_us(), time1) > 30000:  # Timeout 30ms
                return -1  # Timeout, retourner -1 si l'impulsion est trop longue
        
        time2 = time.ticks_us()  # Temps de fin pour le calcul de la largeur de l'impulsion
        
        # Calculer la distance en fonction de la durée de l'impulsion echo
        during = time.ticks_diff(time2, time1)
        distance_cm = during * 340 / 2 / 10000  # Convertir le temps en distance en cm
        return distance_cm

    # Fonction pour faire bipper le buzzer et allumer la LED
    def beep():
        buzzer.value(1)  # Allumer le buzzer
        led.value(1)  # Allumer la LED
        time.sleep(0.1)  # Durée du bip
        buzzer.value(0)  # Éteindre le buzzer
        led.value(0)  # Éteindre la LED
        time.sleep(0.1)  # Petite pause entre les bips

    # Initialiser les variables pour contrôler les intervalles de bips
    intervals = 2000  # Long intervalle initial par défaut
    previousMillis = time.ticks_ms()  # Stocker le temps précédent pour suivre les intervalles de bips

    # Boucle principale pour gérer les intervalles de bips basés sur la distance
    while True:
        dis = distance()  # Mesurer la distance directement dans la boucle principale

        # Ajuster les intervalles de bips en fonction de la distance
        if dis > 0:  # S'assurer que la distance mesurée est valide
            if dis <= 10:
                intervals = 300  # Distance proche, bips plus rapides
            elif dis <= 20:
                intervals = 500  # Distance moyenne-proche, bips modérés
            elif dis <= 50:
                intervals = 1000  # Distance moyenne, bips plus lents
            else:
                intervals = 2000  # Grande distance, bips très lents

            # Afficher la distance mesurée
            print(f'Distance : {dis:.2f} cm')
            
            # Vérifier s'il est temps de bipper à nouveau en fonction de l'intervalle
            currentMillis = time.ticks_ms()  # Obtenir l'heure actuelle
            if time.ticks_diff(currentMillis, previousMillis) >= intervals:
                beep()  # Faire bipper le buzzer et clignoter la LED
                previousMillis = currentMillis  # Mettre à jour le temps du dernier bip
            
        time.sleep_ms(100)  # Petit délai pour éviter les lectures trop fréquentes


* Dès que le programme démarre, le capteur ultrasonique lira en continu la distance jusqu'à l'obstacle devant vous, et vous pourrez voir la valeur exacte de la distance sur le shell.
* La LED et le buzzer changeront la fréquence de clignotement et de bip en fonction de la distance mesurée, indiquant ainsi la proximité de l'obstacle.
* L'article :ref:`py_ultrasonic` mentionne que lorsque le capteur ultrasonique fonctionne, le programme sera en pause.
* Pour éviter de perturber le timing de la LED ou du buzzer, nous avons créé un thread séparé pour la mesure de distance dans cet exemple.
