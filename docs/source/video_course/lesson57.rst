.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Approfondissez vos connaissances en Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 57 : Calibration d'un joystick en MicroPython
=============================================================================

Ce tutoriel explique comment calibrer un joystick avec le Raspberry Pi Pico W :

* **Configuration du câblage** : Connectez la masse à la broche 38, 3,3V à la broche 36, VRX à la broche GPIO 27, et VRY à la broche GPIO 26.
* **Implémentation du code** : Importez ``machine``, ``time``, ``math`` ; configurez les ADC pour les axes du joystick ; lisez et affichez les valeurs du joystick.
* **Calibration** : Convertissez les valeurs brutes de l'ADC sur une échelle de -100 à +100, en ajustant pour éliminer les bruits de la position neutre.
* **Devoir** : Écrivez un programme pour calculer et afficher l'angle du joystick en fonction de sa position.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
