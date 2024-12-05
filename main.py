#### Imports et définition des variables globales
from collections import namedtuple

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    alphabet = "abcdefghijklmnopqrstvwxyz"
    Resultat = namedtuple('caractere', 'occurence')
    
    for i in range (0, len(s)):
        for j in range (0 : len(alphabet))
            if s.charAt(i) = alphabet.charAt(j):
                Resultat(j) +=1

    return Resultat


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    alphabet = "abcdefghijklmnopqrstvwxyz"
    Resultat = namedtuple('caractere', 'occurence')

    # cas de base

    iflen(s)==0:
    return Resultat
    
    # recherche nombre de caractères identiques au premier
    
    
    for i in range (0, len(s)):
        for j in range (0 : len(alphabet))
            if s.charAt(i) = alphabet.charAt(j):
                Resultat(j) +=1

    return Resultat
    # appel récursif

    return []
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
