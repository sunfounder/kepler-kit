.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Plongez dans le monde du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_servo:

3.7 Servomoteur Oscillant
=================================

Dans ce kit, en plus de la LED et du buzzer passif, il y a également un dispositif contrôlé par signal PWM, le Servomoteur.

Le servomoteur est un dispositif de positionnement (angle), adapté aux systèmes de contrôle nécessitant des changements constants d'angle tout en pouvant le maintenir. Il est largement utilisé dans les jouets télécommandés haut de gamme, comme les avions, modèles de sous-marins, et robots télécommandés.

Maintenant, essayons de faire osciller le servomoteur !

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schéma**

|sch_servo|

**Câblage**

|wiring_servo|

* Le fil orange est le signal et est connecté à GP15.
* Le fil rouge est le VCC et est connecté à VBUS (5V).
* Le fil marron est la masse (GND) et est connecté à GND.

.. 1. Fixez le bras du servomoteur sur l'axe de sortie. Si nécessaire, fixez-le avec des vis.
.. #. Connectez **VBUS** (et non 3V3) et GND du Pico W au bus d'alimentation de la breadboard.
.. #. Connectez le fil rouge du servomoteur au bus d'alimentation positif avec un cavalier.
.. #. Connectez le fil jaune du servomoteur à la broche GP15 avec un fil de connexion.
.. #. Connectez le fil marron du servomoteur au bus d'alimentation négatif avec un fil de connexion.

**Code**

.. note::

    * Ouvrez le fichier ``3.7_swinging_servo.py`` sous le chemin ``kepler-kit-main/micropython`` ou copiez ce code dans Thonny, puis cliquez sur "Run Current Script" ou appuyez simplement sur F5 pour l'exécuter.

    * N'oubliez pas de sélectionner l'interpréteur "MicroPython (Raspberry Pi Pico)" en bas à droite.

    * Pour des tutoriels détaillés, veuillez consulter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servo_write(pin,angle):
        pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        pin.duty_u16(duty)

    while True:
        for angle in range(180):
            servo_write(servo,angle)
            utime.sleep_ms(20)
        for angle in range(180,-1,-1):
            servo_write(servo,angle)
            utime.sleep_ms(20)


Lorsque le programme est en cours d'exécution, vous verrez le bras du servomoteur osciller d'avant en arrière de 0° à 180°.

Le programme continuera de fonctionner grâce à la boucle ``while True``, il faudra appuyer sur le bouton Arrêter pour mettre fin au programme.

**Comment ça marche ?**

Nous avons défini la fonction ``servo_write()`` pour faire fonctionner le servomoteur.

Cette fonction a deux paramètres :

* ``pin``, la broche GPIO qui contrôle le servomoteur.
* ``Angle``, l'angle de sortie de l'axe.

Dans cette fonction, ``interval_mapping()`` est appelé pour mapper la plage d'angle de 0 ~ 180 à la plage de largeur d'impulsion de 0.5 ~ 2.5ms.

.. code-block:: python

    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)

Pourquoi 0.5~2.5 ? Cela est déterminé par le mode de fonctionnement du servomoteur.

:ref:`cpn_servo`

Ensuite, la largeur d'impulsion est convertie de la période au rapport cyclique. Comme ``duty_u16()`` ne peut pas accepter de décimales (la valeur ne peut pas être de type float), nous avons utilisé ``int()`` pour forcer la conversion en type entier.

.. code-block:: python

    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))



Enfin, nous écrivons la valeur du rapport cyclique dans ``duty_u16()``.
