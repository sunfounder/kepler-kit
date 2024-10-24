.. note::

    Bonjour, bienvenue dans la communauté des passionnés SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez en profondeur le Raspberry Pi, l'Arduino et l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_music_player:

7.8 Lecteur de Musique RFID
==============================

À travers notre projet précédent, :ref:`py_rfid`, nous avons appris que le module MFRC522 permet d'écrire jusqu'à 48 caractères d'information sur la carte (ou la clé), y compris la clé d'accès et les informations d'identité, ainsi que la partition musicale.

Par exemple, si vous écrivez ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC``, le buzzer jouera la musique lorsque la carte (ou la clé) sera lue à nouveau. Il peut également être équipé d'un WS2812 pour afficher des effets lumineux spectaculaires.

Vous pouvez trouver plus de partitions musicales sur Internet, ou même composer votre propre musique, les enregistrer sur la carte (ou la clé) et les partager avec vos amis !

|rfid_player|

**Composants Requis**

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Buzzer Passif :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schéma**

|sch_music_player|

**Câblage**

|wiring_rfid_music_player| 

**Code**

#. Ouvrez le fichier ``6.5_rfid_write.py`` sous le chemin ``kepler-kit-main/micropython``, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

   .. note::

    Ici, vous devez utiliser les bibliothèques dans le dossier ``mfrc522``, veuillez vérifier si elles ont été téléchargées sur Pico, pour un tutoriel détaillé référez-vous à :ref:`add_libraries_py`.

#. Après l'exécution, tapez ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` dans le shell, puis rapprochez la carte (ou la clé) du module MFRC522 pour enregistrer la partition de "L'Hymne à la Joie".

#. Ouvrez le fichier ``7.8_rfid_music_player.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

   .. code-block:: python

       ###################################
        # Utilisez 'write.py' pour écrire #
        # une partition sur la carte, cet #
        # exemple jouera la partition     #
        ###################################
        # Partition de L'Hymne à la Joie :#
        # EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC  #
        ###################################

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # Configuration des LED WS2812
        # Initialiser une bande WS2812 de 8 LEDs sur la broche 0
        ws = WS2812(machine.Pin(0), 8)

        # Configuration du lecteur RFID MFRC522
        # Initialiser le lecteur RFID en utilisant SPI sur des broches spécifiques
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # Fréquences des notes pour le buzzer (en Hertz)
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # Initialiser le PWM pour le buzzer sur la broche 15
        buzzer = machine.PWM(machine.Pin(15))

        # Liste des fréquences de notes correspondant aux notes musicales
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # Fonction pour jouer un ton sur le buzzer avec une fréquence et une durée spécifiées
        def tone(pin, frequency, duration):
            pin.freq(frequency)  # Régler la fréquence du buzzer
            pin.duty_u16(30000)  # Régler le cycle de service à 50% (approx)
            time.sleep_ms(duration)  # Jouer le ton pour la durée spécifiée
            pin.duty_u16(0)  # Arrêter le ton en mettant le cycle de service à 0

        # Fonction pour allumer une LED WS2812 à un index spécifique avec une couleur aléatoire
        def lumi(index):
            for i in range(8):
                ws[i] = 0x000000  # Éteindre toutes les LEDs
            ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # Définir une couleur aléatoire pour la LED à l'index donné
            ws.write()  # Écrire les données de couleur aux LEDs WS2812

        # Encoder le texte des notes musicales en indices et jouer les notes correspondantes
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # Correspondance des notes musicales aux caractères
        def take_text(text):
            string = text.replace(' ', '').upper()  # Supprimer les espaces et convertir le texte en majuscules
            while len(string) > 0:
                index = words.index(string[0])  # Trouver l'index de la première note dans la chaîne
                tone(buzzer, note[index], 250)  # Jouer la note correspondante sur le buzzer pendant 250 ms
                lumi(index)  # Allumer la LED correspondant à la note
                string = string[1:]  # Passer au caractère suivant dans la chaîne

        # Fonction pour lire la carte RFID et jouer la partition stockée
        def read():
            print("Reading...Please place the card...")
            id, text = reader.read()  # Lire la carte RFID (ID et texte stocké)
            print("ID: %s\nText: %s" % (id, text))  # Afficher l'ID et le texte
            take_text(text)  # Jouer la partition à partir du texte stocké sur la carte
            
        # Commencer la lecture de la carte RFID et jouer la partition correspondante
        read()

#. En rapprochant à nouveau la carte (ou la clé) du module MFRC522, le buzzer jouera la musique stockée sur la carte (ou la clé), et la bande RGB s'allumera avec des couleurs aléatoires.
