.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_lcd:

3.4 - Affichage à Cristaux Liquides
========================================

Le LCD1602 est un afficheur à cristaux liquides de type caractère, 
capable d'afficher 32 (16*2) caractères simultanément.

Comme nous le savons, bien que les écrans LCD et d'autres dispositifs 
d'affichage enrichissent grandement l'interaction homme-machine, ils 
partagent un point faible commun. Lorsqu'ils sont connectés à un contrôleur, 
plusieurs E/S seront occupées, limitant ainsi les autres fonctions du contrôleur. 
Par conséquent, le LCD1602 avec un bus I2C a été développé pour résoudre ce problème.

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_


|pin_i2c|

Nous utiliserons ici l'interface I2C0 pour contrôler le LCD1602 et afficher du texte.

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants. 

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schéma**

|sch_lcd_ar|

**Câblage**

|wiring_lcd_ar|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``3.4_liquid_crystal_display.ino`` sous le chemin ``kepler-kit-main/arduino/3.4_liquid_crystal_display``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * Sélectionnez ensuite la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton Upload.
    * La bibliothèque ``LiquidCrystal I2C`` est utilisée ici, vous pouvez l'installer depuis le **Library Manager**.

      .. image:: img/lib_i2c_lcd.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1f464967-5937-473a-8a0d-8e4577c85e7d/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Après avoir téléchargé le code avec succès, vous verrez “SunFounder”, “Hello World” s'afficher sur le LCD1602 I2C.

.. note:: 
    Si le code et le câblage sont corrects mais que l'affichage reste vide, tournez le potentiomètre à l'arrière pour augmenter le contraste.

**Comment ça fonctionne ?**

En utilisant la bibliothèque ``LiquidCrystal_I2C.h``, vous pouvez facilement piloter le LCD. 

.. code-block:: arduino

    #include "LiquidCrystal_I2C.h"

**Fonctions de la bibliothèque**

.. code-block:: arduino

    LiquidCrystal_I2C(uint8_t lcd_Addr,uint8_t lcd_cols,uint8_t lcd_rows)

Crée une nouvelle instance de la classe ``LiquidCrystal_I2C`` représentant un LCD particulier connecté à votre carte Arduino.

- **lcd_AddR** : L'adresse du LCD est par défaut 0x27.
- **lcd_cols** : Le LCD1602 dispose de 16 colonnes.
- **lcd_rows** : Le LCD1602 dispose de 2 lignes.


.. code-block:: arduino

    void init()

Initialise le LCD.

.. code-block:: arduino

    void backlight()

Allume le rétroéclairage (optionnel).

.. code-block:: arduino

    void nobacklight()

Éteint le rétroéclairage (optionnel).

.. code-block:: arduino

    void display()

Allume l'affichage du LCD.

.. code-block:: arduino

    void nodisplay()

Éteint rapidement l'affichage du LCD.

.. code-block:: arduino

    void clear()

Efface l'affichage, et positionne le curseur à zéro.

.. code-block:: arduino

    void setCursor(uint8_t col,uint8_t row)

Positionne le curseur aux coordonnées col,row.

.. code-block:: arduino

    void print(data,BASE)

Affiche du texte sur le LCD.

- **data** : Les données à afficher (char, byte, int, long, ou string).

- **BASE (optionnel)** : La base pour afficher les nombres : BIN pour binaire (base 2), DEC pour décimal (base 10), OCT pour octal (base 8), HEX pour hexadécimal (base 16).




**En savoir plus**

Téléchargez le code sur le Pico W, le contenu que vous saisissez dans le moniteur série sera imprimé sur le LCD.

.. note::

   * Vous pouvez ouvrir le fichier ``3.4_liquid_crystal_display_2.ino`` sous le chemin ``kepler-kit-main/arduino/3.4_liquid_crystal_display_2``. 
   * Ou copiez ce code dans l'**Arduino IDE**.
   * N'oubliez pas de sélectionner la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631e0380-d594-4a8b-9bac-eb0688079b97/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

En plus de lire les données provenant des composants électroniques, le Pico W peut lire les données 
saisies dans le moniteur de port série, et vous pouvez utiliser ``Serial.read()`` comme contrôleur 
pour l'expérience de circuit.

Lancez la communication série dans ``setup()`` et définissez le débit de données à 9600.

.. code-block:: arduino

    Serial.begin(9600);

L'état du moniteur de port série est vérifié dans ``loop()``, et le traitement des informations ne se fera que lorsque les données seront reçues.

.. code-block:: arduino

    if (Serial.available() > 0){}

Effacez l'écran.

.. code-block:: arduino

    lcd.clear();

Lisez la valeur d'entrée dans le moniteur de port série et stockez-la dans la variable incomingByte.

.. code-block:: arduino

    char incomingByte = Serial.read();

Affichez chaque caractère sur le LCD en sautant le caractère de saut de ligne.

.. code-block:: arduino

    while (Serial.available() > 0) {
        char incomingByte=Serial.read();
        if(incomingByte==10){break;}// saute le caractère de saut de ligne
        lcd.print(incomingByte);// affiche chaque caractère sur le LCD  
    } 


* `Serial Read <https://www.arduino.cc/reference/en/language/functions/communication/serial/read/>`_
