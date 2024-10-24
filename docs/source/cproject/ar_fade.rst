.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_fade:

2.3 - LED avec variation d'intensité
========================================

Jusqu'à présent, nous avons utilisé uniquement deux signaux de sortie : niveau haut et niveau bas (ou appelés 1 & 0, ALLUMÉ & ÉTEINT), ce que l'on appelle une sortie numérique.
Cependant, dans la pratique, de nombreux dispositifs ne fonctionnent pas simplement en mode ON/OFF, par exemple, ajuster la vitesse d'un moteur ou la luminosité d'une lampe de bureau.
Autrefois, un curseur permettant de régler la résistance était utilisé pour atteindre cet objectif, mais cela était souvent peu fiable et inefficace.
C'est pourquoi la modulation de largeur d'impulsion (PWM) est apparue comme une solution viable à ces problèmes complexes.

Une sortie numérique composée d'un niveau haut et d'un niveau bas est appelée une impulsion. La largeur de l'impulsion de ces broches peut être ajustée en modifiant la vitesse de commutation ON/OFF.

En termes simples, lorsque nous faisons clignoter la LED dans un court intervalle de temps (par exemple 20 ms, correspondant au temps de persistance visuelle de la plupart des gens),
la LED s'allume, s'éteint et se rallume, nous ne percevons pas qu'elle s'éteint, mais la luminosité de la lumière sera légèrement réduite.
Pendant cette période, plus la LED est allumée longtemps, plus elle est lumineuse.
Autrement dit, plus l'impulsion est large au cours du cycle, plus le "signal électrique" émis par le microcontrôleur est puissant.
C'est ainsi que le PWM contrôle la luminosité de la LED (ou la vitesse du moteur).

* `Pulse-width modulation - Wikipedia <https://en.wikipedia.org/wiki/Pulse-width_modulation>`_

Il y a quelques points à noter lorsque Pico W utilise le PWM. Jetons un œil à cette image.

|pin_pwm|

Chaque broche GPIO de Pico W supporte le PWM, mais en réalité, il dispose de 16 sorties PWM indépendantes (au lieu de 30), réparties entre GP0 et GP15 à gauche, et la sortie PWM des GPIO à droite est une copie équivalente de celle de gauche.

Il est important d'éviter de définir le même canal PWM pour différents usages durant la programmation (par exemple, GP0 et GP16 sont tous deux PWM_0A).

Après avoir compris cela, essayons de réaliser l'effet d'une LED avec variation d'intensité.

* :ref:`cpn_led`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN D'ACHAT
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCTION DES COMPOSANTS	
        - QUANTITÉ
        - LIEN D'ACHAT

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schéma**

|sch_led|

Ce projet utilise le même circuit que le premier projet :ref:`ar_led`, mais le type de signal est différent. Le premier projet utilisait des niveaux numériques haut et bas (0 & 1) directement depuis GP15 pour allumer ou éteindre les LED, tandis que ce projet utilise un signal PWM de GP15 pour contrôler la luminosité de la LED.

**Câblage**

|wiring_led|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.3_fading_led.ino`` sous le chemin ``kepler-kit-main/arduino/2.3_fading_led``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/86807da4-4714-4d3c-b6af-0f1b9a62223b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


La LED deviendra progressivement plus lumineuse au fur et à mesure que le programme s'exécute.

**Comment ça fonctionne ?**

Déclarez la broche 15 comme ledPin.

.. code-block:: C

    const int ledPin = 15;

``analogWrite()`` dans ``loop()`` attribue à ledPin une valeur analogique (onde PWM) comprise entre 0 et 255 pour changer la luminosité de la LED.

.. code-block:: C

    analogWrite(ledPin, value);

En utilisant une boucle for, la valeur de ``analogWrite()`` peut être modifiée progressivement entre la valeur minimale (0) et la valeur maximale (255).

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
    }

Pour voir clairement le phénomène expérimental, un ``delay(30)`` doit être ajouté à la boucle for pour contrôler le temps de changement de luminosité.

.. code-block:: C

    for (int value = 0 ; value <= 255; value += 5) {
        analogWrite(ledPin, value);
        delay(30);
    }
