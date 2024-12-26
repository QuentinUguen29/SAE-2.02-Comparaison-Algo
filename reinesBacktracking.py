from timeit import default_timer as timer

N = int(input("Saisissez la taille de la grille : "))
nb_solution = 0

# Demande à l'utilisateur de saisir le numéro de ligne et de colonne pour placer la première reine.
ligne_choisie = int(input(f"Saisissez le numéro de la ligne où placer la première reine (1-{N}): ")) - 1
colonne_choisie = ord(input(f"Saisissez la colonne où placer la reine (A-{chr(65 + N - 1)}): ")) -65

# Vérifie si placer une reine à une certaine position (lig, col) dans la grille est possible.
def est_valide(grille, lig, col):
    # Parcourt les lignes précédentes pour vérifier s'il y a des conflits entre les reines.
    for i in range(lig):
        # Vérifie si une reine est déjà placee dans la même colonne, diagonale
        if grille[i] == col or \
           grille[i] - i == col - lig or \
           grille[i] + i == col + lig:
            return False
    return True

# Affichage de la grille avec les reines placées.
def afficher_solution(grille):
    # Affiche les lettres de colonne.
    print("  ", end='')
    for lettre_col in range(N):
        print(" ", chr(ord('A') + lettre_col), "", end='')
    # Parcourt chaque ligne de la grille.
    for lig in range(N):
        chaine = ""
        # Parcourt chaque colonne de la grille.
        for col in range(N):
            # Si une reine est présente à cette position, affiche "R", sinon affiche un espace.
            if grille[lig] == col:
                chaine += "│ R "
            else:
                chaine += "│   "
        # Affiche le haut d'une ligne.
        if lig == 0:
            print("\n  ┌───" + "┬───"*(N-1) + "┐")
        else:
            print("  ├───" + "┼───"*(N-1) + "┤")
        # Affiche le numéro de ligne suivi des reines.
        print("{:<2}".format(lig+1), end='')
        print("" + chaine + "│")
    # Affiche le bas d'une grille.
    print("  └───" + "┴───"*(N-1) + "┘")
    print("\n",end="\r")

# Place récursivement les reines dans la grille de manière à ce qu'elles ne soit pas en conflit.
def placer_reines(grille, lig):
    global nb_solution
    # Si toutes les reines sont placées (reines de la dernière ligne), affiche la solution.
    if lig == N:
        afficher_solution(grille)
        nb_solution += 1
        return
    # Si la ligne actuelle correspond à la ligne choisie par l'utilisateur, place la reine à la colonne choisie.
    if lig == ligne_choisie:
        col_choisie = colonne_choisie
        # Vérifie si la position choisie est valide, puis passe à la prochaine ligne avec de la recursivité.
        if est_valide(grille, lig, col_choisie):
            grille[lig] = col_choisie
            placer_reines(grille, lig + 1)
            grille[lig] = -1
    # Si ce n'est pas la ligne choisie par l'utilisateur, alors on test toutes les colonnes possibles pour cette ligne.
    else:
        for col in range(N):
            # Si la position est valide, place la reine et passe à la prochaine ligne récursivement.
            if est_valide(grille, lig, col):
                grille[lig] = col
                placer_reines(grille, lig + 1)
                grille[lig] = -1

# Trouve toutes les solutions possibles en utilisant le backtracking.
def trouver_solutions():
    # Creer une liste de taille N remplie de -1
    grille = [-1] * N
    # appel de la fonction placer_reine a partir de la premiere ligne
    placer_reines(grille, 0)

# MAIn
def main():
    start = timer()
    trouver_solutions()
    end = timer()
    time = end - start
    print(f"{nb_solution} grilles ont été résolues en {time} secondes avec une reine placée en ({ligne_choisie+1}, {chr(colonne_choisie+65)}) avec la technique du \033[1m\033[4mBACKTRACKING\033[0m.")

main()
