import tkinter as tk

root = tk.Tk()
root.title("Listbox")
root.geometry("500x500")


listbox = tk.Listbox(root, height=3, selectmode=tk.SINGLE)
listbox.pack(padx= 20, pady=30)

text = "abcde"
for i in text:
    listbox.insert(tk.END, i)

seleccionado = tk.Label(root, text = "")
seleccionado.pack(padx= 20, pady=30)

def mostrar (event):
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        valor = listbox.get(indice)
        seleccionado.config(text = valor)


listbox.bind("<<ListboxSelect>>", mostrar)
root.bind("<Return>", mostrar)


root.mainloop()
