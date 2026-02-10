import tkinter as tk

def sumar():
    a = int(e1.get())
    b = int(e2.get())
    resu.config(text = a + b)

root = tk.Tk()
root.title("Calucladora básica")

tk.Label(root, text="Numero 1").grid(row=0, column=0, padx=0, pady=15, sticky="e")
tk.Label(root, text="Numero 2").grid(row=1, column=0, padx=0, pady=15, sticky="e")

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10,pady=5)

e2 = tk.Entry(root)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Sumar", command = sumar).grid(row = 2, column=0, columnspan=2, pady=10)

resu = tk.Label(root, text="Resultado:")
resu.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()