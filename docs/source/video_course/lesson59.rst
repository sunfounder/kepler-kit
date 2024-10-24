.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 59 : Contrôler un servomoteur avec un joystick
=============================================================================

Ce tutoriel explique comment contrôler un servomoteur avec un joystick en utilisant le Raspberry Pi Pico W :

* **Configuration du câblage** : Connectez la masse du joystick à la broche 38, 3,3V à la broche 36, VRX à la broche GPIO 27, et VRY à la broche GPIO 26. Connectez le 5V du servomoteur à la broche 40, la masse à la broche 38, et le contrôle à la broche GPIO 15.
* **Implémentation du code** : Importez ``machine``, ``time``, ``math``. Configurez l'ADC pour le joystick et le PWM pour le servomoteur. Lisez et affichez les valeurs du joystick.
* **Calibration et contrôle** : Échelle des valeurs de l'ADC de -100 à +100. Calculez l'angle du joystick. Mappez cet angle au PWM pour le servomoteur.
* **Devoir** : Écrivez du code pour contrôler le servomoteur à partir de l'angle du joystick (0-180 degrés).

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

