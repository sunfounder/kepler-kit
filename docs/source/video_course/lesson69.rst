.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions pendant les périodes festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 69 : Arrêter proprement les threads MicroPython lors de la fin du programme
======================================================================================

Ce tutoriel explique comment contrôler un servo et des LEDs avec le Raspberry Pi Pico W en utilisant les deux cœurs :

* **Configuration des connexions** : Connectez la LED rouge au GPIO 15, la LED verte au GPIO 14, et le servo au GPIO 17, avec l'alimentation sur le pin 40 et la masse sur le pin 38.
* **Implémentation du code** : Importez ``machine``, ``time``, ``_thread`` et ``Servo``. Configurez les broches pour les LEDs et le servo. Définissez ``other_core`` pour faire clignoter les LEDs en fonction du mouvement du servo. Créez une boucle pour contrôler le servo et les LEDs.
* **Devoir** : Modifiez le code pour faire clignoter la LED rouge pour un mouvement horaire et la LED verte pour un mouvement antihoraire du servo.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

