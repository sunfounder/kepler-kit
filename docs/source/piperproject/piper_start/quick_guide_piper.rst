.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _quick_guide_piper:

1.2 Guide Rapide sur Piper Make
====================================

1. Créer un Nouveau Projet
------------------------------

Maintenant que vous avez configuré le Pico W, il est temps d'apprendre à le programmer. 
Allons allumer la LED intégrée.

Passez en ``MODE CRÉATIF`` et cliquez sur le bouton **Nouveau Projet**, 
un nouveau projet apparaîtra dans la section **MES PROJETS** et 
se verra attribuer un nom aléatoire que vous pourrez modifier depuis la page de programmation.

|media9-s|

Ouvrez ensuite le nouveau projet que vous venez de créer.

|media11-s|

Vous arrivez maintenant sur la page de programmation de Piper Make.

|piper_intro1|

* **DÉMARRER** : Utilisé pour exécuter le code, s'il est grisé, cela signifie qu'il n'est pas connecté au Pico W.
* **Palette de Blocs** : contient différents types de blocs.
* **CONNECTER** : Utilisé pour se connecter au Pico W, il est vert lorsqu'il n'est pas connecté, et devient **DÉCONNECTER(rouge)** lorsqu'il est connecté.
* **Zone de Programmation** : Faites glisser les blocs ici pour terminer la programmation en les empilant.
* **Zone d'Outils** : Vous pouvez cliquer sur **VUE NUMÉRIQUE** pour voir la distribution des broches du Pico W ; visualiser les informations d'impression dans la **CONSOLE** ; lire les données dans **DATA**, et cliquer sur **Python** pour voir le code source Python.
* **Nom et description du projet** : Vous pouvez modifier le nom et la description du projet.
* **TÉLÉCHARGER** : Cliquez sur le bouton **TÉLÉCHARGER** pour le sauvegarder localement, généralement au format **|**. Vous pourrez l'importer via le bouton **Importer un Projet** sur la page d'accueil.

Cliquez sur la palette **Chip** et faites glisser le bloc [start] vers la **Zone de Programmation**.

|media12|

Ensuite, faites glisser le bloc [loop] de la palette **loops** sous le bloc [start], et définissez l'intervalle de boucle à 1 seconde.

|media14|

La LED intégrée du Raspberry Pi Pico est sur la broche 25, donc nous utilisons le bloc [allumer/éteindre la broche ()] de la palette **Chip** pour la contrôler.

|media15|

.. _connect_pico_per:

2. Connecter au Pico W
---------------------------

Cliquez maintenant sur le bouton **CONNECTER** pour se connecter au Pico W, après avoir cliqué, une nouvelle fenêtre contextuelle apparaîtra.

|media16|

Sélectionnez le port reconnu **CircuitPython CDC control (COMXX)**, puis cliquez sur **Connecter**.

|pico_port|

Lorsque la connexion est réussie, le **CONNECTER** vert en bas à gauche devient **DÉCONNECTER** rouge.

|disconnect_per|

3. Exécuter le Code
------------------------

Cliquez maintenant sur le bouton **DÉMARRER** pour exécuter ce code et vous verrez la LED du Pico W s'allumer. Si le bouton est grisé, cela signifie que le Pico W n'est pas connecté, veuillez le reconnecter.

|media166|

Ensuite, éteignez la broche 25 toutes les secondes dans le cycle, et cliquez de nouveau sur **DÉMARRER** en haut à gauche, pour voir les voyants LED clignoter.

|media17|
