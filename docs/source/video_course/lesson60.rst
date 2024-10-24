.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 60 : Contrôler les couleurs des NeoPixels avec un joystick en MicroPython
====================================================================================

Ce tutoriel explique comment contrôler une bande LED NeoPixel avec un joystick en utilisant le Raspberry Pi Pico W :

* **Configuration du câblage** :

    - Connectez la masse du joystick à la broche 38, 3,3V à la broche 36, VRX à la broche GPIO 27, VRY à la broche GPIO 26. 
    - Connectez la masse du Neopixel à la broche 38, le 5V à la broche 40, et le signal de données à la broche GPIO 0.
    
* **Implémentation du code** : 

    - Importez les bibliothèques (``machine``, ``time``, ``math``, ``neopixel``). 
    - Configurez l'ADC pour le joystick et le Neopixel. Lisez les valeurs du joystick, calculez les angles. 
    - Convertissez les angles en valeurs RGB pour le Neopixel.

* **Devoir** : Écrivez un programme pour contrôler la couleur et la luminosité du Neopixel en fonction de l'angle du joystick et de la distance par rapport au centre.


**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
