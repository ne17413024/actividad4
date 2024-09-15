import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, PhotoImage, Frame
from PIL import Image, ImageTk
import time

anch = 87
    
def screen1():
     print('pantalla 1')
     widgets = []

     contactos = {
        'nata':{
            'pais': '+52',
            'correo': 'natanaelja@gmial.com',
            'celular': 4521222255
        },
        'samuel':{
            'pais': '+52',
            'correo': 'prueba@gmail.com',
            'celular': 4521222255
        }
     }

     def navegacion(pantalla):
        if pantalla == "1":
            from main import inicio
            ventana.after(100, lambda: [ventana.destroy(), inicio()])
        elif pantalla == "2":
            print("es aqui")
        elif pantalla == "3":
            from screen2 import screen2
            ventana.after(100, lambda: [ventana.destroy(), screen2()])
        elif pantalla == "4":
            from screen3 import screen3
            ventana.after(100, lambda: [ventana.destroy(), screen3()])
        elif pantalla == "5":
            from screen4 import screen4
            ventana.after(100, lambda: [ventana.destroy(), screen4()])

     ventana = tk.Tk()
     ventana.title("Pantalla 2")
     ventana.geometry("375x812")
     ventana.config(bg="white")

     alert = Label(ventana, text="Pantalla 2")
     alert.pack(pady=10)


     def añadir():
        print("boton añadir")
        popupwindow = Toplevel(ventana)
        popupwindow.title("Alert")
        popupwindow.geometry("600x400")

        alert = Label(popupwindow, text="Ingrese los datos del nuevo contacto:")
        alert.pack(pady=10)

        alert = Label(popupwindow, text="Nombre:")
        alert.pack(pady=1)
        global entry_nombre
        entry_nombre = Entry(popupwindow, width=25)
        entry_nombre.pack(pady=1)

        Pais = Label(popupwindow, text="Correo:")
        Pais.pack(pady=1)
        global entry_Pais
        entry_Pais = Entry(popupwindow, width=25)
        entry_Pais.pack(pady=1)

        Ciudad = Label(popupwindow, text="Denominacion del pais:")
        Ciudad.pack(pady=1)
        global entry_Ciudad
        entry_Ciudad = Entry(popupwindow, width=25)
        entry_Ciudad.pack(pady=1)

        Numero = Label(popupwindow, text="Numero:")
        Numero.pack(pady=1)
        global entry_Numero
        entry_Numero = Entry(popupwindow, width=25)
        entry_Numero.pack(pady=1)

        def agregar():
            contactos[entry_nombre.get()] = {
                'pais': entry_Pais.get(),  
                'correo': entry_Ciudad.get(),    
                'celular': entry_Numero.get()  
            }
            mostrar_contactos()
            print("se agregaron", contactos)
            popupwindow.destroy()

        button1 = Button(popupwindow, text="OK", command=lambda: agregar())
        button1.pack(pady=10)

     def buscar():
        print("boton buscar")
        popupwindow = Toplevel(ventana)
        popupwindow.title("Alert")
        popupwindow.geometry("600x400")

        alert = Label(popupwindow, text="Ingrese los datos del contacto:")
        alert.pack(pady=10)

        Nombre = Label(popupwindow, text="Nombre:")
        Nombre.pack(pady=1)
        global entry_Nombre
        entry_Nombre = Entry(popupwindow, width=25)
        entry_Nombre.pack(pady=1)

        # Función que realiza la búsqueda
        def realizar_busqueda():
            nombre = entry_Nombre.get()
            if nombre in contactos:
                detalles = contactos[nombre]
                resultado = f"Contacto encontrado:\nNombre: {nombre}\n"
                for clave, valor in detalles.items():
                    resultado += f"{clave.capitalize()}: {valor}\n"
                resultado_label.config(text=resultado)
            else:
                resultado_label.config(text="Contacto no encontrado.")


        button1 = Button(popupwindow, text="Buscar", command=realizar_busqueda)
        button1.pack(pady=10)

        button1 = Button(popupwindow, text="Cerrar", command=popupwindow.destroy)
        button1.pack()

        resultado_label = Label(popupwindow, text="")
        resultado_label.pack(pady=10)
        

     agregar = tk.Button(ventana, text="Agregar",command= lambda: añadir(), state="normal")
     agregar.pack(pady=5)

     BTbuscar = tk.Button(ventana, text="Buscar",command= lambda: buscar(), state="normal")
     BTbuscar.pack(pady=5)

     contac = Label(ventana, text="Contactos:")
     contac.pack()



    # Función para mostrar los contactos
     def mostrar_contactos():
        for widget in widgets:
            widget.destroy()
        widgets.clear()

        for nombre, detalles in contactos.items():
       
            nombre_label = Label(ventana, text=f"Nombre: {nombre}")
            nombre_label.pack(pady=(20, 0))
            widgets.append(nombre_label)

            for clave, valor in detalles.items():
                detalle_label = Label(ventana, text=f"  {clave.capitalize()}: {valor}")
                detalle_label.pack()
                widgets.append(detalle_label)

       

            
            

     mostrar_contactos()


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


     #pantalla dos


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