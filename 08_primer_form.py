import tkinter as tk

root = tk.Tk()
root.title("Formulario")
root.geometry("600x700")

titulo = tk.Label(root, text="Formulario Básico")
titulo.grid(row=0, columnspan=3)

labelNombre = tk.Label(root, text="Nombre:")
labelNombre.grid(column=0, row=1, pady= 20)
nombre = tk.Entry(root)
nombre.grid(column=1, columnspan=2, row=1)

labelApellido = tk.Label(root, text="Apellido:", pady= 20)
labelApellido.grid(column=0, row=2)
apellido = tk.Entry(root)
apellido.grid(column=1, columnspan=2,  row=2)

previosAnos = []
for i in range (1990, 2026):
    previosAnos.append(i)

labelAnos = tk.Label(root, text="Selecciona tu año de nacimiento")
labelAnos.grid(column=0, columnspan=3, row=3, pady=20)
listaAnos = tk.Listbox(root, height= 4 )
listaAnos.grid(column=0, columnspan=3, row = 4 )

for i in previosAnos:
    listaAnos.insert(tk.END, i)

def seleccionar (event=None):
    seleccion = listaAnos.curselection()
    if seleccion:
        indice = seleccion[0]
        valor = listaAnos.get(indice)
        return valor

def saludar ():
    final.config(text = f"Bienvenid@: {nombre.get()} {apellido.get()} nacido en {seleccionar()}.")

boton = tk.Button(root, text= "Saludar", command=saludar)
boton.grid(row = 5, columnspan=3, pady=10)

final = tk.Label(root, text="Bienvenid@...")
final.grid(row = 7, pady = 20)
root.bind("<Return>", seleccionar)




root.mainloop()