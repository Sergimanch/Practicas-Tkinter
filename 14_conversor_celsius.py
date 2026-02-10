import tkinter as tk

root = tk.Tk()
root.geometry("300x400")

def convertir():
    try:
        c = float(celsius.get())
        f = c * 9 / 5 + 32
        resultado.config(text=f"Fahrenheit: {f:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

def fahrenheit_a_celsius():
    try:
        f = float(entry_f.get())
        c = (f - 32) * 5 / 9
        mostrar_resultado(c, c, "Celsius")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido en Fahrenheit")

celsius = tk.Label(text="Celsius").grid(row=0, column=0, pady=10, sticky="w")
fahrenheit = tk.Label(text="Fahrenheit").grid(row=1, column=0, pady=10,  sticky="w")

