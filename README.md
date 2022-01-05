# Projet-python
Un projet de DataScience qui traite de la consommation de drogue

# Résumé du projet
Sur la base d'un dataset contenant des informations sur des individus, le but était de prédire la consommation de certaines drogues. 

Beaucoup de choix ont été appliqués lors de cette étude, et nous avons au mieux essayé de comprendre nos données, aux travers de graphiques et de documents.
En effet, nous avons choisi de binariser les différentes targets (drogues) qui étaient composées de plusieurs catégories peu équilibrées. Nous avons également utilisés des groupes d'association de drogues (pleiades), pour la visualisation des relations target/features et features/features. 

Enfin, nous avons décidés de privilégier dans le modelling, le recall, car il nous a paru plus pertinant, dans le cadre de l'étude, d'arriver à detecter les personnes à risque fort de consommation, dans l'optique de pouvoir les aider à tout prix. Cette vision des choses est très commune dans le domaine du médical, car on cherche plutôt à "prévenir que guérir".

En conclusion de cette étude, nous pensons que les critères utilisés dans la prediction de la consommation de drogues sont relativement pertinants. Néanmoins, pour obtenir de bonne performance dans la prédiction de la consommation de drogues, d'autres paramètres doivent surement rentrer en compte comme la localisation. Dans la majorité des modèles implémentés, plus de données permettrait d'augmenter les performances. 

# Schéma d'étude suivi 

## **Exploratory Data Analysis**

### Objectif: comprendre au maximum les données dont on dispose pour définir une stratégie de modélisation.

#### I - Analyse de la forme:
- Première approche du dataset 
- Identification de la target
- Nombre des lignes et de colonnes 
- Identification des valeurs manquantes
- Types de variables

#### II - Analyse du fond:
- Visualisation et compréhension des targets (histogramme/boxplot)
- Compréhension des différentes variables (recherche)
- Visualisation des relations : features/targets
- Relation variable / variable


## **Pre-processing** and modelling

### Objectif: transformer le data pour le mettre dans un format propice au machine learning
- Création du Train Set / Test Set
- Encodage (Dummies variables)



### Objectif: développer des modèle de machine learning capable de répondre a l'objectif final.

- Définir des fonctions utiles au modelling
- Selection des meilleurs modèles
- Optimisation avec GridSearchCV
- Analyse des  modèles, learning curve et prise de décision


## Bonus features engineering

- Création d'une feature
- Pca
