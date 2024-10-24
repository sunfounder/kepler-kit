.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_joystick:

4.1 Basculer le Joystick
================================

Si vous jouez beaucoup aux jeux vidéo, vous connaissez sûrement bien le joystick.
Il est souvent utilisé pour déplacer un personnage, faire pivoter l'écran, etc.

Le principe qui permet au joystick de transmettre nos actions à l'ordinateur est très simple.
On peut le considérer comme étant composé de deux potentiomètres perpendiculaires l'un à l'autre.
Ces deux potentiomètres mesurent la valeur analogique du joystick sur les axes vertical et horizontal, produisant ainsi une valeur (x, y) dans un système de coordonnées cartésiennes.

Le joystick de ce kit dispose également d'une entrée numérique, qui s'active lorsque le joystick est pressé.

* :ref:`cpn_joystick`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 


**Schéma**

|sch_joystick|

La broche SW est connectée à une résistance de tirage de 10KΩ, ce qui permet d'obtenir un niveau haut stable sur la broche SW (axe Z) lorsque le joystick n'est pas pressé ; sinon, le SW serait en état de flottement et la valeur de sortie pourrait varier entre 0 et 1.

**Câblage**

|wiring_joystick|


**Code**

.. note::

    * Ouvrez le fichier ``4.1_toggle_the_joystick.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200)    

Après l'exécution du programme, le terminal affiche les valeurs x, y, z du joystick.


* Les valeurs des axes x et y sont des valeurs analogiques variant de 0 à 65535.
* L'axe Z est une valeur numérique avec un état de 1 ou 0.
