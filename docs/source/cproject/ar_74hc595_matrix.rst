.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_74hc_788bs:


5.4 - Graphiques 8x8 Pixels
================================

La matrice LED est un affichage à points bas résolution. Elle utilise un ensemble de diodes électroluminescentes en tant que pixels pour afficher des motifs.

Elles sont suffisamment lumineuses pour être visibles en plein soleil, et vous pouvez les voir dans certains magasins, panneaux publicitaires, enseignes, et affichages de messages variables (comme ceux des véhicules de transport en commun).

Ce kit contient une matrice de points 8x8 avec 16 broches. Les anodes sont connectées en lignes et les cathodes en colonnes (au niveau du circuit), ce qui permet de contrôler les 64 LED.

Pour allumer la première LED, vous devez fournir un niveau haut pour Row1 et un niveau bas pour Col1. 
Pour allumer la deuxième LED, il faut fournir un niveau haut pour Row1, un niveau bas pour Col2, et ainsi de suite. En contrôlant le courant à travers chaque paire de lignes et de colonnes, chaque LED peut être contrôlée individuellement pour afficher des caractères ou des images.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

**Composants requis**

Pour ce projet, nous avons besoin des composants suivants.

Il est plus pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom
        - ARTICLES DANS CE KIT
        - LIEN D'ACHAT
    *   - Kit Kepler
        - 450+
        - |link_kepler_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - N°
        - INTRODUCTION DES COMPOSANTS
        - QUANTITÉ
        - LIEN D'ACHAT

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

La matrice 8x8 est contrôlée par deux puces 74HC595, l'une contrôlant les lignes et l'autre les colonnes, tandis que ces deux puces partagent G18~G20, ce qui permet de réduire considérablement les ports I/O de la carte Pico W.

Pico W doit sortir un nombre binaire de 16 bits à la fois, les 8 premiers bits sont donnés au 74HC595 qui contrôle les lignes, et les 8 derniers au 75HC595 qui contrôle les colonnes, permettant ainsi à la matrice de points d'afficher un motif spécifique.

Q7' : broche de sortie série, connectée à DS d'un autre 74HC595 pour connecter plusieurs 74HC595 en série.

**Câblage**

Construisez le circuit. Comme le câblage est complexe, faisons-le étape par étape.

**Étape 1 :** Insérez d'abord la Pico W, la matrice LED et les deux puces 74HC595 
sur la breadboard. Connectez le 3,3V et le GND de la Pico W aux trous sur les deux 
côtés de la carte, puis branchez les broches 16 et 10 des deux puces 74HC595 à VCC, 
les broches 13 et 8 à GND.

.. note::
   Dans l'image Fritzing ci-dessus, le côté avec l'étiquette est en bas.

|wiring_ledmatrix_4|

**Étape 2 :** Connectez la broche 11 des deux 74HC595 ensemble, puis à GP20 ; 
ensuite, la broche 12 des deux puces à GP19 ; puis, la broche 14 du 74HC595 à 
gauche à GP18 et la broche 9 à la broche 14 du second 74HC595.

|wiring_ledmatrix_3|

**Étape 3 :** Le 74HC595 sur la droite contrôle les colonnes de la matrice LED. 
Voir le tableau ci-dessous pour le mapping. Les broches Q0-Q7 du 74HC595 sont 
respectivement reliées aux broches 13, 3, 4, 10, 6, 11, 15, et 16.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Étape 4 :** Connectez maintenant les lignes de la matrice LED. Le 74HC595 à 
gauche contrôle les lignes de la matrice LED. Voir le tableau ci-dessous pour 
le mapping. Les broches Q0-Q7 du 74HC595 à gauche sont reliées respectivement 
aux broches 9, 14, 8, 12, 1, 7, 2, et 5.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``5.4_8x8_pixel_graphics.ino`` sous le chemin ``kepler-kit-main/arduino/5.4_8x8_pixel_graphics``.
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3682592-17d4-4690-a730-1c0a6fcbd353/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Une fois le programme en cours d'exécution, vous verrez un graphique **x** affiché sur la matrice de points 8x8.


**Comment ça marche ?**

Ici, nous utilisons deux 74HC595 pour fournir des signaux aux lignes et colonnes de la matrice. 
La méthode de fourniture des signaux est la même que ``shiftOut()`` dans les chapitres précédents, sauf qu'ici nous devons écrire un nombre binaire de 16 bits à la fois.

La boucle principale appelle ``shiftOut()`` deux fois, écrit deux nombres binaires de 8 bits, puis les envoie au bus pour afficher un motif.

Cependant, puisque les LED dans la matrice utilisent des pôles communs, contrôler plusieurs lignes/colonnes en même temps entraînera des interférences. 
Il est donc nécessaire d'activer une colonne (ou une ligne) à la fois, de boucler 8 fois, et d'utiliser le principe de rémanence visuelle pour permettre à l'œil humain de fusionner 8 motifs en un seul.

.. code-block:: arduino

   for(int num = 0; num <=8; num++)
   {
      digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
      shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
      shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
      //return the latch pin high to signal chip that it 
      //no longer needs to listen for information
      digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
   }

Dans cet exemple, la fonction principale intègre une boucle ``for``. Lorsque ``i`` vaut 1, 
seule la première ligne est activée (le chip de contrôle reçoit la valeur ``0x80``) et l'image de la première ligne est écrite. 

Quand ``i`` vaut 2, la deuxième ligne est activée (le chip reçoit ``0x40``) et l'image de la seconde ligne est écrite. Et ainsi de suite pour 8 sorties.


**En savoir plus**

Essayez de remplacer ``datArray`` par les tableaux suivants et voyez ce qui apparaît !

.. code-block:: arduino

   int datArray1[] = {0xFF,0xEF,0xC7,0xAB,0xEF,0xEF,0xEF,0xFF};
   int datArray2[] = {0xFF,0xEF,0xEF,0xEF,0xAB,0xC7,0xEF,0xFF};
   int datArray3[] = {0xFF,0xEF,0xDF,0x81,0xDF,0xEF,0xFF,0xFF};
   int datArray4[] = {0xFF,0xF7,0xFB,0x81,0xFB,0xF7,0xFF,0xFF};
   int datArray5[] = {0xFF,0xBB,0xD7,0xEF,0xD7,0xBB,0xFF,0xFF};
   int datArray6[] = {0xFF,0xFF,0xF7,0xEB,0xDF,0xBF,0xFF,0xFF};

Ou, essayez de créer vos propres graphiques.
