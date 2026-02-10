import tkinter as tk

root = tk.Tk()
root.title("Mi app")
root.geometry("300x200")
root.configure(bg="lightblue")
tk.Label(root, text="Mi primera GUI").pack(pady = 30)

root.mainloop()