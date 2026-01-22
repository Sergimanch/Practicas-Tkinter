import tkinter as tk

contador =0
def sumar():
    global contador
    contador+=1
    label.config(text = contador)
def restar():
    global contador
    contador-=1
    label.config(text = contador)


root=tk.Tk()

label = tk.Label(root, text = contador)
label.pack()

boton = tk.Button(root, text = "+", command = sumar )
boton.pack()

boton1 = tk.Button(root, text = "-", command = restar )
boton1.pack()
tk.mainloop()