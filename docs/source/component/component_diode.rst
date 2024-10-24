.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_diode:

Diode
=================

|img_diode|

Une diode est un composant électronique avec deux électrodes. Elle permet au courant de circuler uniquement dans un sens, ce que l'on appelle souvent la fonction de "redressement".
Ainsi, une diode peut être considérée comme une version électronique d'un clapet anti-retour.

Les deux bornes d'une diode sont polarisées, l'extrémité positive est appelée anode et l'extrémité négative est appelée cathode. 
La cathode est généralement marquée par une bande argentée ou colorée. 
Le contrôle de la direction du flux de courant est une caractéristique clé des diodes : le courant circule de l'anode vers la cathode. Le comportement de la diode est similaire à celui d'un clapet anti-retour. L'une des caractéristiques les plus importantes d'une diode est la relation non linéaire entre le courant et la tension. Si une tension plus élevée est appliquée à l'anode, le courant circule de l'anode vers la cathode, un processus connu sous le nom de polarisation directe. En revanche, si la tension plus élevée est appliquée à la cathode, la diode ne conduit pas, ce processus est appelé polarisation inverse.

En raison de sa conductivité unidirectionnelle, la diode est utilisée dans presque tous les circuits électroniques complexes. Elle a été l'un des premiers dispositifs à semi-conducteurs créés et ses applications sont nombreuses.

Cependant, en pratique, les diodes ne présentent pas une conductivité parfaite en marche ou arrêt, mais des caractéristiques électroniques non linéaires plus complexes, déterminées par la technologie spécifique de la diode.

Une diode est une jonction p-n formée par un semi-conducteur de type p et un semi-conducteur de type n, avec une couche de charge d'espace aux deux côtés de son interface et un champ électrique auto-généré, en équilibre électrique lorsqu'aucune tension n'est appliquée. Cela se produit parce que le courant de diffusion dû à la différence de concentration des porteurs entre les deux côtés de la jonction p-n est égal au courant de dérive dû au champ électrique auto-généré. Lorsque la tension de polarisation directe est appliquée, l'effet mutuel du champ électrique externe et du champ auto-généré augmente le courant de diffusion des porteurs, générant ainsi un courant direct (c'est ce qui cause la conductivité). Lorsque la tension de polarisation inverse est appliquée, le champ électrique externe et le champ auto-généré se renforcent, formant un courant de saturation inverse I0 dans une certaine plage de tension inverse, indépendant de la valeur de la tension de polarisation inverse (c'est la raison de la non-conductivité).
Lorsque la tension inverse appliquée atteint un certain seuil, la force du champ électrique dans la couche de charge d'espace de la jonction p-n atteint une valeur critique, provoquant un processus de multiplication des porteurs, générant de nombreuses paires électron-trou et produisant un courant de rupture inverse important, phénomène appelé le claquage de la diode.

**1. Caractéristique directe**

Lorsqu'une tension directe externe est appliquée, au début de la caractéristique directe, la tension est très faible et ne suffit pas à surmonter l'effet de blocage du champ électrique dans la jonction p-n. Le courant direct est alors presque nul, 
cette zone est appelée la zone morte. Cette tension directe qui empêche la conduction de la diode est appelée la tension de seuil. Lorsque la tension directe est supérieure à la tension de seuil, le champ électrique de la jonction p-n est surmonté, la diode conduit en direct, et le courant augmente rapidement avec la tension.
Dans la plage normale d'utilisation du courant, la tension terminale de la diode en conduction reste presque constante, c'est ce qu'on appelle la tension de polarisation directe.

**2. Caractéristique inverse**

Lorsque la tension inverse appliquée reste dans une certaine plage, le courant traversant la diode est formé par quelques porteurs de dérive, appelé courant inverse.
Comme ce courant inverse est très faible, la diode est en état de coupure. Ce courant est également connu sous le nom de courant de saturation inverse ou courant de fuite et est fortement influencé par la température.

**3. Claquage**

Lorsque la tension inverse appliquée dépasse une certaine valeur, le courant inverse augmente brusquement, un phénomène connu sous le nom de claquage électrique.
La tension critique provoquant ce claquage est appelée tension de claquage inverse, et la diode perd alors sa conductivité unidirectionnelle.
Il est donc conseillé d'éviter d'utiliser la diode lorsque la tension inverse appliquée est trop élevée.

Les premières diodes consistaient en des cristaux à "moustaches de chat" et des tubes à vide (également appelés "valves thermioniques"). La plupart des diodes courantes aujourd'hui utilisent des matériaux semi-conducteurs comme le silicium ou le germanium.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_
 
* `Diode - Wikipedia <https://en.wikipedia.org/wiki/Diode>`_


