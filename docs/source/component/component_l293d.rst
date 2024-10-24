.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_l293d:

Circuit intégré L293D
=======================

|img_l293d0|

Le L293D est un pilote de moteur à 4 canaux intégré dans une puce capable de gérer des tensions et des courants élevés. 
Il est conçu pour se connecter aux niveaux logiques DTL et TTL standard, et pour piloter des charges inductives (telles que des bobines de relais, des moteurs à courant continu, des moteurs pas à pas) ainsi que des transistors de commutation de puissance. 
Les moteurs à courant continu (DC) convertissent l'énergie électrique en énergie mécanique et sont largement utilisés dans les systèmes d'entraînement électrique grâce à leur excellente performance de régulation de vitesse.

Voir la figure des broches ci-dessous. Le L293D dispose de deux broches (Vcc1 et Vcc2) pour l'alimentation. 
Vcc2 sert à alimenter le moteur, tandis que Vcc1 alimente la puce. Étant donné qu'un petit moteur DC est utilisé ici, connectez les deux broches au +5V.

|img_l293d1| 

Voici la structure interne du L293D. 
La broche EN est une broche d'activation qui ne fonctionne qu'à un niveau haut ; A représente l'entrée et Y la sortie. 
Vous pouvez voir la relation entre elles en bas à droite. 
Lorsque la broche EN est à un niveau haut, si A est à un niveau haut, Y émet un niveau haut ; si A est à un niveau bas, Y émet un niveau bas. Lorsque la broche EN est à un niveau bas, le L293D ne fonctionne pas.

|img_l293d2|

* `L293D Datasheet <https://cdn-shop.adafruit.com/datasheets/l293d.pdf>`_

**Exemple**

* :ref:`py_motor` (pour les utilisateurs de MicroPython)
* :ref:`ar_motor` (pour les utilisateurs d'Arduino)
* :ref:`py_pump` (pour les utilisateurs de MicroPython)
* :ref:`ar_pump` (pour les utilisateurs d'Arduino)
* :ref:`per_smart_fan` (pour les utilisateurs de Piper Make)
