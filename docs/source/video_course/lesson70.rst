.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux nouvelles annonces de produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions pendant les périodes festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 70 : Exemple de sortie propre d'un programme double cœur en MicroPython
===================================================================================

Ce tutoriel explique comment utiliser le multi-threading pour contrôler un servo et un bouton avec le Raspberry Pi Pico W :

* **Configuration des connexions** : Connectez le contrôle du servo au GPIO 17, l'alimentation au pin 40 et la masse au pin 38. Connectez le bouton au GPIO 16 et à la masse.
* **Implémentation du code** : Importez ``machine``, ``time``, ``_thread``, ``Servo``. Configurez les broches pour le bouton et le servo. Implémentez un interrupteur pour contrôler la position du servo. Utilisez le multi-threading pour le mouvement du servo et pour assurer une sortie propre du programme.
* **Devoir** : Modifiez le programme pour qu'il puisse se terminer proprement, même en cas d'interruption pendant le mouvement du servo.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
