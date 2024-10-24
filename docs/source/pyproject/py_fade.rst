.. note::

    Bonjour, bienvenue dans la communauté SunFounder des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_fade:

2.3 Variation progressive de la LED
===================================

Jusqu'à présent, nous avons seulement utilisé deux signaux de sortie : niveau 
haut et niveau bas (aussi appelés ON et OFF), ce que l'on appelle une sortie 
numérique. Cependant, dans de nombreux cas pratiques, les dispositifs ne 
fonctionnent pas uniquement en mode ON/OFF, par exemple pour ajuster la vitesse 
d'un moteur ou la luminosité d'une lampe de bureau. Pour atteindre cet objectif, 
on utilisait autrefois un curseur pour ajuster la résistance, mais cette méthode 
est peu fiable et inefficace. Ainsi, la modulation par largeur d'impulsion (PWM) 
est apparue comme une solution viable pour résoudre ces problèmes complexes.

Une impulsion est une sortie numérique comprenant un niveau haut et un niveau 
bas. La largeur d'impulsion de ces broches peut être ajustée en modifiant la 
vitesse de passage entre ON et OFF.

Lorsque nous faisons clignoter rapidement une LED (par exemple, toutes les 20ms, 
ce qui correspond à la période de rétention visuelle pour la plupart des gens), en l'allumant, en l'éteignant, puis en la rallumant, nous ne verrons pas qu'elle s'éteint. Cependant, la luminosité de la lumière sera légèrement plus faible. Pendant cette période, plus la LED reste allumée, plus elle paraît lumineuse. Autrement dit, pendant le cycle, plus l'impulsion est large, plus le "signal électrique" émis par le microcontrôleur est fort. C'est ainsi que la PWM contrôle la luminosité des LED (ou la vitesse d'un moteur).

* `Pulse-width modulation - Wikipedia <https://en.wikipedia.org/wiki/Pulse-width_modulation>`_

Il y a quelques points importants à prendre en compte lorsque le Pico W utilise la PWM. Jetons un coup d'œil à cette image.

|pin_pwm|

Le Pico W prend en charge la PWM sur chaque broche GPIO, mais il existe en réalité 16 sorties PWM indépendantes (et non 30), réparties entre les broches GP0 à GP15 sur la gauche, et la sortie PWM des GPIO de droite est identique à celle de gauche.

Il est essentiel d'éviter d'assigner le même canal PWM à des usages différents dans un programme. Par exemple, GP0 et GP16 sont tous deux PWM_0A.

Essayons maintenant de réaliser l'effet de variation progressive de la luminosité de la LED après avoir compris ces concepts.

* :ref:`cpn_led`

**Composants requis**

Pour ce projet, nous avons besoin des composants suivants :

Il est très pratique d'acheter un kit complet, voici le lien :

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schéma**

|sch_led|

Ce projet utilise le même circuit que le premier projet :ref:`py_led`, mais le type de signal est différent. Dans le premier projet, on émettait des niveaux haut et bas (0 & 1) numériques directement depuis GP15 pour allumer ou éteindre les LED. Dans ce projet, nous utilisons un signal PWM sur GP15 pour contrôler la luminosité de la LED.

**Câblage**

|wiring_led|

**Code**

.. note::

    * Ouvrez le fichier ``2.3_fading_led.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.
    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.
    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    for brightness in range(0,65535,50):
        led.duty_u16(brightness)
        utime.sleep_ms(10)
    led.duty_u16(0)


La LED deviendra progressivement plus lumineuse à mesure que le code s'exécute.

**Comment ça marche ?**

Ici, nous changeons la luminosité de la LED en modifiant le cycle de travail de la sortie PWM de GP15. Examinons ces lignes de code.

.. code-block:: python
    :emphasize-lines: 4,5,8

    import machine
    import utime

    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    for brightness in range(0,65535,50):
        led.duty_u16(brightness)
        utime.sleep_ms(10)
    led.duty_u16(0)

* ``led = machine.PWM(machine.Pin(15))`` configure la broche GP15 pour la sortie PWM.
* La ligne ``led.freq(1000)`` fixe la fréquence PWM à 1000 Hz, ce qui signifie que chaque cycle dure 1 ms (1/1000).
* La ligne ``led.duty_u16()`` définit le cycle de travail, qui est un entier 16 bits (2^16=65536). Un 0 indique un cycle de travail de 0 %, ce qui signifie que chaque cycle a 0 % de temps de signal haut, c'est-à-dire que toutes les impulsions sont désactivées. La valeur 65535 indique un cycle de travail de 100 %, ce qui signifie que l'impulsion entière est activée, donnant '1'. Avec une valeur de 32768, la LED s'allume à moitié, ce qui fait qu'elle est moitié moins brillante par rapport à un allumage complet.
