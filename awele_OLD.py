awele = [4] * 12


# Il y a 12 cases, les 6 premieres sont pour l'ordi et les autre pour le joueur


def distribue(n: int, joueur: int) -> int:
    """
    :param n: la case dans laquelle on pioche
    :param joueur: le joueur (0 : ordi, 1: humain)
    :return: le nombre de graines gagnées
    """
    resultat = 0
    graines = awele[n]
    awele[n] = 0
    laisser_vide = None
    if graines >= 12:
        laisser_vide = n
    while graines:
        n = (n + 1) % 12
        if n != laisser_vide:
            awele[n] += 1
            graines -= 1
    while 2 <= awele[n] <= 3 and n // 6 != joueur:
        resultat += awele[n]
        awele[n] = 0
        n = (n - 1) % 12
    return resultat


def simule(n: int, joueur: int) -> int:
    """
    pareil que distribue, mais seulement simulée
    """
    awele2 = awele[:]
    resultat = 0
    graines = awele2[n]
    awele2[n] = 0
    laisser_vide = None
    if graines >= 12:
        laisser_vide = n
    while graines:
        n = (n + 1) % 12
        if n != laisser_vide:
            awele2[n] += 1
            graines -= 1
    while 2 <= awele2[n] <= 3 and n // 6 != joueur:
        resultat += awele2[n]
        awele2[n] = 0
        n = (n - 1) % 12
    return resultat


def display()->None:
    """
    Affichage basique
    """
    print("*" * 22)
    for i in range(6):
        print(str(awele[i]).zfill(2), end="\t")
    print()
    for i in range(11, 5, -1):
        print(str(awele[i]).zfill(2), end="\t")
    print()
    print("*" * 22)
    print()


def trouve_meilleur():
    """ Trouve le meilleur coup à jouer"""
    return max([i for i in range(6) if awele[i] != 0], key=lambda x: simule(x, 0))


score_joueur = 0
score_ordi = 0
display()
while score_ordi + score_joueur < 48:
    j = int(input("quel trou voulez vous jouer ? (1..6) "))
    j = 12 - j
    score_joueur += distribue(j, 1)
    display()
    print(f"votre score : {score_joueur}")
    if score_ordi + score_joueur < 48:
        j = trouve_meilleur()
        score_ordi += distribue(j, 0)
        print(f"score ordi : {score_ordi}")
        display()
if score_ordi > score_joueur:
    print("L'ordi a gagné.")
else:
    print("Bravo à vous !")
