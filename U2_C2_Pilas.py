class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def __str__(self):
        return f"{self.nombre}: {self.items}"


def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        disco = origen.pop()
        destino.push(disco)
        print(f"Mover disco {disco} de {origen.nombre} → {destino.nombre}")
    else:
        hanoi(n-1, origen, destino, auxiliar)
        hanoi(1, origen, auxiliar, destino)
        hanoi(n-1, auxiliar, origen, destino)


# ------- Ejemplo con 3 discos -------
torreA = Pila("A")
torreB = Pila("B")
torreC = Pila("C")

# Insertamos discos (3, 2, 1) en la torre A (de mayor abajo a menor arriba)
for disco in [3, 2, 1]:
    torreA.push(disco)

print("Resolviendo Torres de Hanoi con 3 discos:\n")
hanoi(3, torreA, torreB, torreC)

print("\nEstado final:")
print(torreA)
print(torreB)
print(torreC)
