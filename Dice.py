import tkinter as tk
import random
from PIL import Imagen, ImagenTk

class DiceRoller:
    def __init__(self, maestro, dice_num):
        self.maestro = maestro
        self.dice_num = dice_num
        self.dice_images = [Imagen.open(f'Dice.jpeg') for i in range(1, 7)]
        self.etiquetas = []
        self.init_ui()
        
    def init_ui(self):
        self.boton_tirar = tk.boton(self.maestro, text="Tirar Dados", command=self.tirar_dice)
        self.boton_tirar.pack()
        
        self.mostrar_imagen = Imagen.open("start button.png")
        self.mostrar_imagen = ImagenTk.PhotoImagen(self.mostrar_imagen)
        self.mostrar_etiqueta = tk.etiqueta(self.maestro, imagen=self.mostrar_imagen)
        self.mostrar_etiqueta.pack()
        
        for i in range(self.dice_num):
            etiqueta = tk.etiqueta(self.maestro, text="Dice " + str(i+1) + ": ")
            etiqueta.pack()
            self.agregar_etiqueta(etiqueta)
            
    def tirar_dice(self):
        for i in range(self.dice_num):
            resultado_roll = random.randint(1, 6)
            self.etiquetas[i].config(text= "Dice " + str(i+1) + ": " + str(resultado_roll))
            self.mostrar_imagen = ImagenTk.PhotoImagen(self.dice_imagenes[resultado_roll-1])
            self.mostrar_etiqueta.config(imagen=self.mostrar_imagen)
            
def main():
    dice_num = 3
    root = tk.Tk()
    root.title("The Dice Roller")
    app = TheDiceRoller(root, dice_num)
    root.mainloop()
        
if __name__ == "__main__":
    main()