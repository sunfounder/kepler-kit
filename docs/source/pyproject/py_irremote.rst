.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_irremote:

6.4 Télécommande IR
================================

Dans l'électronique grand public, les télécommandes sont utilisées pour contrôler des appareils tels que les télévisions et les lecteurs DVD.
Elles permettent aussi de piloter des dispositifs hors de portée, comme des climatiseurs centraux.

Le récepteur IR est un composant doté d'une cellule photoélectrique calibrée pour recevoir la lumière infrarouge. 
Il est presque toujours utilisé pour la détection de télécommande - chaque téléviseur et lecteur DVD en a un à l'avant pour capter le signal IR de la télécommande.
À l'intérieur de la télécommande se trouve une LED IR correspondante, qui émet des impulsions IR pour indiquer au téléviseur de s'allumer, s'éteindre ou changer de chaîne.

* :ref:`cpn_ir_receiver`

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ÉLÉMENTS DANS CE KIT
        - LIEN
    *   - Kit Kepler	
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPOSANT	
        - QUANTITÉ
        - LIEN

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Câble Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Plusieurs
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schéma**

|sch_irrecv|

**Câblage**


|wiring_irrecv|


**Code**

.. note::

    * Ouvrez le fichier ``6.4_ir_remote_control.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`. 
    
    * Vous devez utiliser les bibliothèques dans le dossier ``ir_rx``, assurez-vous qu'elles ont été chargées sur le Pico. Pour un tutoriel détaillé, reportez-vous à :ref:`add_libraries_py`.


.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.print_error import print_error
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

    # Fonction de rappel utilisateur
    def callback(data, addr, ctrl):
        if data < 0:  # Le protocole NEC envoie des codes répétitifs.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instancier le récepteur
    ir.error_function(print_error)  # Afficher les informations de débogage

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()


La nouvelle télécommande a un morceau de plastique à son extrémité pour isoler la pile à l'intérieur. Vous devez retirer cette pièce pour alimenter la télécommande lorsque vous l'utilisez.
Une fois le programme en cours d'exécution, lorsque vous appuyez sur la télécommande, le terminal affichera la touche que vous avez pressée.

**Comment ça fonctionne ?**

Ce programme peut sembler un peu complexe, mais il exécute en fait les fonctions de base du récepteur IR avec seulement quelques lignes de code.

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    # Fonction de rappel utilisateur
    def callback(data, addr, ctrl):
        if data < 0:  # Le protocole NEC envoie des codes répétitifs.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instancier le récepteur

Ici, un objet ``ir`` est instancié, capable de lire les signaux acquis par le récepteur IR à tout moment.

Le résultat sera enregistré dans ``data`` de la fonction de rappel.

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

Si le récepteur IR reçoit des valeurs en double (par exemple, en maintenant une touche enfoncée), alors ``data < 0`` et ces données doivent être filtrées.

Sinon, ``data`` contiendra une valeur utilisable, qui sera décodée par la fonction ``decodeKeyValue(data)``.

.. code-block:: python

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

Si vous appuyez sur la touche **1**, le récepteur IR émet une valeur comme ``0x0C``, qui doit être décodée pour correspondre à la touche spécifique.

Ensuite, quelques fonctions de débogage sont incluses. Elles sont importantes, mais non essentielles pour l'effet recherché, donc nous les incluons simplement dans le programme.

.. code-block:: python

    from ir_rx.print_error import print_error

    ir.error_function(print_error) # Afficher les informations de débogage

Enfin, nous utilisons une boucle vide comme programme principal, avec un try-except pour quitter proprement et fermer l'objet ``ir``.

.. code-block:: python

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()



* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_