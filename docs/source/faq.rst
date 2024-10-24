.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans le Raspberry Pi, l'Arduino et l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support expert** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

FAQ
=========

Arduino
---------------------

#. L'upload du code a échoué dans l'IDE Arduino ?
    * Vérifiez que votre Pico est bien reconnu par l'IDE Arduino, le port devrait être COMXX (Raspberry Pi Pico). Pour les instructions, veuillez consulter :ref:`setup_pico_arduino`.
    * Assurez-vous que la carte (Raspberry Pi Pico) ou le port (COMXX (Raspberry Pi Pico)) est correctement sélectionné.
    * Si votre code est correct et que vous avez sélectionné la bonne carte et le bon port, mais que l'upload échoue encore, cliquez à nouveau sur l'icône **Upload**. Lorsque la progression affiche "Upload...", débranchez le câble USB, puis maintenez le bouton **BOOTSEL** enfoncé tout en rebranchant le câble, et le code sera chargé avec succès.


MicroPython
------------------

#. Comment ouvrir et exécuter le code ?
    Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.

#. Comment télécharger une bibliothèque sur le Raspberry Pi Pico W ?
    Pour des tutoriels détaillés, veuillez consulter :ref:`add_libraries_py`.

#. Pas d'option MicroPython (Raspberry Pi Pico W) dans l'IDE Thonny ?
    * Vérifiez que votre Pico W est connecté à votre ordinateur via un câble USB.
    * Assurez-vous d'avoir installé MicroPython pour le Pico W (:ref:`install_micropython_on_pico`).
    * L'interpréteur Raspberry Pi Pico W est disponible uniquement dans la version 3.3.3 ou supérieure de Thonny. Si vous avez une version plus ancienne, veuillez la mettre à jour (:ref:`thonny_ide`).
    * Si le module chargeur Li-po est connecté à la breadboard, débranchez-le d'abord puis reconnectez le Pico W à l'ordinateur.

#. Impossible d'ouvrir le code Pico W ou de sauvegarder du code sur le Pico W via Thonny IDE ?
    * Vérifiez que votre Pico W est connecté à votre ordinateur via un câble USB.
    * Assurez-vous d'avoir sélectionné l'interpréteur **MicroPython (Raspberry Pi Pico)**.

#. Le Raspberry Pi Pico W peut-il être utilisé à la fois sur Thonny et Arduino ?
    NON, des opérations différentes sont nécessaires.

    * Si vous l'avez utilisé sur Arduino et souhaitez maintenant l'utiliser sur Thonny, vous devez :ref:`install_micropython_on_pico`.
    * Si vous l'avez utilisé sur Thonny et souhaitez maintenant l'utiliser sur Arduino IDE, vous devez :ref:`setup_pico_arduino`.


#. Si votre ordinateur est sous Windows 7 et que le Pico W n'est pas détecté.
    * Téléchargez le pilote USB CDC à partir de http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver
    * Décompressez le fichier ``amtel_devices_cdc.inf`` dans un dossier nommé ``pico-serial``.
    * Renommez le fichier ``amtel_devices_cdc.inf`` en ``pico-serial.inf``.
    * Ouvrez/modifiez le fichier ``pico-serial.inf`` dans un éditeur basique comme Notepad.
    * Supprimez et remplacez les lignes sous les en-têtes suivants :

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Fermez et sauvegardez en vous assurant de conserver le nom ``pico-serial.inf``.
    #. Accédez à la liste des périphériques de votre PC, trouvez le Pico sous Ports, nommé comme "CDC Device". Un point d'exclamation jaune l'indiquera.
    #. Faites un clic droit sur le "CDC Device" et mettez à jour ou installez le pilote en choisissant le fichier que vous avez créé à partir de l'emplacement où vous l'avez enregistré.



Piper Make
------------------

#. Comment configurer le Pico W sur Piper Make ?
    Pour des tutoriels détaillés, veuillez consulter :ref:`per_setup_pico`.

#. Comment télécharger ou importer du code ?
    Pour des tutoriels détaillés, veuillez consulter :ref:`per_save_import`.

#. Comment se connecter au Pico W ?
    Pour des tutoriels détaillés, veuillez consulter :ref:`connect_pico_per`.

