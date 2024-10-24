.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_button:

2.5 Lecture de la Valeur du Bouton
==============================================

Ces broches ont à la fois des fonctions d'entrée et de sortie, comme l'indique leur nom GPIO (General-purpose input/output). Auparavant, nous avons utilisé la fonction de sortie ; dans ce chapitre, nous utiliserons la fonction d'entrée pour lire la valeur du bouton.

* :ref:`cpn_button`

**Composants Requis**

Pour ce projet, nous avons besoin des composants suivants : 

Il est plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous :

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
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schéma**

|sch_button|

Il suffit de connecter une broche du bouton à 3.3V et l'autre broche à GP14 ; ainsi, lorsque le bouton est pressé, GP14 sera à un niveau haut. Cependant, quand le bouton n'est pas pressé, GP14 est en état flottant et peut être soit haut, soit bas. Pour obtenir un niveau bas stable lorsque le bouton n'est pas pressé, GP14 doit être relié à la masse via une résistance de pull-down de 10KΩ.

**Câblage**

|wiring_button|

.. Suivons la direction du schéma pour construire le circuit !

.. 1. Connectez la broche 3V3 du Pico W au bus d'alimentation positif de la breadboard.
.. #. Insérez le bouton dans la breadboard en chevauchant la ligne centrale.

.. note::
    Un bouton à quatre broches a la forme d'un "H". Les deux broches de gauche ou de droite sont connectées, ce qui signifie que lorsqu'il est placé sur la ligne centrale, il connecte deux demi-rangées ayant le même numéro de rangée. (Par exemple, dans mon circuit, E23 et F23 sont déjà connectés, tout comme E25 et F25).

    Tant que le bouton n'est pas pressé, les broches gauche et droite sont indépendantes et le courant ne peut pas circuler d'un côté à l'autre.

.. #. Utilisez un fil de connexion pour relier une broche du bouton au bus positif (dans mon cas, la broche en haut à droite).
.. #. Connectez l'autre broche (en haut à gauche ou en bas à gauche) à GP14 avec un fil de connexion.
.. #. Utilisez une résistance de 10KΩ pour connecter la broche en haut à gauche du bouton au bus négatif.
.. #. Connectez le bus d'alimentation négatif de la breadboard à la masse (GND) du Pico.

**Code**

.. note::

    * Ouvrez le fichier ``2.5_read_button_value.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

Dès que le code s'exécute, le Shell affiche "Vous avez appuyé sur le bouton !"

**Mode de Fonctionnement Pull-up**

La prochaine partie concerne le câblage et le code lorsque vous utilisez le bouton en mode pull-up.

|sch_button_pullup|

|wiring_button_pullup|

La seule différence avec le mode pull-down est que la résistance de 10KΩ est connectée à 3.3V et le bouton à la masse, de sorte que lorsque le bouton est pressé, GP14 recevra un niveau bas, ce qui est l'inverse de la valeur obtenue en mode pull-down. 
Il suffit donc de modifier le code par ``if button.value() == 0:``.

Voir également la référence ici :

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_