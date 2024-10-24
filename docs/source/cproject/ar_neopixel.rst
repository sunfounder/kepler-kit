.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_neopixel:

3.3 - Bande LED WS2812 RGB
===============================

Le WS2812 est une source lumineuse LED à contrôle intelligent, où le circuit de contrôle et la puce RGB sont intégrés dans un composant de type 5050. 
Il comprend un verrouillage de données numériques intelligent pour le port de données, ainsi qu'un circuit de restructuration et d'amplification des signaux. 
Il intègre également un oscillateur interne de précision et un contrôle programmable de courant constant, 
garantissant ainsi une uniformité de couleur élevée des points lumineux.

Le protocole de transfert de données utilise un mode de communication NZR unique. 
Après la réinitialisation de l'alimentation du pixel, le port DIN reçoit les données du contrôleur, le premier pixel collecte les 24 premiers bits de données puis les envoie au verrou de données interne. Les autres données, restructurées par le circuit d'amplification interne, sont envoyées au pixel suivant via le port DO. Après la transmission de chaque pixel, le signal réduit de 24 bits. 
Les pixels adoptent une technologie de transmission de retransmission automatique, ce qui signifie que le nombre de pixels en cascade n'est pas limité par la transmission du signal, mais uniquement par la vitesse de transmission du signal.


* :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schéma**

|sch_ws2812|

**Câblage**

|wiring_ws2812|


.. warning::
    Un point important auquel vous devez prêter attention est le courant.

    Bien que la bande LED avec n'importe quel nombre de LEDs puisse être utilisée avec le Pico W, la puissance de son pin VBUS est limitée.
    Ici, nous utiliserons huit LEDs, ce qui est sans danger.
    Mais si vous souhaitez utiliser davantage de LEDs, vous devez ajouter une alimentation séparée.
    

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``3.3_rgb_led_strip.ino`` sous le chemin ``kepler-kit-main/arduino/3.3_rgb_led_strip``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * Ensuite, sélectionnez la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton Upload.
    * La bibliothèque ``Adafruit_NeoPixel`` est utilisée ici, vous pouvez l'installer depuis le **Gestionnaire de Bibliothèques**.

      .. image:: img/lib_neopixel.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/efe5d60f-ea0f-4446-bc5b-30c76197fedf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Choisissons quelques couleurs préférées et affichons-les sur la bande LED RGB !

**Comment ça fonctionne ?**

Déclarez un objet de type Adafruit_NeoPixel, connecté au ``PIXEL_PIN``, 
et définissez ``PIXEL_COUNT`` comme le nombre de LEDs RGB sur la bande.

.. code-block:: arduino

    #define PIXEL_PIN    0
    #define PIXEL_COUNT 8

    // Déclarer notre objet bande NeoPixel :
    Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
    // Argument 1 = Nombre de pixels dans la bande NeoPixel
    // Argument 2 = Numéro de pin Arduino (la plupart sont valides)
    // Argument 3 = Indicateurs de type de pixel, à combiner selon les besoins :
    //   NEO_KHZ800  Flux de bits à 800 KHz (la plupart des produits NeoPixel avec LEDs WS2812)
    //   NEO_KHZ400  400 KHz (pixels 'v1' classiques (pas v2) FLORA, pilotes WS2811)
    //   NEO_GRB     Pixels câblés pour flux de bits GRB (la plupart des produits NeoPixel)
    //   NEO_RGB     Pixels câblés pour flux de bits RGB (pixels FLORA v1, pas v2)
    //   NEO_RGBW    Pixels câblés pour flux de bits RGBW (produits NeoPixel RGBW)

Initialisez l'objet bande et allumez tous les pixels sur 'off'.

Fonctions
    * ``strip.begin()`` : Initialise l'objet bande NeoPixel (OBLIGATOIRE).
    * ``strip.setPixelColor(index, color)`` : Définit la couleur d'un pixel (en RAM), la ``couleur`` doit être une valeur 32 bits unique 'compactée'.
    * ``strip.Color(red, green, blue)`` : Couleur en tant que valeur 32 bits 'compactée'.
    * ``strip.show()`` : Met à jour la bande avec les nouvelles couleurs.
  
**En savoir plus**

Nous pouvons générer des couleurs aléatoires et créer une lumière fluide colorée.

.. note::

    * Vous pouvez ouvrir le fichier ``3.3_rgb_led_strip_flowing.ino`` sous le chemin ``kepler-kit-main/arduino/3.3_rgb_led_strip_flowing``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a3d7c520-b4f8-4445-9454-5fe7d2a24fd9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Vous pouvez également faire en sorte que cette bande LED WS2812 effectue un cycle arc-en-ciel sur la roue chromatique (plage 65535).

.. note::

   * Vous pouvez ouvrir le fichier ``3.3_rgb_led_strip_rainbow.ino`` sous le chemin ``kepler-kit-main/arduino/3.3_rgb_led_strip_rainbow``. 
   * Ou copiez ce code dans l'**Arduino IDE**.
   * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.

    

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/47d84804-3560-48fa-86df-49f8e2f6ad63/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>   


* ``strip.getPixelColor(index)`` : Interroge la couleur d'un pixel précédemment défini.
* ``strip.ColorHSV(pixelHue)`` : Convertit la teinte, la saturation et la valeur en une couleur RGB 32 bits compactée pouvant être passée à ``setPixelColor()`` ou à d'autres fonctions compatibles RGB.
* ``strip.gamma32()`` : Offre une couleur plus fidèle avant de l'attribuer à chaque pixel.

