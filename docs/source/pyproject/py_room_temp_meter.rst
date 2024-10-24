.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans le monde du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_room_temp:

7.2 Thermomètre de Pièce
======================================

À l'aide d'une thermistance et d'un écran LCD1602 I2C, nous pouvons créer un thermomètre de pièce.

Ce projet est très simple, il se base sur :ref:`py_temp` avec l'ajout d'un écran LCD1602 I2C pour afficher la température.


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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schéma**

|sch_room_temp|


**Câblage**

|wiring_room_temp|

**Code**

.. note::

    * Ouvrez le fichier ``7.2_room_temperature_meter.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import math

    # Initialiser la thermistance (ADC sur la broche 28) et l'écran LCD
    thermistor = machine.ADC(28)  # Entrée analogique de la thermistance

    # Initialiser la communication I2C pour l'écran LCD1602
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Créer un objet LCD pour contrôler l'écran LCD1602
    lcd = LCD(i2c)

    # Boucle principale pour lire en continu la température et l'afficher
    while True:
        # Lire la valeur brute de l'ADC de la thermistance
        temperature_value = thermistor.read_u16()

        # Convertir la valeur brute de l'ADC en tension (gamme de 0-3,3V)
        Vr = 3.3 * float(temperature_value) / 65535  # Conversion de la valeur ADC en tension

        # Calculer la résistance de la thermistance (en utilisant un diviseur de tension avec une résistance de 10kΩ)
        Rt = 10000 * Vr / (3.3 - Vr)  # Rt = résistance de la thermistance

        # Utiliser l'équation de Steinhart-Hart pour calculer la température en Kelvin
        # Les valeurs utilisées sont spécifiques à la thermistance (3950 est le coefficient bêta)
        temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))  # Température en Kelvin

        # Convertir la température de Kelvin en Celsius
        Cel = temp - 273.15

        # Afficher la température sur l'écran LCD en Celsius
        string = " Temperature is \n    " + str('{:.2f}'.format(Cel)) + " C"  # Format de la chaîne pour l'affichage LCD
        lcd.message(string)  # Afficher la chaîne sur l'écran LCD

        utime.sleep(1)  # Attendre 1 seconde
        lcd.clear()  # Effacer l'écran LCD pour la prochaine lecture


L'écran LCD affichera la valeur de la température dans l'environnement actuel après le démarrage du programme.

.. note:: 
    Si le code et le câblage sont corrects mais que l'écran LCD ne montre toujours rien, vous pouvez tourner le potentiomètre à l'arrière pour augmenter le contraste.

