.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support expert** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_pico_w:

Raspberry Pi Pico W
=======================================

|pico_w_side|

Le Raspberry Pi Pico W apporte la connectivité sans fil à la gamme de produits 
Raspberry Pi Pico, qui connaît un grand succès. Construit autour de notre 
plateforme RP2040, les produits Pico incarnent nos valeurs de haute performance, 
faible coût et facilité d'utilisation dans le domaine des microcontrôleurs.

Le Raspberry Pi Pico W offre une connexion LAN sans fil 2,4 GHz 802.11 b/g/n avec 
une antenne intégrée et une certification de conformité modulaire. Il peut fonctionner 
en mode station et point d'accès. Un accès complet aux fonctionnalités réseau est disponible pour les développeurs C et MicroPython. Le Pico W associe le RP2040 à 2 Mo de mémoire flash et une puce d'alimentation supportant des tensions d'entrée de 1,8 à 5,5V. Il dispose de 26 broches GPIO, dont trois peuvent fonctionner comme entrées analogiques, sur des pads traversants de 0,1" avec des bords à trous métallisés. Le Pico W est disponible à l'unité ou en rouleaux de 480 unités pour un assemblage automatisé.






Caractéristiques
----------------------

* Format 21 mm x 51 mm
* Microcontrôleur RP2040 conçu par Raspberry Pi au Royaume-Uni
* Processeur double cœur Arm Cortex-M0+, horloge flexible jusqu'à 133 MHz
* 264kB de SRAM intégrée
* 2MB de flash QSPI embarquée
* Réseau sans fil LAN 2.4GHz 802.11n
* 26 broches GPIO multifonctions, dont 3 entrées analogiques
* 2 x UART, 2 x contrôleurs SPI, 2 x contrôleurs I2C, 16 x canaux PWM
* 1 x contrôleur USB 1.1 et PHY, avec support hôte et périphérique
* 8 x machines d'état I/O programmable (PIO) pour le support de périphériques personnalisés
* Alimentation supportée : 1,8-5,5V DC
* Température de fonctionnement : -20°C à +70°C
* Module à bords métallisés permettant une soudure directe aux cartes porteuses
* Programmation par glisser-déposer via stockage de masse USB
* Modes de sommeil et de repos à faible consommation
* Horloge interne précise
* Capteur de température
* Bibliothèques accélérées pour les calculs entiers et à virgule flottante intégrées

Les broches du Pico
--------------------------

|pico_pin|


.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - Nom
        - Description
        - Fonction
    *   - GP0-GP28
        - Broches d'entrée/sortie à usage général
        - Agissent comme entrée ou sortie et n'ont pas de fonction fixe propre
    *   - GND
        - Masse 0 volt
        - Plusieurs broches GND autour du Pico W pour faciliter le câblage.
    *   - RUN
        - Active ou désactive votre Pico
        - Permet de démarrer ou arrêter votre Pico W depuis un autre microcontrôleur.
    *   - GPxx_ADCx
        - Entrée/sortie à usage général ou entrée analogique
        - Peut être utilisée comme entrée analogique ou numérique, mais pas les deux en même temps.
    *   - ADC_VREF
        - Référence de tension pour le convertisseur analogique-numérique (ADC)
        - Broche spéciale qui définit une tension de référence pour les entrées analogiques.
    *   - AGND
        - Masse 0 volt pour le convertisseur analogique-numérique (ADC)
        - Connexion de masse spéciale à utiliser avec la broche ADC_VREF.
    *   - 3V3(O)
        - Alimentation 3,3 volts
        - Source de puissance 3,3V, la même tension que votre Pico W utilise en interne, générée à partir de l'entrée VSYS.
    *   - 3V3(E)
        - Active ou désactive l'alimentation
        - Permet d'allumer ou éteindre l'alimentation 3V3(O), peut également éteindre votre Pico W.
    *   - VSYS
        - Alimentation 2-5 volts
        - Broche directement connectée à l'alimentation interne de votre Pico, ne peut être désactivée sans éteindre le Pico W.
    *   - VBUS
        - Alimentation 5 volts
        - Source de 5 V prise depuis le port micro USB de votre Pico, utilisée pour alimenter du matériel nécessitant plus de 3,3 V.

Le meilleur endroit pour trouver tout ce dont vous avez besoin pour commencer avec votre Raspberry Pi Pico W est `ici <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`_

Ou vous pouvez cliquer sur les liens ci-dessous :

* `Raspberry Pi Pico W product brief <https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf>`_
* `Raspberry Pi Pico W datasheet <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf>`_
* `Getting started with Raspberry Pi Pico: C/C++ development <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `API-level Doxygen documentation for the Raspberry Pi Pico C/C++ SDK <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2040 datasheet <https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf>`_
* `Hardware design with RP2040 <https://datasheets.raspberrypi.org/rp2040/hardware-design-with-rp2040.pdf>`_
* `Raspberry Pi Pico W design files <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEP file <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
