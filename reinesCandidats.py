from timeit import default_timer as timer

N = int(input("Saisissez la taille de la grille : "))
nb_solution = 0
ligne_choisie = int(input(f"Saisissez le numéro de la ligne où placer la première reine (1-{N}): ")) - 1
colonne_choisie = ord(input(f"Saisissez la colonne où placer la reine (A-{chr(65 + N - 1)}): ")) -65


def est_valide(grille, lig, col):
    for i in range(lig):
        if grille[i] == col or \
           grille[i] - i == col - lig or \
           grille[i] + i == col + lig:
            return False
    return True


def generer_candidats(grille, lig):
    candidats = []
    for col in range(N):
        if est_valide(grille, lig, col):
            candidats.append(col)
    return candidats


def afficher_solution(grille):
    print("  ", end='')
    for lettre_col in range(N):
        print(" ", chr(ord('A') + lettre_col), "", end='')
    for lig in range(N):
        chaine = ""
        for col in range(N):
            if grille[lig] == col:
                chaine += "│ R "
            else:
                chaine += "│   "
        if lig == 0:
            print("\n  ┌───" + "┬───"*(N-1) + "┐")
        else:
            print("  ├───" + "┼───"*(N-1) + "┤")
        print("{:<2}".format(lig+1), end='')
        print("" + chaine + "│")
    print("  └───" + "┴───"*(N-1) + "┘")
    print("\n",end="\r")


def placer_reines(grille, lig):
    global nb_solution
    if lig == N:
        afficher_solution(grille)
        nb_solution += 1
        return

    if lig == ligne_choisie:
        col_choisie = colonne_choisie
        if est_valide(grille, lig, col_choisie):
            grille[lig] = col_choisie
            placer_reines(grille, lig + 1)
            grille[lig] = -1
    else:
        candidats = generer_candidats(grille, lig)
        for col in candidats:
            grille[lig] = col
            placer_reines(grille, lig + 1)
            grille[lig] = -1


def trouver_solutions():
    grille = [-1] * N
    placer_reines(grille, 0)


def main():
    start = timer()
    trouver_solutions()
    end = timer()
    time = end - start
    print(f"{nb_solution} grilles ont été résolues en {time} secondes avec une reine placée en ({ligne_choisie+1}, {chr(colonne_choisie+65)}) avec la technique des \033[1m\033[4mCANDIDATS\033[0m.")


main()
