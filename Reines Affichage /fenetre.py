from tkinter import *
from PIL import Image, ImageTk
import os

fen = Tk()
fen.title("Probleme des 8 reines")
fen.geometry("750x750")

# Dimensions du damier
ligs = 8
cols = 8

# Taille d'une case
cell_size = 750 // max(ligs, cols)

# Création du canevas
canvas = Canvas(fen, width=cell_size * cols, height=cell_size * ligs)
canvas.pack()

# Dessiner le damier
for lig in range(ligs):
    for col in range(cols):
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

x = 0
y = 0

canvas.create_image(x*(750//ligs), y*(750//cols), anchor=NW, image=reine_image)

fen.mainloop()
