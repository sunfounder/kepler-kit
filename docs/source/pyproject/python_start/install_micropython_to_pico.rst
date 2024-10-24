.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_micropython_on_pico:

1.3 Installer MicroPython sur votre Pico
==========================================

Passons maintenant à l'installation de MicroPython sur le Raspberry Pi Pico. L'IDE Thonny propose un moyen très pratique de l'installer en un seul clic.

.. note::
    Si vous ne souhaitez pas mettre à jour Thonny, vous pouvez utiliser l'outil officiel de Raspberry Pi |link_micropython_pi| en glissant-déposant un fichier ``rp2_pico_xxxx.uf2`` dans le Raspberry Pi Pico.

#. Ouvrez l'IDE Thonny.

    .. image:: img/set_pico1.png

#. Maintenez enfoncé le bouton **BOOTSEL** puis connectez le Pico à l'ordinateur via un câble Micro USB. Relâchez le bouton **BOOTSEL** après que votre Pico soit monté en tant que périphérique de stockage de masse nommé **RPI-RP2**.

    .. image:: img/bootsel_onboard.png

#. En bas à droite, cliquez sur le bouton de sélection de l'interpréteur et choisissez **Installer MicroPython**.

    .. note::
        Si votre Thonny n'a pas cette option, veuillez le mettre à jour vers la dernière version.

    .. image:: img/set_pico2.png

#. Dans **Cible**, le volume du Pico que vous venez de brancher apparaîtra automatiquement, et dans **Variante Micropython**, sélectionnez **Raspberry Pi.Pico W/Pico WH**.

    .. image:: img/set_pico3.png

#. Cliquez sur le bouton **Installer**, attendez que l'installation soit terminée, puis fermez cette page.

    .. image:: img/set_pico4.png

Félicitations, votre Raspberry Pi Pico est maintenant prêt à être utilisé.
