from timeit import default_timer as timer
 
class ChessboardGraph:
    def __init__(self, size):
        self.size = size
        self.graph = self.create_graph()
 
    def create_graph(self):
        graph = {}
        for row in range(self.size):
            for col in range(self.size):
                node = (row, col)
                neighbors = []
                for i in range(self.size):
                    if i != row:
                        neighbors.append((i, col))
                    if i != col:
                        neighbors.append((row, i))
                    if 0 <= row + i < self.size and 0 <= col + i < self.size:
                        neighbors.append((row + i, col + i))
                    if 0 <= row + i < self.size and 0 <= col - i < self.size:
                        neighbors.append((row + i, col - i))
                graph[node] = neighbors
        return graph
 
def est_valide(grille, lig, col):
    for i in range(lig):
        if grille[i] == col or \
           grille[i] - i == col - lig or \
           grille[i] + i == col + lig:
            return False
    return True
 
def placer_reines(grille, lig, graph):
    if lig == len(grille):
        afficher_solution(grille)
        return True
    for col in range(len(grille)):
        if est_valide(grille, lig, col):
            grille[lig] = col
            if placer_reines(grille, lig + 1, graph):
                return True
            grille[lig] = -1
    return False
 
def afficher_solution(grille):
    print("  ", end='')
    for lettre_col in range(len(grille)):
        print(" ", chr(ord('A') + lettre_col), "", end='')
    for lig in range(len(grille)):
        chaine = ""
        for col in range(len(grille)):
            if grille[lig] == col:
                chaine += "│ R "
            else:
                chaine += "│   "
        if lig == 0:
            print("\n  ┌───" + "┬───"*(len(grille)-1) + "┐")
        else:
            print("  ├───" + "┼───"*(len(grille)-1) + "┤")
        print("{:<2}".format(lig+1), end='')
        print("" + chaine + "│")
    print("  └───" + "┴───"*(len(grille)-1) + "┘")
    print("\n",end="\r")
 
def main():
    N = int(input("Saisissez la taille de la grille : "))
    ligne_manuelle = int(input(f"Saisissez le numéro de la ligne où placer la première reine (1-{N}): ")) - 1
    colonne_manuelle = ord(input(f"Saisissez la colonne où placer la reine (A-{chr(65 + N - 1)}): ")) - 65
 
    start = timer()
    graph = ChessboardGraph(N)
    grille = [-1] * N
    grille[ligne_manuelle] = colonne_manuelle
    placer_reines(grille, 0, graph)
    end = timer()
    time = end - start
    print(f"Solution trouvée en {time} secondes.")
 
main()