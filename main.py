# Daniel Mora, Astrid Polanco, Felipe Guzman, Karol Rodriguez 
# Lista principal de datos
gastos = []

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
            print("   El valor debe ser mayor a 0.")
        except ValueError:
            print("   Ingrese un número válido.")
    
    gastos.append({"placa": placa, "concepto": concepto, "valor": valor})
    print("   Gasto registrado exitosamente.")

def mostrar_resumen():
    print("\n--- RESUMEN DE GASTOS ---")
    if len(gastos) == 0:
        print("   No hay gastos registrados.")
        return
    
    total = 0
    for gasto in gastos:
        total += gasto["valor"]
        print(f"  Placa: {gasto['placa']} | Concepto: {gasto['concepto']} | Valor: ${gasto['valor']:,.2f}")
    
    print("-" * 40)
    print(f"   TOTAL ACUMULADO: ${total:,.2f}")

# Función de búsqueda por placa - Desarrollado por Astrid Polanco
def buscar_gastos():
    print("\n--- BUSCAR GASTOS POR PLACA ---")
    if len(gastos) == 0:
        print("   No hay gastos registrados.")
        return
        
    placa_buscar = input("Ingrese la placa a buscar: ").strip().upper()
    encontrado = False
    
    for gasto in gastos:
        if gasto["placa"] == placa_buscar:
            encontrado = True
            print(f"  Concepto: {gasto['concepto']} | Valor: ${gasto['valor']:,.2f}")
    
    if not encontrado:
        print(f"   No se encontraron gastos para la placa: {placa_buscar}")

# --- NUEVA FUNCIÓN: ELIMINAR GASTO ---
def eliminar_gasto():
    print("\n--- ELIMINAR GASTO POR PLACA ---")
    if len(gastos) == 0:
        print("   No hay gastos registrados.")
        return

    placa_buscar = input("Ingrese la placa del vehículo para ver sus gastos: ").strip().upper()
    
    # Creamos una lista temporal para guardar los gastos que coinciden y sus posiciones reales en la lista 'gastos'
    coincidencias = []
    
    # Buscamos y enumeramos los gastos de esa placa
    for indice_real, gasto in enumerate(gastos):
        if gasto["placa"] == placa_buscar:
            coincidencias.append((indice_real, gasto))
            
    if len(coincidencias) == 0:
        print(f"   No se encontraron gastos para la placa: {placa_buscar}")
        return

    # Mostramos los gastos encontrados con un número de opción para el usuario
    print(f"\nGastos encontrados para la placa {placa_buscar}:")
    for i, (indice_real, gasto) in enumerate(coincidencias, start=1):
        print(f"  [{i}] Concepto: {gasto['concepto']} | Valor: ${gasto['valor']:,.2f}")

    # Validamos la selección del usuario
    while True:
        seleccion_str = input("\nIngrese el número del gasto que desea eliminar (o '0' para cancelar): ").strip()
        try:
            seleccion = int(seleccion_str)
            if seleccion == 0:
                print("   Operación cancelada.")
                return
            if 1 <= seleccion <= len(coincidencias):
                # Obtenemos el índice real en la lista principal y lo eliminamos usando pop()
                indice_a_borrar = coincidencias[seleccion - 1][0]
                gasto_eliminado = gastos.pop(indice_a_borrar)
                print(f"   ¡Éxito! Se eliminó el gasto de '{gasto_eliminado['concepto']}' por ${gasto_eliminado['valor']:,.2f}")
                return
            else:
                print(f"   Por favor, elija un número entre 1 y {len(coincidencias)}.")
        except ValueError:
            print("   Ingrese un número válido.")

def mostrar_menu():
    print("\n" + "=" * 40)
    print("   GESTOR DE GASTOS DE VEHÍCULOS ")
    print("=" * 40)
    print("  1. Registrar gasto")
    print("  2. Ver resumen de gastos")
    print("  3. Buscar gastos por placa")
    print("  4. Eliminar gasto") # Opción añadida
    print("  5. Salir")            # Cambió de 4 a 5
    print("=" * 40)

def main():
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            buscar_gastos()
        elif opcion == "4": # Caso añadido
            eliminar_gasto()
        elif opcion == "5": # Cambió de 4 a 5
            print("\n   ¡Hasta pronto!\n")
            break
        else:
            print("\n   Opción no válida.")

if __name__ == "__main__":
    main()