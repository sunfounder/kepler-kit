.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_button:

2.5 - Lecture de la Valeur d'un Bouton
==============================================

Le nom GPIO (Entrée/Sortie Générale) suggère que ces broches ont à la fois des fonctions d'entrée et de sortie. 
Dans les leçons précédentes, nous avons utilisé la fonction de sortie ; dans ce chapitre, nous allons utiliser la fonction d'entrée pour lire la valeur du bouton.

* :ref:`cpn_button`

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schéma**

|sch_button|

Un côté de la broche du bouton est connecté à 3,3V et l'autre côté est connecté à GP14. Ainsi, lorsque le bouton est appuyé, GP14 sera en niveau haut. Cependant, lorsque le bouton n'est pas appuyé, GP14 est en état flottant et peut être haut ou bas. Pour obtenir un niveau bas stable lorsque le bouton n'est pas appuyé, GP14 doit être reconnecté à la masse (GND) via une résistance de tirage de 10K.

**Câblage**

|wiring_button|

.. note::
    Nous pouvons considérer le bouton à quatre broches comme un bouton en forme de H. Ses deux pieds gauche (droite) sont connectés, ce qui signifie que lorsqu'il traverse la ligne de séparation centrale, il connecte les deux demi-rangées du même numéro de rangée ensemble. (Par exemple, dans mon circuit, E23 et F23 sont connectés, tout comme E25 et F25).

    Avant que le bouton ne soit pressé, les côtés gauche et droit sont indépendants l'un de l'autre, et le courant ne peut pas circuler d'un côté à l'autre.

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.5_reading_button_value.ino`` sous le chemin ``kepler-kit-main/arduino/2.5_reading_button_value``.
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6fcb7cac-e866-4a2d-8162-8e0c6fd17660/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après l'exécution du code, cliquez sur l'icône de la loupe dans le coin supérieur droit de l'IDE Arduino (Moniteur Série).

.. image:: img/open_serial_monitor.png

Maintenant, lorsque vous appuyez sur le bouton, le Moniteur Série affichera "Vous avez appuyé sur le bouton !".


**Comment ça fonctionne ?**

Pour activer le Moniteur Série, vous devez démarrer la communication série dans ``setup()`` et définir le débit de données à 9600.

.. code-block:: arduino

    Serial.begin(115200);

    
* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

Pour le bouton, nous devons définir leur mode sur ``INPUT`` pour pouvoir obtenir leurs valeurs.

.. code-block:: arduino

    pinMode(buttonPin, INPUT);

Lisez l'état de ``buttonPin`` dans ``loop()`` et assignez-le à la variable ``buttonState``.

.. code-block:: arduino

    buttonState = digitalRead(buttonPin);
    
* `digitalRead() <https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/>`_

Si ``buttonState`` est HAUT, la LED clignotera.
Affichez "Vous avez appuyé sur le bouton !" sur le Moniteur Série.

.. code-block:: arduino

    if (buttonState == HIGH) {
        Serial.println("You pressed the button!");
    }


**Mode de fonctionnement Pull-up**

Voici le câblage et le code lorsque le bouton est en mode pull-up. Veuillez essayer.

|wiring_button_pullup|

.. 1. Connectez la broche 3V3 du Pico W au bus d'alimentation positif de la breadboard.
.. #. Insérez le bouton dans la breadboard et faites-le traverser la ligne de séparation centrale.
.. #. Utilisez un fil pour connecter une des broches du bouton au bus **négatif** (dans mon cas, la broche en haut à droite).
.. #. Connectez l'autre broche (en haut à gauche ou en bas à gauche) à GP14 avec un fil.
.. #. Utilisez une résistance de 10K pour connecter la broche en haut à gauche du bouton au bus **positif**.
.. #. Connectez le bus d'alimentation négatif de la breadboard à la masse (GND) du Pico.

La seule différence que vous verrez avec le mode pull-down est que la résistance de 10K est connectée à 3,3V et le bouton est connecté à la masse, de sorte que lorsque le bouton est pressé, GP14 recevra un niveau bas, ce qui est l'opposé de la valeur obtenue en mode pull-down.
Il suffit donc de changer ce code en ``if (buttonState == LOW)``.
