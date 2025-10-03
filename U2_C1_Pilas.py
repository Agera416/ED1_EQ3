class Pila:
    def __init__(self):
        self.items = []

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


# ------------------ PRIORIDAD ------------------
def prioridad(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


# ------------------ INFIX → POSTFIX ------------------
def infija_a_posfija(expresion):
    pila = Pila()
    salida = []
    for token in expresion:
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.push(token)
        elif token == ')':
            while not pila.esta_vacia() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()  # quitar el "("
        else:  # operador
            while (not pila.esta_vacia() and prioridad(token) <= prioridad(pila.peek())):
                salida.append(pila.pop())
            pila.push(token)

    while not pila.esta_vacia():
        salida.append(pila.pop())

    return ''.join(salida)


# ------------------ INFIX → PREFIX ------------------
def infija_a_prefija(expresion):
    # Invertimos la expresión, cambiando paréntesis
    expresion = expresion[::-1]
    expresion = expresion.replace('(', 'tmp').replace(')', '(').replace('tmp', ')')

    # Convertimos a posfija con la expresión invertida
    posfija = infija_a_posfija(expresion)

    # Invertimos la salida para obtener prefija
    return posfija[::-1]


# ------------------ EVALUAR POSTFIJO ------------------
def evaluar_posfija(expresion):
    pila = Pila()
    for token in expresion:
        if token.isdigit():
            pila.push(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+': pila.push(a + b)
            elif token == '-': pila.push(a - b)
            elif token == '*': pila.push(a * b)
            elif token == '/': pila.push(a / b)
    return pila.pop()


# ------------------ EVALUAR PREFIJO ------------------
def evaluar_prefija(expresion):
    pila = Pila()
    for token in expresion[::-1]:
        if token.isdigit():
            pila.push(int(token))
        else:
            a = pila.pop()
            b = pila.pop()
            if token == '+': pila.push(a + b)
            elif token == '-': pila.push(a - b)
            elif token == '*': pila.push(a * b)
            elif token == '/': pila.push(a / b)
    return pila.pop()


# ------------------ PROGRAMA PRINCIPAL ------------------
print("=== Conversor y Evaluador de Expresiones ===")
expresion = input("Ingrese una expresión en notación infija (ej: (3+2)*4): ")

posfija = infija_a_posfija(expresion)
prefija = infija_a_prefija(expresion)

print(f"\nExpresión en notación posfija: {posfija}")
print(f"Expresión en notación prefija: {prefija}")

print(f"\nEvaluación posfija = {evaluar_posfija(posfija)}")
print(f"Evaluación prefija = {evaluar_prefija(prefija)}")
