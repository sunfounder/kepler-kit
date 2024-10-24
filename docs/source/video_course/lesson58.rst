.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 58 : Déterminer la position angulaire d'un joystick en MicroPython
=============================================================================

Ce tutoriel explique comment calibrer un joystick avec le Raspberry Pi Pico W :

* **Configuration du câblage** : Connectez la masse à la broche 38, 3,3V à la broche 36, VRX à la broche GPIO 27, et VRY à la broche GPIO 26.
* **Implémentation du code** : Importez les bibliothèques nécessaires. Configurez les ADC pour les axes du joystick et lisez les valeurs pour la calibration.
* **Calibration** : Convertissez les valeurs brutes de l'ADC sur une échelle de -100 à +100. Utilisez la trigonométrie pour calculer l'angle du joystick.
* **Devoir** : Écrivez un programme pour contrôler un servomoteur en fonction de l'angle du joystick, assurant un suivi précis entre 0 et 180 degrés.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KpDIv0i41Tw?si=PUEInyKbRTIUcvCa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
