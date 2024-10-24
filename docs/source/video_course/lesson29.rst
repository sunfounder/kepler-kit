.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 29 : Projet client-serveur simple pour contrôler une LED RGB
=============================================================================

Ce tutoriel explique comment configurer une LED RGB contrôlée à distance via un Raspberry Pi Pico W et un PC connecté en Wi-Fi :

* **Introduction** : L'objectif est de contrôler une LED RGB sur un Raspberry Pi Pico W à distance en utilisant le Wi-Fi.
* **Schéma de câblage et configuration** : Connectez la LED RGB aux broches GPIO 16, 17, 18 et l'OLED aux broches GPIO 2 (SDA) et 3 (SCL).
* **Configuration côté serveur** : Importez les bibliothèques, initialisez les broches GPIO, connectez-vous au Wi-Fi, créez un serveur UDP, et affichez l'adresse IP sur l'OLED.
* **Configuration côté client** : Créez un client UDP sur le PC pour envoyer des commandes de couleur au serveur.
* **Démonstration pratique** : Montrez comment changer la couleur de la LED RGB via les commandes envoyées depuis le PC, avec l'OLED affichant les commandes et l'adresse IP.
* **Configuration finale et tests** : Alimentez le Raspberry Pi Pico W avec une batterie, enregistrez le code sous ``main.py`` et démontrez le fonctionnement sans fil.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
