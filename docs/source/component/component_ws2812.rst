.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avance aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_ws2812:

Bande LED WS2812 RGB 8 LEDs
=================================

|img_ws2812|

La bande WS2812 RGB 8 LEDs est composée de 8 LED RGB. 
Un seul pin est nécessaire pour contrôler toutes les LEDs. Chaque LED RGB possède une puce WS2812, qui peut être contrôlée indépendamment. 
Elle permet d'afficher des niveaux de luminosité sur 256 niveaux et de reproduire la couleur réelle avec 16 777 216 couleurs. 
De plus, chaque pixel intègre un circuit de verrouillage des données de l'interface numérique intelligente, ainsi qu'un circuit de mise en forme du signal d'amplification, garantissant efficacement une uniformité de couleur élevée des pixels lumineux.

Elle est flexible, peut être raccordée, pliée et découpée à volonté. L'arrière est équipé d'un ruban adhésif, ce qui permet de la fixer sur des surfaces irrégulières et dans des espaces étroits.

**Caractéristiques**

* Tension de fonctionnement : DC5V
* IC : Une puce contrôle une LED RGB
* Consommation : 0,3W par LED
* Température de fonctionnement : -15 à 50°C
* Couleur : RGB pleine couleur
* Type de RGB : 5050RGB (IC intégré WS2812B)
* Épaisseur de la bande lumineuse : 2mm
* Chaque LED peut être contrôlée individuellement

**Présentation du WS2812B**

* `WS2812B Datasheet <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

Le WS2812B est une source lumineuse LED à contrôle intelligent où le circuit 
de contrôle et la puce RGB sont intégrés dans un composant 5050. Il comprend 
un port de données numériques intelligent avec verrouillage des données et un 
circuit d'amplification de mise en forme du signal. Il intègre également un 
oscillateur interne de haute précision et une partie de contrôle de courant 
constant programmable en 12V, garantissant ainsi la cohérence de la couleur des 
points lumineux.

Le protocole de transfert de données utilise un mode de communication NZR unique. 
Après le réinitialisation du pixel, le port DIN reçoit les données du contrôleur, 
le premier pixel collecte les premières 24 bits de données puis les envoie au verrou 
de données interne. Les autres données, restructurées par le circuit d'amplification 
interne, sont envoyées au pixel suivant via le port DO. Après la transmission par chaque 
pixel, le signal est réduit de 24 bits. Grâce à la technologie de retransmission automatique, 
le nombre de pixels en cascade n'est pas limité par la transmission du signal, mais seulement 
par la vitesse de transmission du signal.

Les LED présentent une faible tension de conduite, sont écologiques et économes en 
énergie, avec une haute luminosité, un grand angle de diffusion, une bonne cohérence, une 
faible consommation d'énergie et une longue durée de vie. Le circuit de contrôle intégré dans 
la LED rend le montage plus simple, de petite taille et facile à installer.

.. Example
.. -------------------

.. :ref:`Bande LED RGB`


**Exemple**

* :ref:`py_neopixel` (Pour utilisateurs MicroPython)
* :ref:`py_music_player` (Pour utilisateurs MicroPython)
* :ref:`ar_neopixel` (Pour utilisateurs Arduino)
* :ref:`per_flowing_leds` (Pour utilisateurs Piper Make)
