import tkinter as tk

def convertir():
    millas = float(entry_millas.get())
    km = millas * 1.60934
    label_resultado.config(text=f"{km:.2f} Km")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Millas a Km")
ventana.geometry("600x300")  # Ajustar el tamaño de la ventana

# Crear y colocar la ventana de las millas
label_millas = tk.Label(ventana, text="Millas:")
label_millas.grid(column=0, row=0, padx=10, pady=10)


entry_millas = tk.Entry(ventana)
entry_millas.grid(column=1, row=0, padx=10, pady=10)

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(column=0, row=1, columnspan=2, pady=10)


label_resultado = tk.Label(ventana, text="0 Km")
label_resultado.grid(column=0, row=2, columnspan=2, pady=10)

# Iniciar el bucle principal
ventana.mainloop()
