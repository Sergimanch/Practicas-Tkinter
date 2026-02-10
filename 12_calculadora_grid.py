import tkinter as tk

root = tk.Tk()
root.title("Calculadora grid")

pantalla = tk.Entry(root, justify="right")

pantalla.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

tk.Button(root, text="1").grid(row=1, column=0)
tk.Button(root, text="2").grid(row=1, column=1)
tk.Button(root, text="3").grid(row=1, column=2)

tk.Button(root, text="4").grid(row=2, column=0)
tk.Button(root, text="5").grid(row=2, column=1)
tk.Button(root, text="6").grid(row=2, column=2)

tk.Button(root, text="0").grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()