import tkinter as tk

def cambiar():
    a = "ON"
    label.config(text = a)
root = tk.Tk()
a = "OFF"
label = tk.Label(root, text = a)
label.pack(pady=10)

boton = tk.Button(root, text="Cambiar", command = cambiar)
boton.pack()

root.mainloop()