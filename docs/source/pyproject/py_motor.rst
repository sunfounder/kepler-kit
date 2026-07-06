.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_motor:

3.5 Petit ventilateur
=======================

Nous allons utiliser le TA6586 pour piloter le moteur à courant continu (DC) afin de le faire tourner dans le sens horaire et antihoraire. 
Étant donné que le moteur DC nécessite un courant relativement important, par mesure de sécurité, 
nous utilisons ici un module d'alimentation pour alimenter le moteur.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - Power Pack
        - 1
        -  
    *   - 9
        - Support de batterie
        - 1
        -  

**Schéma**

|sch_motor|

**Câblage**

.. note::

    * Comme les moteurs DC nécessitent un courant élevé, nous utilisons ici un module chargeur Li-po pour alimenter le moteur par sécurité.
    * Assurez-vous que votre module chargeur Li-po est connecté comme indiqué dans le schéma. Sinon, un court-circuit pourrait endommager votre batterie et votre circuiterie.

|wiring_motor|

**Code**

.. note::

    * Ouvrez le fichier ``3.5_small_fan.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

Une fois le programme lancé, le moteur tournera d'avant en arrière selon un schéma régulier.

.. note::

    * Si le moteur continue de tourner après que vous ayez cliqué sur le bouton d'arrêt, vous devez réinitialiser la broche **RUN** sur le Pico W avec un fil connecté à la masse (GND), puis débrancher ce fil pour relancer le code.
    * Cela est dû au fait que le moteur fonctionne avec un courant trop élevé, ce qui peut entraîner la déconnexion du Pico W de l'ordinateur.

    |wiring_run_reset|