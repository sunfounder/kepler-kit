.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_arduino:

1.1 Installer l'IDE Arduino (Important)
===========================================

L'IDE Arduino, connu sous le nom d'Environnement de Développement Intégré Arduino, fournit tout le support logiciel nécessaire pour réaliser un projet Arduino. Il s'agit d'un logiciel de programmation spécialement conçu par l'équipe Arduino, permettant d'écrire des programmes et de les téléverser sur la carte Arduino.

L'IDE Arduino 2.0 est un projet open-source. C'est une avancée majeure par rapport à son prédécesseur robuste, l'IDE Arduino 1.x, avec une interface utilisateur rénovée, un gestionnaire de cartes et de bibliothèques amélioré, un débogueur, la fonction d'auto-complétion, et bien plus encore.

Dans ce tutoriel, nous allons montrer comment télécharger et installer l'IDE Arduino 2.0 sur votre ordinateur Windows, Mac ou Linux.

Configuration requise
------------------------

* Windows - Win 10 et plus récent, 64 bits
* Linux - 64 bits
* Mac OS X - Version 10.14 : "Mojave" ou plus récent, 64 bits

Télécharger l'IDE Arduino 2.0
--------------------------------

#. Visitez la page |link_download_arduino|.

#. Téléchargez l'IDE pour la version de votre système d'exploitation.

    .. image:: img/sp_001.png

Installation
----------------

Windows
^^^^^^^^^^

#. Double-cliquez sur le fichier ``arduino-ide_xxxx.exe`` pour exécuter le fichier téléchargé.

#. Lisez l'accord de licence et acceptez-le.

    .. image:: img/sp_002.png

#. Choisissez les options d'installation.

    .. image:: img/sp_003.png

#. Choisissez le répertoire d'installation. Il est recommandé d'installer le logiciel sur un disque autre que le disque système.

    .. image:: img/sp_004.png

#. Enfin, cliquez sur Terminer.

    .. image:: img/sp_005.png

macOS
^^^^^^^^

Double-cliquez sur le fichier ``arduino_ide_xxxx.dmg`` téléchargé et suivez les instructions pour copier **Arduino IDE.app** dans le dossier **Applications**. Après quelques secondes, vous verrez que l'IDE Arduino est installé avec succès.

.. image:: img/macos_install_ide.png
    :width: 800

Linux
^^^^^^^^

Pour le tutoriel sur l'installation de l'IDE Arduino 2.0 sur un système Linux, veuillez vous référer à : https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux


Ouvrir l'IDE
------------

#. Lors de la première ouverture de l'IDE Arduino 2.0, il installe automatiquement les cartes Arduino AVR, les bibliothèques intégrées et d'autres fichiers nécessaires.

    .. image:: img/sp_901.png

#. De plus, votre pare-feu ou centre de sécurité peut apparaître plusieurs fois pour vous demander si vous souhaitez installer certains pilotes de périphériques. Veuillez les installer tous.

    .. image:: img/sp_104.png

#. Votre IDE Arduino est maintenant prêt !

    .. note::
        Dans le cas où certaines installations n'auraient pas réussi en raison de problèmes de réseau ou autres, vous pouvez rouvrir l'IDE Arduino et il terminera le reste de l'installation. La fenêtre de sortie ne s'ouvrira pas automatiquement une fois toutes les installations terminées, sauf si vous cliquez sur Vérifier ou Téléverser.
