
"""
TP3 : Système de gestion de livres pour une bibliothèque

IMPORTANT :
- Suivre attentivement les directives dans le fichier README.md.
- Chaque partie du TP doit être réalisée à l'intérieur d'une fonction que vous devez créer.
- Vous devez ensuite appeler chacune des fonctions dans la fonction principale "main()"

"""

import csv
from datetime import datetime


##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

"""
Créer une fonction `charger_collection` qui permet de : 
    - Lire le fichier collection_bibliotheque.csv
    - Créer un dictionnaire nommé 'bibliotheque'
        - La cote doit être la clé principale
        - Chaque clé principale doit contenir :
            - titre
            - auteur
            - date_publication

Cette partie doit être faite dans une fonction qui s'appelle "charger_collection". 
"""

# Écrire votre code ici

def charger_collection(file= 'collection_bibliotheque.csv'):
    with open(file, 'r', newline='') as newfile:
        books = csv.reader(newfile, delimiter=',')
        next(books)
        bibliotheque = {book[-1]: {'titre': book[0], 'auteur': book[1], 'date_publication': book[2]} for book in books}
    return bibliotheque


##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

"""
Exigences :
- Lire nouvelle_collection.csv
- Ajouter seulement les livres dont la cote n'existe pas déjà
- Afficher les messages demandés dans l'énoncé
- Retourner ou mettre à jour la bibliothèque

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_nouvelle_collection". 
"""

# Écrire votre code ici

def ajouter_nouvelle_collection(bibliotheque, file= 'nouvelle_collection.csv'):
    with open(file, 'r', newline='') as library:
        books = csv.reader(library, delimiter=',')
        next(books)
        for book in books:
            title = book[0]
            author = book[1]
            pub_date = book[2]
            sort_nb = book[-1]
            if sort_nb not in bibliotheque:
                bibliotheque[sort_nb] = {'titre': title, 'auteur': author, 'date_publication': pub_date}
                print(f"Le livre {sort_nb} ---- {title} par {author} ---- a été ajouté avec succès")
            else: print(f"Le livre {sort_nb} ---- {title} par {author} ---- est déjà présent dans la bibliothèque")
    return bibliotheque


##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

"""
Exigences :
- Modifier les cotes des livres de William Shakespeare
- Exemple : S028 → WS028
- Modifier correctement les clés du dictionnaire

Cette partie doit être faite dans une fonction qui s'appelle "modifier_cote_shakespeare". 
"""

# Écrire votre code ici


def modifier_cote_shakespeare(bibliotheque):
    for sort_nb in list(bibliotheque.keys()):
        book = bibliotheque[sort_nb]
        
        if sort_nb[0] == 'S' and book['auteur'] == 'William Shakespeare':
            new_sort_nb = 'W' + sort_nb
            bibliotheque[new_sort_nb] = bibliotheque.pop(sort_nb)

    return bibliotheque






##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

"""
Exigences :
- Ajouter les clés :
    - emprunt
    - date_emprunt
- Lire emprunts.csv
- Mettre à jour l'état des livres

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_emprunts". 
"""

# Écrire votre code ici



def ajouter_emprunts(bibliotheque, file= 'emprunts.csv'):
    for book in bibliotheque.values():
        book['emprunt'] = 'disponible'
        book['date_emprunt'] = None
    with open(file, 'r', newline='') as borrowed_books:
        books = csv.reader(borrowed_books, delimiter=',')
        next(books)
        for book in books:
            sort_nb = book[0]
            borrowed_date = book[1]
            if sort_nb in bibliotheque:
                bibliotheque[sort_nb]['emprunt'] = 'emprunté'
                bibliotheque[sort_nb]['date_emprunt'] = borrowed_date
    return bibliotheque

        







##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

"""
Exigences :
- Ajouter les clés :
    - frais_retard
    - livre_perdu
- 30 jours autorisés
- 2$ par jour de retard (max 100$)
- Livre perdu après 365 jours
- Utiliser datetime

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_retards". 
"""

# Écrire votre code ici

def calculer_retards(bibliotheque):
    lost_books = []
    date = datetime.today()
    for sort_nb, book in bibliotheque.items():
        book['perdu'] = False
    for sort_nb, book in bibliotheque.items():
        if book['date_emprunt']:
            borrowed_date = datetime.strptime(book['date_emprunt'], "%Y-%m-%d")
            delta_time = date - borrowed_date

            if delta_time.days > 30:
                book['frais_retard'] = (delta_time.days - 30)*2

                if book['frais_retard'] > 100:
                    book['frais_retard'] = 100
            else: book['frais_retard'] = 0
            if delta_time.days >= 365:
                lost_books.append(sort_nb)
                book['perdu'] = True

        else: book['frais_retard'] = 0

    print('--- Livres en retard ---')
    for sort_nb, book in bibliotheque.items():
        if book['frais_retard'] != 0: print(f"{sort_nb} - {book['titre']} : {book['frais_retard']}$ de frais")

    bibliotheque['livres_perdus'] = lost_books
    return bibliotheque



##########################################################################################################
# PARTIE 6 : Sauvegarde de la bibliothèque
##########################################################################################################

"""
Exigences :
- Créer le fichier bibliotheque_mise_a_jour.csv
- Colonnes obligatoires :
    cote, titre, auteur, date_publication,
    emprunt, date_emprunt, frais_retard, livre_perdu
- Utiliser le module csv pour écrire le fichier

Cette partie doit être faite dans une fonction qui s'appelle "sauvegarder_bibliotheque". 
"""

# Écrire votre code ici

def sauvegarder_bibliotheque(bibliotheque, file='updated_library.csv'):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cote_rangement', 'titre', 'auteur', 'date_publication', 'emprunt', 'date_emprunt', 'frais_retard', 'perdu'])
        for sort_nb, book in bibliotheque.items():
            if sort_nb != 'livres_perdus': 
                writer.writerow([sort_nb, book['titre'], book['date_publication'], book['emprunt'], book['date_emprunt'], book['frais_retard'], book['perdu']])
            else: 
                writer.writerow([bibliotheque['livres_perdus']])










##########################################################################################################
# PROGRAMME PRINCIPAL
##########################################################################################################

"""
Exigences :
- Appeler toutes vos fonctions dans le bon ordre
- Vérifier que le programme fonctionne sans erreur
- Afficher les résultats demandés
"""

# Écrire votre code ici
def main():


    

    ############################################################
    # Partie 1 : Appel de la fonction charger_collection 
    ############################################################
    
    # Écrire votre code ici 
    

    library = charger_collection('collection_bibliotheque.csv')
    print(library)

    ############################################################
    # Partie 2 : Appel de la fonction ajouter_nouvelle_collection
    ############################################################
    
    # Écrire votre code ici 
    
    ajouter_nouvelle_collection(library, 'nouvelle_collection.csv')



    ############################################################
    # Partie 3 : Appel de la fonction modifier_cote_shakespeare
    ############################################################

    # Écrire votre code ici 

    modifier_cote_shakespeare(library)


    ############################################################
    # Partie 4 : Appel de la fonction ajouter_emprunts
    ############################################################

    # Écrire votre code ici 
    
    ajouter_emprunts(library, 'emprunts.csv')



    ############################################################
    # Partie 5 : Appel de la fonction calculer_retards
    ############################################################

    # Écrire votre code ici 
   
    calculer_retards(library)
   

    ############################################################
    # Partie 6 : Appel de la fonction sauvegarder_bibliotheque
    ############################################################
    
    # Écrire votre code ici 
    
    sauvegarder_bibliotheque(library)



if __name__ == "__main__":
    main()