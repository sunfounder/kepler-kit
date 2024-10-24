.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans le monde du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à notre communauté et notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_rgb:

2.4 Lumière Colorée
==============================================

Comme nous le savons, la lumière peut se superposer. Par exemple, le mélange de la lumière bleue et de la lumière verte donne de la lumière cyan, et le rouge et le vert donnent du jaune. 
C'est ce qu'on appelle la "synthèse additive des couleurs".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

En utilisant cette méthode, nous pouvons mélanger les trois couleurs primaires pour produire n'importe quelle couleur visible selon différentes proportions. Par exemple, l'orange peut être obtenu avec plus de rouge et moins de vert.

Dans ce chapitre, nous allons utiliser une LED RGB pour explorer le mystère de la synthèse additive des couleurs !

Une LED RGB est équivalente à l'encapsulation d'une LED rouge, d'une LED verte et d'une LED bleue sous un même capot, et les trois LEDs partagent une seule broche cathode. 
En fournissant un signal électrique à chaque broche d'anode, la lumière de la couleur correspondante peut être affichée. En modifiant l'intensité du signal électrique de chaque anode, on peut obtenir diverses couleurs.

* :ref:`cpn_rgb`

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
        - 3 (1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schéma**

|sch_rgb|

Les broches PWM GP13, GP14 et GP15 contrôlent respectivement les broches rouge, verte et bleue de la LED RGB, et la broche cathode commune est connectée à la masse (GND). Cela permet à la LED RGB d'afficher une couleur spécifique en superposant la lumière sur ces broches avec différentes valeurs PWM.


**Câblage**

|img_rgb_pin|

La LED RGB a 4 broches : la longue broche est la cathode commune, qui est généralement connectée à la masse (GND) ; la broche à gauche de la plus longue est la rouge ; et les deux broches à droite sont la verte et la bleue.


|wiring_rgb|


**Code**


.. note::

    * Ouvrez le fichier ``2.4_colorful_light.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
        return rgb_value

    def color_set(red_value,green_value,blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255,128,0)

Ici, nous pouvons choisir notre couleur préférée dans un logiciel de dessin (comme Paint) et l'afficher avec la LED RGB.

|img_take_color|

Inscrivez la valeur RGB dans ``color_set()``, et vous verrez la LED RGB s'illuminer avec les couleurs souhaitées.


**Comment ça marche ?**

Pour permettre aux trois couleurs primaires de fonctionner ensemble, nous avons défini une fonction ``color_set()``.

À l'heure actuelle, les pixels du matériel informatique utilisent généralement des représentations en 24 bits. Chaque couleur primaire est divisée en 8 bits, et la plage de valeurs des couleurs est de 0 à 255. Il y a 256 combinaisons possibles pour chacune des trois couleurs primaires (n'oubliez pas de compter 0 !), donc 256 x 256 x 256 = 16 777 216 couleurs.
La fonction ``color_set()`` utilise également la notation en 24 bits, ce qui permet de choisir plus facilement une couleur.


Et comme la plage de valeurs de ``duty_u16()`` est de 0 à 65535 (au lieu de 0 à 255) lors de la transmission des signaux aux LEDs RGB via PWM, nous avons défini les fonctions ``color_to_duty()`` et ``interval_mapping()`` pour mapper les valeurs de couleur aux valeurs de cycle de service.
