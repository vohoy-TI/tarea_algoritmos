import openpyxl
from openpyxl import Workbook

def crear_archivo_excel():
    # Crear un nuevo libro de Excel y una hoja de cálculo
    libro = Workbook()
    hoja = libro.active
    hoja.title = "Gastos"
    
    # Agregar encabezados
    hoja.append(["Fecha", "Descripción", "Monto"])
    
    # Guardar el archivo
    libro.save("informe_gastos.xlsx")

def agregar_gastos(hoja):
    gastos = []
    
    while True:
        # Solicitar detalles del gasto
        fecha = input("Ingrese la fecha en numeros (dia-mes-año): ")
        descripcion = input("Ingrese la descripción del gasto: ")
        monto = float(input("Ingrese el monto del gasto: "))
        
        # Agregar los datos a la hoja de cálculo
        hoja.append([fecha, descripcion, monto])
        
        # Guardar el gasto en la lista
        gastos.append({"fecha": fecha, "descripcion": descripcion, "monto": monto})
        
        # Preguntar si desea ingresar otro gasto
        continuar = input("¿Desea ingresar otro gasto? (s/n): ").lower()
        if continuar != 's':
            break
    
    return gastos

def generar_informe(gastos):
    if not gastos:
        print("No se ingresaron gastos.")
        return
    
    total_gastos = sum(gasto["monto"] for gasto in gastos)
    gasto_mas_caro = max(gastos, key=lambda x: x["monto"])
    gasto_mas_barato = min(gastos, key=lambda x: x["monto"])
    
    # Mostrar el resumen en consola
    print("\nResumen de Gastos:")
    print(f"Número total de gastos: {len(gastos)}")
    print(f"Gasto más caro: {gasto_mas_caro['descripcion']} el {gasto_mas_caro['fecha']} por ${gasto_mas_caro['monto']:.2f}")
    print(f"Gasto más barato: {gasto_mas_barato['descripcion']} el {gasto_mas_barato['fecha']} por ${gasto_mas_barato['monto']:.2f}")
    print(f"Monto total de gastos: ${total_gastos:.2f}")

def main():
    crear_archivo_excel()
    
    # Cargar el archivo existente
    libro = openpyxl.load_workbook("informe_gastos.xlsx")
    hoja = libro["Gastos"]
    
    # Agregar gastos
    gastos = agregar_gastos(hoja)
    
    # Generar informe
    generar_informe(gastos)
    
    # Guardar cambios en el archivo Excel
    libro.save("informe_gastos.xlsx")
    print("\nInforme de gastos guardado en 'informe_gastos.xlsx'.")

if __name__ == "__main__":
    main()
