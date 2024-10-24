.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_mpr121:

4.3 Clavier à électrodes
================================

Le MPR121 est un excellent choix si vous souhaitez ajouter un grand nombre d'interrupteurs tactiles à votre projet. Il dispose d'électrodes qui peuvent être étendues avec des conducteurs. 
En connectant les électrodes à une banane, par exemple, vous pouvez transformer cette banane en interrupteur tactile.

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Schéma**

|sch_mpr121|

**Câblage**

|wiring_mpr121|

**Code**

.. note::

    * Ouvrez le fichier ``4.3_electrode_keyboard.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.
    
    * Vous devez utiliser la bibliothèque appelée ``mpr121.py``, veuillez vérifier si elle a été téléchargée sur Pico W. Pour un tutoriel détaillé, consultez :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # vérifiez toutes les touches
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

Une fois le programme lancé, vous pouvez toucher les douze électrodes du MPR121 avec votre main, et les électrodes touchées seront affichées.

Vous pouvez étendre les électrodes pour connecter d'autres conducteurs tels que des fruits, des fils, du papier d'aluminium, etc. Cela vous offrira plus de possibilités pour déclencher ces électrodes.

**Comment ça marche ?**

Dans la bibliothèque mpr121, nous avons intégré les fonctionnalités dans la classe ``MPR121``.

.. code-block:: python

    from mpr121 import MPR121

Le MPR121 est un module I2C qui nécessite un ensemble de broches I2C pour initialiser l'objet ``MPR121``. À ce stade, l'état des électrodes du module sera enregistré comme valeurs initiales. Si les électrodes sont étendues, l'exemple doit être relancé pour réinitialiser ces valeurs initiales.

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

Ensuite, utilisez ``mpr.get_all_states()`` pour lire si les électrodes sont déclenchées. Si les électrodes 2 et 3 sont activées, la valeur ``[2, 3]`` sera générée.


.. code-block::

    while True:
        value = mpr.get_all_states()
        if len(value) ! = 0:
            print(value)
        time.sleep_ms(100)

Vous pouvez également utiliser ``mpr.is_touched(electrode)`` pour détecter une électrode spécifique. Lorsqu'elle est déclenchée, elle renvoie ``True``, sinon elle renvoie ``False``.

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)