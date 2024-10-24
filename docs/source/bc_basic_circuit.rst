.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions durant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Circuit Électronique
=========================

De nombreux objets que vous utilisez quotidiennement fonctionnent à l'électricité, comme les lumières de votre maison et l'ordinateur sur lequel vous lisez ceci.

Pour utiliser l'électricité, il faut créer un circuit électrique. Un circuit électrique se compose de fils métalliques et de composants électriques et électroniques.

Les circuits ont besoin d'une source d'énergie. Dans votre maison, la plupart des appareils (par exemple, téléviseurs, lumières) sont alimentés par des prises murales. Mais de nombreux circuits plus petits et portables (par exemple, jouets électroniques, téléphones portables) sont alimentés par des piles. Une pile possède deux bornes : l'une est appelée la borne positive et est marquée par un signe plus (+). Les bornes négatives sont symbolisées par des signes moins (-), bien qu'elles ne soient généralement pas imprimées sur les piles.

Pour que le courant circule, un chemin conducteur doit relier la borne positive de la batterie à la borne négative, ce que l'on appelle un circuit fermé (s'il est déconnecté, on parle de circuit ouvert). Le courant électrique passera à travers les appareils, comme les lampes, pour les faire fonctionner (par exemple, s'allumer).

|bc1|

Un Pico W dispose de quelques broches de sortie d'alimentation (positives) et de broches de masse (négatives). Vous pouvez utiliser ces broches comme pôles positif et négatif de l'alimentation en branchant le Pico W sur une source d'énergie.

|bc2|

Avec l'électricité, vous pouvez créer des œuvres lumineuses, sonores et mécaniques. Vous pouvez allumer une LED en connectant la broche longue au terminal positif et la broche courte au terminal négatif. La LED se détériorera très rapidement si vous faites cela sans ajouter une résistance de 220* ohms dans le circuit pour la protéger.

Le circuit qu'ils forment est illustré ci-dessous.

|bc2.5|

Vous vous demandez peut-être comment construire ce circuit : faut-il tenir les fils à la main ou fixer les broches et les fils avec du ruban adhésif ?

Dans cette situation, les plaques de montage sans soudure (breadboards) seront vos meilleurs alliés.

.. _bc_bb:


Bonjour, Breadboard !
------------------------------

Une breadboard est une plaque rectangulaire en plastique avec une multitude de petits trous. Ces trous nous permettent d'insérer facilement des composants électroniques et de construire des circuits. Les breadboards ne fixent pas les composants de manière permanente, ce qui permet de réparer facilement un circuit et de recommencer en cas de problème.

.. note::
    Il n'est pas nécessaire d'avoir des outils spéciaux pour utiliser des breadboards. Cependant, de nombreux composants électroniques sont très petits, et une paire de pinces peut nous aider à les manipuler plus facilement.

Sur Internet, on peut trouver beaucoup d'informations sur les breadboards.

* `How to Use a Breadboard - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `What is a BREADBOARD? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_

Voici quelques informations à savoir sur les breadboards.

#. Chaque groupe de demi-ligne (comme la colonne A-E de la ligne 1 ou la colonne F-J de la ligne 3) est connecté. Ainsi, si un signal électrique entre par A1, il peut ressortir par B1, C1, D1, E1, mais pas par F1 ou A2.

#. En général, les deux côtés de la breadboard sont utilisés comme bus d'alimentation, et les trous de chaque colonne (environ 50 trous) sont connectés ensemble. La règle générale est que les alimentations positives sont reliées aux trous près du fil rouge, et les alimentations négatives près du fil bleu.

#. Dans un circuit, le courant circule du pôle positif au pôle négatif après avoir traversé la charge. Dans ce cas, un court-circuit peut survenir.

|bc3|

Suivons la direction du courant pour construire le circuit !

1. Dans ce circuit, nous utilisons la broche 3V3 de la carte Pico W pour alimenter la LED. Utilisez un câble de raccordement mâle-à-mâle (M2M) pour le connecter au bus d'alimentation rouge.
#. Pour protéger la LED, le courant doit passer par une résistance de 220 ohms. Connectez une extrémité (n'importe laquelle) de la résistance au bus d'alimentation rouge, et l'autre extrémité à une rangée libre de la breadboard (la ligne 24 dans mon circuit).

    .. note::
        Les anneaux de couleur de la résistance de 220 ohms sont rouge, rouge, noir, noir et brun.

#. Si vous prenez la LED, vous verrez qu'une de ses pattes est plus longue que l'autre. Connectez la patte la plus longue à la même rangée que la résistance, et la patte la plus courte à la rangée correspondante de l'autre côté de la breadboard.

    .. note::
        La patte la plus longue est l'anode, qui représente le côté positif du circuit ; la plus courte est la cathode, représentant le côté négatif.

        L'anode doit être connectée à la broche GPIO via une résistance ; la cathode doit être reliée à la broche GND.

#. Utilisez un câble de raccordement mâle-à-mâle (M2M) pour connecter la patte courte de la LED au bus d'alimentation négatif de la breadboard.
#. Connectez la broche GND du Pico W au bus d'alimentation négatif à l'aide d'un câble.

Attention aux courts-circuits
---------------------------------
Les courts-circuits peuvent se produire lorsque deux composants qui ne devraient pas être connectés le sont "accidentellement". Ce kit comprend des résistances, transistors, condensateurs, LED, etc. qui ont de longues broches métalliques pouvant se toucher et causer un court-circuit. Certains circuits cessent simplement de fonctionner correctement lorsqu'un court-circuit se produit. Parfois, un court-circuit peut endommager les composants de manière permanente, notamment entre l'alimentation et le bus de masse, rendant le circuit très chaud, fondant le plastique de la breadboard, et même brûlant les composants !

Assurez-vous donc toujours que les broches de tous les composants électroniques sur la breadboard ne se touchent pas.

Orientation du circuit
----------------------------------
Les circuits ont une orientation, et cela joue un rôle significatif dans certains composants électroniques. Certains dispositifs sont polarisés, ce qui signifie qu'ils doivent être connectés correctement en fonction de leurs pôles positif et négatif. Les circuits construits avec une mauvaise orientation ne fonctionneront pas correctement.

|bc3|

Si vous inversez la LED dans ce simple circuit que nous avons construit plus tôt, vous constaterez qu'elle ne fonctionne plus.

À l'inverse, certains dispositifs n'ont pas de direction, comme les résistances dans ce circuit, vous pouvez donc les inverser sans affecter le fonctionnement des LED.

La plupart des composants et modules avec des indications telles que "+", "-", "GND", "VCC" ou avec des broches de différentes longueurs doivent être connectés au circuit d'une manière spécifique.

Protection du circuit
-------------------------------------

Le courant est le débit auquel les électrons passent par un point dans un circuit électrique complet. À son niveau le plus basique, le courant = flux. Un ampère (AM-pir), ou ampère, est l'unité internationale utilisée pour mesurer le courant. Il exprime la quantité d'électrons (parfois appelés "charge électrique") passant par un point d'un circuit sur une période donnée.

La force motrice (tension) derrière le flux de courant est appelée tension et est mesurée en volts (V).

La résistance (R) est la propriété du matériau qui limite le flux de courant, et elle est mesurée en ohms (Ω).

Selon la loi d'Ohm (tant que la température reste constante), le courant, la tension et la résistance sont proportionnels.
Le courant d'un circuit est proportionnel à sa tension et inversement proportionnel à sa résistance.

Donc, current (I) = voltage (V) / resistance (R).

* `Ohm's law - Wikipedia <https://en.wikipedia.org/wiki/Ohm%27s_law>`_

Concernant la loi d'Ohm, nous pouvons faire une expérience simple.

|bc3|

En changeant le fil connectant 3V3 à 5V (c'est-à-dire VBUS, la 40e broche du Pico W), la LED deviendra plus lumineuse.
Si vous changez la résistance de 220 ohms à 1000 ohms (anneaux de couleur : marron, noir, noir, marron et marron), vous remarquerez que la LED devient moins lumineuse qu'avant. Plus la résistance est grande, plus la LED est faible.

.. note::
    Pour une introduction aux résistances et comment calculer les valeurs de résistance, voir :ref:`cpn_resistor`.

La plupart des modules empaquetés ne nécessitent qu'un accès à la tension appropriée (généralement 3,3V ou 5V), comme le module ultrasonique.

Cependant, dans vos circuits auto-construits, vous devez faire attention à la tension d'alimentation et à l'utilisation des résistances pour les dispositifs électriques.

Par exemple, les LED consomment généralement 20 mA de courant, et leur chute de tension est d'environ 1,8V. Selon la loi d'Ohm, si nous utilisons une alimentation de 5V, nous devons connecter une résistance d'au moins 160 ohms ((5-1,8)/20mA) pour éviter de brûler la LED.
