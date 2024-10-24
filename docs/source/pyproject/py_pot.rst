.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_pot:

2.11 Tournez le Bouton
===========================

Dans les projets précédents, nous avons utilisé les entrées numériques sur le Pico W.
Par exemple, un bouton peut faire passer une broche d'un niveau bas (éteint) à un niveau haut (allumé). C'est un état de fonctionnement binaire.

Cependant, le Pico W peut également recevoir un autre type de signal d'entrée : l'entrée analogique.
Elle peut être dans n'importe quel état, allant de totalement fermé à totalement ouvert, et présente une plage de valeurs possibles.
L'entrée analogique permet au microcontrôleur de percevoir l'intensité de la lumière, du son, la température, l'humidité, etc. du monde physique.

Généralement, un microcontrôleur nécessite un matériel supplémentaire pour gérer les entrées analogiques - un convertisseur analogique-numérique (ADC).
Mais le Pico W dispose d'un ADC intégré que nous pouvons utiliser directement.


|pin_adc|

Le Pico W dispose de trois broches GPIO pouvant utiliser une entrée analogique : GP26, GP27, GP28. Celles-ci correspondent aux canaux analogiques 0, 1 et 2.
De plus, il existe un quatrième canal analogique, connecté au capteur de température intégré, mais il ne sera pas abordé ici.

Dans ce projet, nous allons essayer de lire la valeur analogique d'un potentiomètre.

* :ref:`cpn_potentiometer`

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schéma**

|sch_pot|

Le potentiomètre est un dispositif analogique, et lorsque vous le tournez dans deux directions différentes, il modifie sa résistance.

Connectez la broche centrale du potentiomètre à la broche analogique GP28. Le Raspberry Pi Pico W contient un convertisseur analogique-numérique multicanaux de 16 bits. Cela signifie qu'il convertit la tension d'entrée comprise entre 0 et la tension de fonctionnement (3,3 V) en une valeur entière comprise entre 0 et 65535, donc la valeur de GP28 varie de 0 à 65535.

La formule de calcul est la suivante :

    (Vp/3.3V) x 65535 = Ap

Ensuite, programmez la valeur de GP28 (potentiomètre) comme la valeur PWM de GP15 (LED).
De cette manière, vous constaterez qu'en tournant le potentiomètre, la luminosité de la LED changera simultanément.

**Câblage**

|wiring_pot|

**Code**

.. note::

    * Ouvrez le fichier ``2.11_turn_the_knob.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value=potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

Lorsque le programme est en cours d'exécution, nous pouvons voir la valeur analogique actuellement lue par la broche GP28 dans la console. 
Tournez le bouton, et la valeur changera de 0 à 65535.
En même temps, la luminosité de la LED augmentera à mesure que la valeur analogique augmente.

**Comment ça marche ?**

.. code-block:: python

    potentiometer = machine.ADC(28)

Accédez à l'ADC associé à une source identifiée par id. Dans cet exemple, il s'agit de GP28.

.. code-block:: python

    potentiometer.read_u16()

Prenez une lecture analogique et renvoyez un entier compris entre 0 et 65535. La valeur de retour représente la lecture brute prise par l'ADC, mise à l'échelle de sorte que la valeur minimale soit 0 et la valeur maximale soit 65535.

* `machine.ADC - MicroPython Docs <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_