import tkinter as tk
root = tk.Tk()
root.geometry("400x500")
root.configure(bg="grey")

def sumar():
    a = int(entrada1.get())
    b = int(entrada2.get())
    label.config(text = a + b)
    simbolo.config(text ="+")
def restar():
    a = int(entrada1.get())
    b = int(entrada2.get())
    label.config(text = a - b)
    simbolo.config(text ="-")
def multiplicar():
    a = int(entrada1.get())
    b = int(entrada2.get())
    label.config(text = a * b)
    simbolo.config(text ="*")
def dividir():
    a = int(entrada1.get())
    b = int(entrada2.get())
    label.config(text = a / b)
    simbolo.config(text ="/")


entrada1 = tk.Entry(root)
entrada1.grid(column = 0, columnspan= 2, row = 0, pady = 10, padx = 10)
entrada2 = tk.Entry(root)
entrada2.grid(column = 3, columnspan= 2, row = 0, padx=10)
simbolo = tk.Label(root, text= " ")
simbolo.grid(row = 0, column = 2)
simbolo.configure(bg = "grey")


label = tk.Label(root, text= "...")
label.grid(row = 1, column=2)
label.configure(bg = "yellow")


bot1 = tk.Button(root, text="Sumar", command=sumar)
bot1.grid(row = 3, column=0, columnspan=2)
bot2 = tk.Button(root, text="Restar", command=restar)
bot2.grid(row = 3, column=3, columnspan=2)
bot3 = tk.Button(root, text="Multiplicar", command=multiplicar)
bot3.grid(row = 5, column=0, columnspan=2)
bot4 = tk.Button(root, text="Dividir", command=dividir)
bot4.grid(row = 5, column=3, columnspan=2)


root.mainloop()