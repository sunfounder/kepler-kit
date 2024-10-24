.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Explorez plus en profondeur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_light_theremin:

7.1 Theremin lumineux
=========================

Le Theremin est un instrument de musique électronique qui ne nécessite aucun contact physique. En fonction de la position de la main du joueur, il produit différents sons.

Sa partie de contrôle est généralement composée de deux antennes métalliques qui détectent la position des mains du thereministe : l'une contrôle les oscillateurs et l'autre le volume. Les signaux électriques émis par le theremin sont amplifiés et envoyés à un haut-parleur.

Nous ne pouvons pas reproduire exactement le même instrument avec la Pico W, mais nous pouvons utiliser une photo-résistance et un buzzer passif pour obtenir un effet similaire.

* `Theremin - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

**Composants requis**

Pour ce projet, nous aurons besoin des composants suivants. 

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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Buzzer passif :ref:`cpn_buzzer`
        - 1
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schéma**

|sch_light_theremin|

Avant de commencer le projet, passez votre main de haut en bas au-dessus de la photo-résistance pour calibrer la plage d'intensité lumineuse. La LED connectée au GP16 est utilisée pour indiquer la période de calibration : la LED s'allume pour signaler le début de la calibration et s'éteint pour indiquer la fin.

Lorsque GP15 émet un niveau haut, le transistor S8050 (NPN) conduit et le buzzer passif commence à émettre un son.

Plus la lumière est forte, plus la valeur de GP28 est faible ; à l'inverse, elle est plus élevée lorsque la lumière est plus faible.
En programmant la valeur de la photo-résistance pour affecter la fréquence du buzzer passif, on peut simuler un dispositif photosensible.


**Câblage**

|wiring_light_theremin|


**Code**

.. note::

    * Ouvrez le fichier ``7.1_light_theremin.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite. 

    * Pour des tutoriels détaillés, veuillez vous référer à :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # Initialiser la LED, la photo-résistance et le buzzer
    led = machine.Pin(16, machine.Pin.OUT)  # LED sur la broche 16
    photoresistor = machine.ADC(28)  # Photo-résistance sur la broche ADC 28
    buzzer = machine.PWM(machine.Pin(15))  # Buzzer sur la broche 15 avec PWM

    # Variables pour stocker les valeurs maximales et minimales de la lumière pour la calibration
    light_low = 65535 
    light_high = 0 

    # Fonction pour mapper une plage de valeurs à une autre
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Fonction pour jouer une tonalité sur le buzzer à une fréquence spécifiée pendant une durée définie
    def tone(pin, frequency, duration):
        pin.freq(frequency)  # Définir la fréquence du buzzer
        pin.duty_u16(30000)  # Régler le cycle de service à environ 50%
        utime.sleep_ms(duration)  # Jouer la tonalité pendant la durée spécifiée
        pin.duty_u16(0)  # Éteindre la tonalité en réglant le cycle de service à 0

    # Calibrer la photo-résistance en trouvant les valeurs maximales et minimales de la lumière sur 5 secondes
    timer_init_start = utime.ticks_ms()  # Obtenir l'heure actuelle (heure de début)
    led.value(1)  # Allumer la LED pour indiquer que la calibration est en cours
    while utime.ticks_diff(utime.ticks_ms(), timer_init_start) < 5000:  # Effectuer la calibration pendant 5 secondes
        light_value = photoresistor.read_u16()  # Lire la valeur de la lumière de la photo-résistance
        if light_value > light_high:  # Suivre la valeur maximale de la lumière
            light_high = light_value
        if light_value < light_low:  # Suivre la valeur minimale de la lumière
            light_low = light_value
    led.value(0)  # Éteindre la LED après la calibration

    # Boucle principale pour lire les niveaux de lumière et jouer les tonalités correspondantes
    while True:
        light_value = photoresistor.read_u16()  # Lire la valeur actuelle de la lumière de la photo-résistance
        pitch = int(interval_mapping(light_value, light_low, light_high, 50, 6000))  # Mapper la valeur de la lumière à une plage de tonalités
        if pitch > 50:  # Jouer les tonalités uniquement si la fréquence est au-dessus d'un seuil minimal
            tone(buzzer, pitch, 20)  # Jouer la tonalité correspondante pendant 20ms
        utime.sleep_ms(10)  # Petit délai entre les lectures


Dès que le programme se lance, la LED s'allume et vous aurez cinq secondes pour calibrer la plage de détection de la photo-résistance.

Cela est nécessaire en raison des différentes conditions d'éclairage auxquelles nous pouvons être confrontés (par exemple, intensités lumineuses différentes à midi et au crépuscule), ainsi que de la hauteur de votre main au-dessus de la photo-résistance. Vous devez définir la hauteur maximale et minimale de votre main par rapport à la photo-résistance, qui déterminera également la manière dont vous jouerez de l'instrument.

Après cinq secondes, la LED s'éteindra, et vous pourrez alors agiter votre main au-dessus de la photo-résistance et commencer à jouer.
