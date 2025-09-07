# EMIR ALBERTO PINO MALDONADO ESTRUCTURA DE DATOS AD2

def memoria_estatica():
    calificaciones = [0] * 5  

    for i in range(5):
        calificaciones[i] = int(input("Captura la calificación: "))

    print("Calificaciones capturadas:", calificaciones)


def memoria_dinamica():
    frutas = [] 
    frutas.append("mango")
    frutas.append("manzana")
    frutas.append("banana")
    frutas.append("uvas")
    frutas.append("pitaya")
    frutas.append("maracuya")
    print("Frutas iniciales:", frutas)

    frutas.pop(0) 
    frutas.pop(1)  
    frutas.append("sandía")
    print("Frutas finales:", frutas)


if __name__ == "__main__":
    print("=== Memoria Estática ===")
    memoria_estatica()

    print("\n=== Memoria Dinámica ===")
    memoria_dinamica()
