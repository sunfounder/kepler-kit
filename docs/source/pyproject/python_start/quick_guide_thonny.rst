.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

1.5 Guide Rapide sur Thonny
==================================

.. _open_run_code_py:

Ouvrir et Exécuter du Code Directement
---------------------------------------------

La section de code des projets vous indique exactement quel code est utilisé, il suffit donc de double-cliquer sur le fichier ``.py`` avec le numéro de série dans le chemin ``kepler-kit-main/micropython/`` pour l'ouvrir.

Cependant, vous devez d'abord télécharger le package et charger la bibliothèque, comme décrit dans :ref:`add_libraries_py`.

#. Ouvrir le code.

    Par exemple, ``2.1_hello_led.py``.

    Si vous double-cliquez dessus, une nouvelle fenêtre s'ouvrira sur la droite. Vous pouvez ouvrir plusieurs codes en même temps.

    |open_code|

#. Sélectionner le bon interpréteur

    Utilisez un câble micro USB pour connecter le Pico W à votre ordinateur et sélectionnez l'interpréteur "MicroPython (Raspberry Pi Pico)".

    |sec_inter|

#. Exécuter le code

    Pour exécuter le script, cliquez sur le bouton **Exécuter le script actuel** ou appuyez sur F5.

    |run_it|

    Si le code contient des informations à imprimer, elles apparaîtront dans le Shell ; sinon, seule l'information suivante apparaîtra.

    Cliquez sur **Affichage** -> **Modifier** pour ouvrir la fenêtre Shell si elle n'apparaît pas sur votre Thonny.

        .. code-block::

            MicroPython vx.xx on xxxx-xx-xx; Raspberry Pi Pico W  With RP2040

            Type "help()" for more information.
            >>> %Run -c $EDITOR_CONTENT

    * La première ligne indique la version de MicroPython, la date, et les informations de votre appareil.
    * La deuxième ligne vous invite à entrer "help()" pour obtenir de l'aide.
    * La troisième ligne est une commande de Thonny qui demande à l'interpréteur MicroPython sur votre Pico W d'exécuter le contenu de la zone de script - "EDITOR_CONTENT".
    * Si un message apparaît après la troisième ligne, il s'agit généralement d'un message que vous avez demandé à MicroPython d'imprimer, ou d'un message d'erreur pour le code.


#. Arrêter l'exécution

    |stop_it|

    Pour arrêter l'exécution du code, cliquez sur le bouton **Arrêter/Redémarrer le backend**. La commande **%RUN -c $EDITOR_CONTENT** disparaîtra après l'arrêt.

#. Enregistrer ou enregistrer sous

    Vous pouvez enregistrer les modifications apportées à l'exemple ouvert en appuyant sur **Ctrl+S** ou en cliquant sur le bouton **Enregistrer** sur Thonny.

    Le code peut être enregistré comme un fichier distinct sur le Raspberry Pi Pico W en cliquant sur **Fichier** -> **Enregistrer sous**.

    |save_as|

    Sélectionnez **Raspberry Pi Pico**.

    |sec_pico|

    Puis cliquez sur **OK** après avoir entré le nom du fichier et l'extension **.py**. Sur le lecteur Raspberry Pi Pico W, vous verrez votre fichier enregistré.

    |sec_name|

    .. note::
        Quel que soit le nom que vous donnez à votre code, il est préférable de décrire le type de code et de ne pas lui donner un nom inutile comme ``abc.py``.
        Lorsque vous enregistrez le code sous ``main.py``, il s'exécutera automatiquement au démarrage.


Créer un Fichier et l'Exécuter
------------------------------------


Le code est directement affiché dans la section de code. Vous pouvez le copier dans Thonny et l'exécuter comme suit.

#. Créer un nouveau fichier

    Ouvrez Thonny IDE, cliquez sur le bouton **Nouveau** pour créer un fichier vierge.

    |new_file|

#. Copier le code

    Copiez le code du projet dans Thonny IDE.

    |copy_file|

#. Sélectionner le bon interpréteur

    Branchez le Pico W sur votre ordinateur avec un câble micro USB et sélectionnez l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    |sec_inter|

#. Exécuter et enregistrer le code

    Vous devez cliquer sur **Exécuter le script actuel** ou simplement appuyer sur F5 pour l'exécuter. Si votre code n'a pas été enregistré, une fenêtre apparaîtra vous demandant d'enregistrer sur **Cet ordinateur** ou **Raspberry Pi Pico**.

    |where_save|

    .. note::
        Thonny enregistre votre programme sur le Raspberry Pi Pico W lorsque vous lui demandez, donc si vous débranchez le Pico W et le connectez à l'ordinateur de quelqu'un d'autre, votre programme reste intact.

    Cliquez sur OK après avoir sélectionné l'emplacement, nommé le fichier et ajouté l'extension **.py**.

    |sec_name|

    .. note::
        Quel que soit le nom que vous donnez à votre code, il est préférable de décrire le type de code et de ne pas lui donner un nom inutile comme ``abc.py``.
        Lorsque vous enregistrez le code sous ``main.py``, il s'exécutera automatiquement au démarrage.

    Une fois votre programme enregistré, il s'exécutera automatiquement et vous verrez les informations suivantes dans la zone Shell.

    Cliquez sur **Affichage** -> **Modifier** pour ouvrir la fenêtre Shell si elle n'apparaît pas sur votre Thonny.

    .. code-block::

        MicroPython vx.xx.x on xxxx-xx-xx; Raspberry Pi Pico W With RP2040

        Type "help()" for more information.
        >>> %Run -c $EDITOR_CONTENT

    * La première ligne indique la version de MicroPython, la date, et les informations de votre appareil.
    * La deuxième ligne vous invite à entrer "help()" pour obtenir de l'aide.
    * La troisième ligne est une commande de Thonny qui demande à l'interpréteur MicroPython sur votre Pico W d'exécuter le contenu de la zone de script - "EDITOR_CONTENT".
    * Si un message apparaît après la troisième ligne, il s'agit généralement d'un message que vous avez demandé à MicroPython d'imprimer, ou d'un message d'erreur pour le code.

#. Arrêter l'exécution

    |stop_it|

    Pour arrêter l'exécution du code, cliquez sur le bouton **Arrêter/Redémarrer le backend**. La commande **%RUN -c $EDITOR_CONTENT** disparaîtra après l'arrêt.

#. Ouvrir un fichier

    Voici deux façons d'ouvrir un fichier de code enregistré.

    * La première méthode consiste à cliquer sur l'icône d'ouverture sur la barre d'outils de Thonny. Comme pour l'enregistrement d'un programme, vous serez invité à choisir si vous souhaitez l'ouvrir depuis **cet ordinateur** ou **Raspberry Pi Pico**, par exemple, cliquez sur **Raspberry Pi Pico** et vous verrez la liste de tous les programmes que vous avez enregistrés sur le Pico W.
    * La seconde est d'ouvrir directement l'aperçu du fichier en cliquant sur **Affichage** -> **Fichier** -> puis en double-cliquant sur le fichier ``.py`` correspondant pour l'ouvrir.
