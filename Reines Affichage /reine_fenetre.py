from tkinter import *
from PIL import Image, ImageTk
import os
from timeit import default_timer as timer

taille_fen = 750

fen = Tk()
fen.title("Probleme des 8 reines")
fen.geometry(f"{taille_fen}x{taille_fen}")
fen.configure (bg='white')

N = int(input("Saisissez la taille de la grille : "))

nb_solution = 0
affichage = 'O'
# Taille d'une case
cell_size = taille_fen // max(N, N)

# Création du canevas
canvas = Canvas(fen, width=cell_size * N, height=cell_size * N)
canvas.pack()


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
    canvas.delete("reine")
    for lig in range(N):
        chaine = ""
        for col in range(N):
            if grille[lig] == col:
                chaine += "R "
                canvas.create_image(lig*(taille_fen//N), col*(taille_fen//N), anchor=NW, image=reine_image, tags="reine")
            else:
                chaine += ". "
        print(chaine)
        canvas.delete("image")
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
 


# Dessiner le damier
def damier():
    for lig in range(N):
        for col in range(N):
            x1 = col * cell_size
            y1 = lig * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Alterner la couleur des cases pour créer le damier
            couleur = "#f0c580" if (lig + col) % 2 == 0 else "#5f3c2f"
            canvas.create_rectangle(x1, y1, x2, y2, fill=couleur)

# Charger et convertir l'image de la reine
script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "reine.png")

image = Image.open(image_path)
image = image.resize((cell_size, cell_size), Image.NEAREST)
reine_image = ImageTk.PhotoImage(image)

# x = 0
# y = 0

# canvas.create_image(x*(taille_fen//N), y*(taille_fen//N), anchor=NW, image=reine_image)
# canvas.create_image((x+1)*(taille_fen//N), (y+1)*(taille_fen//N), anchor=NW, image=reine_image)



def trouver_solutions():
    # Initialise un tableau pour représenter l'échiquier
    grille = [-1] * N
    placer_reines(grille, 0)
font = 'arial 15 bold'
def main():
    # Appel de la fonction principale pour trouver et afficher les solutions
    
    damier()
    start = timer()
    trouver_solutions()
    end = timer()
    texteResultat = Label(fen,  font = font,  text = f"{nb_solution} grilles ont été résolues en  {end-start} secondes.", bg=fen.cget('bg'))
    texteResultat.pack()
    texteResultat.anchor(CENTER)
    texteResultat.place(relx=0.5, rely = 0.1, anchor=CENTER)
    print(texteResultat.winfo_width())
main()
fen.mainloop()
