#Calculadora de divisas
import tkinter as tk

def convertir():
    cantidad = float(entry_cantidad.get())
    tasa = float(entry_tasa.get())
    resultado = cantidad * tasa
    label_resultado.config(text=f"{resultado:.2f}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Divisas")
ventana.geometry("400x300")  # Ajustar el tamaño de la ventana

# Crear y colocar la ventana de la cantidad 
label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.grid(column=0, row=0, padx=10, pady=10)

entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(column=1, row=0, padx=10, pady=10)

#crear la ventana de la tasa de cambio 
label_tasa = tk.Label(ventana, text="Tasa de Cambio:")
label_tasa.grid(column=0, row=1, padx=10, pady=10)

entry_tasa = tk.Entry(ventana)
entry_tasa.grid(column=1, row=1, padx=10, pady=10)

#creamos el boton para convertir 
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir, width=20, height=2, bg="purple", fg="white")
boton_convertir.grid(column=0, row=2, columnspan=2, pady=10)

#creamos la ventana del resultado
label_resultado = tk.Label(ventana, text="Resultado")
label_resultado.grid(column=0, row=3, columnspan=2, pady=10)

# Iniciar el bucle principal
ventana.mainloop()
