
class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")



class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.top = None   
        self.tail = None  
        self.size = 0    

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def front(self):
        """Devuelve el primer elemento sin eliminarlo."""
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        """Agrega un nuevo elemento al final de la cola."""
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola."""
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return info

    def get_nth(self, pos):
        """Devuelve el n-ésimo elemento sin eliminarlo (1 = primero)."""
        if pos <= 0 or pos > self.size:
            return None
        node = self.top
        for _ in range(pos - 1):
            node = node.next
        return node.info

    def print_info(self):
        """Imprime el contenido completo de la cola."""
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")
        node = self.top
        i = 1
        while node is not None:
            print(f"   ** Element {i}")
            if isinstance(node.info, Order):
                node.info.print()
            else:
                print(f"     {node.info}")
                print("     ------------")
            node = node.next
            i += 1
        print("******************************")



if __name__ == "__main__":
    queue = Queue()

    # Crear pedidos (Order)
    o1 = Order(20, "cust1")
    o2 = Order(30, "cust2")
    o3 = Order(40, "cust3")
    o4 = Order(50, "cust4")


    queue.enqueue(o1)
    queue.enqueue(o2)
    queue.enqueue(o3)
    queue.enqueue(o4)

    queue.print_info()


    print("\nFRONT ELEMENT:")
    front_order = queue.front()
    if front_order:
        front_order.print()


    print("\nDEQUEUE ELEMENT:")
    removed = queue.dequeue()
    if removed:
        removed.print()


    queue.print_info()


    print("\nGET Nth ELEMENT (3rd):")
    third = queue.get_nth(3)
    if third:
        third.print()
