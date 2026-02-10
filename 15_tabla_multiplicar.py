import tkinter as tk

def multiplicar():
    txt = ""
    a = int(e1.get())

    for i in range(1, 11):
        txt += f"{a} x {i} = {a*i}\n"
    resu.config(text = txt)

root = tk.Tk()
root.title("Calucladora básica")

tk.Label(root, text="Numero:").grid(row=0, column=0, padx=0, pady=15, sticky="e")

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10,pady=5)



tk.Button(root, text="Multiplicar", command = multiplicar).grid(row = 2, column=0, columnspan=2, pady=10)

resu = tk.Label(root, text="Resultado:")
resu.grid(row=3, column=0, columnspan=2, pady=10, sticky= "we")

root.mainloop()