
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


    pass # À enlever

    ############################################################
    # Partie 1 : Appel de la fonction charger_collection 
    ############################################################
    
    # Écrire votre code ici 
    




    ############################################################
    # Partie 2 : Appel de la fonction ajouter_nouvelle_collection
    ############################################################
    
    # Écrire votre code ici 
    




    ############################################################
    # Partie 3 : Appel de la fonction modifier_cote_shakespeare
    ############################################################

    # Écrire votre code ici 

    



    ############################################################
    # Partie 4 : Appel de la fonction ajouter_emprunts
    ############################################################

    # Écrire votre code ici 
    




    ############################################################
    # Partie 5 : Appel de la fonction calculer_retards
    ############################################################

    # Écrire votre code ici 
   

   

    ############################################################
    # Partie 6 : Appel de la fonction sauvegarder_bibliotheque
    ############################################################
    
    # Écrire votre code ici 
    




if __name__ == "__main__":
    main()