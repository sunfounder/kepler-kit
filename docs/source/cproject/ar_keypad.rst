.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_keypad:

4.2 - Clavier 4x4
========================

Le clavier 4x4, également connu sous le nom de clavier matriciel, est une matrice de 16 touches disposées sur un seul panneau.

Le clavier peut être trouvé sur des appareils nécessitant principalement une saisie numérique, tels que les calculatrices, télécommandes de télévision, téléphones à boutons-poussoirs, distributeurs automatiques, guichets automatiques (DAB), serrures à combinaison et serrures de porte numériques.

Dans ce projet, nous allons apprendre à déterminer quelle touche est pressée et obtenir la valeur de la touche correspondante.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schéma**

|sch_keypad_ar|

Les rangées du clavier (G2 ~ G5) sont programmées pour être en état haut ; si l'une des broches G6 ~ G9 est lue comme étant en état haut, cela indique quelle touche est pressée.

Par exemple, si G6 est en état haut, alors la touche numérique 1 est pressée ; c'est parce que les broches de commande de la touche numérique 1 sont G2 et G6, et quand cette touche est pressée, G2 et G6 seront connectées ensemble, donc G6 sera également en état haut.


**Câblage**

|wiring_keypad_ar|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``4.2_4x4_keypad.ino`` sous le chemin ``kepler-kit-main/arduino/4.2_4x4_keypad``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton **Upload**.
    * La bibliothèque ``Adafruit Keypad`` est utilisée ici, vous pouvez l'installer depuis le **Library Manager**.

      .. image:: img/lib_ad_keypad.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/6c776dfc-cb74-49d7-8906-f1382e0e7b7b/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Après l'exécution du programme, la console affichera les touches que vous avez pressées sur le clavier.

**Comment ça fonctionne**

1. Inclusion de la bibliothèque

   Nous commençons par inclure la bibliothèque ``Adafruit_Keypad``, qui nous permet de facilement interagir avec le clavier.

   .. code-block:: arduino

     #include "Adafruit_Keypad.h"

2. Configuration du clavier

   .. code-block:: arduino

     const byte ROWS = 4;
     const byte COLS = 4;
     char keys[ROWS][COLS] = {
       { '1', '2', '3', 'A' },
       { '4', '5', '6', 'B' },
       { '7', '8', '9', 'C' },
       { '*', '0', '#', 'D' }
     };
     byte rowPins[ROWS] = { 2, 3, 4, 5 };
     byte colPins[COLS] = { 8, 9, 10, 11 };

   - Les constantes ``ROWS`` et ``COLS`` définissent les dimensions du clavier. 
   - ``keys`` est un tableau 2D qui stocke l'étiquette de chaque touche sur le clavier.
   - ``rowPins`` et ``colPins`` sont des tableaux qui stockent les broches de l'Arduino connectées aux lignes et colonnes du clavier.

   .. raw:: html

      <br/>


3. Initialisation du clavier

   Créez une instance de ``Adafruit_Keypad`` appelée ``myKeypad`` et initialisez-la.

   .. code-block:: arduino

     Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

4. Fonction setup()

   Initialisez la communication série et le clavier personnalisé.

   .. code-block:: arduino

     void setup() {
       Serial.begin(9600);
       myKeypad.begin();
     }

5. Boucle principale

   Vérifiez les événements de touche et affichez-les dans le moniteur série.

   .. code-block:: arduino

     void loop() {
       myKeypad.tick();
       while (myKeypad.available()) {
         keypadEvent e = myKeypad.read();
         Serial.print((char)e.bit.KEY);
         if (e.bit.EVENT == KEY_JUST_PRESSED) Serial.println(" pressed");
         else if (e.bit.EVENT == KEY_JUST_RELEASED) Serial.println(" released");
       }
       delay(10);
     }

