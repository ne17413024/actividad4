import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, PhotoImage, Frame
from PIL import Image, ImageTk
import time

anch = 87 
    
def screen2():
     print('pantalla 2')
    # Variables globales para operaciones
     operacion = None
     primer_numero = None

     def navegacion(pantalla):
        if pantalla == "1":
            from main import inicio
            ventana.after(100, lambda: [ventana.destroy(), inicio()])
        elif pantalla == "2":
            from screen1 import screen1
            ventana.after(100, lambda: [ventana.destroy(), screen1()])
        elif pantalla == "3":
            print("es aqui")
        elif pantalla == "4":
            from screen3 import screen3
            ventana.after(100, lambda: [ventana.destroy(), screen3()])
        elif pantalla == "5":
            from screen4 import screen4
            ventana.after(100, lambda: [ventana.destroy(), screen4()])


     ventana = tk.Tk()
     ventana.title("Pantalla 3")
     ventana.geometry("375x812")
     ventana.config(bg="white")

     alert = Label(ventana, text="Pantalla 3")
     alert.pack(pady=10)

     tit = Label(ventana, text="Calculadora ")
     tit.pack(pady=10)


     def agregar_numero(num):
        entrada_var.set(entrada_var.get() + num)
        print(entrada_var.get())

     def set_operacion(op):
        global operacion, primer_numero 
        operacion = op
        primer_numero = entrada_var.get()
        entrada_var.set('')

     def calcular():
        global primer_numero, operacion  
        try:
            segundo_numero = entrada_var.get()

            if not primer_numero:  
                entrada_var.set('Error: Falta primer número')
                return

            if not segundo_numero: 
                entrada_var.set('Error: Falta segundo número')
                return

            # Convertir los números a flotantes
            primer_valor = float(primer_numero)
            segundo_valor = float(segundo_numero)

        
            if operacion == '+':
                resultado = primer_valor + segundo_valor
            elif operacion == '-':
                resultado = primer_valor - segundo_valor
            elif operacion == '*':
                resultado = primer_valor * segundo_valor
            elif operacion == '/':
                
                if segundo_valor == 0:
                    resultado = 'Error: División por cero'
                else:
                    resultado = primer_valor / segundo_valor
            else:
                resultado = 'Error: Operación desconocida'

            entrada_var.set(str(resultado))

        except ValueError as ve:
            entrada_var.set(f'Error: {ve}')  # Error si los valores no son válidos
        except Exception as e:
            entrada_var.set(f'Error: {e}')  # Mostrar cualquier otro error
 
     def borrar():
        entrada_var.set('')
     
     
     # Variable para mostrar los números y resultados
     entrada_var = tk.StringVar()
     entrada = tk.Entry(ventana, textvariable=entrada_var, font=('Arial', 16), borderwidth=2, relief="solid")
     entrada.pack(padx=10, pady=10)
     
     teclado_frame = Frame(ventana)
     teclado_frame.pack(pady=20)
     botones = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 1)
     ]

     for (text, row, col) in botones:
        boton = tk.Button(teclado_frame, text=text, width=5, height=2, command=lambda t=text: agregar_numero(t))
        boton.grid(row=row, column=col, padx=5, pady=5)

     # Botones de operaciones
     operaciones = [
        ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
        ('=', 4, 2), ('C', 4, 0)
     ]

     for (text, row, col) in operaciones:
        if text == '=':
            boton = tk.Button(teclado_frame, text=text, width=5, height=2, command=calcular)
        elif text == 'C':
            boton = tk.Button(teclado_frame, text=text, width=5, height=2, command=borrar)
        else:
            boton = tk.Button(teclado_frame, text=text, width=5, height=2, command=lambda t=text: set_operacion(t))
        boton.grid(row=row, column=col, padx=5, pady=5)









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