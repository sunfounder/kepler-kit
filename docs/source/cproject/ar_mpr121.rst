.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_mpr121:

4.3 - Clavier à Électrodes
================================

Le MPR121 est un excellent choix si vous souhaitez ajouter un grand nombre de boutons tactiles à votre projet. Il dispose d'électrodes qui peuvent être étendues avec des conducteurs. 
Si vous connectez les électrodes à une banane, vous pouvez transformer cette banane en interrupteur tactile.

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schéma**

|sch_mpr121_ar|


**Câblage**

|wiring_mpr121_ar|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``4.3_electrode_keyboard.ino`` sous le chemin ``kepler-kit-main/arduino/4.3_electrode_keyboard``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * Ensuite, sélectionnez la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton Upload.
    * La bibliothèque ``Adafruit MPR121`` est utilisée ici, vous pouvez l'installer depuis le **Gestionnaire de Bibliothèques**.

      .. image:: img/lib_mpr121.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f31048b7-0f98-4d49-8c2e-26b3908e98cb/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après le lancement du programme, vous pouvez toucher les douze électrodes du module MPR121 avec la main, et l'état de contact de ces électrodes sera enregistré dans un tableau booléen de 12 bits qui sera affiché sur le moniteur série. 
Si la première et la onzième électrode sont touchées, ``100000000010`` s'affiche.

Vous pouvez étendre les électrodes en connectant d'autres conducteurs tels que des fruits, des fils, du papier aluminium, etc. Cela vous permettra de trouver davantage de moyens de déclencher ces électrodes.

**Comment ça fonctionne ?**

Initialisez l'objet ``MPR121``. À ce stade, l'état des électrodes du module sera enregistré comme valeurs initiales. 
Si vous étendez les électrodes, vous devrez relancer l'exemple pour réinitialiser les valeurs de départ.

.. code-block:: arduino

    #include "Adafruit_MPR121.h"

    Adafruit_MPR121 cap = Adafruit_MPR121();

    void setup() {
        Serial.begin(9600);
        int check = cap.begin(0x5A);
        if (!check) {
            Serial.println("MPR121 not found, check wiring?");
            while (1);
        }
        Serial.println("MPR121 found!");
    }

Récupère la valeur de l'électrode actuelle, obtenant ainsi une valeur binaire de 12 bits. Si vous touchez la première et la onzième électrode, vous obtenez ``100000000010``.

.. code-block:: arduino

    // Récupérer les pads actuellement touchés
    currtouched = cap.touched();

Détermine si l'état des électrodes a changé.

.. code-block:: arduino

    void loop() {
        currtouched = cap.touched();
        if (currtouched != lasttouched) {}

        // Réinitialiser notre état
        lasttouched = currtouched;
    }

Si un changement d'état est détecté, les valeurs de ``currtouched`` sont stockées bit par bit dans le tableau ``touchStates[12]``. Enfin, le tableau est affiché.

.. code-block:: arduino

    if (currtouched != lasttouched) {
        for (int i = 0; i < 12; i++) {
            if (currtouched & (1 << i)) touchStates[i] = 1;
            else touchStates[i] = 0;
        }
        for (int i = 0; i < 12; i++){
            Serial.print(touchStates[i]);
        }
        Serial.println();
    }