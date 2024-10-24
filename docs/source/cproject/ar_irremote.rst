.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_irremote:

6.4 - Télécommande IR
================================

Dans l'électronique grand public, les télécommandes sont utilisées pour contrôler des appareils tels que les téléviseurs et les lecteurs DVD.
Dans certains cas, elles permettent aux utilisateurs de manipuler des dispositifs hors de portée, comme les climatiseurs centraux.

Le récepteur IR est un composant avec une photocellule réglée pour recevoir la lumière infrarouge. 
Il est presque toujours utilisé pour la détection des télécommandes - chaque téléviseur et lecteur DVD en possède un à l'avant pour recevoir le signal IR de la télécommande.
À l'intérieur de la télécommande se trouve une LED IR correspondante, qui émet des impulsions IR pour indiquer à la télévision de s'allumer, s'éteindre ou changer de chaîne.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schéma**

|sch_irrecv|

**Câblage**

|wiring_irrecv|

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``6.4_ir_remote_control.ino`` sous le chemin ``kepler-kit-main/arduino/6.4_ir_remote_control``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * Ensuite, sélectionnez la carte Raspberry Pi Pico et le port correct avant de cliquer sur le bouton **Upload**.
    * La bibliothèque ``IRremote`` est utilisée ici, vous pouvez l'installer depuis le **Gestionnaire de bibliothèques**.

      .. image:: img/lib_ir.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

La nouvelle télécommande possède un morceau de plastique à l'extrémité pour isoler la batterie à l'intérieur. Vous devez retirer ce morceau de plastique pour alimenter la télécommande lors de son utilisation.
Une fois le programme en cours d'exécution, lorsque vous appuyez sur la télécommande, le Moniteur Série affichera la touche que vous avez pressée.


**Comment ça fonctionne ?**

Ce code est conçu pour fonctionner avec une télécommande infrarouge (IR) en utilisant la bibliothèque ``IRremote``. Voici le détail :

#. Inclusion de la bibliothèque et définition des constantes. Tout d'abord, la bibliothèque IRremote est incluse, et le numéro de broche pour le récepteur IR est défini sur 2.

   .. code-block:: cpp
 
     #include <IRremote.h>
     const int IR_RECEIVE_PIN = 17;

#. Initialise la communication série à un débit de 9600 bauds. Initialise le récepteur IR sur la broche spécifiée (``IR_RECEIVE_PIN``) et active le retour LED (si applicable).

   .. code-block:: arduino

       void setup() {
           Serial.begin(9600);                                     // Démarrer la communication série à 9600 bauds
           IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // Démarrer le récepteur IR
       }

#. La boucle s'exécute en continu pour traiter les signaux entrants de la télécommande IR.

   .. code-block:: arduino

      void loop() {
         if (IrReceiver.decode()) {  // Vérifier si le récepteur IR a reçu un signal
            bool result = 0;
            String key = decodeKeyValue(IrReceiver.decodedIRData.command);
            if (key != "ERROR") {
              Serial.println(key);  // Imprimer la commande lisible
              delay(100);
            }
         IrReceiver.resume();  // Préparer le récepteur IR à recevoir le prochain signal
        }
      }

   * Vérifie si un signal IR est reçu et décodé avec succès.
   * Décode la commande IR et la stocke dans ``decodedValue`` en utilisant une fonction personnalisée ``decodeKeyValue()``.
   * Imprime la valeur décodée IR sur le moniteur série.
   * Relance la réception de signal IR pour le prochain signal.

   .. raw:: html

        <br/>

#. Fonction auxiliaire pour mapper les signaux IR reçus aux touches correspondantes

   .. image:: img/ir_key.png
      :align: center
      :width: 80%

   .. code-block:: arduino

      // Fonction pour mapper les signaux IR reçus aux touches correspondantes
      String decodeKeyValue(long result) {
        // Chaque case correspond à une commande IR spécifique
        switch (result) {
          case 0x16:
            return "0";
          case 0xC:
            return "1";
          case 0x18:
            return "2";
          case 0x5E:
            return "3";
          case 0x8:
            return "4";
          case 0x1C:
            return "5";
          case 0x5A:
            return "6";
          case 0x42:
            return "7";
          case 0x52:
            return "8";
          case 0x4A:
            return "9";
          case 0x9:
            return "+";
          case 0x15:
            return "-";
          case 0x7:
            return "EQ";
          case 0xD:
            return "U/SD";
          case 0x19:
            return "CYCLE";
          case 0x44:
            return "PLAY/PAUSE";
          case 0x43:
            return "FORWARD";
          case 0x40:
            return "BACKWARD";
          case 0x45:
            return "POWER";
          case 0x47:
            return "MUTE";
          case 0x46:
            return "MODE";
          case 0x0:
            return "ERROR";
          default:
            return "ERROR";
        }
      }



