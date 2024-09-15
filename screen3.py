import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, PhotoImage, Frame
from PIL import Image, ImageTk
import time

anch = 87
cara = {'longitud:': 12, 'mayus:': 'HOLA', 'newMensaje:': '¢OLA', 'minus:': 'hola', 'Cantidad_Palabras:': 12}

def screen3():
     print('pantalla 3')
     widgets = []

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
            print("es aqui")
        elif pantalla == "5":
            from screen4 import screen4
            ventana.after(100, lambda: [ventana.destroy(), screen4()])

     ventana = tk.Tk()
     ventana.title("Pantalla 4")
     ventana.geometry("375x812")
     ventana.config(bg="white")

     alert = Label(ventana, text="Pantalla 4")
     alert.pack(pady=10)

     men = Label(ventana, text="mensaje: ")
     men.pack(pady=10)

     global mensaje
     mensaje = Entry(ventana, width=25)
     mensaje.pack(pady=1)

     def caract():
        def cantidad(stri):
            contador = stri.split()
            numero_de_palabras = len(contador)
            print("cantidad de palabras: ", numero_de_palabras)
            return numero_de_palabras

        palabra = mensaje.get()
        longitud = len(palabra)
        print("longitud: ", longitud)
        may = palabra.upper()
        print("texto mayusculas: ", may)
        reemplazo = palabra.replace("o", "$")
        print("texto reemplazado 0 x $", reemplazo)
        minus = palabra.lower()
        print("texto minusculas: ", minus)
        

        #actualizar el diccionario
        cara['longitud:'] = longitud
        cara['mayus:'] = may
        cara['newMensaje:'] = reemplazo
        cara['newMensaje:'] = reemplazo
        cara['minus:'] = minus
        cara['Cantidad_Palabras:'] = cantidad(palabra)
        print(cara)

        mostrar(mensaje.get())
        
        

        

     button1 = Button(ventana, text="Investigar", command=lambda: caract())
     button1.pack(pady=10)

     carac = Label(ventana, text="caracteristicas: ")
     carac.pack(pady=10)


     def mostrar(palabra):
        for widget in widgets:
            widget.destroy()
        widgets.clear()


        nom = Label(ventana, text="palabra: " + palabra)
        nom.pack(pady=10)
        widgets.append(nom)
        for elemento in cara:
            print("elemento: ", elemento,  cara[elemento])
            testo = elemento,  cara[elemento]
            carac = Label(ventana, text=testo)
            carac.pack(pady=5)
            widgets.append(carac)

     mostrar("hola")




     #la barra
     barra_superior= Frame(ventana)
     barra_superior.config(height="430", bg="white")
     barra_superior.pack(fill="x", side=tk.BOTTOM, pady=30)

     #   ----------  imagenes ------------------
     # imagen 1 
     imagen_original = Image.open("assets/frutas.png")
     imagen_redimensionada = imagen_original.resize((anch, 50))
     imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

     # imagen 2 
     imagen_original2 = Image.open("assets/contactos.png")
     imagen_redimensionada2 = imagen_original2.resize((anch, 50))
     imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada2)

     # imagen 3
     imagen_original3 = Image.open("assets/calculadora.webp")
     imagen_redimensionada3 = imagen_original3.resize((anch, 50))
     imagen_tk3 = ImageTk.PhotoImage(imagen_redimensionada3)

     # imagen 4
     imagen_original4 = Image.open("assets/diccionario.png")
     imagen_redimensionada4 = imagen_original4.resize((anch, 50))
     imagen_tk4 = ImageTk.PhotoImage(imagen_redimensionada4)



     #pantalla uno


     #   ----------  Botones ------------------
     boton1 = tk.Button(barra_superior, text="Boton 1", image=imagen_tk, command=lambda: navegacion("1"), state="normal")
     boton1.pack(side="left", pady=5)

     #pantalla dos
     boton2 = tk.Button(barra_superior, text="Boton 2", image=imagen_tk2, command=lambda: navegacion("2"), state="normal")
     boton2.pack(side="left", pady=5)

     #pantalla tres
     boton3 = tk.Button(barra_superior, text="Boton 3", image=imagen_tk3, command=lambda: navegacion("3"), state="normal")
     boton3.pack(side="left", pady=5)

     #pantalla cuatro
     boton4 = tk.Button(barra_superior, text="Boton 4", image=imagen_tk4, command=lambda: navegacion("4"), state="normal")
     boton4.pack(side="left", pady=5)

     #pantalla cinco
     # boton5 = tk.Button(barra_superior, text="Boton 5", image=imagen_tk, command=lambda: navegacion("5"), state="normal")
     # boton5.pack(side="left", pady=5)

     # Iniciar el bucle principal de tkinter
     ventana.mainloop()