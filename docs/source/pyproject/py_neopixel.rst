.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux démonstrations exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_neopixel:

3.3 Bande LED RGB
======================

Le WS2812 est une source lumineuse LED à contrôle intelligent où le circuit de contrôle et la puce RGB sont intégrés dans un boîtier de composants 5050. 
Il comprend en interne un verrouillage de données numériques et un circuit de conduite d'amplification de signal. 
Il dispose également d'un oscillateur interne de précision et d'une partie de contrôle de courant constant programmable, 
garantissant efficacement la cohérence de la couleur de chaque point lumineux.

Le protocole de transfert de données utilise un mode de communication NZR unique. 
Après la réinitialisation de l'alimentation du pixel, le port DIN reçoit les données du contrôleur. Le premier pixel collecte les données initiales de 24 bits puis les envoie au verrouillage de données interne, tandis que les autres données, remodelées par le circuit interne d'amplification du signal, sont envoyées au pixel suivant via le port DO. Après la transmission de chaque pixel, le signal est réduit de 24 bits. 
Les pixels adoptent une technologie de transmission de remodelage automatique, ce qui permet de rendre le nombre de pixels en cascade illimité tant que la vitesse de transmission du signal est maintenue.


* :ref:`cpn_ws2812`

**Composants requis**

Dans ce projet, nous aurons besoin des composants suivants. 

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schéma**

|sch_ws2812|

**Câblage**

|wiring_ws2812|

.. warning::
    Une chose à surveiller est le courant.

    Bien que la bande LED avec n'importe quel nombre de LED puisse être utilisée avec Pico W, la puissance de son pin VBUS est limitée.
    Ici, nous utiliserons huit LED, ce qui est sûr.
    Mais si vous souhaitez utiliser plus de LED, il faudra ajouter une alimentation séparée.

**Code**

.. note::

    * Ouvrez le fichier ``3.3_rgb_led_strip.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.
    
    * Vous devez utiliser la bibliothèque appelée ``ws2812.py``, vérifiez si elle a été téléchargée sur Pico W. Pour un tutoriel détaillé, consultez :ref:`add_libraries_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812

    ws = WS2812(machine.Pin(0),8)

    ws[0] = [64,154,227]
    ws[1] = [128,0,128]
    ws[2] = [50,150,50]
    ws[3] = [255,30,30]
    ws[4] = [0,128,255]
    ws[5] = [99,199,0]
    ws[6] = [128,128,128]
    ws[7] = [255,100,0]
    ws.write()


Choisissons quelques couleurs préférées et affichons-les sur la bande LED RGB !

**Comment ça marche ?**

Dans la bibliothèque ws2812, nous avons intégré les fonctions associées dans la classe WS2812.

Vous pouvez utiliser la bande LED RGB avec l'instruction suivante.

.. code-block:: python

    from ws2812 import WS2812

Déclarez un objet de type WS2812, nommé "ws", qui est connecté à "pin", avec "number" LED RGB sur la bande WS2812.

.. code-block:: python

    ws = WS2812(pin,number)

ws est un objet tableau, chaque élément correspond à une LED RGB sur la bande WS2812, par exemple, ws[0] est la première et ws[7] est la huitième.

Nous pouvons attribuer des valeurs de couleur à chaque LED RGB, ces valeurs doivent être des couleurs 24 bits (représentées par six chiffres hexadécimaux) ou une liste de trois valeurs RGB sur 8 bits.

Par exemple, la valeur pour le rouge est "0xFF0000" ou "[255,0,0]".

.. code-block:: python

    ws[i] = color value

Ensuite, utilisez cette instruction pour écrire la couleur sur la bande LED et l'allumer.

.. code-block:: python

    ws.write()

Vous pouvez également utiliser directement l'instruction suivante pour faire en sorte que toutes les LED s'allument avec la même couleur.

.. code-block:: python

    ws.write_all(color value)


**En savoir plus**

Nous pouvons générer aléatoirement des couleurs et créer une lumière fluide et colorée.

.. note::

    * Ouvrez le fichier ``3.3_rgb_led_strip_2.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine 
    from ws2812 import WS2812
    import utime
    import urandom

    ws = WS2812(machine.Pin(0),8)

    def flowing_light():
        for i in range(7,0,-1):
            ws[i] = ws[i-1]
        ws[0] = int(urandom.uniform(0, 0xFFFFFF))  
        ws.write()
        utime.sleep_ms(80)

    while True:
        flowing_light()
        print(ws[0])