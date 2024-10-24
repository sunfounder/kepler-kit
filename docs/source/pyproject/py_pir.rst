.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans le Raspberry Pi, l'Arduino et l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_pir:

2.10 Détection de Mouvement Humain
========================================

Le capteur infrarouge passif (capteur PIR) est un capteur courant capable de mesurer la lumière infrarouge (IR) émise par les objets dans son champ de vision.
En termes simples, il capte le rayonnement infrarouge émis par le corps, détectant ainsi les mouvements des personnes et d'autres animaux.
Plus précisément, il informe la carte de contrôle principale que quelqu'un est entré dans votre pièce.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Schéma**

|sch_pir|

Lorsque le module PIR détecte le passage de quelqu'un, le GP14 sera à un niveau haut, sinon il sera bas.

.. note::
    Le module PIR possède deux potentiomètres : l'un ajuste la sensibilité, l'autre ajuste la distance de détection. Pour un fonctionnement optimal, tournez les deux dans le sens inverse des aiguilles d'une montre jusqu'à la butée.

    |img_PIR_TTE|

**Câblage**

|wiring_pir|

**Code**

.. note::

    * Ouvrez le fichier ``2.10_detect_human_movement.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Somebody here!")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

Après l'exécution du programme, si le module PIR détecte la présence de quelqu'un à proximité, la console Shell affichera "Quelqu'un est là !"

**En savoir plus**

Le PIR est un capteur très sensible. Pour l'adapter à l'environnement d'utilisation, il nécessite des ajustements. Positionnez la face avec les deux potentiomètres face à vous, tournez les deux potentiomètres dans le sens inverse des aiguilles d'une montre jusqu'à la butée et placez le cavalier sur le Pin L et le Pin central.

.. note::

    * Ouvrez le fichier ``2.10_pir_adjustment.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    global timer_delay
    timer_delay = utime.ticks_ms()
    print("start")

    def pir_in_high_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_FALLING, handler=pir_in_low_level)    
        intervals = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()
        print("the dormancy duration is " + str(intervals) + "ms")

    def pir_in_low_level(pin):
        global timer_delay    
        pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 
        intervals2 = utime.ticks_diff(utime.ticks_ms(), timer_delay)
        timer_delay = utime.ticks_ms()        
        print("the duration of work is " + str(intervals2) + "ms")

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_in_high_level) 

Analysons maintenant la méthode de réglage à travers les résultats expérimentaux.

|img_pir_back|

1. Mode de déclenchement

    Regardons les broches avec le cavalier à l'angle.
    Cela permet au PIR d'entrer en mode de déclenchement répétitif ou non répétitif.

    Actuellement, notre cavalier connecte la broche centrale et la broche L, plaçant ainsi le PIR en mode de déclenchement non répétitif.
    Dans ce mode, lorsque le PIR détecte un mouvement, il enverra un signal haut pendant environ 2,8 secondes à la carte de contrôle principale.
    On peut voir dans les données imprimées que la durée de fonctionnement est toujours autour de 2800 ms.

    Ensuite, modifions la position du cavalier inférieur et connectons-le à la broche centrale et à la broche H pour mettre le PIR en mode de déclenchement répétitif.
    Dans ce mode, lorsque le PIR détecte le mouvement (notez qu'il s'agit de mouvement, pas de stationnaire devant le capteur), tant que l'organisme continue à bouger dans la zone de détection, le PIR continuera d'envoyer un signal haut à la carte de contrôle principale.
    On peut voir dans les données imprimées que la durée de fonctionnement est une valeur variable.

#. Réglage du délai

    Le potentiomètre de gauche ajuste l'intervalle entre deux détections.
    
    Actuellement, il est tourné dans le sens inverse des aiguilles d'une montre jusqu'à la butée, ce qui fait que le PIR entre dans un mode de sommeil d'environ 5 secondes après avoir envoyé le signal haut. Pendant ce temps, le PIR ne détectera plus de rayonnement infrarouge dans la zone cible.
    On peut voir dans les données imprimées que la durée de sommeil est toujours supérieure ou égale à 5000 ms.

    Si nous tournons le potentiomètre dans le sens des aiguilles d'une montre, le temps de sommeil augmentera également. Lorsqu'il est tourné complètement dans le sens des aiguilles d'une montre, le temps de sommeil peut atteindre jusqu'à 300 secondes.

#. Réglage de la distance

    Le potentiomètre central sert à ajuster la portée de détection du PIR.

    Tournez le potentiomètre **dans le sens des aiguilles d'une montre** pour augmenter la portée de détection, avec une distance maximale d'environ 0 à 7 mètres.
    En le tournant **dans le sens inverse des aiguilles d'une montre**, la portée de détection diminue, avec une distance minimale d'environ 0 à 3 mètres.
