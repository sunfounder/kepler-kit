.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _setup_pico_arduino:

1.3 Configuration du Raspberry Pi Pico W (Important)
========================================================

1. Installer le Firmware UF2
------------------------------------

Lorsque vous connectez pour la première fois le Raspberry Pi Pico W ou maintenez le bouton BOOTSEL enfoncé tout en l'insérant, l'appareil apparaît comme un lecteur sans être assigné à un port COM. Cela rend le téléversement de code impossible.

Pour résoudre ce problème, vous devez installer le firmware UF2. Ce firmware prend en charge MicroPython et est également compatible avec l'IDE Arduino.

1. Téléchargez le Firmware UF2 via le lien ci-dessous.

    * :download:`Raspberry Pi Pico W UF2 Firmware <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Connectez votre Raspberry Pi Pico W à votre ordinateur à l'aide d'un câble Micro USB. Votre Pico W se montera en tant que périphérique de stockage de masse nommé **RPI-RP2**.

    .. image:: img/install_pico_plugin.png

3. Glissez-déposez le firmware UF2 téléchargé dans le lecteur **RPI-RP2**.

    .. image:: img/install_pico_uf2.png

4. Après cela, le lecteur **RPI-RP2** disparaîtra, et vous pourrez continuer avec les étapes suivantes.


2. Installation du Package de Carte
---------------------------------------

Pour programmer le Raspberry Pi Pico W, vous devrez installer le package correspondant dans l'IDE Arduino. Voici un guide étape par étape :

1. Dans la fenêtre **Gestionnaire de cartes**, recherchez **pico**. Cliquez sur le bouton **Installer** pour commencer l'installation. Cela installera le package **Arduino Mbed OS RP2040 Boards**, qui inclut la prise en charge du Raspberry Pi Pico W.

    .. image:: img/install_pico.png

2. Au cours du processus, quelques fenêtres contextuelles apparaîtront pour l'installation de pilotes spécifiques. Sélectionnez **"Installer"**.

    .. image:: img/install_pico_sa.png

3. Ensuite, une notification indiquera que l'installation est terminée.

3. Sélection de la Carte et du Port
----------------------------------------

1. Pour sélectionner la carte appropriée, allez dans **Outils** -> **Carte** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico**.

    .. image:: img/install_pico_tool_board.png

2. Si votre Raspberry Pi Pico W est connecté à l'ordinateur, définissez le port correct en allant dans **Outils** -> **Port**.

    .. image:: img/install_pico_tool_port.png

3. L'Arduino 2.0 propose une nouvelle fonctionnalité de sélection rapide. Pour le Raspberry Pi Pico W, qui n'est généralement pas reconnu automatiquement, cliquez sur **Sélectionner une autre carte et port**.

    .. image:: img/install_pico_select.png

4. Tapez **Raspberry Pi Pico** dans la barre de recherche, sélectionnez-le lorsqu'il apparaît, choisissez le port approprié et cliquez sur **OK**.

    .. image:: img/install_pico_board.png

5. Vous pourrez facilement le re-sélectionner plus tard via cette fenêtre d'accès rapide.

    .. image:: img/install_pico_quick.png

6. L'une ou l'autre de ces méthodes vous permettra de définir la carte et le port corrects. Vous êtes maintenant prêt à téléverser du code sur le Raspberry Pi Pico W.

4. Téléversement du Code
--------------------------------

Passons maintenant à la façon de téléverser du code sur votre Raspberry Pi Pico W.

1. Ouvrez un fichier ``.ino`` ou utilisez le croquis vide actuellement affiché. Ensuite, cliquez sur le bouton **Téléverser**.

    .. image:: img/install_pico_upload.png

2. Attendez que le message de téléversement apparaisse, comme indiqué ci-dessous.

    .. image:: img/install_pico_upload_dot.png

3. Maintenez le bouton **BOOTSEL** enfoncé, débranchez rapidement votre Raspberry Pi Pico W, puis rebranchez-le.

    .. image:: img/led_onboard.png 

    .. note::
        
        * Cette étape est cruciale, surtout pour les utilisateurs débutant avec l'IDE Arduino. La sauter entraînera un échec du téléversement.

        * Une fois que vous avez réussi à téléverser le code, votre Pico W sera reconnu par l'ordinateur. Pour les utilisations futures, il suffira simplement de le brancher à l'ordinateur.

4. Une invite indiquant un téléversement réussi apparaîtra.

    .. image:: img/install_pico_upload_done.png
