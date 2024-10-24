.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_led:

2.1 - Bonjour, LED ! 
=======================================

Tout comme imprimer “Hello, world!” est la première étape pour apprendre à programmer, utiliser un programme pour contrôler une LED est la traditionnelle introduction à la programmation physique.

* :ref:`cpn_led`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants. 

Il est pratique d'acheter un kit complet, voici le lien : 

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

Le principe de ce circuit est simple et la direction du courant est illustrée sur le schéma. Lorsque GP15 émet un signal de haut niveau (3,3 V), la LED s'allume après la résistance de limitation de courant de 220 ohms. Lorsque GP15 émet un signal de bas niveau (0 V), la LED s'éteint.

**Câblage**

|wiring_led|

Suivons la direction du courant pour construire le circuit !

1. Ici, nous utilisons le signal électrique de la broche GP15 de la carte Pico W pour faire fonctionner la LED, et le circuit commence ici.
#. Le courant doit passer par une résistance de 220 ohms (utilisée pour protéger la LED). Insérez une extrémité (n'importe laquelle) de la résistance dans la même rangée que la broche GP15 de la Pico W (rangée 20 dans mon circuit), et insérez l'autre extrémité dans une rangée libre de la breadboard (rangée 24 dans mon circuit).
#. Prenez la LED, vous verrez que l'une de ses pattes est plus longue que l'autre. Insérez la patte la plus longue dans la même rangée que l'extrémité de la résistance, et connectez la patte la plus courte en traversant la fente centrale de la breadboard vers la même rangée.
#. Insérez un fil jumper mâle-à-mâle (M2M) dans la même rangée que la patte courte de la LED, puis connectez-le au bus d'alimentation négatif de la breadboard.
#. Utilisez un jumper pour connecter le bus d'alimentation négatif à la broche GND de la Pico W.

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.1_hello_led.ino`` sous le chemin ``kepler-kit-main/arduino/2.1_hello_led``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/898b8ba7-9bdf-468d-9181-ca8535e8dca6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Après l'exécution du code, vous verrez la LED clignoter.


**Comment ça fonctionne ?**

Ici, nous connectons la LED à la broche numérique 15, donc nous devons déclarer une variable int appelée ledPin au début du programme et lui attribuer la valeur 15.

.. code-block:: C

    const int ledPin = 15;

Ensuite, initialisez la broche dans la fonction ``setup()``, où vous devez la configurer en mode ``OUTPUT``.

.. code-block:: C

    void setup() {
        pinMode(ledPin, OUTPUT);
    }

Dans ``loop()``, ``digitalWrite()`` est utilisé pour fournir un signal de haut niveau de 3,3 V à ledPin, ce qui provoquera une différence de tension entre les broches de la LED et l'allumera.

.. code-block:: C

    digitalWrite(ledPin, HIGH);

Si le signal est changé en bas niveau (LOW), le signal de ledPin sera ramené à 0 V pour éteindre la LED.

.. code-block:: C

    digitalWrite(ledPin, LOW);


Un intervalle entre l'allumage et l'extinction est nécessaire pour permettre aux gens de voir le changement, 
nous utilisons donc un code ``delay(1000)`` pour laisser le contrôleur ne rien faire pendant 1000 ms.

.. code-block:: C

    delay(1000);   
