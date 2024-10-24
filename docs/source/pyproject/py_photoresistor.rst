.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans le monde du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux démonstrations exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_photoresistor:

2.12 Ressentir la Lumière
=============================

La photorésistance est un dispositif typique pour les entrées analogiques, et elle est utilisée de manière très similaire à un potentiomètre. Sa valeur de résistance dépend de l'intensité de la lumière : plus la lumière irradiée est forte, plus sa résistance diminue ; à l'inverse, elle augmente.

* :ref:`cpn_photoresistor`

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
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schéma**

|sch_photoresistor|

Dans ce circuit, la résistance de 10K et la photorésistance sont connectées en série, et le courant qui les traverse est identique. La résistance de 10K agit comme une protection, et le GP28 lit la valeur après la conversion de la tension de la photorésistance.

Lorsque la lumière est plus intense, la résistance de la photorésistance diminue, ce qui réduit sa tension, donc la valeur de GP28 diminue également ; si la lumière est suffisamment forte, la résistance de la photorésistance sera proche de 0, et la valeur de GP28 se rapprochera de 0. À ce moment, la résistance de 10K joue un rôle de protection, empêchant ainsi de connecter le 3.3V et la masse (GND) directement, ce qui provoquerait un court-circuit.

Si vous placez la photorésistance dans un environnement sombre, la valeur de GP28 augmentera. Dans une obscurité totale, la résistance de la photorésistance sera infinie et sa tension sera proche de 3,3V (la résistance de 10K devient négligeable), et la valeur de GP28 sera proche de la valeur maximale de 65535.

La formule de calcul est la suivante :

    (Vp/3.3V) x 65535 = Ap

**Câblage**

|wiring_photoresistor|

**Code**

.. note::

    * Ouvrez le fichier ``2.12_feel_the_light.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

Après l'exécution du programme, la console Shell affichera les valeurs de la photorésistance. Vous pouvez éclairer la photorésistance avec une lampe de poche ou la couvrir avec votre main pour observer les variations de la valeur.
