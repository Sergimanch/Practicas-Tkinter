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

genero = tk.StringVar(value="")

labelGenero = tk.Label(root, text="Selecciona tu género:")
labelGenero.grid(column=0, columnspan=3, row=5, pady=20)

radioHombre = tk.Radiobutton(root, text="Hombre", variable=genero, value="Hombre")
radioHombre.grid(column=0, row=6, sticky="w", padx=20)

radioMujer = tk.Radiobutton(root, text="Mujer", variable=genero, value="Mujer")
radioMujer.grid(column=1, row=6, sticky="w")

radioOtro = tk.Radiobutton(root, text="Otro", variable=genero, value="Otro")
radioOtro.grid(column=2, row=6, sticky="w")

def saludar ():
    gen = genero.get()
    if gen == "Hombre":
        final.config(text = f"Bienvenido: {nombre.get()} {apellido.get()} nacido en {seleccionar()}.")
    elif gen == "Mujer":
        final.config(text = f"Bienvenida: {nombre.get()} {apellido.get()} nacida en {seleccionar()}.")
    else: 
        final.config(text = f"Bienvenid@: {nombre.get()} {apellido.get()} nacid@ en {seleccionar()}.")

boton = tk.Button(root, text= "Saludar", command=saludar)
boton.grid(row = 7, columnspan=3, pady=10)

final = tk.Label(root, text="Bienvenid@...")
final.grid(row = 8, pady = 20, columnspan=200)
root.bind("<Return>", seleccionar)




root.mainloop()