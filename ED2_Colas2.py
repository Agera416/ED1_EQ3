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

    def __len__(self):
        return len(self.items)

def sistema_servicios():
    servicios = {1: Cola(), 2: Cola(), 3: Cola()}
    contadores = {1: 0, 2: 0, 3: 0}

    while True:
        comando = input().upper().strip()
        if comando == 'S':
            break
        if len(comando) < 2 or not comando[1:].isdigit():
            continue
        accion = comando[0]
        servicio = int(comando[1:])
        if servicio not in servicios:
            continue
        if accion == 'C':
            contadores[servicio] += 1
            numero = contadores[servicio]
            servicios[servicio].encolar(numero)
            print(f"Cliente agregado al servicio {servicio}. Número de atención: {numero}")
        elif accion == 'A':
            if servicios[servicio].esta_vacia():
                print(f"No hay clientes en la cola del servicio {servicio}.")
            else:
                numero = servicios[servicio].desencolar()
                print(f"Atendiendo al cliente número {numero} del servicio {servicio}.")

if __name__ == "__main__":
    sistema_servicios()
