from timeit import default_timer as timer
 
N = int(input("Saisissez la taille de la grille : "))
nb_solution = 0
affichage = 'O' #input("Voulez-vous un affichage des grilles ? (O/n) : ")
def est_valide(grille, lig, col):
    # Vérifie si une reine peut être placée dans la case (lig, col)
    # en vérifiant la ligne, la colonne et les diagonales
    for i in range(lig):
        if grille[i] == col or \
           grille[i] - i == col - lig or \
           grille[i] + i == col + lig:
            return False
    return True
 
def afficher_solution(grille):
    # Affiche la solution sous forme de tableau
    for lig in range(N):
        chaine = ""
        for col in range(N):
            if grille[lig] == col:
                chaine += "R "
            else:
                chaine += ". "
        print(chaine)
    print("\n")
 
def placer_reines(grille, lig):
    global nb_solution
    global affichage
    # Place les reines de manière récursive en utilisant l'algorithme de backtracking
    if lig == N:
        # Toutes les reines sont placées, affiche la solution
        if affichage == 'O':
            afficher_solution(grille)
        nb_solution += 1
        return "Fini !"
 
    for col in range(N):
        if est_valide(grille, lig, col):
            # Place une reine et passe à la ligne suivante
            grille[lig] = col
            placer_reines(grille, lig + 1)
            # Retire la reine pour explorer d'autres possibilités
            grille[lig] = -1
 
def trouver_solutions():
    # Initialise un tableau pour représenter l'échiquier
    grille = [-1] * N
    placer_reines(grille, 0)
 
 
def main():
    # Appel de la fonction principale pour trouver et afficher les solutions
    start = timer()
    trouver_solutions()
    end = timer()
    print(f"{nb_solution} grilles ont été résolues en  {end-start} secondes.")
 
main()