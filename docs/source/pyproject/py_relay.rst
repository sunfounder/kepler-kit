.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_relay:

2.16 Contrôler un autre circuit
=================================

Dans notre vie quotidienne, nous appuyons sur un interrupteur pour allumer ou éteindre une lampe.
Mais que faire si vous souhaitez contrôler la lampe avec le Pico W afin qu'elle puisse s'éteindre automatiquement après dix minutes ?

Un relais peut vous aider à réaliser cette idée.

Un relais est en réalité un type d'interrupteur particulier qui est contrôlé par un côté du circuit (généralement un circuit basse tension) et utilisé pour contrôler l'autre côté du circuit (généralement un circuit haute tension).
Cela permet de rendre nos appareils ménagers contrôlables par un programme, de les transformer en dispositifs intelligents, voire de les connecter à Internet.

.. warning::
    La modification des appareils électriques présente un grand danger, ne tentez pas cela à la légère, faites-le sous la supervision de professionnels.

* :ref:`cpn_relay`

Ici, nous utilisons simplement un circuit alimenté par un module d'alimentation sur breadboard comme exemple pour montrer comment le contrôler à l'aide d'un relais.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Câblage**

Commencez par créer un circuit basse tension pour contrôler un relais.
L'activation du relais nécessite un courant élevé, donc un transistor est nécessaire, ici nous utilisons le S8050.

|sch_relay_1|

|wiring_relay_1|

Une diode (diode de roue libre) est utilisée ici pour protéger le circuit. La cathode est l'extrémité avec la bande argentée connectée à l'alimentation, et l'anode est reliée au transistor.

Lorsque l'entrée de tension passe de Haut (5V) à Bas (0V), le transistor passe de la saturation (amplification, saturation, et coupure) à la coupure, et il n'y a soudainement plus de passage pour le courant à travers la bobine.

À ce stade, si cette diode de roue libre n'existe pas, la bobine produira un potentiel électrique auto-induit aux deux extrémités, plusieurs fois supérieur à la tension d'alimentation, et cette tension, additionnée à celle provenant de l'alimentation du transistor, sera suffisante pour l'endommager.

En ajoutant la diode, la bobine et la diode forment instantanément un nouveau circuit alimenté par l'énergie stockée dans la bobine pour se décharger, évitant ainsi qu'une tension excessive n'endommage des composants tels que les transistors.

* :ref:`cpn_diode`    
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

À ce stade, le programme est prêt à être exécuté, et une fois lancé, vous entendrez le son "tik tok", correspondant au fonctionnement du contacteur interne du relais.

Ensuite, connectez les deux extrémités du circuit de charge aux broches 3 et 6 du relais respectivement.

..(Prenons comme exemple le circuit simple alimenté par le module d'alimentation sur breadboard décrit dans l'article précédent.)

|sch_relay_2|

|wiring_relay_2|

À ce stade, le relais pourra contrôler l'allumage et l'extinction du circuit de charge.

**Code**

.. note::

    * Ouvrez le fichier ``2.16_control_another_circuit.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    relay = machine.Pin(15, machine.Pin.OUT)
    while True:
        relay.value(1)
        utime.sleep(2)
        relay.value(0)
        utime.sleep(2)

Lorsque le code est exécuté, le relais changera l'état de fonctionnement du circuit contrôlé toutes les deux secondes.
Vous pouvez commenter manuellement l'une des lignes pour mieux comprendre la correspondance entre le circuit du relais et le circuit de charge.


**En savoir plus**


La broche 3 du relais est normalement ouverte et ne se ferme que lorsque la bobine du contacteur est activée ; la broche 4 est normalement fermée et se ferme lorsque la bobine du contacteur est alimentée.
La broche 1 est reliée à la broche 6 et constitue la borne commune du circuit de charge.

En passant une extrémité du circuit de charge de la broche 3 à la broche 4, vous obtiendrez l'état de fonctionnement exactement opposé.
