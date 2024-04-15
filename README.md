# sorting-algorithms

# Projet de tri d'algorithmes

Ce projet vise à fournir un outil d'automatisation de tri d'objets, en particulier des listes de nombres réels, en utilisant différents algorithmes de tri.

## Contexte du projet

Dans l'effervescence de la ville égyptienne au Ier siècle apr. J.-C., se dressait la Grande Bibliothèque d’Alexandrie, tel un phare du savoir antique. Parmi les érudits arpentant les couloirs sacrés se trouvait Héron, un esprit brillant réputé pour ses prouesses et son habileté en mathématiques, en mécanique et en ingénierie. Un jour, alors que Héron parcourait la vaste collection de papyrus et de parchemins, il ne put s'empêcher de remarquer le désordre qui sévissait dans la Bibliothèque. Déterminé à rétablir l'ordre, Héron s'est attelé à la tâche en explorant différentes méthodes pour résoudre ce nouveau défi qui se présentait à lui.

## Algorithmes de tri implémentés

1. Tri par sélection
2. Tri à bulles
3. Tri par insertion
4. Tri fusion
5. Tri rapide
6. Tri par tas
7. Tri à peigne

## Exécution du code

- Assurez-vous d'avoir Python installé sur votre système.
- Exécutez le fichier main.py et suivez les instructions pour choisir l'algorithme de tri et saisir la liste de nombres réels à trier.

## Conclusion

Ce projet démontre l'application pratique des différents algorithmes de tri et fournit un outil utile pour automatiser le processus de tri des données. Des améliorations futures pourraient inclure une interface utilisateur graphique et l'optimisation des performances des algorithmes de tri.

## tri par selection

Trouver le minimum de la liste et placez-le  à la fin de la section triée

[5 3 1 4 2]
[1-3 5 4 2]
[1 2-5 4 3]
[1 2 3-4 5]
[1 2 3 4-5]
[1 2 3 4 5 -]


## tri à bulles :
Étape 1
1.1. ( 5 1 4 2 8 ) → ( 1 5 4 2 8 ). 
1.2. ( 1 5 4 2 8 ) → ( 1 4 5 2 8 )
1.3. ( 1 4 5 2 8 ) → ( 1 4 2 5 8 )
1.4. ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )
Étape 2
2.1. ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )
2.2. ( 1 4 2 5 8 ) → ( 1 2 4 5 8 )
2.3. ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
Étape 3
3.1. ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
3.2. ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
Étape 4
4.1. ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )

## tri par insertion :

i = 1 : 	
6	5	3	1	8	7	2	4 ⟶  5	6	3	1	8	7	2	4
 	
i = 2 : 	
5	6	3	1	8	7	2	4  ⟶ 3	5	6	1	8	7	2	4
 	
i = 3 : 	
3	5	6	1	8	7	2	4  ⟶  1	3	5	6	8	7	2	4
	
i = 4 : 	
1	3	5	6	8	7	2	4  ⟶ 1	3	5	6	8	7	2	4
 	
i = 5 : 	
1	3	5	6	8	7	2	4 ⟶  1	3	5	6	7	8	2	4
	
i = 6 : 	
1	3	5	6	7	8	2	4  ⟶  1	 2	3	5	6	7	8	4	 

i = 7 : 	
1	2	3	5	6	7	8	4   ⟶  1	2	3	4	5	6	7	8

## tri fusion :

Fusionner [1;2;5] et [3;4] : le premier élément de la liste fusionnée sera le premier élément d'une des deux listes d'entrée (soit 1, soit 3) car ce sont des listes triées.

Comparer 1 et 3 : 1 est plus petit
[2;5] - [3;4] → [1]
Comparer 2 et 3 : 2 est plus petit
[5] - [3;4] → [1;2]
Compare 5 et 3 → 3 est plus petit
[5] - [4] → [1;2;3]
Compare 5 et 4 : 4 est plus petit
[5] → [1;2;3;4]
Résultat de la fusion :
[1;2;3;4;5]

## tri rapide :

Prenons 5, 9, 7, 3, 8 comme suite de nombres, et trions la dans l'ordre croissant avec l'algorithme du tri rapide :

5, 9, 7, 3, 8 -> on choisit le pivot, dans notre cas je choisis l'élément du milieu, 7.

5, 3 | 7 | 9, 8 -> on découpe le tableau en trois parties, une partie avec des éléments inférieurs au pivot (5 et 3), la partie contenant le pivot (7), et une partie avec les éléments supérieurs au pivot (9 et 8). On peut déjà dire qu'on a placé le pivot à sa place définitive dans le tableau, puisque les autres éléments sont soit supérieurs soit inférieurs à lui.

5, 3 | 7 | 9, 8 -> on recommence en choisissant de nouveau un pivot pour chaque sous tableaux créés.

3 | 5 | 7 | 8 | 9 -> dernière étape du partitionnement, désormais aucuns sous tableaux ne contient plus d'un élément, le tri est donc terminé.

3, 5, 7, 8, 9

## tri par tas :
Comme organiser un groupe de personnes par taille, en plaçant la plus grande personne à la fin de la file et en déplaçant les personnes plus petites vers l'avant jusqu'à ce que tout le monde soit en ordre.


## tri a peigne :

Reprenons la liste suivante : 14 - 21 - 8 - 15 - 35 - 59 - 63 - 9 - 42 - 69
Ici N = 10, on prend la partie entière de 10 // 1,3 soit 7
            14 − 21 − 8 − 15 − 35 − 59 − 63 − 9 − 42 − 69
Seuls 14 et 9 sont à permuter, on calcule la partie  entière de 7 // 1,3 soit 5, on a alors :
            9 − 21 − 8 − 15 − 35 − 59 − 63 − 14 − 42 − 69
Aucun élément n’est à permuter, on calcule la partie entière de 5 // 1,3 soit 3, on a
alors en ne visualisant que les paires à permuter :
            9 − 21 − 8 − 15 − 35 − 59 − 63 − 14 − 42 − 69
Deux paires sont à permuter, on calcule la partie entière de 3 // 1,3 soit 2, on a alors
en ne visualisant que les paires à permuter :
            9 − 21 − 8 − 15 − 14 − 42 − 63 − 35 − 59 − 69
Quatre paires sont à permuter. on calcule 2 // 1,3 < 1, on prend 1, on a alors en ne
visualisant que les paires à permuter :
            8 − 15 − 9 − 21 − 14 − 35 − 59 − 42 − 63 − 69
Trois paires sont à permuter. On observe que l’on peut encore permuter deux
nombres consécutifs :
            8 − 9 − 15 − 14 − 21 − 35 − 42 − 59 − 63 − 69
On obtient alors la liste triée :
            8 − 9 − 14 − 15 − 21 − 35 − 42 − 59 − 63 − 69


 	

## Sorting Times

| Algorithm | Time (seconds) |
|-----------|----------------|
| Selection Sort | 2.830722 |
| Bubble Sort | 58.457065 |
| Insertion Sort | 2.462820 |
| Fusion Sort | 1.228675 |
| Rapide Sort | 0.978017 |
| Tas Sort | 1.935479 |
| Peigne Sort | 0.283942 |
## Sorting Times

| Algorithm | Time (seconds) |
|-----------|----------------|
| Selection Sort | 1.678550 |
| Bubble Sort | 38.059007 |
| Insertion Sort | 1.380674 |
| Fusion Sort | 0.681395 |
| Rapide Sort | 0.468437 |
| Tas Sort | 1.305620 |
| Peigne Sort | 0.203261 |
## Sorting Times

| Algorithm | Time (seconds) |
|-----------|----------------|
| Selection Sort | 1.584885 |
| Bubble Sort | 32.936402 |
| Insertion Sort | 1.321990 |
| Fusion Sort | 0.625487 |
| Rapide Sort | 0.400303 |
| Tas Sort | 1.258361 |
| Peigne Sort | 0.218193 |
