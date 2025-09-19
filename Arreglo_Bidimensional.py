# EMIR ALBERTO PINO MALDONADO


import random

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

departamentos = ["Ropa", "Deportes", "Juguetería"]

ventas_tienda = [[random.randint(500, 10000) for _ in range(len(departamentos))] 
                 for _ in range(len(meses))]

def insertar_venta(mes, depto, valor):
    ventas_tienda[mes][depto] = valor

def buscar_venta(mes, depto):
    return ventas_tienda[mes][depto]

def eliminar_venta(mes, depto):
    ventas_tienda[mes][depto] = "/////"

def imprimir_tabla():
    print(f"{'Mes':<12}{'Ropa':<12}{'Deportes':<12}{'Juguetería':<12}")
    for i, fila in enumerate(ventas_tienda):
        print(f"{meses[i]:<12}", end="")
        for venta in fila:
            print(f"{venta:<12}", end="")
        print()

print("=== VENTAS INICIALES ===")
imprimir_tabla()

print("\n--- PRUEBAS DE FUNCIONES ---")
print("Venta en Febrero (Deportes):", buscar_venta(1, 1))  

insertar_venta(2, 2, 9999)  
print("Nueva venta en Marzo (Juguetería):", buscar_venta(2, 2))

eliminar_venta(2, 0)  
print("Venta eliminada en Marzo (Ropa):", buscar_venta(2, 0))

print("\n=== VENTAS FINALES ===")
imprimir_tabla()
