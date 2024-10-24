.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_74hc_4dig:

5.3 Compteur de Temps
================================

L'afficheur 7 segments à 4 chiffres est composé de quatre afficheurs 7 segments fonctionnant ensemble.

L'afficheur 7 segments à 4 chiffres fonctionne de manière indépendante. Il utilise le principe de la persistance 
rétinienne pour afficher rapidement les caractères de chaque segment en boucle afin de former des chaînes continues.

Par exemple, lorsque "1234" est affiché, "1" s'affiche sur le premier segment 7, et "234" ne s'affiche pas. Après un 
certain temps, le deuxième segment 7 affiche "2", tandis que les 1er, 3e et 4e segments sont éteints, et ainsi de suite,
les quatre chiffres s'affichent à tour de rôle. Ce processus est très court (environ 5 ms), et grâce à l'effet de rémanence 
optique et au principe de persistance visuelle, nous pouvons voir les quatre caractères simultanément.

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

Vous pouvez également les acheter séparément avec les liens ci-dessous :

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
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schéma**

|sch_4dig|

Ici, le principe de câblage est essentiellement le même que pour :ref:`py_74hc_led`, la seule différence étant que Q0-Q7 sont connectés aux broches a ~ g de l'afficheur 7 segments à 4 chiffres.

Ensuite, G10 ~ G13 sélectionnera quel segment 7 doit fonctionner.

**Câblage**

|wiring_4dig|

**Code**

.. note::

    * Ouvrez le fichier ``5.3_time_counter.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()
        time.sleep_us(200)

    while True:
        count = timer1()
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])     

Après avoir exécuté le programme, vous verrez l'afficheur 7 segments à 4 chiffres se transformer en compteur, augmentant de 1 chaque seconde.

**Comment ça fonctionne ?**

L'écriture des signaux sur chaque segment 7 se fait de la même manière que pour :ref:`py_74hc_7seg`, en utilisant la fonction ``hc595_shift()``.
Le point central de l'afficheur 7 segments à 4 chiffres est de sélectionner chaque segment individuellement. Le code associé est le suivant.

.. code-block:: python

    placePin = []
    pin = [13,12,11,10]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    while True:
        
        hc595_shift(SEGCODE[count%10])
        pickDigit(0)

        hc595_shift(SEGCODE[count%100//10])
        pickDigit(1)
        
        hc595_shift(SEGCODE[count%1000//100])
        pickDigit(2)    
        
        hc595_shift(SEGCODE[count%10000//1000])
        pickDigit(3)   

Ici, quatre broches (GP10, GP11, GP12, GP13) contrôlent chaque chiffre de l'afficheur 7 segments à 4 chiffres individuellement.
Lorsque l'état de ces broches est ``0``, l'afficheur correspondant est actif ; lorsque l'état est ``1``, l'afficheur est inactif.

La fonction ``pickDigit(digit)`` désactive les quatre chiffres puis active un chiffre spécifique individuellement.
Ensuite, ``hc595_shift()`` est utilisé pour écrire le code 8 bits correspondant sur l'afficheur 7 segments.

L'afficheur 7 segments à 4 chiffres doit être activé en continu et en alternance pour que nous puissions voir l'affichage des quatre chiffres, ce qui signifie que le programme principal ne peut pas ajouter facilement du code qui affecterait le minutage.
Cependant, nous devons ajouter une fonction de chronométrage à cet exemple, et si nous ajoutons un ``sleep(1)``, nous saurons qu'il a quatre chiffres.
Nous verrons alors l'illusion d'un affichage simultané des quatre chiffres, révélant qu'un seul segment est allumé à la fois.
L'utilisation de la fonction ``time.ticks_ms()`` de la bibliothèque ``time`` est une excellente méthode pour cela.

.. code-block:: python

    import time

    timerStart=time.ticks_ms()

    def timer1():
        return int((time.ticks_ms()-timerStart)/1000)

    while True:
        count = timer1()


La fonction ``time.ticks_ms()`` récupère un temps (non explicite), et nous enregistrons la première valeur obtenue sous ``timerStart``.
Ensuite, lorsque le temps est requis, la fonction ``time.ticks_ms()`` est appelée de nouveau, et la valeur est soustraite de ``timerStart`` pour obtenir la durée d'exécution du programme (en millisecondes).

Enfin, convertissez et affichez cette valeur sur l'afficheur 7 segments à 4 chiffres, et c'est terminé.

* `Time - MicroPython Docs <https://docs.micropython.org/en/latest/library/time.html>`_
