.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_buzzer:


Buzzer
=========


Le buzzer est un type de dispositif sonore électronique à structure intégrée, alimenté par une source de courant continu. On le retrouve couramment dans les ordinateurs, imprimantes, photocopieurs, alarmes, jouets électroniques, dispositifs électroniques automobiles, téléphones, minuteurs et autres produits ou appareils à commande vocale.

Les buzzers peuvent être classés en deux catégories : actifs et passifs (voir l'image ci-dessous). En orientant le buzzer de manière à ce que ses broches soient dirigées vers le haut, vous verrez que celui avec une carte de circuit imprimé verte est un buzzer passif, tandis que celui entouré d'un ruban noir est un buzzer actif.

|img_buzzer|

Différence entre un buzzer actif et un buzzer passif :

Un buzzer actif possède une source d'oscillation intégrée, il émet donc un son lorsqu'il est alimenté. Un buzzer passif, en revanche, ne dispose pas de cette source, il ne produira donc pas de bip avec des signaux en courant continu ; vous devrez utiliser des ondes carrées dont la fréquence est comprise entre 2 kHz et 5 kHz pour le faire fonctionner. Le buzzer actif est souvent plus coûteux que le passif en raison des circuits oscillants intégrés.

Voici le symbole électrique d'un buzzer. Il possède deux broches avec des pôles positif et négatif. Le + sur la surface indique l'anode, l'autre broche étant la cathode.

|img_buzzer_symbol|

Vous pouvez identifier les broches du buzzer : la plus longue est l'anode et la plus courte est la cathode. Veillez à ne pas les inverser lors du branchement, sinon le buzzer ne produira aucun son.

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Example
.. -------------------

.. :ref:`Alarme anti-intrusion`

.. :ref:`Tonalité personnalisée`

**Exemple**

* :ref:`py_ac_buz` (pour les utilisateurs de MicroPython)
* :ref:`py_pa_buz` (pour les utilisateurs de MicroPython)
* :ref:`py_light_theremin` (pour les utilisateurs de MicroPython)
* :ref:`py_alarm_lamp` (pour les utilisateurs de MicroPython)
* :ref:`py_music_player` (pour les utilisateurs de MicroPython)
* :ref:`py_fruit_piano` (pour les utilisateurs de MicroPython)
* :ref:`py_reversing_aid` (pour les utilisateurs de MicroPython)
* :ref:`ar_ac_buz` (pour les utilisateurs d'Arduino)
* :ref:`ar_pa_buz` (pour les utilisateurs d'Arduino)
* :ref:`per_service_bell` (pour les utilisateurs de Piper Make)
* :ref:`per_reversing_system` (pour les utilisateurs de Piper Make)
* :ref:`per_reaction_game` (pour les utilisateurs de Piper Make)
