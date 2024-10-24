.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_led_bar:

2.2 Afficher le Niveau
=============================

Le premier projet consiste simplement à faire clignoter une LED. Pour ce projet, utilisons la barre de LED, qui contient 10 LED dans un boîtier en plastique, généralement utilisée pour afficher les niveaux de puissance ou de volume.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schéma**

|sch_ledbar|

Dans la barre de LED, il y a 10 LED, chacune pouvant être contrôlée individuellement. L'anode de chaque LED est connectée aux broches GP6 à GP15, et la cathode est reliée à une résistance de 220Ω, puis à la terre (GND).

**Câblage**

|wiring_ledbar|

**Code**

.. note::

    * Ouvrez le fichier ``2.2_display_the_level.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

Sur la barre de LED, vous verrez les LED s'allumer et s'éteindre successivement lorsque le programme est en cours d'exécution.

**Comment ça fonctionne ?**

La barre de LED se compose de dix LED contrôlées par dix broches, ce qui signifie que nous devons définir ces broches. Le processus serait trop fastidieux si nous les définissions une par une. Nous utilisons donc des ``listes``.

.. note::
    Les listes Python sont l'un des types de données les plus polyvalents, permettant de travailler avec plusieurs éléments en même temps. Elles sont créées en plaçant les éléments entre crochets [], séparés par des virgules.

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

Une liste ``pin`` est définie par cette ligne de code, contenant les dix éléments ``6,7,8,9,10,11,12,13,14,15``.
Nous pouvons utiliser l'opérateur d'indexation [] pour accéder à un élément dans une liste. En Python, les indices commencent à 0. Ainsi, une liste de 10 éléments aura des indices de 0 à 9.
Avec cette liste, ``pin[0]`` est ``6`` et ``pin[4]`` est ``10``.

Ensuite, déclarez une liste vide ``led`` qui sera utilisée pour définir dix objets LED.

.. code-block:: python

    led = []    

En raison de la longueur initiale de la liste qui est 0, les opérations directes comme imprimer ``led[0]`` ne fonctionneraient pas. Il y a de nouveaux éléments que nous devons ajouter.

.. code-block:: python

    led.append(None)

Avec cette méthode ``append()``, la liste ``led`` obtient son premier élément, de longueur 1, et ``led[0]`` devient un élément valide malgré sa valeur actuelle de ``None`` (qui signifie null).

Notre prochaine étape est de définir ``led[0]``, la LED connectée à la broche 6, comme le premier objet LED.

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

Le premier objet LED est maintenant défini.

Comme vous pouvez le voir, nous avons créé les dix numéros de broches sous forme de liste **pin**, que nous pouvons substituer dans cette ligne pour faciliter les opérations en masse.

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

Utilisez une instruction ``for`` pour faire en sorte que toutes les 10 broches exécutent l'instruction ci-dessus.

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`syntax_list`
* :ref:`syntax_forloop`

Utilisez une autre boucle ``for`` pour faire changer d'état les dix LED de la barre de LED une par une.

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

Le code est terminé en plaçant le morceau de code ci-dessus dans une boucle while.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)


