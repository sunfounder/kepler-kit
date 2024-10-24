.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les périodes festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 68 : Exemple de multithreading en MicroPython avec LEDs et Servo
===================================================================================

Ce tutoriel explique comment contrôler un servo et des LEDs avec le Raspberry Pi Pico W en utilisant les deux cœurs :

* **Configuration des connexions** : Connectez la LED rouge au GPIO 15, la LED verte au GPIO 14, le servo au GPIO 17, l'alimentation au pin 40 et la masse au pin 38.
* **Implémentation du code** : Importez ``machine``, ``time``, ``_thread`` et ``Servo``. Configurez les broches pour les LEDs et le servo. Définissez la fonction ``other_core`` pour faire clignoter les LEDs en fonction de la direction du servo.
* **Devoir** : Modifiez le code pour faire clignoter la LED rouge en cas de mouvement horaire du servo et la LED verte en cas de mouvement antihoraire.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/n2eQTw9axHg?si=TRVLEM1EqyD_DefA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
