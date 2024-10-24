.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_rfid:

6.5 - Identification par Radiofréquence (RFID)
===========================================================

L'identification par radiofréquence (RFID) désigne les technologies qui utilisent la communication sans fil entre un objet (ou étiquette) et un dispositif d'interrogation (ou lecteur) pour suivre et identifier automatiquement ces objets. La portée de transmission de l'étiquette est limitée à quelques mètres du lecteur. Une ligne de vue directe entre le lecteur et l'étiquette n'est pas forcément requise.

La plupart des étiquettes contiennent au moins un circuit intégré (IC) et une antenne. 
La puce stocke des informations et gère la communication par radiofréquence (RF) avec le lecteur. Les étiquettes passives ne disposent pas de source d'énergie indépendante et dépendent d'un signal électromagnétique externe, fourni par le lecteur, pour alimenter leurs opérations. 
Les étiquettes actives, quant à elles, contiennent une source d'énergie indépendante, comme une batterie. Elles peuvent donc avoir une capacité accrue de traitement, de transmission et une portée plus étendue.

* :ref:`cpn_mfrc522`

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants.

Il est pratique d'acheter un kit complet, voici le lien :

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Schéma**

|sch_rfid|

**Câblage**

|wiring_rfid|

**Code**

.. note::

   * La bibliothèque ``MFRC522`` est utilisée ici, vous pouvez l'installer depuis le **Library Manager**.

      .. image:: img/lib_mfrc522.png

La fonction principale est divisée en deux :

* ``6.5_rfid_write`` pour écrire des informations sur la carte (ou la clé).

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b4f9156a-711a-442c-8271-329847e808dc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  Après exécution, vous pourrez entrer un message dans le moniteur série, en terminant par ``#``, puis écrire ce message sur la carte en la plaçant (ou la clé) près du module MFRC522.

* ``6.5_rfid_read`` pour lire les informations de la carte (ou de la clé).

  .. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/df57b5cb-9162-4b4b-b28a-7f02363885c9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

  Après exécution, vous pourrez lire le message stocké sur la carte (ou la clé).

**Comment ça marche ?**

.. code-block:: arduino

    #include <MFRC522.h>

    #define RST_PIN         9
    #define SS_PIN          17

    MFRC522 mfrc522(SS_PIN, RST_PIN);

Tout d'abord, instanciez la classe ``MFRC522()``.

Pour simplifier l'utilisation, la bibliothèque ``MFRC522`` est encapsulée avec les fonctions suivantes.

* ``void simple_mfrc522_init()`` : Démarre la communication SPI et initialise le module mfrc522.
* ``void simple_mfrc522_get_card()`` : Suspend le programme jusqu'à ce que la carte (ou la clé) soit détectée, puis imprime l'UID de la carte et le type de PICC.
* ``void simple_mfrc522_write(String text)`` : Écrit une chaîne de caractères sur la carte (ou la clé).
* ``void simple_mfrc522_write(byte* buffer)`` : Écrit des informations sur la carte (ou la clé), généralement depuis le port série.
* ``void simple_mfrc522_write(byte section, String text)`` : Écrit une chaîne sur un secteur spécifique. ``section`` est réglé à 0 pour écrire sur les secteurs 1-2 ; ``section`` est réglé à 1 pour écrire sur les secteurs 3-4.
* ``void simple_mfrc522_write(byte section, byte* buffer)`` : Écrit des informations sur un secteur spécifique, généralement depuis le port série. ``section`` réglé à 0, écrit sur les secteurs 1-2 ; ``section`` réglé à 1, écrit sur les secteurs 3-4.
* ``String simple_mfrc522_read()`` : Lit les informations de la carte (ou clé), retourne une chaîne de caractères.
* ``String simple_mfrc522_read(byte section)`` : Lit les informations d'un secteur spécifique, retourne une chaîne. ``section`` est réglé à 0, lit les secteurs 1-2 ; ``section`` est réglé à 1, lit les secteurs 3-4.

Dans l'exemple ``6.5_rfid_write.ino``, la fonction ``Serial.readBytesUntil()`` est utilisée, c'est une méthode courante d'entrée série.

* `Serial.readBytesUntil <https://www.arduino.cc/reference/en/language/functions/communication/serial/readbytesuntil/>`_