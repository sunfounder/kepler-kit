.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_led:

LED
==========

|img_led|

La diode électroluminescente (LED) est un composant semi-conducteur capable de convertir l'énergie électrique en énergie lumineuse grâce aux jonctions PN. Selon la longueur d'onde, elle peut être classée en diode laser, diode émettant des infrarouges, et diode émettant de la lumière visible, généralement appelée LED.

La diode a une conductivité unidirectionnelle, ce qui signifie que le courant circulera comme indiqué par la flèche dans le symbole de circuit. Il faut fournir une alimentation positive à l'anode et une alimentation négative à la cathode pour que la LED s'allume.

|img_led_symbol|

Une LED possède deux broches : la plus longue est l'anode et la plus courte est la cathode. Faites attention à ne pas les connecter à l'envers. Il existe une chute de tension fixe en polarisation directe dans la LED, ce qui empêche de la connecter directement au circuit, car la tension d'alimentation pourrait dépasser cette chute de tension et endommager la LED. La tension de polarisation directe des LED rouges, jaunes et vertes est de 1,8 V, tandis que celle de la LED blanche est de 2,6 V. La plupart des LED supportent un courant maximum de 20 mA, il est donc nécessaire de connecter une résistance de limitation de courant en série.

La formule pour déterminer la valeur de la résistance est la suivante :

    R = (Vsupply – VD)/I

**R** représente la valeur de la résistance de limitation de courant, **Vsupply** la tension d'alimentation, **VD** la chute de tension et **I** le courant de fonctionnement de la LED.

Voici une introduction détaillée sur les LED : `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

.. **Exemple**

.. * :ref:`Hello, Breadboard!` (pour les utilisateurs de MicroPython)
.. * :ref:`fading_led_micropython` (pour les utilisateurs de MicroPython)
.. * :ref:`fading_led_arduino` (pour les utilisateurs de C/C++(Arduino))
.. * :ref:`hello_led_arduino` (pour les utilisateurs de C/C++(Arduino))

**Exemple**

* :ref:`py_led` (pour les utilisateurs de MicroPython)
* :ref:`py_fade` (pour les utilisateurs de MicroPython)
* :ref:`py_alarm_lamp` (pour les utilisateurs de MicroPython)
* :ref:`py_traffic_light` (pour les utilisateurs de MicroPython)
* :ref:`py_reversing_aid` (pour les utilisateurs de MicroPython)
* :ref:`ar_led` (pour les utilisateurs d'Arduino)
* :ref:`ar_fade` (pour les utilisateurs d'Arduino)
* :ref:`per_blink` (pour les utilisateurs de Piper Make)
* :ref:`per_button` (pour les utilisateurs de Piper Make)
* :ref:`per_service_bell` (pour les utilisateurs de Piper Make)
* :ref:`per_reversing_system` (pour les utilisateurs de Piper Make)
* :ref:`per_reaction_game` (pour les utilisateurs de Piper Make)
