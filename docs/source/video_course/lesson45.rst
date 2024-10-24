.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Recevez en avant-première les annonces de nouveaux produits et des avant-goûts exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 45 : Calculer la hauteur d'un objet en chute libre
=============================================================================

Ce tutoriel explique comment utiliser le capteur MPU6050 avec le Raspberry Pi Pico W pour mesurer des distances verticales :

* **Configuration** : Connectez le MPU6050 et l'écran OLED 1306 au Raspberry Pi Pico W, en vous assurant que les connexions sont sécurisées pour réduire le bruit.
* **Concept** : Mesurez la distance verticale en calculant le temps (T_drop) de chute libre et utilisez-le pour déterminer la hauteur de la chute.
* **Équation** : Calculez la hauteur (H) avec \( H = 16 \times (T_{drop})^2 \), en convertissant le temps de millisecondes en secondes.
* **Implémentation du code** : Configurez les bibliothèques, mesurez l'accélération sur l'axe Z pour détecter le 0G, lancez un chronomètre pendant la chute libre et affichez la hauteur et le temps de chute sur l'écran OLED.
* **Démonstration pratique** : Testez en laissant tomber le capteur d'une hauteur connue et ajustez pour améliorer la précision si nécessaire.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
