import tkinter as tk

#root = tk.Tk()
# root.title("Mi app")
# root.geometry("300x200")
# tk.Label(root, text="Hola").pack()

from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Mi primera interfaz gráfica")

def saludar():
    messagebox.showinfo("Saludo" , "¡Hola mundo!")

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=20)











ventana.mainloop()