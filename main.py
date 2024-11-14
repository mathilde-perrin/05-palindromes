#### Fonction secondaire
"""
Vérifier si p est un palindrome
"""

def ispalindrome(p):
    """Vérifie si p, la chaine de caractères entrée est un palindrome.

    Args:
        p (str): la chaine de caractère

    Returns:
        booléen: True si palindrome, false si pas le cas
        p (str) : la chaine de caractère
    """
    #Conversion des caractères en minuscule
    p = p.lower()
    #Conversion des caractères spéciaux en caractères simples
    accents = str.maketrans("éèêëàâäîïôöùûüç?!',-:", "eeeeaaaiioouuuc      ")
    p = p.translate(accents)
    #Suppression des espaces
    p = p.replace(" ","")
    #Réciprocité
    return p == p[::-1]
#### Fonction principale


def main():

    """
    Appel à la fonction
    """

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
