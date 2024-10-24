.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_keypad:

4.2 Clavier 4x4
========================

Le clavier 4x4, également connu sous le nom de clavier matriciel, est une matrice de 16 touches regroupées sur un seul panneau.

Le clavier se retrouve sur des dispositifs nécessitant principalement une entrée numérique, comme les calculatrices, les télécommandes, les téléphones à boutons-poussoirs, les distributeurs automatiques, les guichets automatiques, les serrures à combinaison et les serrures numériques.

Dans ce projet, nous apprendrons à déterminer quelle touche est pressée et à obtenir la valeur correspondante.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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
        - :ref:`cpn_resistor`
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Schéma**

|sch_keypad|

4 résistances de tirage sont connectées à chacune des colonnes du clavier matriciel, afin que G6 ~ G9 obtiennent un niveau bas stable lorsque les touches ne sont pas pressées.

Les rangées du clavier (G2 ~ G5) sont programmées pour être à un niveau haut ; si l'une des broches G6 ~ G9 est lue à un niveau haut, cela signifie qu'une touche a été pressée.

Par exemple, si G6 est lue à un niveau haut, alors la touche numérique 1 est pressée ; c'est parce que les broches de contrôle de la touche 1 sont G2 et G6. Lorsque la touche 1 est pressée, G2 et G6 sont connectées, et G6 est donc également à un niveau haut.


**Câblage**

|wiring_keypad|

Pour faciliter le câblage, dans le schéma ci-dessus, la rangée de colonnes du clavier matriciel et les résistances de 10KΩ sont insérées dans les trous où se trouvent G6 ~ G9.

**Code**

.. note::

    * Ouvrez le fichier ``4.2_4x4_keypad.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

Après l'exécution du programme, le terminal affichera les touches que vous avez pressées sur le clavier.

**Comment ça fonctionne**

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

Déclarez chaque touche du clavier matriciel dans le tableau ``characters[]`` et définissez les broches de chaque rangée et colonne.

.. code-block:: python

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

Ceci est la partie principale de la fonction qui lit et affiche la valeur de la touche pressée.

La fonction ``readKey()`` lit l'état de chaque touche.

Les instructions ``if current_key != None`` et ``if current_key == last_key`` 
sont utilisées pour déterminer si une touche est pressée et son état. 
(Si vous appuyez sur '3' après avoir appuyé sur '1', la condition est vérifiée.)

La valeur de la touche pressée est affichée lorsque la condition est vérifiée.

L'instruction ``last_key = current_key`` assigne l'état de chaque évaluation 
à un tableau ``last_key`` pour faciliter la prochaine évaluation conditionnelle.

.. code-block:: python

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

Cette fonction attribue un niveau haut à chaque rangée à tour de rôle, et lorsque la touche est pressée, 
la colonne où se trouve la touche reçoit un niveau haut. 
Après le double bouclage, la valeur de la touche dont l'état est à 1 est stockée dans le tableau ``key``.

Si vous appuyez sur la touche '3' :

|img_keypad_pressed|


``row[0]`` est mis à un niveau haut, et ``col[2]`` reçoit un niveau haut.



``col[0]``, ``col[1]``, ``col[3]`` restent à un niveau bas.

Il y a quatre états : 0, 0, 1, 0 ; et nous enregistrons \'3\' dans ``pressed_keys``.

Lorsque ``row[1]``, ``row[2]``, ``row[3]`` passent à un niveau haut,
``col[0]`` à ``col[4]`` restent à un niveau bas.

La boucle s'arrête, et la fonction retourne key = \'3\'.

Si vous appuyez sur les touches \'1\' et \'3\', il retournera key = [\'1\',\'3\'].
