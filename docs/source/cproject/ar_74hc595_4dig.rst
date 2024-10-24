.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_74hc_4dig:

5.3 - Compteur de temps
================================

Un affichage à 4 chiffres de 7 segments est composé de quatre affichages 
de 7 segments fonctionnant ensemble.

L'affichage à 4 chiffres de 7 segments fonctionne indépendamment. Il utilise 
le principe de persistance de la vision humaine pour afficher rapidement les 
caractères de chaque segment en boucle, formant ainsi des chaînes continues.

Par exemple, lorsque "1234" est affiché, "1" apparaît sur le premier segment, 
et "234" n'est pas affiché. Après un certain temps, le deuxième segment affiche 
"2", tandis que les 1er, 3e et 4e segments restent éteints, et ainsi de suite. 
Ce processus est très rapide (environ 5 ms), et grâce à l'effet de rémanence 
optique et au principe de persistance rétinienne, nous pouvons voir les quatre 
chiffres simultanément.

**Composants requis**

Pour ce projet, nous avons besoin des composants suivants.

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
        - 4 (220Ω)
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

Ici, le principe de câblage est essentiellement le même que pour :ref:`ar_74hc_led`, la seule différence est que Q0-Q7 sont connectés aux broches a~g de l'affichage à 4 chiffres de 7 segments.

Ensuite, G10 ~ G13 sélectionneront quel segment de l'affichage de 7 segments doit fonctionner.

**Câblage**

|wiring_4dig|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``5.3_time_counter.ino`` sous le chemin ``kepler-kit-main/arduino/5.3_time_counter``.
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/0e97386e-417e-4f53-a026-5f37e36deba4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après l'exécution du programme, vous verrez l'affichage à 4 chiffres de 7 segments devenir un compteur qui augmente de 1 par seconde.

**Comment ça marche ?**

L'écriture des signaux sur chaque segment de 7 est effectuée de la même manière que :ref:`ar_74hc_7seg`, en utilisant la fonction ``hc595_shift()``.
Le point central de l'affichage à 4 chiffres de 7 segments est d'activer sélectivement chaque segment. Le code associé est le suivant.

.. code-block:: arduino

    const int placePin[4] = {13,12,11,10}; 

    void setup ()
    {
        for (int i = 0; i<4;i++){
            pinMode(placePin[i],OUTPUT);
        }
    }

    void loop()
    { 
        pickDigit(0);
        hc595_shift(count%10/1);
        
        pickDigit(1);
        hc595_shift(count%100/10);
        
        pickDigit(2);
        hc595_shift(count%1000/100);
        
        pickDigit(3);
        hc595_shift(count%10000/1000);
    }

    void pickDigit(int digit){
        for(int i = 0; i < 4; i++){
            digitalWrite(placePin[i],HIGH);
        }
        digitalWrite(placePin[digit],LOW);
    }

Ici, quatre broches (GP10, GP11, GP12, GP13) sont utilisées pour contrôler individuellement chaque bit de l'affichage à 4 chiffres de 7 segments.
Lorsque l'état de ces broches est ``LOW``, l'affichage correspondant est actif ; lorsqu'il est ``HIGH``, l'affichage ne fonctionne pas.


La fonction ``pickDigit(digit)`` est utilisée pour désactiver tous les affichages de 7 segments, puis activer un chiffre particulier individuellement.
Ensuite, ``hc595_shift()`` est utilisé pour écrire le code binaire correspondant pour le segment de 7.

L'affichage à 4 chiffres de 7 segments doit être activé en continu et à tour de rôle pour afficher les quatre chiffres, ce qui signifie que le programme principal ne peut pas facilement ajouter du code qui affecterait le timing.

Cependant, nous devons ajouter une fonction de chronométrage à cet exemple. Si nous ajoutons un ``delay (1000)``, nous serons en mesure de détecter l'illusion des quatre affichages fonctionnant en même temps, révélant le fait qu'un seul segment est allumé à la fois.

Ensuite, utiliser la fonction ``millis()`` est une excellente méthode pour y parvenir.

.. code-block:: arduino

    void setup ()
    {
        timerStart = millis();
    }

    void loop()
    {
        unsigned int count = (millis()-timerStart)/1000;
    }

La fonction ``millis()`` récupère le nombre de millisecondes écoulées depuis le démarrage du programme en cours. Nous enregistrons la première valeur de temps en tant que ``timerStart`` ; 

puis lorsque nous devons obtenir à nouveau l'heure, nous rappelons la fonction ``millis()`` et soustrayons ``timerStart`` de la valeur pour obtenir la durée de fonctionnement du programme.

Enfin, nous convertissons cette valeur de temps et faisons en sorte que l'affichage à 4 chiffres de 7 segments la montre.

* `millis() <https://www.arduino.cc/reference/en/language/functions/time/millis/>`_