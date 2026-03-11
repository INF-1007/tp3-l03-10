[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TnxT_FeD)
# TP3 : Système de gestion de livres pour une bibliothèque :books:

## Directives
:alarm_clock: Date de remise : Le 15 mars 2026

:mailbox_with_mail: À remettre sur Github Classrooms

## Objectifs 
Le travail pratique vise principalement à :

- Structurer un programme en créant des fonctions
- Manipuler des fichiers `.csv` en lecture et en écriture
- Organiser un programme avec une fonction main()
- Modifier et sauvegarder des données persistantes

## Introduction

L'objectif de ce travail pratique est de développer un système de gestion d'une collection de livres dans une bibliothèque. Le système contiendra des fonctions qui permettront de gérer les emprunts et les retours de livres, d'ajouter des nouveaux livres à la collection, et autres fonctionnalités essentielles pour la gestion efficace de la bibliothèque.

Pour chacune des 6 parties du TP, vous devrez ajouter une nouvelle fonction à l'intérieur du fichier `TP3.py`, aux endroits désignés dans le corps principal du fichier : 

```python

# Fonction 1
def charger_collection(fichier_csv):
    # écrire votre code ici

# Fonction 2
def ajouter_nouvelle_collection(bibliotheque, fichier_csv):
    # écrire votre code ici

# Fonction 3
def modifier_cote_shakespeare(bibliotheque):
    # écrire votre code ici

# Fonction 4
def ajouter_emprunts(bibliotheque, fichier_csv):
    # écrire votre code ici

# Fonction 5
def calculer_retards(bibliotheque):
    # écrire votre code ici

# Fonction 6
def sauvegarder_bibliotheque(bibliotheque, fichier_sortie):
    # écrire votre code ici
```

Par la suite, au fur et à mesure que vous créez les fonctions, vous devrez les appeler à l'intérieur de la fonction principale `main()`. : 
```python
def main():
    # appelez vos fonctions 1 à 6 ici

if __name__ == "__main__":
    main()
```

# :books: Partie 1 : Création du système de gestion et ajout de la collection actuelle

Vous avez à votre disposition la liste des livres de la collection actuelle de la bibliothèque, disponible dans le fichier `collection_bibliotheque.csv`. Ce fichier contient les informations suivantes pour chaque livre :
- Le titre du livre
- L'auteur
- La date de publication
- La cote de rangement

La cote de rangement, composée d'une lettre suivie de trois chiffres, est unique à chaque livre et permet aux employés de la bibliothèque de les localiser facilement.

## 1.1 Fonction à créer : 
Dans cette première partie du laboratoire, vous devez créer une fonction `charger_collection` qui prendra en entrée un fichier `.csv`: 

```python
def charger_collection(fichier_csv):
```

La fonction devra pouvoir : 
- Prendre un fichier `.csv` en entrée, structuré comme `collection_bibliotheque.csv`. 
- Faire la lecture de ce fichier `.csv`. Indice : utilisez le module [csv](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html) intégré dans Python. 
- Construire et retourner un dictionnaire Python appelé `bibliotheque` pour gérer la collection de livres : 
    - La côte de rangement est la clé du dictionnaire
    - Chaque entrée de ce dictionnaire doit inclure les informations suivantes :
        - `titre`
        - `auteur`
        - `date_publication`
     
        Par exemple : 
      ```python
      bibliotheque = 
        {'H007': {'titre': 'A Brief History of Time: From the Big Bang to Black Holes', 'auteur': 'Stephen Hawking', 'date_publication': '1987'},
         'P014': {'titre': 'A Child Called "It": One Child\'s Courage to Survive', 'auteur': 'Dave Pelzer', 'date_publication': '1995'},
          ...}
        ```

- La fonction doit retourner le dictionnaire `bibliotheque`

## 1.2 Appel de la fonction : 
Vous devez ensuite appeler la fonction `charger_collection(fichier_csv)` à l'intérieur de la fonction `main()`. 
Ajoutez également un "print" pour afficher le dictionnaire retourné.

# :books: Partie 2 : Ajout d'une nouvelle collection à la bibliothèque

La bibliothèque a fait l'achat d'une nouvelle collection de livres. Cette nouvelle collection est contenue dans le fichier `nouvelle_collection.csv`. 

## 2.1 Fonction à créer : 

Dans cette partie du TP, vous devez créer une fonction `ajouter_nouvelle_collection` : 

```python
def ajouter_nouvelle_collection(bibliotheque, nouvelle_collection_csv):
```

Cette fonction permettra d'ajouter les livres de cette nouvelle collection (en format `.csv`) au dictionnaire `bibliotheque`, en utilisant des structures de contrôle appropriées. Chacune des entrées doit comprendre la cote de rangement avec le titre du livre, l'auteur et la date de publication. 

**Attention** : Ne pas ajouter les livres qui sont déjà présents dans la collection (c'est-à-dire, les livres qui sont déjà présents dans `collection_bibliotheque.csv`) ! Utilisez des structures conditionnelles appropriées pour éviter l'ajout de ces livres en double dans le système de gestion, en se basant sur leur cote de rangement. Pour chaque livre de la nouvelle collection, affichez l'un des messages suivants selon la situation :

  - Si la cote de rangement n'est pas déjà dans la collection :
      ```
      "Le livre {cote_rangement} ---- {titre} par {auteur} ---- a été ajouté avec succès"
      ```

  - Si la cote de rangement est déjà dans la collection :
      ```
      "Le livre {cote_rangement} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque"
      ```
      
## 2.2 Appel de la fonction : 
Maintenant, appelez la fonction `ajouter_nouvelle_collection` dans `main.py` afin de retourner le dictionnaire modifié. 

# :books: Partie 3 : Modification de la cote de rangement d'une collection de livres 

La bibliothèque souhaite faire des rénovations, et aimerait déplacer sa collection de Shakespeare dans une nouvelle rangée identifiée par "WS". Par conséquent, pour tous les livres de l'auteur William Shakespeare, la cote de rangement, qui débute actuellement par "S" suivi de 3 chiffres, devra être modifiée dans le système de gestion par "WS", suivi des mêmes trois chiffres qu'auparavant. (Par exemple, le livre ayant la cote "S028" devra être changé à "WS028"). 

## 3.1 Fonction à créer : 
Pour ce faire, vous devez créer une fonction `modifier_cote_shakespeare` : 

```python
def modifier_cote_shakespeare(bibliotheque):
```

Cette fonction permettra de : 
- Prendre en entrée le dictionnaire `bibliotheque`
- Trouver tous les livres de William Shakespeare
- Modifier les côtes S à WS
- Retourner le dictionnaire mis à jour

## 3.2 Appel de la fonction : 
Maintenant, appelez la fonction `modifier_cote_shakespeare` dans `main.py` afin de retourner le dictionnaire modifié. 

# :books: Partie 4 : Gestion des emprunts

La bibliothèque souhaite tenir compte des emprunts et des retours de livres dans son système de gestion. Les cotes des livres empruntés ont été enregistrés avec la date d'emprunt dans le fichier `emprunts.csv`. 

## 4.1 Fonction à créer : 

Dans cette partie, vous devez créer une fonction `ajouter_emprunts` qui prendra en entrée le dictionnaire `bibliotheque` ainsi que le fichier `.csv` des emprunts : 

```python
def ajouter_emprunts(bibliotheque, emprunts_csv):
```

La fonction doit : 
- Ajouter une clé intitulée `emprunts` dans le dictionnaire `bibliotheque` pour suivre l'état de chaque livre. 
    - Associez à cette clé la valeur `disponible` si le livre est présent dans la bibliothèque, ou `emprunté` si le livre a été emprunté. Cette clé permettra de gérer facilement les emprunts et les retours des livres.

- Ajouter une clé `date_emprunt`, qui contient les dates auxquelles les livres ont été empruntés. 

- Retourner le dictionnaire mis à jour

## 4.2 Appel de la fonction : 
Maintenant, appelez la fonction `ajouter_emprunts` dans `main.py` afin de retourner le dictionnaire modifié. 

# :books: Partie 5 : Livres en retard

La politique de prêt de la bibliothèque stipule que les livres doivent être retournés dans un délai de 30 jours. Si un livre n'est pas retourné dans ce délai, un frais de retard de 2$ par jour est appliqué, jusqu'à un montant maximal de 100$. De plus, si un livre n'a pas été retourné au bout d'un an, la bibliothèque considère le livre comme étant perdu. 

## 5.1 Fonction à créer : 

Dans cette partie, vous devez créer une fonction `calculer_retards` qui prend en entrée le dictionnaire bibliotheque : 

```python
def calculer_retards(bibliotheque):
```

Cette fonction doit : 
- Ajouter une clé `frais_retard` 
- Afficher la liste des livres en retard avec leurs frais respectifs avec le format d'affichage suivant:

```
--- Livres en retard ---
T013 - A Confederacy of Dunces : 100$ de frais
H015 - A Farewell to Arms : 100$ de frais
R005 - A Game of Thrones : 100$ de frais
E004 - A Heartbreaking Work of Staggering Genius : 100$ de frais
B016 - A Short History of Nearly Everything : 100$ de frais
...
```
  
- Identifiez les livres considérés comme perdus en ajoutant une clé `livres_perdus` et en y ajoutant les livres qui ont été empruntés pendant plus d'un an.

Indice : Pour cet exercice, vous pouvez utiliser le module [datetime](https://docs.python.org/3/library/datetime.html) intégré dans Python pour vous aider à manipuler les dates. 

## 5.2 Appeler la fonction : 
Maintenant, appelez la fonction `calculer_retards` dans `main.py` afin de retourner le dictionnaire modifié. 

# :books: Partie 6 : Sauvegarde dans un nouveau fichier `.csv`

## 6.1 Fonction à créer : 

Dans cette partie, vous devez créer une nouvelle fonction `sauvegarder_bibliotheque` qui devra prendre en entrée le dictionnaire `bibliotheque` ainsi qu'un nouveau nom de fichier (`fichier_sortie`) : 
```
sauvegarder_bibliotheque(bibliotheque, fichier_sortie)
```

Cette fonction doit sauvegarder le dictionnaire en fichier `.csv` en utilisant le nom défini par la variable `fichier_sortie`. 

Le fichier `.csv` final doit contenir les colonnes suivantes : 
```
cote_rangement,titre,auteur,date_publication,emprunt,date_emprunt,frais_retard
```

Indice : vous pouvez utiliser le module [csv](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html) pour sauvegarder le nouveau fichier `.csv. `

## 6.2 Appeler la fonction : 
Maintenant, appelez la fonction `ajouter_emprunts` dans `main.py` afin de sauvegarder le dictionnaire en format `.csv`.
Attention : le chemin `fichier_sortie` doit permettre de sauvegarder le fichier `.csv` directement dans le répertoire du TP3, et non ailleurs sur votre ordinateur! 


## Barème de correction
|     Partie    |                 Tâche                 |     Points    |
| ------------- | ------------------------------------- | ------------- |
|                 | **Partie 1**   |       **/4**       |
|       1.1       | Créer la fonction `charger_collection`  |       3       |
|       1.2       | Appel de la fonction `charger_collection` et affichage du dictionnaire avec `print`  |       1       |
|                 | **Partie 2**   |       **/3**       |
|       2.1       | Créer la fonction `ajouter_nouvelle_collection`       |       2.5       |
|       2.2       | Appel de la fonction `ajouter_nouvelle_collection`      |       0.5       |
|                 | **Partie 3**   |       **/3**       |
|       3.1       | Créer la fonction `modifier_cote_shakespeare`      |       2.5       |
|       3.2       | Appel de la fonction `modifier_cote_shakespeare`      |       0.5       |
|                 | **Partie 4**   |       **/3**       |
|       4.1       | Créer la fonction `ajouter_emprunts`       |       2.5       |
|       4.2       | Appel de la fonction `ajouter_emprunts`      |       0.5       |
|                 | **Partie 5**   |       **/4**       |
|       5.1       | Créer la fonction `calculer_retards`       |       3.5       |
|       5.2       | Appel de la fonction `calculer_retards`     |       0.5       |
|                 | **Partie 6**   |       **/3**       |
|       6.1       | Créer la fonction `sauvegarder_bibliotheque`  |       2.5       |
|       6.2       | Appel de la fonction `sauvegarder_bibliotheque`      |       0.5       |
|               |                                **Total**  |       **20**      |


## Références
Les données contenues à l'intérieur des fichiers `collection_bibliotheque.csv` et `nouvelle_collection.csv` ont été tirées et adaptées de cette [base de données](https://github.com/zygmuntz/goodbooks-10k/tree/master). 
