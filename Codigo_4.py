
import random

vector_a = []
vector_b = []
vector_c = []

while True:
    try:
        n = int(input("Ingrese la longitud de los vectores: "))
        if n <= 0:
            print("La longitud debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un número válido.")

def llenar_vector_aleatorio(longitud):
    return [random.randint(-100, 100) for _ in range(longitud)]

def mostrar_vector(vector, nombre):
    print(f"\n{name_format(nombre)}:")
    for i, valor in enumerate(vector):
        print(f"  Posición {i}: {valor}")

def name_format(nombre):
    return f"Contenido de {nombre}"

while True:
    print("\n--- MENÚ ---")
    print("1. Llenar Vector A de manera aleatoria")
    print("2. Llenar Vector B de manera aleatoria")
    print("3. Realizar C = A + B")
    print("4. Realizar C = B - A")
    print("5. Mostrar Vector (A, B, C)")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        vector_a = llenar_vector_aleatorio(n)
        print("Vector A llenado exitosamente.")
    elif opcion == "2":
        vector_b = llenar_vector_aleatorio(n)
        print("Vector B llenado exitosamente.")
    elif opcion == "3":
        if len(vector_a) != n or len(vector_b) != n:
            print("Debe llenar primero los vectores A y B con la longitud correcta.")
        else:
            vector_c = [vector_a[i] + vector_b[i] for i in range(n)]
            print("Vector C = A + B calculado correctamente.")
    elif opcion == "4":
        if len(vector_a) != n or len(vector_b) != n:
            print("Debe llenar primero los vectores A y B con la longitud correcta.")
        else:
            vector_c = [vector_b[i] - vector_a[i] for i in range(n)]
            print("Vector C = B - A calculado correctamente.")
    elif opcion == "5":
        eleccion = input("¿Qué vector desea mostrar? (A/B/C): ").upper()
        if eleccion == "A":
            if vector_a:
                mostrar_vector(vector_a, "Vector A")
            else:
                print("Vector A no ha sido llenado aún.")
        elif eleccion == "B":
            if vector_b:
                mostrar_vector(vector_b, "Vector B")
            else:
                print("Vector B no ha sido llenado aún.")
        elif eleccion == "C":
            if vector_c:
                mostrar_vector(vector_c, "Vector C")
            else:
                print("Vector C no ha sido calculado aún. Use la opción 3 o 4.")
        else:
            print("Opción inválida.")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")
