.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux démonstrations exclusives.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_pa_buz:

3.2 Tonalité Personnalisée
==========================================


Nous avons utilisé un buzzer actif dans le projet précédent, cette fois nous allons utiliser un buzzer passif.

Comme le buzzer actif, le buzzer passif utilise également le phénomène d'induction électromagnétique pour fonctionner. La différence est qu'un buzzer passif n'a pas de source d'oscillation, il ne produira donc pas de bip si des signaux continus (DC) sont utilisés.
Cependant, cela permet au buzzer passif de régler sa propre fréquence d'oscillation et de produire différentes notes telles que "do, ré, mi, fa, sol, la, si".

Faisons émettre une mélodie au buzzer passif !

* :ref:`cpn_buzzer`

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
        - Buzzer passif :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Schéma**

|sch_buzzer|

Lorsque la sortie GP15 est élevée, après la résistance de limitation de courant de 1K (pour protéger le transistor), le S8050 (transistor NPN) va conduire, ce qui permettra au buzzer de sonner.

Le rôle du S8050 (transistor NPN) est d'amplifier le courant et de rendre le son du buzzer plus fort. En effet, vous pouvez également connecter directement le buzzer à GP15, mais vous constaterez que le son du buzzer est plus faible.

**Câblage**

|img_buzzer|

Deux buzzers sont inclus dans le kit, nous utilisons un buzzer passif (celui avec un PCB exposé à l'arrière).

Le buzzer nécessite un transistor pour fonctionner, ici nous utilisons le S8050.

|wiring_buzzer|

.. 1. Connectez 3V3 et GND du Pico W au bus d'alimentation de la breadboard.
.. #. Connectez la broche positive du buzzer au bus d'alimentation positif.
.. #. Connectez la broche cathodique du buzzer au **collecteur** du transistor.
.. #. Connectez la **base** du transistor à la broche GP15 via une résistance de 1kΩ.
.. #. Connectez l'**émetteur** du transistor au bus d'alimentation négatif.

**Code**

.. note::

    * Ouvrez le fichier ``3.2_custom_tone.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    tone(buzzer,440,250)
    utime.sleep_ms(500)
    tone(buzzer,494,250)
    utime.sleep_ms(500)
    tone(buzzer,523,250)

**Comment ça marche ?**

Si le buzzer passif reçoit un signal numérique, il ne pourra que faire vibrer la membrane sans produire de son.

Nous utilisons donc la fonction ``tone()`` pour générer le signal PWM permettant au buzzer passif de sonner.

Cette fonction prend trois paramètres :

* **pin**, la broche GPIO qui contrôle le buzzer.
* **frequency**, la tonalité du buzzer est déterminée par la fréquence ; plus la fréquence est élevée, plus la tonalité est aiguë.
* **duration**, la durée de la note.

Nous utilisons la fonction ``duty_u16()`` pour régler le cycle de service à 30000 (environ 50%). Cela peut être d'autres valeurs, tant qu'il s'agit de générer un signal électrique discontinu pour provoquer une oscillation.

**En savoir plus**

Nous pouvons simuler des tonalités spécifiques en fonction des fréquences fondamentales du piano, afin de jouer un morceau complet.

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_



.. note::

    * Ouvrez le fichier ``3.2_custom_tone_2.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    NOTE_C4 = 262
    NOTE_G3 = 196
    NOTE_A3 = 220
    NOTE_B3 = 247

    melody =[NOTE_C4,NOTE_G3,NOTE_G3,NOTE_A3,NOTE_G3,NOTE_B3,NOTE_C4]

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    for note in melody:
        tone(buzzer,note,250)
        utime.sleep_ms(150)
