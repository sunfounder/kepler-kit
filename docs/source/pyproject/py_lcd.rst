.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_lcd:

3.4 Afficheur à Cristaux Liquides (LCD)
=============================================

Le LCD1602 est un afficheur à cristaux liquides de type caractère, capable 
d'afficher 32 caractères (16*2) simultanément.

Comme nous le savons tous, bien que les écrans LCD et d'autres affichages 
enrichissent grandement l'interaction homme-machine, ils partagent une 
faiblesse commune. Lorsqu'ils sont connectés à un contrôleur, plusieurs 
E/S seront occupées, ce qui peut limiter les autres fonctionnalités du 
contrôleur. C'est pourquoi le LCD1602 avec un bus I2C a été développé pour 
résoudre ce problème.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_


|pin_i2c|

Nous utiliserons ici l'interface I2C0 pour contrôler le LCD1602 et afficher du texte.


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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schéma**

|sch_lcd|

**Câblage**

|wiring_lcd|

**Code**

.. note::

    * Ouvrez le fichier ``3.4_liquid_crystal_display.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`. 
    
    * Vous devez utiliser la bibliothèque appelée ``lcd1602.py``, assurez-vous qu'elle a été téléchargée sur le Pico W. Pour un tutoriel détaillé, reportez-vous à :ref:`add_libraries_py`.


.. code-block:: python

    from machine import I2C, Pin
    from lcd1602 import LCD
    import time

    # Initialiser la communication I2C;
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Créer un objet LCD pour interagir avec l'afficheur LCD1602
    lcd = LCD(i2c)

    # Afficher le premier message sur le LCD
    # Utiliser '\n' pour créer une nouvelle ligne.
    string = "SunFounder\n    LCD Tutorial"
    lcd.message(string)
    # Attendre 2 secondes
    time.sleep(2)
    # Effacer l'écran
    lcd.clear()

    # Afficher le deuxième message sur le LCD
    string = "Hello\n  World!"
    lcd.message(string)
    # Attendre 5 secondes
    time.sleep(5)
    # Effacer l'écran avant de quitter
    lcd.clear()

Après l'exécution du programme, vous verrez apparaître deux lignes de texte sur le LCD à tour de rôle, puis elles disparaîtront.

.. note:: Lorsque le code est en cours d'exécution, si l'écran est vide, vous pouvez ajuster le potentiomètre à l'arrière pour augmenter le contraste.

**Comment ça fonctionne ?**

#. Configuration de la communication I2C

   Le module ``machine`` est utilisé pour configurer la communication I2C. Les broches SDA (données série) et SCL (horloge série) sont définies (broches 20 et 21 respectivement), avec une fréquence I2C de 400kHz.

   .. code-block:: python
      
      from machine import I2C, Pin
      i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

#. Initialisation de l'afficheur LCD

   La classe ``LCD`` du module ``lcd1602`` est instanciée. Cette classe gère la communication avec l'afficheur LCD via I2C. Un objet ``LCD`` est créé en utilisant l'objet ``i2c``.

   Pour plus d'informations sur l'utilisation de la bibliothèque ``lcd1602``, veuillez vous référer à ``lcd1602.py``.

   .. code-block:: python
      
      from lcd1602 import LCD
      lcd = LCD(i2c)

#. Affichage de messages sur le LCD

   La méthode ``message`` de l'objet ``LCD`` est utilisée pour afficher du texte à l'écran. Le caractère ``\n`` permet de créer une nouvelle ligne sur le LCD. La fonction ``time.sleep()`` suspend l'exécution pour un nombre de secondes spécifié.

   .. code-block:: python
      
      string = "SunFounder\n    LCD Tutorial"
      lcd.message(string)
      time.sleep(2)
      lcd.clear()

#. Effacement de l'écran

   La méthode ``clear`` de l'objet ``LCD`` est appelée pour effacer le texte affiché à l'écran.

   .. code-block:: python
      
      lcd.clear()

#. Affichage d'un deuxième message

   Un nouveau message est affiché, suivi d'un délai avant d'effacer à nouveau l'écran.

   .. code-block:: python
      
      string = "Hello\n  World!"
      lcd.message(string)
      time.sleep(5)
      lcd.clear()

