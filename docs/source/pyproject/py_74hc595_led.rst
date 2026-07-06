.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_74hc_led:

5.1 Microcircuit - 74HC595
===========================

Un circuit intégré (Integrated Circuit) est un dispositif électronique miniature, représenté par la lettre "IC" dans les circuits.

Un processus spécifique est utilisé pour interconnecter les transistors, résistances, condensateurs, inducteurs et autres composants et circuits nécessaires dans un dispositif, fabriqué sur une ou plusieurs petites plaquettes semi-conductrices ou substrats diélectriques, puis encapsulé dans un boîtier. Cela devient une microstructure dotée des fonctions nécessaires au circuit ; tous les composants sont structurés comme un ensemble, permettant aux composants électroniques de franchir un grand pas vers la miniaturisation, la faible consommation d'énergie, l'intelligence et une haute fiabilité.

Les inventeurs des circuits intégrés sont Jack Kilby (circuits intégrés à base de germanium (Ge)) et Robert Norton Noyce (circuits intégrés à base de silicium (Si)).

Ce kit est équipé d'un circuit intégré, le 74HC595, qui permet de réduire considérablement l'utilisation des broches GPIO.
Il peut remplacer 8 broches pour la sortie de signaux numériques en écrivant un nombre binaire de 8 bits.

* `Binary number - Wikipedia <https://en.wikipedia.org/wiki/Binary_number>`_

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
        - :ref:`cpn_resistor`
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schéma**

|sch_74hc_led|

* Lorsque MR (broche 10) est au niveau haut et OE (broche 13) est au niveau bas, les données sont entrées au front montant de SHcp et se dirigent vers le registre mémoire par le même front montant de SHcp.
* Si les deux horloges sont connectées ensemble, le registre de décalage est toujours une impulsion avant le registre mémoire.
* Le registre mémoire comprend une entrée de décalage série (Ds), une sortie série (Q) et un bouton de réinitialisation asynchrone (niveau bas).
* Le registre mémoire émet un bus avec un parallélisme de 8 bits et dans trois états. 
* Lorsque OE est activé (niveau bas), les données du registre mémoire sont envoyées sur le bus (Q0 ~ Q7).

**Câblage**

.. Le 74HC595 est un circuit intégré à 16 broches avec une encoche semi-circulaire sur un côté (généralement à gauche de l'étiquette). Avec l'encoche orientée vers le haut, ses broches sont affichées dans le schéma ci-dessous.


.. Référez-vous au schéma ci-dessous pour construire le circuit.

|wiring_74hc_led|

.. 1. Connectez 3V3 et GND du Pico W au bus d'alimentation de la breadboard.
.. #. Insérez le 74HC595 au-dessus de la coupure centrale de la breadboard.
.. #. Connectez la broche GP0 du Pico W à la broche DS (broche 14) du 74HC595 avec un fil de connexion.
.. #. Connectez la broche GP1 du Pico W à la broche STcp (broche 12) du 74HC595.
.. #. Connectez la broche GP2 du Pico W à la broche SHcp (broche 11) du 74HC595.
.. #. Connectez la broche VCC (broche 16) et MR (broche 10) du 74HC595 au bus d'alimentation positif.
.. #. Connectez la broche GND (broche 8) et CE (broche 13) du 74HC595 au bus d'alimentation négatif.
.. #. Insérez 8 LED sur la breadboard, et leurs anodes sont respectivement connectées aux broches Q0~Q7 (15, 1, 2, 3, 4, 5, 6, 7) du 74HC595.
.. #. Connectez les cathodes des LED avec une résistance de 220Ω en série au bus d'alimentation négatif.

**Code**

.. note::

    * Ouvrez le fichier ``5.1_microchip_74hc595.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Exécuter le script actuel" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

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

    num = 0

    for i in range(16):
        if i < 8:
            num = (num<<1) + 1
        elif i>=8:
            num = (num & 0b01111111)<<1
        hc595_shift(num)
        print("{:0>8b}".format(num))
        time.sleep_ms(200)

Lorsque le programme est en cours d'exécution, ``num`` sera écrit dans la puce 74HC595 sous forme de nombre binaire à huit bits pour contrôler l'allumage et l'extinction des 8 LED.
Nous pouvons voir la valeur actuelle de ``num`` dans le shell.

**Comment ça fonctionne ?**

``hc595_shift()`` fait en sorte que le 74HC595 émette 8 signaux numériques. Il envoie le dernier bit du nombre binaire à Q0, et le premier bit à Q7. En d'autres termes, écrire le nombre binaire “00000001” fera que Q0 émette un niveau haut et Q1~Q7 un niveau bas.
