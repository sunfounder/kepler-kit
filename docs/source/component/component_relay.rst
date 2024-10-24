.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_relay:

Relais
==========================================

|img_relay|

Comme nous le savons, un relais est un dispositif utilisé pour établir 
une connexion entre deux ou plusieurs points ou appareils en réponse au 
signal d'entrée appliqué. En d'autres termes, les relais assurent une 
isolation entre le contrôleur et l'appareil, car les appareils peuvent 
fonctionner en courant alternatif (AC) aussi bien qu'en courant continu (DC). 
Cependant, ils reçoivent des signaux d'un microcontrôleur fonctionnant en DC, 
nécessitant ainsi un relais pour combler cette différence. Le relais est 
extrêmement utile lorsque vous devez contrôler une grande quantité de courant 
ou de tension avec un petit signal électrique.

Chaque relais comporte 5 parties :

**Électroaimant** - Il se compose d'un noyau en fer entouré par une bobine 
de fils. Lorsqu'un courant électrique passe à travers, il devient magnétique, 
d'où son nom d'électroaimant.

**Armature** - La bande magnétique mobile est appelée armature. Lorsque le 
courant passe, la bobine s'énergise, produisant un champ magnétique utilisé 
pour établir ou rompre les points normalement ouverts (N/O) ou normalement 
fermés (N/C). L'armature peut être déplacée aussi bien par courant continu (DC) 
que par courant alternatif (AC).

**Ressort** - Lorsque aucun courant ne traverse la bobine de l'électroaimant, 
le ressort tire l'armature vers l'arrière afin que le circuit ne puisse pas 
être complété.

Ensemble de **contacts électriques** - Il existe deux points de contact :

-  Normalement ouvert - connecté lorsque le relais est activé, et déconnecté lorsqu'il est inactif.
-  Normalement fermé - non connecté lorsque le relais est activé, et connecté lorsqu'il est inactif.

**Cadre moulé** - Les relais sont recouverts de plastique pour les protéger.

Le principe de fonctionnement du relais est simple. Lorsque le relais est 
alimenté, le courant commence à circuler dans la bobine de commande ; en 
conséquence, l'électroaimant s'énergise. L'armature est alors attirée par 
la bobine, abaissant le contact mobile qui se connecte ainsi aux contacts 
normalement ouverts, et le circuit avec la charge est alimenté. Pour couper 
le circuit, le contact mobile est ramené aux contacts normalement fermés sous
l'effet du ressort. Ainsi, l'activation et la désactivation du relais permettent 
de contrôler l'état d'un circuit de charge.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Exemple**

* :ref:`py_relay` (pour les utilisateurs de MicroPython)
* :ref:`ar_relay` (pour les utilisateurs d'Arduino)