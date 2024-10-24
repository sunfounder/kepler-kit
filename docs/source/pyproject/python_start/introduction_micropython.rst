.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans le monde des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

1.1 Introduction à MicroPython
======================================

MicroPython est une implémentation logicielle d'un langage de programmation largement compatible avec Python 3, écrite en C, et optimisée pour fonctionner sur un microcontrôleur.

MicroPython se compose d'un compilateur Python en bytecode et d'un interpréteur qui exécute ce bytecode. L'utilisateur dispose d'un invite interactive (le REPL) pour exécuter immédiatement les commandes prises en charge. MicroPython inclut une sélection de bibliothèques Python de base et des modules permettant d'accéder au matériel à bas niveau.

* Référence : `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

L'histoire commence ici
--------------------------------

Tout a changé en 2013 lorsque Damien George a lancé une campagne de financement participatif (Kickstarter).

Damien était étudiant à l'université de Cambridge et passionné de programmation robotique. Il souhaitait réduire le monde de Python d'une machine de gigaoctets à un kilooctet. Sa campagne Kickstarter visait à soutenir son développement pendant qu'il transformait sa preuve de concept en une implémentation finalisée.

MicroPython est soutenu par une communauté diversifiée de Pythonistes qui ont un intérêt marqué pour le succès du projet.

En plus de tester et de soutenir la base de code, les développeurs ont fourni des tutoriels, des bibliothèques de code et du portage matériel, ce qui a permis à Damien de se concentrer sur d'autres aspects du projet.

* Référence : `realpython <https://realpython.com/micropython/>`_


Pourquoi MicroPython ?
----------------------------

Bien que la campagne Kickstarter originale ait lancé MicroPython sous forme de carte de développement "pyboard" avec STM32F4, MicroPython prend en charge de nombreuses architectures de produits basées sur ARM. Les ports pris en charge en ligne principale incluent ARM Cortex-M (nombreuses cartes STM32, TI CC3200/WiPy, cartes Teensy, série Nordic nRF, SAMD21 et SAMD51), ESP8266, ESP32, PIC 16 bits, Unix, Windows, Zephyr et JavaScript.
Ensuite, MicroPython permet une rétroaction rapide. Cela est dû au fait que vous pouvez utiliser le REPL pour entrer des commandes de manière interactive et obtenir des réponses immédiates. Vous pouvez même modifier le code et l'exécuter instantanément au lieu de passer par le cycle code-compilation-téléversement-exécution.

Bien que Python offre les mêmes avantages, certaines cartes de microcontrôleur comme le Raspberry Pi Pico sont petites, simples et ont peu de mémoire pour exécuter le langage Python. C'est pourquoi MicroPython a évolué, en conservant les principales fonctionnalités de Python et en ajoutant de nouvelles pour fonctionner avec ces cartes de microcontrôleurs.

Ensuite, vous apprendrez à installer MicroPython sur le Raspberry Pi Pico.

* Référence : `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* Référence : `realpython <https://realpython.com/micropython/>`_

