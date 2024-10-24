.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_reed:

2.9 Ressentez le Magnétisme
================================

Le type de contact reed le plus courant contient une paire de lames métalliques flexibles et magnétisables dont les extrémités sont séparées par un petit écart lorsque l'interrupteur est ouvert.

Un champ magnétique provenant d'un électroaimant ou d'un aimant permanent provoque l'attraction des lames, complétant ainsi un circuit électrique.
La force de ressort des lames les sépare, ouvrant le circuit lorsque le champ magnétique cesse.

Un exemple courant d'application d'un interrupteur reed est la détection de l'ouverture d'une porte ou d'une fenêtre pour un système d'alarme.

* :ref:`cpn_reed`

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
        - :ref:`cpn_reed`
        - 1
        - 

**Schéma**

|sch_reed|

Par défaut, GP14 est à un niveau bas ; il passe à un niveau haut lorsque l'aimant est proche du contact reed.

La résistance de 10KΩ a pour but de maintenir GP14 à un niveau bas stable en l'absence d'aimant.

**Câblage**

|wiring_reed|

**Code**

.. note::

    * Ouvrez le fichier ``2.9_feel_the_magnetism.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    reed = machine.Pin(14, machine.Pin.IN)
    while True:
        if reed.value() == 1:
            print("There are magnets here!!")
            utime.sleep(1)

Lorsque le code est exécuté, GP14 passe à un niveau haut lorsqu'un aimant est proche du contact reed, sinon il reste à un niveau bas. Tout comme le bouton décrit au chapitre :ref:`py_button`.

**En savoir plus**

Cette fois, nous avons essayé une méthode plus flexible d'utilisation des interrupteurs : les requêtes d'interruption, ou IRQ.

Par exemple, vous lisez un livre page par page, comme si un programme exécutait un fil de processus. À ce moment-là, quelqu'un vous pose une question, interrompant votre lecture. Cette personne effectue alors une requête d'interruption : elle vous demande de cesser ce que vous faites, de répondre à ses questions, puis de reprendre votre lecture une fois terminé.

Les requêtes d'interruption en MicroPython fonctionnent de la même manière, elles permettent à certaines opérations d'interrompre le programme principal.

.. note::

    * Ouvrez le fichier ``2.9_feel_the_magnetism_irq.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    reed_switch = machine.Pin(14, machine.Pin.IN)

    def detected(pin):
        print("Magnet!")

    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=detected)


Ici, une fonction de rappel ``detected(pin)`` est définie, appelée gestionnaire d'interruption. Elle sera exécutée lorsqu'une requête d'interruption sera déclenchée. Ensuite, une requête d'interruption est configurée dans le programme principal, comprenant deux parties : le ``trigger`` et le ``handler``.

Dans ce programme, ``trigger`` est ``IRQ_RISING``, ce qui indique que la valeur de la broche passe de bas à haut (c'est-à-dire, activation du contact).

``handler`` est ``detected``, la fonction de rappel que nous avons définie précédemment.

* `machine.Pin.irq - Micropython Docs <https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.irq>`_