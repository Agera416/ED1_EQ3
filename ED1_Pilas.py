class Pila:
    def __init__(self, capacidad=8):
        self.items = []
        self.capacidad = capacidad

    def insertar(self, elemento):
        if len(self.items) < self.capacidad:
            self.items.append(elemento)
            print(f"Insertar {elemento} → Pila: {self.items}")
        else:
            print(" Error: Desbordamiento (la pila está llena)")

    def eliminar(self, nombre_op):
        if self.items:
            eliminado = self.items.pop()
            print(f"Eliminar {nombre_op} (sacando {eliminado}) → Pila: {self.items}")
        else:
            print(f" Error: Subdesbordamiento en operación {nombre_op} (la pila está vacía)")

# Simulación
pila = Pila()

pila.insertar("X")
pila.insertar("Y")
pila.eliminar("Z")
pila.eliminar("T")
pila.eliminar("U")   
pila.insertar("V")
pila.insertar("W")
pila.eliminar("p")
pila.insertar("R")

print("\nEstado final de la pila:", pila.items)
