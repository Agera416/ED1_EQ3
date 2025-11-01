#Estructura de Datos Unidad 2_Tarea3_Ejercicio_2

class NodoIngrediente:
    """Nodo para la sublista de ingredientes"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class NodoPostre:
    """Nodo principal de la lista de postres"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None  
        self.siguiente = None    


class ListaPostres:
    """Lista enlazada de postres"""
    def __init__(self):
        self.cabeza = None

    def mostrar_ingredientes(self, nombre_postre):
        postre = self.buscar_postre(nombre_postre)
        if not postre:
            print(f"❌ El postre '{nombre_postre}' no existe.")
            return
        print(f"🍰 Ingredientes de {nombre_postre}:")
        actual = postre.ingredientes
        if not actual:
            print("   (Sin ingredientes)")
        while actual:
            print("   -", actual.nombre)
            actual = actual.siguiente

    def insertar_ingrediente(self, nombre_postre, nombre_ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if not postre:
            print(f"❌ El postre '{nombre_postre}' no existe.")
            return
        nuevo = NodoIngrediente(nombre_ingrediente)
        if not postre.ingredientes:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"✅ Ingrediente '{nombre_ingrediente}' agregado a {nombre_postre}.")


    def eliminar_ingrediente(self, nombre_postre, nombre_ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if not postre:
            print(f"❌ El postre '{nombre_postre}' no existe.")
            return
        actual = postre.ingredientes
        anterior = None
        while actual:
            if actual.nombre == nombre_ingrediente:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    postre.ingredientes = actual.siguiente
                print(f"✅ Ingrediente '{nombre_ingrediente}' eliminado de {nombre_postre}.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"⚠️ El ingrediente '{nombre_ingrediente}' no se encontró en {nombre_postre}.")

    def alta_postre(self, nombre_postre, ingredientes=[]):
        if self.buscar_postre(nombre_postre):
            print(f"⚠️ El postre '{nombre_postre}' ya existe.")
            return
        nuevo = NodoPostre(nombre_postre)
        # Insertar ingredientes
        for ing in ingredientes:
            self.insertar_ingrediente_en_postre(nuevo, ing)
        # Insertar postre alfabéticamente
        if not self.cabeza or nombre_postre < self.cabeza.nombre:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.nombre < nombre_postre:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        print(f"🍮 Postre '{nombre_postre}' dado de alta con sus ingredientes.")

    def insertar_ingrediente_en_postre(self, postre, nombre_ingrediente):
        nuevo = NodoIngrediente(nombre_ingrediente)
        if not postre.ingredientes:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def baja_postre(self, nombre_postre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre == nombre_postre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"🗑️ Postre '{nombre_postre}' eliminado junto con sus ingredientes.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"❌ El postre '{nombre_postre}' no se encontró.")


    def buscar_postre(self, nombre_postre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre_postre:
                return actual
            actual = actual.siguiente
        return None


    def mostrar_todo(self):
        actual = self.cabeza
        if not actual:
            print("⚠️ No hay postres en la lista.")
            return
        print("\n📋 LISTA DE POSTRES Y SUS INGREDIENTES:")
        while actual:
            print(f"\n🍨 {actual.nombre}:")
            ing = actual.ingredientes
            while ing:
                print("   -", ing.nombre)
                ing = ing.siguiente
            actual = actual.siguiente

postres = ListaPostres()
postres.alta_postre("Gelatina", ["Agua", "Grenetina", "Saborizante"])
postres.alta_postre("Pastel", ["Harina", "Azúcar", "Huevos", "Mantequilla"])
postres.mostrar_todo()

postres.insertar_ingrediente("Pastel", "Vainilla")
postres.mostrar_ingredientes("Pastel")

postres.eliminar_ingrediente("Gelatina", "Saborizante")
postres.mostrar_ingredientes("Gelatina")

postres.baja_postre("Gelatina")
postres.mostrar_todo()

def eliminar_repetidos(lista_postres):
    """Elimina los postres con nombres repetidos"""
    actual = lista_postres.cabeza
    while actual:
        anterior = actual
        temp = actual.siguiente
        while temp:
            if temp.nombre == actual.nombre:
                # eliminar nodo duplicado
                anterior.siguiente = temp.siguiente
                print(f"❌ Postre duplicado '{temp.nombre}' eliminado.")
            else:
                anterior = temp
            temp = temp.siguiente
        actual = actual.siguiente

lista = ListaPostres()
lista.alta_postre("Flan", ["Leche", "Huevo", "Azúcar"])
lista.alta_postre("Flan", ["Leche", "Huevo", "Azúcar"])
lista.alta_postre("Pastel", ["Harina", "Azúcar", "Huevos"])
lista.alta_postre("Flan", ["Leche", "Huevo", "Caramelo"])

lista.mostrar_todo()
eliminar_repetidos(lista)
lista.mostrar_todo()

print("\n🔍 CONCLUSIÓN:")
print("Al eliminar nodos duplicados, las sublistas de ingredientes asociadas también se eliminan.")
print("Esto sucede porque al no haber referencia al nodo borrado, Python libera la memoria automáticamente.")
