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




def afficher_format_texte_équation(dictionnaire):
    
    '''
    Cette fonction affiche sous format texte une équation encodée sous forme de dictionnaire. 
    Paramètre: dictionnaire. 
    Exemple: 
    '''
    
    texte = ''
    
    for équation in dictionnaire.values():
        
        compteur = 0
        
        for membre_équation in équation:
            
            if compteur == 1:
                
                texte += ' = '
                
            print(membre_équation)
            
            opérateurs = list(membre_équation.keys())[0]
            variables = list(membre_équation.values())[0]
            
            
        
            texte += str(variables[0]) 
            texte = texte + ' ' + str(opérateurs[0])
            
            texte = texte + ' ' + str(variables[1]) + ' * x'
            texte = texte + ' ' + str(opérateurs[1])
            
            texte = texte + ' ' + str(variables[2]) + ' * y'
            texte = texte + ' ' + str(opérateurs[2])
            
            texte = texte + ' ' + str(variables[3]) + ' * z'
            
            compteur += 1
            
    return texte     
        

def resolution() -> tuple:
    '''
    Cette fonction résout le système linéaire à trois équations et trois inconnues x, y et z.
    Les équations sont documentées sous forme de dictionnaires imbriqués. 
    Exemple: x + y + z = 2
    Pour modéliser cette équation, on crée trois dictionnaires. 
    Le premier dictionnaire associe au nom de l'équation un tuple constitué de deux dictionnaires représentant les deux membres de l'équation.
    Le deuxième dictionnaire associe au tuple  d'encodage des deux opérateurs qui relient x, y et z (ici ('+','+','+'))  une liste qui encode les quantités des constantes, de x, y et z, ici [0,1,1,1]
    Le troisième dictionnaire associe au tuple d'encodage des deux opérateurs qui relient x, y et z (ici ('+','+','+')) une liste qui encode les quantités des constantes, de x, y et z, ici [2,0,0,0]
    Renvoie: 
    Un tuple constituée des solutions de l'équation de la forme x, y, z
    '''
    
    première_équation_encodée = {}
    première_équation_encodée_membre_gauche = {}
    première_équation_encodée_membre_droite = {}
    première_équation_encodée_membre_gauche[('+','+','+')] = [0,1,1,1]
    première_équation_encodée_membre_droite[('+','+','+')] = [2,0,0,0]
    première_équation_encodée['première_équation'] = (première_équation_encodée_membre_gauche, première_équation_encodée_membre_droite)
    
    return première_équation_encodée



def normalisation_min_max(X):
    
    '''
    Cette fonction applique une normalisation Min-Max à une matrice à deux dimensions. 
    Paramètre: matrice de forme NumPy array. 
    Variable de sortie: la matrice normalisée avec une normalisation Min-Max. 
    '''
    
    transposée_X = X.T
    dictionnaire_amplitude = {}
    for indice, colonne in enumerate(transposée_X):
        minimum_X = min(colonne)
        maximum_X = max(colonne)
        dictionnaire_amplitude[indice] = minimum_X, maximum_X, maximum_X - minimum_X
        
        transposée_X[indice,:] = (transposée_X[indice,:] - dictionnaire_amplitude[indice][0]) / dictionnaire_amplitude[indice][2]
 
    return transposée_X.T


def mean_squared_error(X, beta, y):
    
    y_chapeau = np.dot(X, beta)
    
    mse = (y_chapeau - y)**2
    
    mse = mse.mean()
    
    return mse
