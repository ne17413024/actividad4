import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, PhotoImage, Frame
from PIL import Image, ImageTk

# pagina que me va ayudar para los botones o el reloj (el header)  
#  https://es.stackoverflow.com/questions/399619/c%C3%B3mo-puedo-hacer-que-un-bot%C3%B3n-cambie-su-icono-seg%C3%BAn-si-est%C3%A1-normal-activo-o-pr
anch = 87

def inicio():

    def navegacion(pantalla):
        if pantalla == "1":
            print("es aqui")
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
            from screen4 import screen4
            ventana.after(100, lambda: [ventana.destroy(), screen4()])

    frutas = ["manzana", "pera", "fresa", "manzana verde", "manzana roja"]
    widgets = []
    etiqueta = []

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Pantalla 1")
    ventana.geometry("375x812")
    ventana.config(bg="white")

    alert = Label(ventana, text="Pantalla 1")
    alert.pack(pady=10)


    global Cant_Elementos
    Cant_Elementos = Entry(ventana, width=25, state="readonly")
    Cant_Elementos.pack(pady=5)

    def cambiar():

        def lista():
            prueba = []
            for elemento in frutas:
                print("elemento de las frutas: ", elemento)
                
                prueba.append(1)
       
            suma = sum(prueba)
            print("total DE ELEMENTOS: ", suma)
            return f"Cantidad de elementos {suma}"

        Cant_Elementos.config(state="normal")  # Habilitar temporalmente para modificar el campo
        Cant_Elementos.delete(0, 'end')
        Cant_Elementos.insert(tk.END, lista())
        Text = lista()
        Cant_Elementos.config(state="readonly")
    cambiar()

    global entry_nombre
    entry_nombre = Entry(ventana, width=25)
    entry_nombre.pack(pady=5)
    def añadir():
        frutas.append(entry_nombre.get())
        entry_nombre.delete(0, 'end')
        print(frutas)
        cambiar()
       
        elementos()
        
    agregar = tk.Button(ventana, text="Agregar",command= lambda: añadir(), state="normal")
    agregar.pack( pady=5)




    tuplas = Label(ventana, text="Frutas: ")
    tuplas.pack( pady=5)

    def elementos():
   
        for widget in widgets:
            widget.destroy()
        widgets.clear()

        frutas_ordenadas = sorted(frutas) 

        for elemento in frutas_ordenadas:
            print("hola")
    
            tupla_label = Label(ventana, text=elemento)
            tupla_label.pack(pady=2)
            widgets.append(tupla_label)

    # Llamar a la función
    elementos()

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
    # boton5.pack(side="left", pady=5)

    # Iniciar el bucle principal de tkinter
    ventana.mainloop()

if __name__ == "__main__":
    inicio()