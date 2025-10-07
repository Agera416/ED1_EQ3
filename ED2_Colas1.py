from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, elemento):
        self.items.append(elemento)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        else:
            return None
    
    def ver_primero(self):
        if not self.esta_vacia():
            return self.items[0]
        return None
    
    def __len__(self):
        return len(self.items)
    
    def mostrar(self):
        print(list(self.items))

def sumar_colas(colaA, colaB):
    cola_resultado = Cola()
    while not colaA.esta_vacia() and not colaB.esta_vacia():
        a = colaA.desencolar()
        b = colaB.desencolar()
        cola_resultado.encolar(a + b)
    return cola_resultado

colaA = Cola()
colaB = Cola()

for n in [3, 4, 2, 8, 12]:
    colaA.encolar(n)

for n in [6, 2, 9, 11, 3]:
    colaB.encolar(n)

print("Cola A:", end=" ")
colaA.mostrar()
print("Cola B:", end=" ")
colaB.mostrar()

resultado = sumar_colas(colaA, colaB)
print("Cola Resultado:", end=" ")
resultado.mostrar()
