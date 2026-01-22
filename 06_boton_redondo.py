import tkinter as tk

def cambiar():
    label.config(fg=color.get())

root = tk.Tk()

color = tk.StringVar(value="black")
for c in ["red", "green","blue"]:
    tk.Radiobutton(root, text = c, value=c, variable=color, command=cambiar).pack()

label = tk.Label(root, text = "Andrea es tonta")
label.pack(pady= 10)

root.mainloop()