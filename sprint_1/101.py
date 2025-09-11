# trier par ordre croissant une liste
import numpy as np

def trier_ordre_croissant_liste(une_liste):
    
    liste_deux = []
    longueur_liste_origine = len(une_liste)
    while len(nouvelle_liste) != longueur_liste_origine:
        liste_trois = []
        minimum_une_liste = identifier_minimum_liste(une_liste)
        liste_trois.append(minimum_une_liste)
        liste_deux += liste_trois
        indice_minimum_une_liste = une_liste.index(minimum_une_liste)
        une_liste.pop(minimum_une_liste)
     return liste_deux
         


def identifier_minimum_liste(une_liste):
    '''
    paramètre: liste de nombre contenant des valeurs entières ou décimales
    '''
    valeur_minimum = -np.inf
    compteur = 0
    for nombre in une_liste:
        if compteur == 0:
            compteur += 1
            valeur_minimum = nombre
        else:
            if valeur_minimum > nombre:
                valeur_minimum = nombre
    return valeur_minimum 
        
    
def verifier_nombre_premier(nombre):
    liste_nombres_premiers = [2]
    if nombre != 2 and nombre %2 != 0:
        for nombre_a_verifier in range(3,nombre):
            for nombre_verifier in liste_nombres_premiers:
                if nombre % nombre_verifier == 0:
                    return False
        return True
    else:
        if nombre == 2:
            return True
        else:
            return False
