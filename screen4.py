import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, PhotoImage, Frame
from PIL import Image, ImageTk
import time

anch = 87
    
def screen4():
     print('pantalla 4')

     def navegacion(pantalla):
        if pantalla == "1":
            from main import inicio
            ventana.after(100, lambda: [ventana.destroy(), inicio()])
        elif pantalla == "2":
            from screen1 import screen1
            ventana.after(100, lambda: [ventana.destroy(), screen1()])
        elif pantalla == "3":
            from screen2 import screen2
            ventana.after(100, lambda: [ventana.destroy(), screen2()])
        elif pantalla == "4":
            from screen3 import screen3
            ventana.after(100, lambda: [ventana.destroy(), screen3()])
        elif pantalla == "5":
            print("es aqui")

     ventana = tk.Tk()
     ventana.title("Pantalla 5")
     ventana.geometry("375x812")
     ventana.config(bg="white")

     alert = Label(ventana, text="Pantalla 5")
     alert.pack(pady=10)

     #la barra
     barra_superior= Frame(ventana)
     barra_superior.config(height="430", bg="white")
     barra_superior.pack(fill="x", side=tk.BOTTOM, pady=30)

     #   ----------  Botones ------------------
     #pantalla uno
     imagen_original = Image.open("assets/frutas.png")
     imagen_redimensionada = imagen_original.resize((87, 50))
     imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

     boton1 = tk.Button(barra_superior, text="Boton 1", image=imagen_tk, command=lambda: navegacion("1"), state="normal")
     boton1.pack(side="left", pady=5)

     #pantalla dos
     boton2 = tk.Button(barra_superior, text="Boton 2", image=imagen_tk, command=lambda: navegacion("2"), state="normal")
     boton2.pack(side="left", pady=5)

     #pantalla tres
     boton3 = tk.Button(barra_superior, text="Boton 3", image=imagen_tk, command=lambda: navegacion("3"), state="normal")
     boton3.pack(side="left", pady=5)

     #pantalla cuatro
     boton4 = tk.Button(barra_superior, text="Boton 4", image=imagen_tk, command=lambda: navegacion("4"), state="normal")
     boton4.pack(side="left", pady=5)

     #pantalla cinco
     # boton5 = tk.Button(barra_superior, text="Boton 5", image=imagen_tk, command=lambda: navegacion("5"), state="normal")
     # boton5.pack(side="left", pady=5)

     # Iniciar el bucle principal de tkinter
     ventana.mainloop()

screen4()