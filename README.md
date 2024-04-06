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

## tri par bulles
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

## tri par insertion 

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
 	

