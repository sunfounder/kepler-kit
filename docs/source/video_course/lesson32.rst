.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 32 : Projet de station météo mobile
=============================================================================

Ce tutoriel explique comment créer une station météo portable en utilisant le Raspberry Pi Pico W :

* **Connexion au Wi-Fi** : Importez les bibliothèques, créez un objet WLAN et connectez-vous au Wi-Fi.
* **Récupération des données météorologiques** : Utilisez l'API OpenWeatherMap pour obtenir des données météorologiques en temps réel, nécessitant une clé API.
* **Analyse des données JSON** : Extrayez la température, l'humidité, la pression, ainsi que les heures de lever et de coucher du soleil à partir de la réponse JSON.
* **Affichage des données sur OLED** : Configurez et connectez un écran OLED, utilisez la bibliothèque ``ssd1306`` et mettez à jour les données météo sur l'écran en boucle.
* **Alimentation de l'appareil** : Alimentez le Raspberry Pi Pico W avec une batterie pour plus de portabilité.
* **Explication du code** : Initialisez l'OLED, connectez-vous au Wi-Fi, récupérez et affichez les données météo, et mettez en place une boucle pour des mises à jour périodiques.
* **Devoir à la maison** : Ajoutez une LED RGB pour indiquer les conditions météorologiques en fonction de la température, de l'humidité ou de la vitesse du vent.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
