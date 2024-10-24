.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus en avant-première.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et cadeaux festifs** : Participez à des promotions spéciales et à des tirages au sort pour les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _cpn_dot_matrix:

Matrice de LED
==========================

|img_led_matrix|

En général, les matrices de LED peuvent être classées en deux types : 
cathode commune (CC) et anode commune (CA). Elles se ressemblent beaucoup, 
mais la différence se trouve à l'intérieur. Vous pouvez les distinguer par 
un test. Ce kit utilise une matrice CA. Vous verrez l'étiquette "788BS" sur 
le côté.

Voyez la figure ci-dessous. Les broches sont disposées aux deux extrémités 
à l'arrière. Prenez le côté avec l'étiquette comme référence : les broches 
sur cette extrémité vont de 1 à 8, et de l'autre côté, elles vont de 9 à 16.

Vue extérieure :

|img_788bs_i|

Les figures ci-dessous montrent leur structure interne. Vous pouvez voir que 
dans une matrice de LED CA, les lignes (ROW) représentent l'anode des LED, et 
les colonnes (COL) sont les cathodes ; c'est l'inverse pour une CC. Un point 
commun : pour les deux types, les broches 13, 3, 4, 10, 6, 11, 15 et 16 sont 
toutes des COL, tandis que les broches 9, 14, 8, 12, 1, 7, 2 et 5 sont toutes 
des ROW. Si vous souhaitez allumer la première LED en haut à gauche, pour une 
matrice CA, il suffit de régler la broche 9 sur haut et la broche 13 sur bas ; 
pour une CC, réglez la broche 13 sur haut et la broche 9 sur bas. Pour allumer 
toute la première colonne, avec une CA, mettez la broche 13 sur bas et les 
lignes 9, 14, 8, 12, 1, 7, 2, et 5 sur haut ; avec une CC, mettez la broche 13 
sur haut et les mêmes lignes sur bas. Consultez les figures suivantes pour mieux 
comprendre.

Vue interne :

|img_788bs_sche|

Correspondance des numéros de broches avec les lignes et colonnes ci-dessus :

=========== ====== ====== ===== ====== ===== ====== ====== ======
**COL**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **13** **3**  **4** **10** **6** **11** **15** **16**
**ROW**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **9**  **14** **8** **12** **1** **7**  **2**  **5**
=========== ====== ====== ===== ====== ===== ====== ====== ======

De plus, deux puces 74HC595 sont utilisées ici. L'une contrôle les lignes de 
la matrice LED tandis que l'autre contrôle les colonnes.

**Exemple**


* :ref:`py_74hc_788bs` (pour les utilisateurs de MicroPython)
* :ref:`py_bubble_level` (pour les utilisateurs de MicroPython)
* :ref:`ar_74hc_788bs` (pour les utilisateurs d'Arduino)
