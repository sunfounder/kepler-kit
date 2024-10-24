.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_74hc_788bs:

5.4 Graphismes 8x8 Pixels
=============================

La matrice LED est un affichage matriciel à points basse résolution. Elle utilise un ensemble de diodes électroluminescentes comme pixels pour créer des motifs visuels.

Elles sont suffisamment lumineuses pour être visibles en plein soleil, et vous pouvez les voir sur certains magasins, panneaux publicitaires, enseignes, et écrans de messages variables (comme ceux des transports publics).

Dans ce kit, nous utilisons une matrice 8x8 à points avec 16 broches. Les anodes sont connectées en lignes et les cathodes en colonnes (au niveau du circuit), ce qui permet de contrôler ces 64 LEDs.

Pour allumer la première LED, il faut fournir un niveau haut pour la ligne 1 et un niveau bas pour la colonne 1. Pour allumer la deuxième LED, il faut fournir un niveau haut pour la ligne 1, un niveau bas pour la colonne 2, et ainsi de suite. En contrôlant le courant à travers chaque paire de lignes et de colonnes, chaque LED peut être contrôlée individuellement pour afficher des caractères ou des images.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

**Composants Requis**

Pour ce projet, nous avons besoin des composants suivants : 

Il est plus pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous :

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Schéma**

|sch_ledmatrix|

La matrice de points 8x8 est contrôlée par deux puces 74HC595, l'une contrôlant les lignes et l'autre les colonnes, tandis que ces deux puces partagent G18~G20, ce qui permet de réduire considérablement les ports I/O de la carte Pico W.

Le Pico W doit sortir un nombre binaire de 16 bits à la fois, les 8 premiers bits sont envoyés au 74HC595 qui contrôle les lignes, et les 8 derniers bits sont envoyés au 74HC595 qui contrôle les colonnes, permettant ainsi à la matrice de points d'afficher un motif spécifique.

Q7': Broche de sortie en série, connectée à DS d'un autre 74HC595 pour connecter plusieurs 74HC595 en série.

**Câblage**

Construisez le circuit. Comme le câblage est complexe, faisons-le étape par étape.

**Étape 1 :** Insérez d'abord le Pico W, la matrice de points LED et les deux puces 74HC595 dans la 
breadboard. Connectez le 3.3V et le GND du Pico W aux trous sur les deux côtés de la carte, puis 
connectez les broches 16 et 10 des deux puces 74HC595 à VCC, les broches 13 et 8 à GND.

.. note::
   Dans l'image Fritzing ci-dessus, le côté avec l'étiquette est en bas.

|wiring_ledmatrix_4|

**Étape 2 :** Connectez la broche 11 des deux 74HC595 ensemble, puis à GP20 ; ensuite, 
la broche 12 des deux puces à GP19 ; ensuite, la broche 14 du 74HC595 sur le côté gauche 
à GP18 et la broche 9 à la broche 14 du second 74HC595.

|wiring_ledmatrix_3|

**Étape 3 :** Le 74HC595 sur le côté droit contrôle les colonnes de la matrice LED. 
Voir le tableau ci-dessous pour le mapping. Par conséquent, les broches Q0-Q7 du 74HC595 
sont mappées respectivement avec les broches 13, 3, 4, 10, 6, 11, 15 et 16.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Étape 4 :** Connectez maintenant les LIGNES de la matrice LED. Le 74HC595 sur 
le côté gauche contrôle les LIGNES de la matrice LED. Voir le tableau ci-dessous 
pour le mapping. Nous voyons que les broches Q0-Q7 du 74HC595 sur la gauche sont 
mappées respectivement avec les broches 9, 14, 8, 12, 1, 7, 2 et 5.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code**

.. note::

    * Ouvrez le fichier ``5.4_8x8_pixel_graphics.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)


    glyph = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]

    # Déplacer les données vers 74HC595
    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

Une fois le programme en cours d'exécution, vous verrez un graphique **x** affiché sur la matrice de points 8x8.

**Comment ça fonctionne ?**

Ici, nous utilisons deux 74HC595 pour fournir des signaux aux lignes et colonnes de la matrice de points.
La méthode pour fournir les signaux est la même que ``hc595_shift(dat)`` des chapitres précédents, mais ici nous devons écrire un nombre binaire de 16 bits à la fois.
Nous avons donc scindé ``hc595_shift(dat)`` en deux fonctions : ``hc595_in(dat)`` et ``hc595_out()``.

.. code-block:: python

    def hc595_in(dat):
        for bit in range(7,-1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

Ensuite, appelez ``hc595_in(dat)`` deux fois dans la boucle principale, écrivez deux nombres binaires de 8 bits et appelez ``hc595_out()`` pour afficher un motif.

Cependant, puisque les LEDs de la matrice partagent des pôles communs, le contrôle de plusieurs lignes/colonnes simultanément peut causer des interférences (par exemple, si vous allumez (1,1) et (2,2) en même temps, (1,2) et (2,1) seront également allumés involontairement).
Il est donc nécessaire d'activer une colonne (ou une ligne) à la fois, de parcourir les 8 cycles, et d'utiliser le principe de l'image résiduelle pour que l'œil humain fusionne 8 motifs et obtienne un motif de 8x8 pixels.

.. code-block:: python

    while True:
        for i in range(0,8):
            hc595_in(glyph[i])
            hc595_in(0x80>>i)
            hc595_out()

Dans cet exemple, la fonction principale contient une boucle ``for``, et lorsque ``i`` est égal à 1, seule la première ligne est activée (la puce de contrôle obtient la valeur ``0x80``) et l'image de la première ligne est écrite. 
Lorsque ``i`` est égal à 2, la deuxième ligne est activée (la puce de contrôle obtient la valeur ``0x40``) et l'image de la deuxième ligne est écrite. Et ainsi de suite, pour compléter les 8 sorties.

Incidemment, comme l'affichage à 4 chiffres et 7 segments, il doit maintenir le taux de rafraîchissement pour éviter que l'œil humain ne perçoive un scintillement. Par conséquent, il est préférable d'éviter les ``sleep()`` supplémentaires dans la boucle principale.

**Pour en savoir plus**

Essayez de remplacer ``glyph`` par les tableaux suivants et voyez ce que cela donne !

.. code-block:: python

    glyph1 = [0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF]
    glyph2 = [0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF]
    glyph3 = [0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF]
    glyph4 = [0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF]
    glyph5 = [0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF]
    glyph6 = [0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF]

Ou bien, essayez de dessiner vos propres graphiques.
