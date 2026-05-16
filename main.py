# Lista principal de datos
gastos = []

# Funciones vacías que los demás llenarán
def registrar_gasto():
    print("\n--- REGISTRAR NUEVO GASTO ---")
    placa = input("Placa del vehículo: ").strip().upper()
    concepto = input("Concepto (Ej: Gasolina, Peaje): ").strip().capitalize()
    
    # Validar que el valor sea un número
    while True:
        valor_str = input("Valor ($): ").strip()
        try:
            valor = float(valor_str)
            if valor > 0:
                break
            print("  ⚠ El valor debe ser mayor a 0.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")
    
    # Guardar en la lista como diccionario
    gastos.append({"placa": placa, "concepto": concepto, "valor": valor})
    print("  ✅ Gasto registrado exitosamente.")

def mostrar_resumen():
    pass # El estudiante 3 programará aquí

def buscar_gastos():
    pass # El estudiante 4 programará aquí

def mostrar_menu():
    print("\n" + "=" * 40)
    print("   GESTOR DE GASTOS DE VEHÍCULOS ")
    print("=" * 40)
    print("  1. Registrar gasto")
    print("  2. Ver resumen de gastos")
    print("  3. Buscar gastos por placa")
    print("  4. Salir")
    print("=" * 40)

def main():
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            buscar_gastos()
        elif opcion == "4":
            print("\n   ¡Hasta pronto!\n")
            break
        else:
            print("\n   Opción no válida.")

if __name__ == "__main__":
    main()
