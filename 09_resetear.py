import tkinter as tk
def sumar():
    a = int(entrada1.get())
    b = int(entrada2.get())
    label.config(text = a + b)
root = tk.Tk()
root.geometry("400x400")

entrada1 = tk.Entry(root)
entrada1.pack()
entrada2 = tk.Entry(root)
entrada2.pack()

boton = tk.Button(root, text="Sumar", command=sumar)
boton.pack()

def resetear():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    label.config(text="0")
botonReset = tk.Button(root, text="Resetear", command=resetear)
botonReset.pack()
label =tk.Label(root, text="0")
label.pack()



root.mainloop()