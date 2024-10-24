.. note::

    Bonjour, bienvenue dans la communauté SunFounder des passionnés de Raspberry Pi, Arduino & ESP32 sur Facebook ! Approfondissez vos connaissances sur le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_tilt:

2.6 Inclinez-le !
==========================

|img_tilt|

Le commutateur à inclinaison est un dispositif à 2 broches avec une bille métallique à l'intérieur. Lorsque le commutateur est en position verticale, les deux broches sont connectées ; lorsqu'il est incliné, les deux broches sont déconnectées.

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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schéma**

|sch_tilt|

Lorsque le commutateur est en position verticale, GP14 passera à un état haut ; une fois incliné, GP14 passera à un état bas.

La résistance de 10K a pour but de maintenir GP14 dans un état bas stable lorsque le commutateur à inclinaison est incliné.

* :ref:`cpn_tilt`

**Câblage**

|wiring_tilt|

**Code**

.. note::

    * Ouvrez le fichier ``2.6_tilt_switch.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 0:
            print("The switch works!")
            utime.sleep(1)

Après l'exécution du programme, lorsque vous inclinez la breadboard (avec le commutateur à inclinaison), "Le commutateur fonctionne !" s'affichera dans la console.
