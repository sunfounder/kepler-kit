.. note::

    Bonjour et bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez aux concours et aux promotions de fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Leçon 31 : Projet de station météo sans capteur à distance
=============================================================================

Ce tutoriel explique comment créer une station météo sans capteur en utilisant le Raspberry Pi Pico W :

* **Connexion au Wi-Fi** : Importez les bibliothèques et connectez-vous au Wi-Fi en utilisant un objet WLAN.
* **Récupération des données météorologiques** : Utilisez l'API OpenWeatherMap pour obtenir des données météorologiques en temps réel, nécessitant une clé API.
* **Analyse des données JSON** : Extrayez la température, l'humidité, la pression, ainsi que les heures de lever et de coucher du soleil à partir de la réponse JSON.
* **Explication du code** : Utilisez ``urequests.get()`` pour récupérer les données, convertissez le temps Unix et ajustez les unités de pression.
* **Affichage des données météorologiques** : Imprimez la température, l'humidité, la pression, les conditions et la vitesse du vent.
* **Devoir à la maison** : Ajoutez un écran et créez une station météo portable alimentée par batterie.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
