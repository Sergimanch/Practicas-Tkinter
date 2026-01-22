import tkinter as tk

root = tk.Tk()
root.title("Label")
label = tk.Label(root, text = "Andrea es la Chusa")
label.pack(padx=60)
label.pack(pady=60)

root.mainloop()