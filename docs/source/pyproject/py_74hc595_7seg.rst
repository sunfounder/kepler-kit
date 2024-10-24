.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_74hc_7seg:

5.2 Affichage de Nombres
===========================

Les affichages 7 segments sont présents partout dans la vie quotidienne.
Par exemple, sur un climatiseur, il peut afficher la température ; sur un panneau de signalisation, il peut indiquer un décompte.

L'affichage 7 segments est essentiellement un dispositif constitué de 8 LED, dont 7 LED en forme de bande forment un "8", et une petite LED en pointillé sert de point décimal. Ces LED sont marquées a, b, c, d, e, f, g et dp. Elles ont leurs propres broches d'anode et partagent des cathodes communes. Leurs positions sont illustrées dans l'image ci-dessous.

|img_7seg_cathode|

Cela signifie qu'il doit être contrôlé par 8 signaux numériques simultanément pour fonctionner pleinement, et le 74HC595 peut le faire.

* :ref:`cpn_7_segment`

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

Vous pouvez également les acheter séparément avec les liens ci-dessous :


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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schéma**

|sch_74hc_7seg|

Le principe de câblage est essentiellement le même que pour :ref:`py_74hc_led`, la seule différence étant que Q0-Q7 sont connectés aux broches a ~ g de l'affichage 7 segments.

.. list-table:: Câblage
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segment Display
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**Câblage**

.. 1. Connectez 3V3 et GND du Pico W au bus d'alimentation de la breadboard.
.. #. Insérez le 74HC595 au-dessus de la coupure centrale de la breadboard.
.. #. Connectez la broche GP0 du Pico W à la broche DS (broche 14) du 74HC595 avec un fil de connexion.
.. #. Connectez la broche GP1 du Pico W à la broche STcp (broche 12) du 74HC595.
.. #. Connectez la broche GP2 du Pico W à la broche SHcp (broche 11) du 74HC595.
.. #. Connectez la broche VCC (broche 16) et MR (broche 10) du 74HC595 au bus d'alimentation positif.
.. #. Connectez la broche GND (broche 8) et CE (broche 13) du 74HC595 au bus d'alimentation négatif.
.. #. Insérez l'afficheur LED Segment sur la breadboard et connectez une résistance de 220Ω en série avec la broche GND au bus d'alimentation négatif.
.. #. Suivez le tableau ci-dessous pour connecter le 74hc595 et l'affichage LED Segment.

|wiring_74hc_7seg|

**Code**

.. note::

    * Ouvrez le fichier ``5.2_number_display.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)
        
    while True:
        for num in range(10):
            hc595_shift(SEGCODE[num])
            time.sleep_ms(500)

Lorsque le programme est en cours d'exécution, vous verrez l'afficheur LED Segment afficher les chiffres de 0 à 9 en séquence.

**Comment ça fonctionne ?**

``hc595_shift()`` fait en sorte que le 74HC595 émette 8 signaux numériques.
Il envoie le dernier bit du nombre binaire à Q0, et le premier bit à Q7. En d'autres termes, écrire le nombre binaire "00000001" fera que Q0 émette un niveau haut et Q1~Q7 un niveau bas.

Supposons que l'affichage 7 segments affiche le chiffre "1", il faut envoyer un niveau haut aux broches b, c, et un niveau bas aux broches a, d, e, f, g et dp.

|img_1_segment|

C'est-à-dire que le nombre binaire "00000110" doit être écrit. Pour plus de lisibilité, nous utiliserons la notation hexadécimale "0x06".

* `Hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_

* `BinaryHex Converter <https://www.binaryhexconverter.com/binary-to-hex-converter>`_

De même, nous pouvons faire en sorte que l'afficheur LED Segment affiche d'autres chiffres de la même manière. Le tableau suivant montre les codes correspondants à ces chiffres.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Chiffres
        - Code Binaire
        - Code Hexadécimal
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f

Écrivez ces codes dans ``hc595_shift()`` pour faire en sorte que l'afficheur LED Segment affiche les chiffres correspondants.
