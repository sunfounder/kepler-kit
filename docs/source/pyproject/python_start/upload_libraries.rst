.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _add_libraries_py:

1.4 Télécharger les Bibliothèques sur le Pico
==================================================

Dans certains projets, vous aurez besoin de bibliothèques supplémentaires. Nous allons donc d'abord télécharger ces bibliothèques sur le Raspberry Pi Pico W, puis nous pourrons exécuter le code directement par la suite.

#. Téléchargez le code pertinent depuis le lien ci-dessous.

   * :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

#. Ouvrez l'IDE Thonny, branchez le Pico sur votre ordinateur avec un câble micro USB et cliquez sur l'interpréteur "MicroPython (Raspberry Pi Pico).COMXX" en bas à droite.

    .. image:: img/sec_inter.png

#. Dans la barre de navigation en haut, cliquez sur **Affichage** -> **Fichiers**.

    .. image:: img/th_files.png

#. Changez le chemin vers le dossier où vous avez précédemment téléchargé le `code package <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`_, puis accédez au dossier ``kepler-kit-main/libs``.

    .. image:: img/th_path.png

#. Sélectionnez tous les fichiers ou dossiers du dossier ``libs/``, faites un clic droit et cliquez sur **Télécharger vers**, cela prendra un certain temps pour terminer le téléchargement.

    .. image:: img/th_upload.png

#. Vous verrez maintenant les fichiers que vous venez de télécharger dans votre lecteur ``Raspberry Pi Pico``.

    .. image:: img/th_done.png