.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ar_pa_buz:


3.2 - Tonalité personnalisée
==========================================

Dans le projet précédent, nous avons utilisé un buzzer actif. Cette fois, nous utiliserons un buzzer passif.

Tout comme le buzzer actif, le buzzer passif fonctionne grâce au phénomène d'induction 
électromagnétique. La différence réside dans le fait qu'un buzzer passif ne possède pas 
de source d'oscillation intégrée, il ne produit donc pas de son avec des signaux continus DC. 
Cependant, cela permet au buzzer passif de modifier sa fréquence d'oscillation et d'émettre 
différentes notes comme "do, ré, mi, fa, sol, la, si".

Faisons jouer une mélodie au buzzer passif !

* :ref:`Buzzer`

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
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Buzzer passif :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schéma**

|sch_buzzer|

Lorsque la sortie de GP15 est haute, après le passage par la résistance de limitation de courant de 1K (pour protéger le transistor), le S8050 (transistor NPN) conduit, permettant ainsi au buzzer de sonner.

Le rôle du S8050 (transistor NPN) est d'amplifier le courant et de rendre le son du buzzer plus fort. En fait, vous pouvez également connecter le buzzer directement à GP15, mais le son sera plus faible.


**Câblage**

|img_buzzer|

Deux buzzers sont inclus dans le kit, nous utilisons un buzzer passif (celui avec le PCB visible à l'arrière).

Le buzzer nécessite un transistor pour fonctionner, nous utilisons ici le S8050.

|wiring_buzzer|

**Code**


.. note::

    * Vous pouvez ouvrir le fichier ``3.2_custom_tone.ino`` sous le chemin ``kepler-kit-main/arduino/3.2_custom_tone``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.




.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/69c55e56-9eeb-46bb-b3a8-b354c500cc17/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>



**Comment ça fonctionne ?**

Si un signal numérique est appliqué au buzzer passif, il ne fera que déplacer la membrane sans produire de son.

Nous utilisons donc la fonction ``tone()`` pour générer le signal PWM permettant au buzzer passif de produire un son.

Cette fonction a trois paramètres :

  * **pin**, le pin GPIO qui contrôle le buzzer.
  * **frequency**, la hauteur du son du buzzer est déterminée par la fréquence ; plus la fréquence est élevée, plus le son est aigu.
  * **duration**, la durée de la tonalité.


* `tone <https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/>`_

**En savoir plus**

Nous pouvons simuler des notes spécifiques en fonction des fréquences fondamentales du piano, afin de jouer une pièce musicale complète.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_

.. note::

    * Vous pouvez ouvrir le fichier ``3.2_custom_tone_2.ino`` sous le chemin ``kepler-kit-main/arduino/3.2_custom_tone_2``. 
    * Ou copiez ce code dans l'**Arduino IDE**.
    * N'oubliez pas de sélectionner la carte (Raspberry Pi Pico) et le port correct avant de cliquer sur le bouton Upload.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f934c785-7204-4972-aae5-01edde3c79cc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>