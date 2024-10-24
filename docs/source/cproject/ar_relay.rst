.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_relay:

2.16 - Contrôler un autre circuit
======================================

Dans notre vie quotidienne, nous appuyons sur un interrupteur pour allumer ou éteindre une lampe. 
Mais que faire si vous voulez contrôler la lampe avec le Pico W pour qu'elle s'éteigne automatiquement après dix minutes ?

Un relais peut vous aider à réaliser cette idée.

Un relais est en réalité un type particulier d'interrupteur, contrôlé par un côté du circuit (généralement un circuit basse tension) et utilisé pour contrôler l'autre côté (généralement un circuit haute tension).
Cela permet de rendre nos appareils ménagers programmables, en les transformant en dispositifs intelligents, voire connectés à Internet.

.. warning::
    La modification d'appareils électriques présente de grands dangers, ne l'essayez pas à la légère, faites-le sous la supervision de professionnels.

* :ref:`cpn_relay`

Ici, nous utilisons un simple circuit alimenté par un module d'alimentation de breadboard comme exemple pour montrer comment le contrôler avec un relais.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Câblage**

Tout d'abord, construisez un circuit basse tension pour contrôler un relais.
La commande du relais nécessite un courant élevé, d'où la nécessité d'un transistor ; ici, nous utilisons le S8050.

|sch_relay_1|

|wiring_relay_1|

Une diode (diode de roue libre) est utilisée ici pour protéger le circuit. Le côté cathode, marqué par la bande argentée, est connecté à l'alimentation, et l'anode est reliée au transistor.

Lorsque la tension d'entrée passe de haut (5V) à bas (0V), le transistor passe de la saturation (amplification, saturation et coupure) à la coupure, et le courant ne peut plus circuler dans la bobine.

Sans cette diode, la bobine produirait une tension auto-induite à ses extrémités, plusieurs fois supérieure à la tension d'alimentation, risquant de brûler les composants. 

Avec la diode ajoutée, la bobine et la diode forment instantanément un nouveau circuit alimenté par l'énergie stockée dans la bobine, ce qui permet de décharger l'excès de tension et de protéger les composants comme les transistors.

* :ref:`cpn_diode`    
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

À ce stade, le programme est prêt à fonctionner, et après exécution, vous entendrez un bruit de "tik tok", qui est le son de la bobine interne du relais qui s'active et se désactive.

Ensuite, connectez les deux extrémités du circuit de charge aux broches 3 et 6 du relais.

..(Prenons le circuit simple alimenté par le module d'alimentation de breadboard décrit dans l'article précédent comme exemple.)

|sch_relay_2|

|wiring_relay_2|

À ce stade, le relais pourra contrôler l'état du circuit de charge.

**Code**

.. note::

    * Vous pouvez ouvrir le fichier ``2.16_relay.ino`` sous le chemin ``kepler-kit-main/arduino/2.16_relay``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/3be98f10-8223-49f2-8238-2acc53ebbf80/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Lorsque le code est exécuté, le relais basculera l'état de fonctionnement du circuit contrôlé toutes les deux secondes.
Vous pouvez commenter manuellement certaines lignes pour mieux comprendre la correspondance entre le circuit du relais et celui de la charge.


**En savoir plus**


La broche 3 du relais est normalement ouverte et ne se ferme que lorsque la bobine du contacteur fonctionne ; la broche 4 est normalement fermée et se ferme lorsque la bobine est alimentée.
La broche 1 est connectée à la broche 6 et constitue le terminal commun du circuit de charge.

En déplaçant une extrémité du circuit de charge de la broche 3 à la broche 4, vous obtiendrez un état de fonctionnement opposé.
