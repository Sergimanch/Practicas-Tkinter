import tkinter as tk
def sumar():
    a = int(entrada1.get())
    b = int(entrada2.get())
    label.config(text = a + b)
root = tk.Tk()
root.geometry("300x200")

entrada1 = tk.Entry(root)
entrada1.pack()
entrada2 = tk.Entry(root)
entrada2.pack()

boton = tk.Button(root, text="Sumar", command=sumar)
boton.pack()

label =tk.Label(root, text="0")
label.pack()



root.mainloop()