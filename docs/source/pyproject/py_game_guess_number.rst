.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_guess_number:

7.7 Devine le Nombre
==============================


"Devine le Nombre" est un jeu amusant où vous et vos amis devez deviner un nombre (0-99). À chaque tentative, la plage des possibilités se réduit jusqu'à ce qu'un joueur trouve la bonne réponse. Celui qui découvre le nombre mystère est considéré comme perdant et reçoit une petite punition.

Par exemple, si le nombre mystère est 51 (invisible pour les joueurs) et que le joueur 1 entre 50, la plage devient 50 - 99 ; si le joueur 2 entre 70, la plage passe à 50 - 70 ; si le joueur 3 entre 51, il perd la partie. Dans ce jeu, les numéros sont entrés via un clavier, et les résultats sont affichés sur un écran LCD.

|guess_number|

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
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|


**Schéma**


|sch_guess_number|

Ce circuit est basé sur :ref:`py_keypad` avec l'ajout d'un écran LCD1602 I2C pour afficher les touches pressées.


**Câblage**

|wiring_game_guess_number| 

Pour faciliter le câblage, dans le schéma ci-dessus, la rangée de colonnes du clavier matriciel et les résistances de 10KΩ sont insérées simultanément dans les trous où G10 ~ G13 sont situés.


**Code**

.. note::

    * Ouvrez le fichier ``7.7_game_guess_number.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import time
    import urandom

    # Initialiser la communication I2C pour l'écran LCD1602
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Créer un objet LCD pour contrôler l'écran LCD1602
    lcd = LCD(i2c)

    # Mappage des caractères du clavier pour un clavier matriciel 4x4
    characters = [["1", "2", "3", "A"], 
                ["4", "5", "6", "B"], 
                ["7", "8", "9", "C"], 
                ["*", "0", "#", "D"]]

    # Définir les broches pour les rangées du clavier
    pin = [21, 20, 19, 18]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Configurer les broches de rangée en sortie

    # Définir les broches pour les colonnes du clavier
    pin = [13, 12, 11, 10]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)  # Configurer les broches de colonne en entrée

    # Fonction pour lire une touche du clavier
    def readKey():
        key = []
        for i in range(4):
            row[i].high()  # Activer la broche de rangée
            for j in range(4):
                if col[j].value() == 1:  # Vérifier si une colonne est pressée
                    key.append(characters[i][j])  # Enregistrer la touche correspondante
            row[i].low()  # Désactiver la broche de rangée
        if key == []:
            return None  # Retourner None si aucune touche n'est pressée
        else:
            return key  # Retourner la touche pressée

    # Initialiser et réinitialiser les variables du jeu (pointValue aléatoire, limites supérieure/inférieure)
    def init_new_value():
        global pointValue, upper, count, lower
        pointValue = int(urandom.uniform(0, 99))  # Générer un nombre aléatoire entre 0 et 99
        print(pointValue)  # Afficher le nombre cible (pour le débogage)
        upper = 99  # Limite supérieure initiale
        lower = 0  # Limite inférieure initiale
        count = 0  # Réinitialiser le compteur de tentatives du joueur
        return False  # Indiquer que le jeu n'est pas terminé

    # Fonction pour afficher les informations du jeu sur l'écran LCD
    # Si le joueur a trouvé le bon nombre, afficher "GAME OVER"
    # Sinon, montrer la tentative actuelle et la plage des possibilités
    def lcd_show(result):
        lcd.clear()  # Effacer l'écran LCD
        if result == True:  # Si le joueur a deviné correctement
            string = "GAME OVER!\n"
            string += "Point is " + str(pointValue)  # Afficher le nombre correct
        else:
            string = "Enter number: " + str(count) + "\n"  # Afficher la tentative actuelle
            string += str(lower) + " < Point < " + str(upper)  # Afficher la plage de valeurs possibles
        lcd.message(string)  # Envoyer la chaîne de caractères à l'écran LCD
        return

    # Traiter la tentative du joueur et mettre à jour la limite supérieure ou inférieure
    # Si la tentative correspond à pointValue, retourner True pour indiquer que le jeu est terminé
    # Sinon, mettre à jour les limites et retourner False
    def number_processing():
        global upper, count, lower
        if count > pointValue:
            if count < upper:
                upper = count  # Mettre à jour la limite supérieure si la tentative est trop élevée
        elif count < pointValue:
            if count > lower:
                lower = count  # Mettre à jour la limite inférieure si la tentative est trop basse
        elif count == pointValue:
            return True  # Retourner True si la tentative correspond à pointValue
        count = 0  # Réinitialiser le compteur de tentatives pour la prochaine tentative
        return False

    ## Configuration et boucle principale du jeu
    # Afficher un message de bienvenue et inviter l'utilisateur à appuyer sur 'A' pour commencer
    string = "Press A to Start!"
    lcd.message(string)
    result = init_new_value()  # Initialiser les variables du jeu

    # Boucle principale pour gérer l'entrée du clavier et mettre à jour l'affichage
    last_key = None
    while True:
        current_key = readKey()  # Lire la touche actuellement pressée
        if current_key == last_key:
            continue  # Ignorer le traitement si la même touche est encore pressée
        last_key = current_key  # Mettre à jour la dernière touche pressée
        
        if current_key != None:
            # Si 'A' est pressé, recommencer le jeu avec un nouveau nombre cible
            if current_key == ["A"]:
                result = init_new_value()
            # Si 'D' est pressé, vérifier si la tentative actuelle est correcte
            elif current_key == ["D"]:
                result = number_processing()
            # Si un nombre est pressé et que le compteur a moins de 10 chiffres
            elif current_key[0] in list("1234567890") and count < 10:
                count = count * 10 + int(current_key[0])  # Ajouter le chiffre à la tentative actuelle
            lcd_show(result)  # Mettre à jour l'écran LCD avec l'état actuel du jeu
        time.sleep(0.1)  # Petit délai pour le rebond des touches


* Après avoir exécuté le code, appuyez sur ``A`` pour commencer le jeu. Un nombre aléatoire ``point`` est généré mais n'est pas affiché sur l'écran LCD, et vous devez le deviner.
* Le nombre que vous saisissez apparaît à la fin de la première ligne jusqu'à ce que la vérification finale soit effectuée. (Appuyez sur ``D`` pour démarrer la comparaison.)
* La plage de valeurs possibles de ``point`` est affichée sur la deuxième ligne, et vous devez saisir un nombre dans cette plage.
* À chaque tentative, la plage se réduit ; si vous trouvez le nombre chanceux (ou malchanceux), le message ``GAME OVER!`` s'affichera.

.. note:: 
    Si le code et le câblage sont corrects mais que l'écran LCD n'affiche toujours rien, vous pouvez ajuster le potentiomètre à l'arrière pour augmenter le contraste.

